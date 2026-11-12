---
name: ab-test-readout
description: Turn raw A/B test results into a decision-ready readout with significance, confidence intervals, a full funnel per variant, a sample ratio check and a recommendation. Use when someone shares test results, an Optimizely or analytics export, or asks whether a test won.
---

# A/B test results readout

You write the results readout for a finished website experiment. The goal is a document a stakeholder can act on in two minutes and an analyst can trust: every number computed, not estimated, and every recommendation tied to the hypothesis.

## 1. Gather the inputs

Collect these before calculating. Ask for anything missing in one message, listing exactly what's needed.

- Test name, page or flow, dates, audience and devices
- The hypothesis (if we change X, we expect Y, because Z) and the primary metric it named
- Experiences: control first, then each variant, with a one-line description of what changed
- For each experience: unique visitors, and the count of unique people reaching each funnel step (for example: CTA clicks, signups, trial starts, activation, purchase)
- Intended traffic split (default: equal)
- Anything that happened during the test: launches, outages, tracking changes, campaigns

If the user pastes an export or spreadsheet, extract the counts yourself and confirm the mapping of columns to funnel steps before going further.

Watch for these data problems and raise them:
- Rates without counts. Ask for counts; you can't test significance on percentages alone.
- Event totals instead of unique people. Funnel steps must count people.
- A step larger than the step before it. Usually a tracking or definition problem.

## 2. Calculate with the script

Metrics that aren't sequential funnel steps (navigation clicks by menu item, for example) can go in the same file; add `"funnel": false` so the script skips the step-to-step funnel.

Never do the statistics in your head. Write the inputs to a JSON file in the format documented at the top of `scripts/abtest.py` (see `examples/example-input.json`) and run:

```
python3 scripts/abtest.py readout input.json
```

The script reports, for every step and variant: rates per visitor, relative lift, a 95% confidence interval on the lift, the p-value and significance (two-sided two-proportion z-test), the step-to-step funnel, and a chi-square sample ratio mismatch (SRM) check. With more than one variant it suggests a Bonferroni-adjusted alpha.

If code execution isn't available, say so and show the formulas you would use; don't present hand-estimated p-values as results.

## 3. Interpret

Decide the call from the primary metric named in the hypothesis, then use the rest of the funnel to explain why.

- **Sample ratio mismatch first.** If the SRM check fails (p < 0.001), say so at the top. The split didn't match the plan, which usually means a targeting, redirect or tracking problem, and every result below is less trustworthy until it's explained.
- **Winner:** the primary metric improves and is significant at the chosen alpha, and no downstream guardrail metric (activation, retention, revenue) is significantly worse.
- **Loser:** the primary metric is significantly worse.
- **Mixed result:** the primary metric and an important downstream step disagree. Example: fewer signups but a higher share of signups that start a trial. Name the trade-off and quantify it.
- **Inconclusive:** nothing significant. Report the confidence interval, so readers see the range of plausible effects, and check whether the test was underpowered with `python3 scripts/abtest.py detectable --baseline <control rate> --visitors <per variant>`. "Couldn't have detected less than a 50% lift" is a different lesson from "there's no effect".
- **The primary metric is flat but a downstream step moved significantly.** Report it plainly, but don't promote it to the call; recommend a follow-up test with that step as the primary metric, sized for it.
- Treat lifts on steps far down the funnel with small counts as directional, and say so.
- Don't call a winner from a secondary metric when the primary metric was flat.

## 4. Write the readout

Use this structure and plain language. Sentence case headings, no jargon a marketer wouldn't know without a short explanation.

```
# [Test name]: [one-line result, e.g. "Variant B lifted trial signups 69%"]

**Call:** Winner / Loser / Mixed result / Inconclusive
**Recommendation:** [ship, don't ship, iterate, or re-run], in one sentence

## Summary
Two or three sentences: what changed, what happened to the primary metric (rate, lift, confidence interval, p-value), and what it means.

## Test details
Dates · page or flow · audience · devices · traffic split · visitors per experience · primary and secondary metrics

## Hypothesis
## Results
Table from the script output: step, control, variant, relative lift, 95% CI, significant.
## Funnel
One line per experience showing each step and the step-to-step rate.
## Data caveats
SRM result, anything that happened during the test, small counts, tracking notes.
## What we learned
The insight, whether or not the test won.
## Next steps
Numbered recommendations, including the next test this result suggests.
```

Every test should produce an insight, and every insight should suggest the next test. End with that next test.

## Example

`examples/example-input.json` holds a real two-variant test (a trial page redesign). Running the script on it shows a 69% lift in signups (p < 0.001) and also a sample ratio mismatch: 53% of visitors saw control instead of 50%. A good readout leads with the win, flags the mismatch as a caveat to investigate, and notes that data activation didn't move.
