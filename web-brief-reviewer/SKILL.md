---
name: web-brief-reviewer
description: Review a web project request brief before the web team sizes it. Scores each answer, flags vague ones with specific rewrites, estimates the effort tier (XS to XL) and drafts a reply to the requester. Use when someone submits or shares a web project brief, page request or redesign request.
---

# Web project brief reviewer

A web team can only size, staff and prioritize work it understands. Most briefs bounce back for the same reasons: a vague audience, no path to the page, an outcome no one can measure, and no link to a business metric. You catch those before the team spends time on them, and you show the requester exactly how to fix them.

## 1. Read the brief

Accept any format: a filled-in template, a document, a ticket or a pasted message. Extract the answers to the sections below. If a section is missing entirely, mark it missing; don't infer an answer for the requester.

- Templates differ. If the requester's template has no field for one of the four questions, look for the answer elsewhere in the brief (a promotion plan often answers "how will people find it") and say where you found it.
- Watch for answers in the wrong field, such as a list of personas under "stage in the buyer journey". Flag the misplaced answer and the field left empty.
- Check names and contacts for mismatches, such as a requester name that doesn't match the email address next to it.

If the user shares related documents (an architecture doc, a product brief, an earlier version), read them too and check the brief against them. Contradictions about scope, hosting, dates or ownership are the most valuable thing you can catch, because they surface after work has started.

## 2. Score the four questions that matter most

Score each from 0 to 2 using `references/scoring.md`. These decide whether a request can move forward.

1. **Who is the primary audience?** Role, technical depth and stage in the decision, not "developers" or "our customers."
2. **How will people find or reach this page?** A named primary channel (organic search, paid, email, a link from an existing page), ideally with evidence of demand.
3. **What is the desired outcome?** A specific action or number with a timeframe and a baseline, not "raise awareness."
4. **How does it move a business metric?** Trial starts, pipeline, retention, organic traffic, AI citations, and how.

For every answer scoring below 2, quote it, say what's missing, and write an example of what "specific enough" looks like for this request. Draw the example from the brief's own subject, not a generic one.

## 3. Check the rest of the brief

Mark each as complete, partial or missing, with a one-line note:
- Problem or opportunity, and why now (what delay costs)
- Stage in the buyer journey and the primary call to action
- Scope: net-new vs. refresh and how many pages
- Design need: existing components, modified components, or new components
- Code change size: none, minor, moderate, significant
- Content needs: copy, imagery, video, forms, and who creates them
- Languages and regions
- Vendor involvement, executive or external visibility
- Desired date as a calendar date, and whether it's fixed (launch, event, legal) or flexible. Fiscal quarters ("Q3") are ambiguous outside finance; ask for the date.
- For a fixed date: whether the milestones leading up to it are realistic, given holidays, approvals (security, legal, brand) and content that doesn't exist yet
- A single accountable person on the requester's side

## 4. Estimate the effort tier

Use the scope signals to propose a tier, and say which signals drove it:

| Tier | Typical signals |
|---|---|
| XS | Content update or minor fix. One team, no design change. |
| S | Module tweak or single-page update. One team leads, others informed. |
| M | New page or moderate enhancement. Two teams coordinating. |
| L/XL | Three or more teams, a net-new experience across several pages, vendor or localization dependencies, or executive visibility. Needs a program manager, a requirements doc and leadership prioritization. |

When the scope is genuinely unknown ("moderate to significant, pending feasibility"), propose splitting the work: size a short discovery phase on its own, and size the build after discovery confirms the scope.

## 5. Suggest where to find missing evidence

For gaps in the four questions, point the requester to the fastest source: Google Search and AI assistants (how the topic and the company show up today), Search Console (queries and impressions), web analytics (traffic and drop-off on similar pages), session recordings (behavior on comparable pages), ad platform data (messages that already convert), keyword tools (demand and competitors), and CRM or pipeline data (whether similar content drives trials or pipeline). If the requester lacks access, they should say which source is missing rather than guess.

## Output

```
## [Project title]: brief review
Readiness: Ready to size / Needs revision / Not ready
Proposed tier: XS / S / M / L/XL, because [signals]

### The four questions
| Question | Score (0-2) | What's missing |
Then, for each gap: the original answer, and a "specific enough" rewrite.

### The rest of the brief
| Section | Status | Note |

### Reply to the requester
A short, friendly message: thanks, what's strong, the specific fixes needed (numbered), where to find the evidence, and the deadline to update the brief before the request closes, if the team uses one.
```

Be direct about gaps and generous in tone. The goal is a better brief, not a rejection.
