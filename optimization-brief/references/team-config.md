# Team settings for the optimization brief

Replace the example values with your team's. The skill reads this file every time it runs. Anything left as a placeholder in [brackets] is flagged in the output.

## Tools

- Testing and personalization platform: [Optimizely, VWO, AB Tasty, Adobe Target, LaunchDarkly…]
- Issue tracker: GitHub
- Repo for test requests: [owner/repo]
- Labels: `a/b-test`, `personalization`
- Docs tool for test plans: [Google Docs, Confluence, Notion…]
- Folder or space for test plans: [link]
- Analytics, heatmap and session recording tools: [GA4, Adobe Analytics, Hotjar, FullStory, Crazy Egg…]

## Test IDs

- Format: `TEST-{issue number}`
- Metric naming: `{element description} [{issue number}]`
- Tracking parameter per experience: `cta={test-id}-{experience letter}`

## Audience segments

List segments exactly as they're named in your platform, so the brief uses names the builder can find.

| Category | Value | Segment name in the platform |
|---|---|---|
| Customer status | Active customer | [segment name] |
| Industry | Financial services | [segment name] |
| Persona | Technical practitioner | [segment name] |
| Persona | Business decision maker | [segment name] |

## Placements and character limits

| Placement | Headline | Body | CTA | Image |
|---|---|---|---|---|
| Site-wide alert banner | none | 40 max | 2 words max | not supported |
| Homepage hero | 50 max | 90 to 150 | primary required, secondary optional | [specs] |
| Homepage card or carousel slide | 55 max | 115 max | none | [specs] |
| Product or solution page hero | 30 to 57 | 145 to 180 | copy and URL | supported |
| Mid-page callout | 33 max, optional | 90 to 124 | 1 to 3 words | not supported |
| Page footer callout | 50 max | 100 max | 1 to 3 words | not supported |

Placements scheduled on an editorial calendar: homepage hero, homepage carousel, alert banner

## Approval rules

- Homepage hero changes need sign-off from [role or name] before launch.
- [Add others, for example legal review for pricing claims]

## Review email

- To: [test team addresses]
- Launch and results announcements go to: [mailing list or channel]

## Launch checklist

Pre-launch
- [ ] Hypothesis or objective confirmed by the requester
- [ ] Test plan created and linked
- [ ] Sizing complete (sample size and duration)
- [ ] Platform brief reviewed by the test team
- [ ] Experiment or personalization built
- [ ] QA complete on all devices and browsers
- [ ] Heatmap snapshots set up
- [ ] Launched

Post-launch
- [ ] Launch announcement sent
- [ ] Added to the team testing calendar

Test end
- [ ] Results analyzed
- [ ] Test plan updated with results and recommendation
- [ ] Results announcement sent
- [ ] Added to the test archive
