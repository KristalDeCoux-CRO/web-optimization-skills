# Web optimization skills for Claude

Seven [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that turn the repetitive parts of web strategy and experimentation into a conversation. Built by Kristal DeCoux from the playbooks she has used to run testing programs and web teams.

| Skill | What you give it | What you get back |
|---|---|---|
| [ab-test-readout](ab-test-readout/SKILL.md) | Visitors and funnel counts for a finished test | Significance, confidence intervals, a sample ratio check, the funnel per variant, and a decision-ready readout |
| [ab-test-sizing](ab-test-sizing/SKILL.md) | Baseline conversion, the smallest lift worth detecting, daily traffic | Visitors needed, test duration, and RICE scores to rank ideas |
| [test-archive-search](test-archive-search/SKILL.md) | A proposed test and your test archive | Similar past tests, what they taught, and whether the idea is worth revisiting |
| [web-brief-reviewer](web-brief-reviewer/SKILL.md) | A web project request brief | Scores on the four questions that matter, specific rewrites for vague answers, an effort tier, and a reply to the requester |
| [launch-page-updater](launch-page-updater/SKILL.md) | A launch, report, customer story or event | Which page zones to update, draft copy and FAQ entries, and an SEO checklist |
| [optimization-brief](optimization-brief/SKILL.md) | A test or personalization request from an email, chat or ticket | A tracking issue, a testing platform brief, a test plan, placement copy fitted to character limits and a review email. Set your tools and segments once in `references/team-config.md` |
| [seo-review](seo-review/SKILL.md) | Draft page copy | A meta title and description, JSON-LD schema, and prioritized fixes for search and AI answer engines |

The statistics run in a small Python script (`scripts/abtest.py`, standard library only) so numbers are calculated, not estimated. It uses a two-sided two-proportion z-test, delta-method confidence intervals on relative lift, a chi-square sample ratio mismatch check, and the standard sample size formula for two proportions.

## Install

**Claude.ai or the Claude app:** zip a skill folder and upload it under Settings → Capabilities → Skills (code execution must be on for the two statistics skills).

**Claude Code:** copy a skill folder into `~/.claude/skills/` (or your project's `.claude/skills/`).

## Try it

```
python3 ab-test-readout/scripts/abtest.py readout ab-test-readout/examples/example-input.json
python3 ab-test-sizing/scripts/abtest.py size --baseline 0.03 --mde 0.10 --daily 5000
```

## License

MIT
