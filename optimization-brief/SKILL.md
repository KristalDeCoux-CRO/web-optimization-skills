---
name: optimization-brief
description: Turn an A/B test or web personalization request into ready-to-use deliverables - a tracking issue, a testing platform brief, a test plan, placement copy fitted to character limits and a review email. Use when someone shares a test idea, an experiment request, or a request to promote content in a page placement.
---

# Optimization brief

Test and personalization requests arrive as emails, chat messages, tickets and meeting notes, and almost none of them contain everything the team needs. You turn each one into the complete set of documents a testing program runs on, and you flag what's missing instead of guessing.

## Before you start: load the team settings

Read `references/team-config.md`. It holds everything specific to a team: the testing platform, the issue tracker and repo, the test ID format, audience segments, placement character limits, approval rules, the review email list and the launch checklist. If a value there is still a placeholder, use a neutral default, mark it `[SET IN team-config.md]` in the output, and mention it once at the end.

## 1. Classify the request

Decide whether it's:
- **A/B test:** a control and one or more variants, with a winner decided by a metric. Signals: test, experiment, variant, control, "see if", "measure the impact", hypothesis language.
- **Personalization (web merchandising):** content shown in a page placement, often to a specific audience, with no control. Signals: promote, feature, swap the hero, add a banner, update a card, show this to a segment.
- **Both:** publish the content and test it.

Requesters often call personalization a test, or the reverse. Classify from what they describe. If it's genuinely ambiguous, state your classification and ask them to confirm before going further.

## 2. Extract the details

Pull out every field the request gives you:

| Field | Notes |
|---|---|
| Name | Descriptive name for the test or placement |
| Page URLs | Pages involved |
| Business goal | The outcome being optimized |
| Hypothesis | If missing, draft one and mark it as a draft for the requester to confirm |
| Audience | All visitors or a segment |
| Devices | Desktop, mobile or all |
| Experiences | Control plus each variant, or the placement content |
| Primary metric | The one metric that decides the test |
| Secondary metrics | Supporting and guardrail metrics |
| Sizing data | Daily visitors, baseline conversion rate, smallest lift worth detecting, number of variants |
| Dates | Requested launch and any hard deadline, and why it's fixed |
| Requester | Name and team |
| Source link | Ticket, email or thread, if any |

Hypothesis template: *If we [make this change], we expect [this effect on the primary metric], because [this reason or evidence].*

## 3. Recommend targeting

Recommend the simplest audience that tests the hypothesis. Use the segment names in the team settings exactly as written. Common options: all visitors; device; new or returning; language; location; traffic source, campaign or referrer; URL or query parameters; time of visit; customer status; account or firmographic segments such as industry, company size or persona. If the request needs targeting the team's platform doesn't support, flag it as a custom request.

## 4. Create the tracking issue first

If the team tracks work in GitHub and the `gh` CLI is available and signed in, create the issue before writing anything else, because its number becomes the test ID used in every document. Create the labels if they don't exist, with the label names from the team settings. Otherwise, write the issue text for the user to paste and use `[TEST ID]` as a placeholder.

Title: `[A/B test] {name}: {page}`, `[Personalization] {placement}: {description}`, or `[A/B test + personalization] {name}: {page}`

Body:
```
## Overview
Type · Page · Requester · Requested launch · Source link

## Summary
One sentence.

## Hypothesis or objective
## Targeting
## Experiences or placement content
## Metrics
Primary · Secondary
## Sizing
The numbers, or: ⚠️ Sizing needed before launch (daily visitors, baseline conversion rate, smallest lift worth detecting, number of variants)

## Checklist
[the launch checklist from the team settings, as task list items]

## Documents
Test plan · Sizing sheet
```

## 5. Write the deliverables

### A/B tests

**Testing platform brief.** The brief the person building the test needs:
```
Experiment name: {TEST ID} | {language} {page} {test description}
Business goal:
Hypothesis:
Problem this solves: the observation or data behind the test
Test location: where on the page
Audience conditions:
Devices:
Experiences: Control ({current experience}); Variant B ({what changes}); add more as needed
Primary metric: {name} [{TEST ID}], triggered by {the exact action}
Secondary metrics: {name} [{TEST ID}], triggered by {action}; one per line
```

**Test plan.** A document to paste into the team's docs tool, named `{language} {page} {test description}`, with these sections:
- Header: test ID, tracking issue link, requester, test owner, start and end dates
- Executive summary: background, hypothesis, estimated business impact ("a 10% lift in X would add about Y per year", or ⚠️ needs sizing data), primary and secondary metrics, sample size and duration, audience, devices, experience names
- Setup notes: audience, devices, each experience, platform campaign link, pages, click tracking for each element, behavioral metrics (bounce, scroll depth, time on page, pages per session)
- Analysis notes: UTM or tracking parameters per experience (for example `cta={test-id}-a` and `cta={test-id}-b`), platform IDs, links to dashboards and session recordings
- Experiences: one section per experience with tracked elements and a placeholder for a screenshot after QA
- Results and recommendation, to fill in when the test ends: dates, data notes, the result on the primary metric with numbers, secondary metrics, heatmap notes, the recommendation (ship the variant, keep control and iterate, or inconclusive) and the reasons

**Review email.** A draft to the review list in the team settings with the subject `[Review needed] {TEST ID} | {test name}`, the tracking issue link, key details (page, requester, launch date, targeting, experiences) and the full platform brief. Draft it; don't send it.

### Personalization

**Placement brief.** For each piece of content, fit the copy to the placement's limits from the team settings and show the counts:
```
Placement · Audience
Headline ({limit}): "{copy}" ({n} characters) ✓ or ⚠️ over the limit
Body ({limit}): "{copy}" ({n} characters) ✓ or ⚠️
CTA: "{copy}" · URL with tracking parameters
Image: specs, or not supported in this placement
```
For placements the team schedules on an editorial calendar, add a calendar entry with the live date, placement, slot, links, copy with counts, destination URL and image status.

## Output order

1. The request type, in one line
2. A short summary of what you extracted, and what's missing
3. Targeting
4. The tracking issue (link and test ID) or its text to paste
5. A/B tests: platform brief, test plan, review email. Personalization: placement brief, then the calendar entry if it applies
6. Approval flags and the sizing flag, if they apply

## Rules

- Never invent traffic, conversion rates or expected lift. Flag missing sizing data with ⚠️ and point to the `ab-test-sizing` skill if it's installed.
- Mark a drafted hypothesis as a draft.
- Base all copy, URLs and metrics on the request. Don't invent details.
- Recommend only targeting the team's platform supports.
- Apply the approval rules in the team settings, for example sign-off needed for homepage hero changes, and flag them every time they're triggered.
- If the requester sends missing details later, run the request through again to regenerate clean documents.
