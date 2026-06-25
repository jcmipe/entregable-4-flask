# Clean code rules

## Purpose
Define strict constraints to ensure code is readable, maintainable, and AI-generatable.

## Scope
Applies to all production code under `code/`.

## Core principles
- Code must be self-explanatory.
- Simplicity over cleverness.
- Consistency across modules.
- Readability is a primary quality attribute.

## Mandatory rules
- Names must express intent clearly (no abbreviations unless standard).
- Functions must do one thing and be <= 20 lines when possible.
- Functions must have <= 3 parameters (else use objects).
- Nesting depth should not exceed 3 levels.
- Avoid boolean flags as parameters.
- No duplicated logic across modules.
- Comments must explain WHY, not WHAT.
- Magic numbers/strings must be replaced with constants.
- Dead code must be removed immediately.
- Code must be formatted consistently.
- Exceptions must not be swallowed silently.

## Additional considerations
Related:
- `ai/rules/solid.md`
- `ai/rules/general.md`

## Rule priority
Readability and simplicity override micro-optimizations.
