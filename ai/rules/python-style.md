# Python style rules

## Purpose

Define mandatory Python coding standards to ensure that Python code is readable, consistent, maintainable, and suitable for AI-assisted development.

This file defines Python style constraints only. Python implementation guidance belongs in the corresponding Python skill.

## Scope

These rules apply to all Python code under `code/`, including:

- production code.
- tests.
- scripts.
- bootstrapping code.
- generated code.
- AI-assisted code changes.

## Core principles

- Python code must be explicit and readable.
- Python code must follow established Python conventions.
- Python code must be consistently formatted.
- Python code must be typed where practical and meaningful.
- Python code must avoid unnecessary cleverness.
- Python code must be easy to test and refactor.

## Mandatory rules

- Python code must follow PEP 8 unless a project-specific convention explicitly overrides it.
- Use `snake_case` for variables, functions, methods, and modules.
- Use `PascalCase` for classes.
- Use `UPPER_SNAKE_CASE` for constants.
- Use meaningful and intention-revealing names.
- Use type hints in public functions, methods, and constructors.
- Use return type hints when the return value is not obvious.
- Avoid untyped public APIs unless explicitly justified.
- Keep line length within the project limit.
- The default maximum line length is 100 characters unless the project config defines another value.
- Imports must be grouped and ordered consistently.
- Unused imports are not allowed.
- Unused variables are not allowed.
- Avoid global mutable state.
- Avoid wildcard imports.
- Prefer f-strings for string formatting.
- Exceptions must be explicit and meaningful.
- Do not swallow exceptions silently.
- Avoid broad `except Exception` blocks unless there is a clear reason and the error is handled safely.
- Use context managers for resources that must be opened and closed.
- Avoid mutable default arguments.
- Avoid hidden side effects in functions.
- Keep modules focused on a single responsibility.
- Keep functions small and focused according to `ai/rules/clean-code.md`.
- Tests must follow the same Python style rules as production code unless a testing convention explicitly requires otherwise.

## Additional considerations

Python-specific implementation guidance belongs in:

- `ai/skills/python/python.md`

Related rules:

- `ai/rules/clean-code.md`
- `ai/rules/testing.md`
- `ai/rules/architecture.md`
- `ai/rules/security.md`

Project-specific formatter, linter, or type-checker configuration should be documented under:

- `docs/dependencies/`
- `docs/testing/`, when related to test execution

Examples and practical Python implementation patterns should be placed in skills, not duplicated in this rule file.

## Rule priority

If there is a conflict between this file and a Python skill, this rule file takes priority.

If there is a conflict between this file and general clean-code guidance, the stricter rule should be applied unless it conflicts with project configuration.

If generated Python code does not comply with these rules, the code must be corrected.

Personal preference must not override project Python style rules.
