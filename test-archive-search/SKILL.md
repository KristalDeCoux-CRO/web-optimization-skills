---
name: test-archive-search
description: Search a team's archive of past A/B tests before running a new one. Finds similar tests, summarizes what happened and why, and advises whether the idea is worth revisiting. Use when someone proposes a test idea, asks "have we tested this before?", or wants the history of a page or element.
---

# Has this been tested?

Good testing programs forget. People leave, wikis sprawl, and the same idea gets tested three times. You search the archive first, so every new test builds on what the team already learned.

## 1. Find the archive

The archive can be any of these. Ask which one the user keeps, and where:
- A spreadsheet or CSV with one row per test (see `templates/test-archive.csv` for the recommended columns)
- A folder of test plan and results documents or decks
- A wiki or Confluence space
- A connected drive or document tool

If there's no archive yet, offer to start one from `templates/test-archive.csv` and fill it from whatever results documents the user can share.

## 2. Understand the new idea

Restate the proposed test as: page or flow · element changed · audience · primary metric · hypothesis. Then list search terms for each part, including synonyms people use for the same thing (for example: hero, banner, masthead; CTA, button; signup, registration, trial start; social proof, reviews, ratings, testimonials).

## 3. Search broadly, then narrow

Look for matches on four levels, and report each level separately:
1. **Same element, same page.** The idea, or nearly the idea, was already tested.
2. **Same element, different page or audience.** Results may transfer, or may not.
3. **Same hypothesis, different execution.** The underlying idea was tested a different way.
4. **Same page, different element.** Context about how the page performs and what moved it.

For every match, read the actual results, not just the title. Record the dates, the experiences, the primary metric result with numbers, the call (winner, loser, mixed, inconclusive) and the stated lesson.

## 4. Advise

Give one of these verdicts, with reasons:
- **Already answered.** A close match produced a clear result recently and nothing important has changed. Recommend not re-testing, or shipping the winner if it was never shipped.
- **Worth revisiting.** A match exists but the context changed: new audience, new traffic source, redesigned page, a test that was underpowered, interrupted or had a data problem, or a result that is several years old.
- **Build on it.** Related tests point to a better version of the idea. Propose the refined hypothesis.
- **New ground.** Nothing similar found. Say what you searched so the user can trust the gap.

Watch for patterns across several tests, such as "every test that added a step before signup reduced volume but raised trial quality." Those patterns are often the most valuable thing an archive holds.

## Output

```
## [Proposed test]: archive check
Verdict: Already answered / Worth revisiting / Build on it / New ground

### Closest matches
| Test | Dates | What changed | Result | Lesson |

### Patterns across tests
### Recommendation
The suggested next step and, if testing, a refined hypothesis.

Searched: [archive location] for [terms]
```

## Keeping the archive useful

When a test ends, add a row: ID, name, dates, page, element, audience, devices, hypothesis, experiences, primary metric, result with numbers, call, lesson, link to the full readout. An archive is only as good as its last entry.
