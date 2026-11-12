---
name: ab-test-sizing
description: Size and prioritize a planned A/B test. Calculates visitors needed and test duration from baseline conversion, minimum detectable lift and traffic, then scores the idea with RICE. Use when someone asks how long a test will take, whether a page has enough traffic to test, or which test ideas to run first.
---

# A/B test sizing and prioritization

You help a marketer or test strategist decide whether a test is worth running, how long it will take, and where it ranks against other ideas.

## 1. Gather the inputs

- **Page and primary metric.** The conversion the test is judged on.
- **Baseline conversion rate** of that metric, per visitor, over a recent stable period (ideally 4 to 12 weeks, excluding holidays and launches). If the user only has totals, compute it as conversions ÷ unique visitors.
- **Daily eligible visitors:** visitors who would enter the test, after audience and device targeting.
- **Minimum detectable effect (MDE):** the smallest relative lift worth acting on. If the user doesn't know, offer 5%, 10% and 20% so they see the trade-off.
- **Number of experiences** including control, and the share of traffic in the test (default 100%).
- Confidence and power: default 95% confidence (alpha 0.05) and 80% power.

## 2. Calculate with the script

Don't estimate sample sizes by hand. Run:

```
python3 scripts/abtest.py size --baseline 0.03 --mde 0.10 --daily 5000 --variants 2
```

Options: `--allocation 0.5` for a 50% traffic test, `--alpha` and `--power` to change thresholds. With more than two experiences the script applies a Bonferroni correction.

Run it for two or three MDE values and present them side by side. That table usually ends the debate faster than any argument.

To work backwards from a fixed amount of traffic ("we can only run it for three weeks", or a finished test that came back flat), run:

```
python3 scripts/abtest.py detectable --baseline 0.004 --visitors 2350 --variants 3
```

It returns the smallest lift that sample can reliably detect.

**Size every metric that decides the test.** Each one needs its own baseline from the same source the test will measure it with. A common failure: the plan is sized on a high-volume rate (for example signups per homepage visitor from analytics) while the test is judged on a low-volume one (trial button clicks per visitor in the testing platform), and the real test needs ten times the traffic. If the baselines in a scoping sheet don't match the primary metric's definition, say so.

## 3. Advise

- **Round duration up to full weeks,** and run at least one full week (two is better) to cover weekday and weekend behavior, even if the sample fills sooner.
- **If the test needs more than about eight weeks,** say it's impractical as designed and offer alternatives: test a bigger change, use a metric higher in the funnel with more volume, combine similar pages into one test, or skip the test and ship with monitoring if risk is low.
- **Don't stop early on a promising number.** The duration is set before launch.
- **Name the guardrail metrics** to watch, such as downstream activation, revenue or bounce.

## 4. Prioritize with RICE

When comparing ideas, score each factor 1 to 5 and run `python3 scripts/abtest.py rice R I C E`:

- **Reach:** how many visitors the change affects (5 = a top entry page or the whole site)
- **Impact:** how much it could move the primary metric (5 = a critical conversion blocker)
- **Confidence:** how strong the evidence behind the hypothesis is (5 = several data sources agree: analytics, recordings, research)
- **Effort:** design, build and QA work (5 = weeks across several teams; low effort scores 1)

Present a ranked table: idea, R, I, C, E, score, estimated duration from step 2, and a one-line rationale. Flag ideas that score high but can't reach significance in a reasonable time.

## Output

```
## [Test name]: sizing
Baseline: x% · Daily eligible visitors: n · Experiences: k
| Minimum detectable lift | Visitors per experience | Total | Duration |
Recommendation: one or two sentences.

## Priority (if several ideas)
| Idea | Reach | Impact | Confidence | Effort | RICE | Duration | Why |
```
