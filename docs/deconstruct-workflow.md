# Deconstruct Workflow

This workflow turns a reference novel into reusable writing rules.

## Input

- Plain text chapters (recommended): one file per chapter, or a single file with clear chapter headings.
- Optional: a short note about what to learn (pacing, hooks, POV, style).

## Output

Write results into `deconstruct/`:

- `blueprint.md` : macro structure (promises, arcs, escalation ladders)
- `chapter-cards/CHXXXX.md` : per-chapter cards (goal/conflict/info/hook)
- `chapter-rhythm.csv` : chapter-level table for analysis
- `style-profile.md` : style rules (no copying)
- `characters.md` : character bios + relationship graph
- `hook-catalog.md` : hook patterns and examples (paraphrased)
- `promise-payoff.md` : promises and where they pay off

## Steps

1) Segment the book into chapters (or chunks) and assign stable ids: `CH0001`...
2) For each chapter, create a Chapter Card.
3) Build `chapter-rhythm.csv` by extracting fields from all Chapter Cards.
4) Summarize macro arcs into `blueprint.md`.
5) Derive `style-profile.md` from statistics and observations, not from sentences.

## Guardrails

- Do not copy passages.
- Do not reuse unique names/terms; paraphrase patterns instead.
- The goal is: learn the *rules*, not clone the book.
