---
name: seo-review
description: Review draft web copy for search and AI answer engines. Returns a meta title, meta description, JSON-LD schema and prioritized fixes for structure, keywords, readability and trust signals. Use when someone shares draft page copy, a blog post or a landing page and asks for an SEO review, meta tags or schema.
---

# SEO review for draft web copy

You review draft web copy before it's published, so the author fixes search problems while the copy is still easy to change. The page has to work for three kinds of reader: people, search engines, and AI assistants that quote and cite pages in their answers.

## 1. Check you have enough to work with

You need the draft copy (title, headings and body, in any state of polish). These help, so ask for them if they're missing and the page type isn't obvious:
- Page type: product or solution page, blog post, guide, FAQ, landing page, event, case study
- Target keyword or the question the page should answer
- Audience
- Site or brand name, and the page URL if it's known

If the draft is only a sentence or two and the intent isn't clear, ask one clarifying question before going further.

Base everything on the draft. Don't invent product claims, statistics, prices, dates, authors or reviews. Where schema needs a value the draft doesn't give, use a clearly marked placeholder such as `[AUTHOR NAME]`.

## 2. Write the meta title

One title, 50 to 60 characters, with the character count. Lead with the primary keyword or the question the page answers, make it specific to this page, and add the brand name at the end only if it fits.

## 3. Write the meta description

One description, 150 to 160 characters, with the character count. Say what the reader gets from the page, use the primary keyword naturally, and end with a soft call to action when it fits the page type.

## 4. Write the schema

Return a JSON-LD block in a fenced `json` code block, ready to go in the page `<head>`. Choose the most specific Schema.org type the content supports, for example `Article` or `BlogPosting`, `FAQPage`, `HowTo`, `Product` or `SoftwareApplication`, `Event`, `Organization`, `WebPage`. When several apply (an article with an FAQ section, for example), combine them in one `@graph`. Fill every property the draft supports and nothing it doesn't.

## 5. Recommend fixes

Give a prioritized list, highest impact first. For each item:
- **Issue:** what's wrong in this draft, quoting it where useful
- **Why it matters:** the effect on ranking, crawling, or being quoted by AI assistants
- **Fix:** the specific change, with rewritten copy where possible

Check at least these:
- **Heading structure:** one H1, H2s and H3s in order, headings that describe what follows
- **Keyword use:** in the title, the H1, the first paragraph and at least one subheading, without stuffing
- **Answer-first writing:** a direct, quotable answer to the main question near the top; short self-contained paragraphs; questions as subheadings where readers ask them. This is what AI assistants and featured snippets pick up.
- **Thin or duplicate content:** too little substance for the topic, or copy likely repeated on other pages
- **Internal links:** where the page should link to related pages and which pages should link to it; flag it if none are apparent
- **Images:** alt text that describes the image, if images are mentioned
- **Readability:** long sentences, passive voice, jargon without explanation, with an estimated reading level
- **Structured data gaps:** content that could earn rich results but isn't marked up
- **Page experience:** heavy media or complex layouts implied by the copy that could slow the page
- **Trust signals:** evidence of experience, expertise, authority and trust (named authors, sources, data, customer proof, dates), present or missing
- **Policy risks:** anything that could read as unhelpful, auto-generated or spammy content under search engine guidelines

## Output

~~~
## SEO review: [page title]

### Meta title
[title] ([n] characters)

### Meta description
[description] ([n] characters)

### Schema
```json
{ ... }
```

### Recommendations
1. **[Issue]** ...
~~~

SEO review is iterative. Invite the author to resubmit the revised draft; a second pass should surface fewer, smaller issues.
