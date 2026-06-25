# Command: Generate tests

## Purpose

Use this command to generate or update automated tests for an approved implementation plan or for an existing code change.

This command is responsible for test generation only. Production implementation must be performed separately with `ai/commands/generate-from-requirements.md`.

This command ensures that test generation is aligned with project rules, architecture, and the selected testing strategy.

## Stage

Testing

## Preconditions

- A requirement exists under `docs/requirements/` when tests are linked to a requirement.
- An approved implementation plan exists under `ai/plans/` when tests are part of a planned change.
- Applicable rules under `ai/rules/` must be available.
- Production code exists under `code/`.
- Applicable testing rules under `ai/rules/testing.md` are available.
- Applicable Python testing guidance under `ai/skills/testing/pytest.md` is available when pytest is used.
- Relevant architecture, API, persistence, security, and style rules are available when they affect the tests.
- No tests should be generated from assumptions that are not present in the requirement, plan, or existing code.

## Inputs

- Requirement file under `docs/requirements/`, when applicable.
- Approved implementation plan under `ai/plans/`, when applicable.
- Existing production code under `code/`.
- Existing tests under the corresponding test folders.
- Applicable rules under `ai/rules/`.
- Applicable skills under `ai/skills/`.
- Existing documentation under `docs/`, when relevant.
- Existing prompt records under `ai/prompts/`, when relevant.

## Steps

1. Read the requirement, if available.

2. Read the approved implementation plan, if available.

3. Read the production code to be tested.

4. Read existing tests related to the same module, feature, or layer.

5. Identify the expected behavior:
   - standard use cases.
   - edge cases.
   - validation scenarios.
   - error scenarios.
   - security-relevant scenarios.
   - persistence or integration scenarios, when applicable.

6. Identify the affected layer:
   - domain.
   - application.
   - infrastructure.
   - api_rest.
   - boot.

7. Select the appropriate test type:
   - unit tests for domain and application behavior.
   - integration tests for persistence, adapters, API behavior, and dependency wiring when relevant.
   - smoke tests for bootstrapping when useful.
   - end-to-end tests only when explicitly required or justified.

8. Define test boundaries:
   - what must be tested directly.
   - what must be mocked, stubbed, or faked.
   - what must not be tested directly.
   - which external dependencies must be isolated.

9. Reuse existing test utilities:
   - fixtures.
   - factories.
   - builders.
   - test clients.
   - mocks.
   - temporary storage helpers.

10. Generate or update tests according to:
    - `ai/rules/testing.md`
    - `ai/skills/testing/pytest.md`
    - `ai/rules/python-style.md`
    - `ai/rules/clean-code.md`

11. Ensure tests validate behavior, not implementation details.

12. Ensure tests are deterministic:
    - no dependency on execution order.
    - no uncontrolled randomness.
    - no real external services unless explicitly required.
    - no production data.
    - no hardcoded environment-specific paths.

13. Add or update unit tests:
    - domain entities.
    - value objects.
    - domain services.
    - application use cases.
    - pure functions.
    - validation logic.

14. Add or update integration tests when needed:
    - repository implementations.
    - persistence mappings.
    - external adapters with mocked or controlled dependencies.
    - REST endpoints.
    - dependency wiring.

15. Add or update security-related tests when relevant:
    - authentication.
    - authorization.
    - invalid tokens.
    - invalid input.
    - sensitive data exposure.
    - error handling.

16. Add or update API tests when relevant:
    - request validation.
    - response structure.
    - status codes.
    - error format.
    - pagination, filtering, or sorting when applicable.

17. Add or update persistence tests when relevant:
    - successful save and retrieval.
    - missing data.
    - invalid data.
    - mapping correctness.
    - transactional behavior when applicable.
    - JSON file edge cases when JSON storage is used.

18. Validate that generated tests:
    - are readable.
    - have descriptive names.
    - use clear arrange, act, assert structure.
    - use fixtures only when they improve clarity.
    - use parametrization for equivalent scenarios.
    - avoid excessive mocking.
    - avoid testing private implementation details.

19. Review coverage expectations:
    - confirm that acceptance criteria are covered.
    - confirm that edge cases are covered.
    - confirm that error scenarios are covered.
    - confirm that test coverage is meaningful.
    - confirm that the expected minimum coverage is respected when measurable.

20. Update testing documentation when the test strategy, tools, or execution instructions change.

21. Provide the command for the user to run the test suite manually.

    Do not execute the test command unless the user explicitly asks you to do so.

22. If a final test-generation prompt is produced, store it under:
    - `ai/prompts/<area>/<requirement-name>-tests.md`

## Output

The command must produce or update:

- unit tests.
- integration tests, when required.
- API tests, when required.
- persistence tests, when required.
- security-related tests, when required.
- test fixtures, factories, or helpers when they reduce duplication and improve clarity.
- testing documentation under `docs/testing/`, when needed.
- optional prompt record under `ai/prompts/`.

The output must include a short summary of:

- test files created or modified.
- behaviors covered.
- edge cases covered.
- error scenarios covered.
- tests intentionally not added, with justification.
- command to run the generated tests manually.

## Constraints

- Do not generate tests for behavior that is not defined by the requirement, plan, or existing code.
- Do not use tests to define new requirements.
- Do not rely on real external services unless explicitly required and documented.
- Do not rely on production data.
- Do not write flaky tests.
- Do not test private methods directly unless there is no better option and the reason is documented.
- Do not duplicate implementation logic inside tests.
- Do not create trivial tests only to increase coverage.
- Do not bypass `ai/rules/testing.md`.
- Do not ignore architecture boundaries when choosing what to mock or integrate.
- Do not leave failing tests without clear explanation.
- Do not execute tests unless the user explicitly asks for automatic execution.
