# AGENTS.md

Operational notes for this repo.

## Deconstruct Outputs (Required)

Goal: deconstruct a reference novel so we can reproduce its *engine* (structure, pacing, hook mechanics, style) while writing an original book (no copying of plot/passage/names).

The deconstruct workflow must produce these 7 outputs:

1) Structure Blueprint
   - File: `deconstruct/blueprint.md`
   - Contents: opening promise, escalation ladder, arc/volume map, reward loop, key beats.

2) Chapter Rhythm Model
   - File: `deconstruct/chapter-rhythm.csv`
   - Contents: per-chapter goal/conflict/action/cost/info gain/emotional peak/hook.

3) Hook System
   - File: `deconstruct/hook-catalog.md`
   - Contents: hook types, triggers, patterns, distribution notes (paraphrased).

4) Information & Foreshadowing System
   - Files: `deconstruct/promise-payoff.md`, `deconstruct/foreshadow-ledger.md`, `deconstruct/exposition-rules.md`
   - Contents: promise->payoff table, foreshadow seeds/resolutions, exposition rules.

5) Character Engine
   - Files: `deconstruct/character-archetypes.md`, `deconstruct/relationship-dynamics.md`
   - Contents: protagonist drive structure, antagonist ladder, relationship dynamics.

6) Style Profile
   - File: `deconstruct/style-profile.md`
   - Contents: narrative distance, sentence rhythm, transitions, anti-AI rules, forbidden list.

7) Writing Spec (Executable)
   - File: `deconstruct/writing-spec.md`
   - Contents: hard gates/checklists, per-chapter must-haves, per-arc targets, quality thresholds.

## Guardrails

- Learn rules, do not copy passages.
- Do not reuse unique named entities or distinctive phrases.
- Prefer paraphrased hook descriptions over quoting.
