#!/usr/bin/env python3
"""A/B test math for the readout and sizing skills. Standard library only.

Commands
  readout <input.json>      Significance, lift, confidence intervals, funnel and a
                            sample ratio mismatch check for a finished test.
  size [options]            Sample size and duration for a planned test.
  detectable [options]      Smallest lift a test of a given size can reliably detect.
  rice R I C E              RICE score (each factor 1-5).

Readout input (JSON)
  {
    "name": "Homepage hero test",
    "expected_split": [0.5, 0.5],          # optional, defaults to equal split
    "alpha": 0.05,                          # optional
    "primary_metric": "signups",            # which step decides the test
    "funnel": true,                         # optional; false when the metrics aren't sequential steps
    "variants": [
      {"name": "Control", "visitors": 2357, "steps": {"cta_clicks": 433, "signups": 166, "starts": 150}},
      {"name": "Variant B", "visitors": 2084, "steps": {"cta_clicks": 420, "signups": 248, "starts": 217}}
    ]
  }
The first variant is treated as the control. Step counts are people, not events.
"""
import argparse, json, math, sys
from statistics import NormalDist

N = NormalDist()


def two_prop(c_x, c_n, v_x, v_n, alpha=0.05):
    """Two-sided two-proportion z-test with a confidence interval on the difference."""
    p1, p2 = c_x / c_n, v_x / v_n
    pooled = (c_x + v_x) / (c_n + v_n)
    se_pooled = math.sqrt(pooled * (1 - pooled) * (1 / c_n + 1 / v_n)) if 0 < pooled < 1 else 0
    z = (p2 - p1) / se_pooled if se_pooled else 0.0
    p_value = 2 * (1 - N.cdf(abs(z)))
    se_diff = math.sqrt(p1 * (1 - p1) / c_n + p2 * (1 - p2) / v_n)
    zc = N.inv_cdf(1 - alpha / 2)
    diff = p2 - p1
    lift = diff / p1 if p1 else float("nan")
    # Relative lift interval via the delta method on log(p2/p1).
    if p1 > 0 and p2 > 0 and c_x > 0 and v_x > 0:
        se_log = math.sqrt((1 - p1) / c_x + (1 - p2) / v_x)
        lo, hi = math.exp(math.log(p2 / p1) - zc * se_log) - 1, math.exp(math.log(p2 / p1) + zc * se_log) - 1
    else:
        lo = hi = float("nan")
    return {"control_rate": p1, "variant_rate": p2, "abs_diff": diff,
            "diff_ci": [diff - zc * se_diff, diff + zc * se_diff],
            "relative_lift": lift, "lift_ci": [lo, hi], "z": z, "p_value": p_value,
            "significant": p_value < alpha}


def srm(counts, expected):
    """Chi-square test for sample ratio mismatch."""
    total = sum(counts)
    chi = sum((o - total * e) ** 2 / (total * e) for o, e in zip(counts, expected))
    dof = len(counts) - 1
    # Survival function of chi-square via the regularized gamma (dof is small here).
    p = _chi2_sf(chi, dof)
    return {"chi_square": chi, "p_value": p, "mismatch": p < 0.001,
            "observed_share": [c / total for c in counts], "expected_share": expected}


def _chi2_sf(x, k):
    a, x2 = k / 2.0, x / 2.0
    if x2 <= 0:
        return 1.0
    # Series for the lower regularized gamma function.
    term = summ = 1.0 / a
    n = 1
    while n < 500:
        term *= x2 / (a + n)
        summ += term
        if term < summ * 1e-12:
            break
        n += 1
    lower = summ * math.exp(-x2 + a * math.log(x2) - math.lgamma(a))
    return max(0.0, 1.0 - lower)


def readout(cfg):
    alpha = cfg.get("alpha", 0.05)
    vs = cfg["variants"]
    k = len(vs)
    expected = cfg.get("expected_split") or [1 / k] * k
    control = vs[0]
    steps = list(control["steps"].keys())
    primary = cfg.get("primary_metric", steps[-1])
    out = {"name": cfg.get("name", ""), "alpha": alpha, "primary_metric": primary, "show_funnel": cfg.get("funnel", True),
           "srm": srm([v["visitors"] for v in vs], expected), "comparisons": [], "funnel": []}
    if k > 2:
        out["note"] = f"{k - 1} variants compared to control; consider a Bonferroni alpha of {alpha / (k - 1):.4f}."
    for v in vs[1:]:
        rows = {}
        for s in steps:
            rows[s] = two_prop(control["steps"][s], control["visitors"], v["steps"][s], v["visitors"], alpha)
        out["comparisons"].append({"variant": v["name"], "per_visitor": rows})
    for v in vs:
        prev, prev_name, f = v["visitors"], "visitors", []
        for s in steps:
            f.append({"step": s, "count": v["steps"][s], "rate_of_visitors": v["steps"][s] / v["visitors"],
                      "rate_from_previous": (v["steps"][s] / prev) if prev else None, "previous": prev_name})
            prev, prev_name = v["steps"][s], s
        out["funnel"].append({"variant": v["name"], "visitors": v["visitors"], "steps": f})
    return out


def sample_size(baseline, mde_rel, alpha=0.05, power=0.8, two_sided=True):
    """Visitors needed per variant to detect a relative lift of mde_rel."""
    p1 = baseline
    p2 = baseline * (1 + mde_rel)
    za = N.inv_cdf(1 - alpha / 2) if two_sided else N.inv_cdf(1 - alpha)
    zb = N.inv_cdf(power)
    pbar = (p1 + p2) / 2
    n = ((za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / (p2 - p1) ** 2
    return math.ceil(n)


def detectable_lift(baseline, visitors_per_variant, alpha=0.05, power=0.8):
    """Smallest relative lift detectable with this many visitors per variant."""
    lo, hi = 1e-4, 50.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if sample_size(baseline, mid, alpha, power) <= visitors_per_variant:
            hi = mid
        else:
            lo = mid
    return hi


def fmt_pct(x, d=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x * 100:.{d}f}%"


def print_readout(r):
    print(f"# {r['name'] or 'Test readout'}\n")
    s = r["srm"]
    flag = "MISMATCH, investigate before trusting results" if s["mismatch"] else "OK"
    print(f"Sample ratio check: {flag} (observed {', '.join(fmt_pct(x, 1) for x in s['observed_share'])}; "
          f"expected {', '.join(fmt_pct(x, 1) for x in s['expected_share'])}; p = {s['p_value']:.2g})\n")
    if r.get("note"):
        print(r["note"] + "\n")
    for c in r["comparisons"]:
        print(f"## {c['variant']} vs. control (rates per visitor)\n")
        print("| Step | Control | Variant | Relative lift | 95% CI on lift | p-value | Significant |")
        print("|---|---|---|---|---|---|---|")
        for step, t in c["per_visitor"].items():
            mark = " (primary)" if step == r["primary_metric"] else ""
            print(f"| {step}{mark} | {fmt_pct(t['control_rate'])} | {fmt_pct(t['variant_rate'])} | "
                  f"{fmt_pct(t['relative_lift'], 1)} | {fmt_pct(t['lift_ci'][0], 1)} to {fmt_pct(t['lift_ci'][1], 1)} | "
                  f"{t['p_value']:.2g} | {'yes' if t['significant'] else 'no'} |")
        print()
    if not r.get("show_funnel", True):
        return
    print("## Funnel by variant\n")
    for f in r["funnel"]:
        parts = [f"{f['visitors']:,} visitors"] + [
            f"{st['count']:,} {st['step']} ({fmt_pct(st['rate_from_previous'], 1)} of {st['previous']})" for st in f["steps"]]
        print(f"- **{f['variant']}:** " + " → ".join(parts))
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("readout"); r.add_argument("file"); r.add_argument("--json", action="store_true")
    s = sub.add_parser("size")
    s.add_argument("--baseline", type=float, required=True, help="baseline conversion rate, e.g. 0.03")
    s.add_argument("--mde", type=float, required=True, help="minimum relative lift to detect, e.g. 0.10")
    s.add_argument("--daily", type=float, required=True, help="eligible visitors per day")
    s.add_argument("--variants", type=int, default=2, help="number of experiences including control")
    s.add_argument("--allocation", type=float, default=1.0, help="share of traffic in the test (0-1)")
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.8)
    s.add_argument("--json", action="store_true")
    d = sub.add_parser("detectable")
    d.add_argument("--baseline", type=float, required=True)
    d.add_argument("--visitors", type=float, required=True, help="visitors per variant")
    d.add_argument("--variants", type=int, default=2)
    d.add_argument("--alpha", type=float, default=0.05)
    d.add_argument("--power", type=float, default=0.8)
    rc = sub.add_parser("rice"); [rc.add_argument(x, type=float) for x in ("reach", "impact", "confidence", "effort")]
    a = ap.parse_args()

    if a.cmd == "readout":
        res = readout(json.load(open(a.file)))
        print(json.dumps(res, indent=2)) if a.json else print_readout(res)
    elif a.cmd == "size":
        alpha = a.alpha / (a.variants - 1) if a.variants > 2 else a.alpha
        per = sample_size(a.baseline, a.mde, alpha, a.power)
        total = per * a.variants
        days = math.ceil(total / (a.daily * a.allocation))
        res = {"per_variant": per, "total": total, "days": days, "weeks": math.ceil(days / 7),
               "alpha_used": alpha, "power": a.power,
               "detectable_rate": a.baseline * (1 + a.mde)}
        if a.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"Visitors per variant: {per:,}\nTotal visitors: {total:,}\n"
                  f"Estimated duration: {days} days (round up to {res['weeks']} full weeks)\n"
                  f"Detects {fmt_pct(a.baseline)} → {fmt_pct(res['detectable_rate'])} "
                  f"at alpha {alpha:.3g}, power {a.power:.0%}")
    elif a.cmd == "detectable":
        alpha = a.alpha / (a.variants - 1) if a.variants > 2 else a.alpha
        m = detectable_lift(a.baseline, a.visitors, alpha, a.power)
        print(f"With {a.visitors:,.0f} visitors per variant and a {fmt_pct(a.baseline)} baseline, the test can reliably detect "
              f"a relative lift of about {m * 100:.0f}% ({fmt_pct(a.baseline)} → {fmt_pct(a.baseline * (1 + m))}) "
              f"at alpha {alpha:.3g}, power {a.power:.0%}. Smaller real effects will usually read as not significant.")
    else:
        score = a.reach * a.impact * a.confidence / a.effort
        print(f"RICE = {a.reach:g} × {a.impact:g} × {a.confidence:g} ÷ {a.effort:g} = {score:.1f}")


if __name__ == "__main__":
    main()
