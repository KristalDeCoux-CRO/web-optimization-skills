---
name: launch-page-updater
description: Decide exactly which parts of a homepage or solution page to update for a launch, report, customer story or event, using a page-zone protocol, and produce the copy changes, FAQ additions and SEO checklist. Use when a product, feature, analyst report, partner, pricing change or event needs to show up on key web pages.
---

# Launch page updater

Key pages decay when every launch rewrites the hero. A page update protocol prevents that: each page is split into zones with different owners and update schedules, and each kind of launch is allowed to touch only certain zones. You apply the protocol so pages stay current without breaking what already ranks and converts.

## 1. Classify the launch

Ask for, or extract from the announcement:
- What is launching, and its launch type (see `references/page-zones.md`)
- Which pages it relates to (homepage, solution pages, platform or product pages)
- Launch date, and whether there's an embargo
- Approved messaging, proof points with sources, links (blog post, docs, report)
- Any metrics or customer names approved for public use

If the launch type is ambiguous (a "major capability" vs. a "minor feature"), ask one question: would a buyer evaluating the product change their decision because of it? If not, treat it as minor.

## 2. Apply the decision guide

Use the decision guide in `references/page-zones.md` to mark each zone on each relevant page as **update**, **optional** or **no change**. Explain each "update" in one line. Hold the line on "no change": the evergreen core (hero headline, value proposition, main pillars) changes only for a rebrand, a category shift or an acquisition, not for individual launches.

## 3. Draft the changes

For each zone marked "update," draft the content, sized to the zone:
- **Announcement bar:** one line, under about 90 characters, with a link
- **What's new module:** a card with a category label (New feature, Report, Integration), a headline, one sentence and a "Read more" link. Name which existing card rotates out to keep the module at two or three cards.
- **Capability grid:** a new or updated card: title, one-sentence description, link
- **Proof layer:** the new stat or logo, with its source cited inline
- **FAQ:** new question-and-answer pairs written in plain, declarative sentences that an AI assistant could quote accurately. Lead each answer with the direct answer.
- **Internal links:** the anchor text and target URL to add, and from which page

Never invent metrics, customer names or claims. Use placeholders such as [approved stat + source] when inputs are missing.

## 4. SEO and AI-readiness checklist

Include only the items this launch triggers:
- Update the meta title or description only if the launch is now the page's primary focus
- Add or update structured data (for example, FAQ content or product details) to match visible content
- Add internal links from the platform page and related solution pages to the launch's main page
- Check that every new stat carries a dated source
- Confirm new copy names the product and category in plain words, so search engines and AI assistants can identify it
- Schedule removal of time-bound items (events, launch banners) so they don't linger

## Output

```
## [Launch]: page updates
Launch type: [type] · Date: [date] · Pages: [list]

| Page | Zone | Action | Why |

### Draft content
Per page and zone, ready to paste.

### SEO and AI-readiness checklist
### Owners and timing
Who updates each zone (from the zone table) and when, including anything to remove later.
```
