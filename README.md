# Novel OS

A doc-driven framework for long-form web novel production.

This repo implements a repeatable pipeline inspired by "long-form writing skill" workflows:
- externalized memory (project docs live in the repo)
- mandatory pre-chapter reads (reduce drift / hallucination)
- mandatory post-chapter updates (make continuity improve over time)

## What You Get

- A project folder structure for a novel
- Markdown templates for:
  - market scan
  - style guide
  - story bible
  - characters + relationship map
  - master outline + chapter outlines
  - progress tracking (the memory hub)
  - review report (reader/editor)
  - consistency checklist
- A chapter lifecycle checklist (READ -> PLAN -> WRITE+CHECK -> UPDATE)

## How To Use

1) Copy `templates/project/` to a new working folder (or use it as-is).
2) Fill in docs top-down:
   - `market-scan.md`
   - `project-brief.md`
   - `style-guide.md`
   - `world-bible.md`
   - `characters.md`
   - `outline.md`
3) For each chapter:
   - read required docs (see `docs/chapter-gates.md`)
   - write/update `chapter-outline/XXXX.md`
   - draft `chapters/XXXX.md`
   - run self-checks and write `reviews/XXXX.review.md`
   - append to `progress-tracking.md`

## Templates

See `templates/`.

## License

MIT
