# Testing rules

## Purpose

This file defines mandatory testing constraints to ensure code correctness, reliability, maintainability, and confidence in AI-assisted changes.

Testing is a required quality control for production code and must not be skipped without explicit approval and documentation.

## Scope

These rules apply to:

- new features.
- changes to existing functionality.
- bug fixes.
- refactoring.
- integration points.
- generated code.
- AI-assisted implementation tasks.

They apply to all production code under `code/`.

## Core principles

- Tests are mandatory for production behavior.
- Tests must validate behavior, not implementation details.
- Tests must be deterministic and reproducible.
- Tests must be readable and maintainable.
- Tests must provide meaningful confidence, not only coverage numbers.
- Testing effort must be proportional to the risk and complexity of the change.

## Mandatory rules

- Automated tests must be added or updated for every production code change.
- Business logic must be covered by unit tests.
- Integration points must be covered by integration tests when they are implemented or modified.
- REST endpoints must be tested when they expose or change application behavior.
- Persistence behavior must be tested when repositories, storage adapters, or persistence mappings are implemented or modified.
- External integrations must not depend on real external services in automated tests unless explicitly required and documented.
- Tests must include standard use cases, relevant edge cases, and error scenarios.
- Tests must validate observable behavior and expected side effects.
- Tests must not rely on execution order.
- Tests must not rely on uncontrolled randomness.
- Tests must not require manual execution as the only validation mechanism.
- Tests must be executable locally.
- Tests must be suitable for automated execution in CI/CD pipelines.
- Test failures must indicate a real behavior problem or an invalid test assumption.
- Flaky tests must be fixed or removed with explicit justification.
- Coverage must be meaningful and must not be increased through trivial or redundant tests.
- Automated test coverage should be at least 80% unless a different threshold is explicitly approved and documented.
- If tests cannot be added for a change, the reason must be documented.

## Additional considerations

The default Python testing framework is pytest unless the project explicitly defines another framework.

Pytest-specific implementation guidance belongs in:

- `ai/skills/testing/pytest.md`

Test generation workflow belongs in:

- `ai/commands/generate-tests.md`

Project-specific testing documentation belongs in:

- `docs/testing/`

Testing decisions that affect the project should be documented in the appropriate project documentation.

## Rule priority

If there is a conflict between this file and a testing skill, this rule file takes priority.

If generated code does not comply with these testing rules, the implementation must be corrected.

If a requirement conflicts with these testing rules, implementation must stop and the conflict must be clarified before continuing.

Tests must not be skipped for speed, convenience, or incomplete implementation unless explicitly approved and documented.
