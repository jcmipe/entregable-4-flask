# Command: Create implementation plan

## Purpose

Use this command to analyze a requirement and produce a structured implementation plan before writing any code.

This command is mandatory for non-trivial changes affecting multiple layers, persistence, integrations, APIs, security, testing, or architecture.

The plan must create a human-in-the-loop checkpoint before implementation starts.

## Stage

Planning

## Preconditions

- A requirement must exist under `docs/requirements/`.
- The requirement must be readable and sufficiently clear to analyze.
- Applicable rules under `ai/rules/`, including:
  - `ai/rules/plans.md`
- Applicable skills under `ai/skills/` should be consulted when relevant.
- Existing documentation under `docs/` should be reviewed when it affects the requirement.
- Existing code under `code/` should be reviewed when available and relevant.
- No production code should be generated before the plan is created and reviewed.
- Applicable rules under `ai/rules/`, including: `ai/rules/plans.md`

## Inputs

- Requirement file under `docs/requirements/`.
- Applicable rules under `ai/rules/`.
- Applicable skills under `ai/skills/`.
- Existing documentation under `docs/`.
- Existing code under `code/`, when available.
- Existing implementation plans under `ai/plans/`, when related.
- Existing prompt records under `ai/prompts/`, when related.

## Steps

1. Read the requirement document completely.

2. Identify the requirement scope:
   - feature or change to build.
   - business goal.
   - expected behavior.
   - explicit constraints.
   - acceptance criteria.
   - out-of-scope elements.

3. Extract assumptions and open questions:
   - explicit assumptions.
   - implicit assumptions.
   - missing information.
   - ambiguous requirements.
   - decisions that require user confirmation.

4. Identify impacted areas:
   - domain.
   - application.
   - infrastructure.
   - api_rest, if applicable.
   - boot.
   - tests.
   - documentation.
   - dependencies.
   - security.

5. Analyze impact:
   - affected modules.
   - affected layers.
   - affected tests.
   - affected documentation.
   - affected API contracts.
   - affected persistence models or data structures.
   - backward compatibility risks.
   - migration risks.

6. Identify reusable components:
   - existing entities.
   - existing value objects.
   - existing use cases.
   - existing repositories.
   - existing mappers.
   - existing controllers.
   - existing schemas.
   - existing tests.
   - existing patterns or utilities.

7. Propose alternative approaches:
   - low-impact solution:
     - minimal changes.
     - lower risk.
     - faster implementation.
     - lower extensibility.
   - high-impact solution:
     - more extensible.
     - cleaner architecture.
     - better long-term design.
     - higher cost or complexity.

8. Select the recommended approach and justify the decision.

9. Identify applicable design patterns, if any:
   - only when they solve a real problem.
   - document the pattern name.
   - document the usage context.
   - explain why the pattern is justified.
   - avoid forced or unnecessary patterns.

10. Define design by layer:
    - Domain:
      - entities.
      - value objects.
      - domain services.
      - repository interfaces or ports.
      - domain exceptions.
    - Application:
      - use cases.
      - commands or queries, if applicable.
      - mappers.
      - application services, if needed.
    - Infrastructure:
      - repositories.
      - persistence mechanism.
      - external integrations.
      - mappers.
    - API REST, if applicable:
      - controllers.
      - request schemas.
      - response schemas.
      - mappers.
      - status codes and errors.
    - Boot:
      - configuration.
      - dependency wiring.

11. Define data flow:
    - input boundary.
    - application orchestration.
    - domain behavior.
    - persistence or external integration.
    - output boundary.

12. Define testing strategy:
    - unit tests.
    - integration tests.
    - end-to-end tests, if applicable.
    - edge cases.
    - error scenarios.
    - minimum expected coverage.
    - whether tests should be generated step-by-step or all at once.

13. Define security considerations:
    - input validation.
    - authentication, if applicable.
    - authorization, if applicable.
    - secrets handling.
    - sensitive data handling.
    - error exposure.
    - logging risks.
    - OWASP Top 10 risks when applicable.

14. Define documentation impact:
    - project README, if applicable.
    - architecture documentation.
    - API documentation.
    - persistence documentation.
    - testing documentation.
    - dependency documentation.
    - ADRs, if needed.

15. Identify risks:
    - technical risks.
    - requirement risks.
    - architecture risks.
    - security risks.
    - testing risks.
    - integration risks.
    - maintainability risks.

16. Identify user decisions required before implementation:
    - selected approach confirmation.
    - unresolved questions.
    - whether implementation should be generated step-by-step or all at once.
    - whether tests should be generated step-by-step or all at once.

17. Ensure the plan:
    - is traceable to the requirement.
    - does not invent requirements.
    - respects all applicable rules.
    - uses skills only as implementation guidance.
    - maximizes reuse.
    - avoids unnecessary duplication.
    - avoids overengineering.
    - supports future extensibility only when justified.

18. Store the generated plan under: `ai/plans/<area>/<requirement-name>.md`. This must follow the naming and structure rules defined in: `ai/rules/plans.md`

1.  If a final implementation prompt is produced, store it under: `ai/prompts/<area>/<requirement-name>.md`

## Output

The generated implementation plan must include:

- requirement summary.
- scope.
- acceptance criteria.
- assumptions and open questions.
- impact analysis.
- reuse analysis.
- alternative solutions.
- selected approach and justification.
- design by layer.
- data flow.
- testing strategy.
- security considerations.
- documentation impact.
- edge cases and error handling.
- risks.
- design patterns used, if any.
- pending user decisions.
- recommended storage path under `ai/plans/`.

The plan must be written as a Markdown file following the standard plan structure defined in `docs/ai-governance/AI_Governance.md`.

## Constraints

- Do not generate production code.
- Do not generate tests.
- Do not modify existing files except the generated plan file.
- Do not invent requirements.
- Do not ignore open questions.
- Do not skip applicable rules under `ai/rules/`.
- Do not duplicate mandatory rules inside the plan.
- Do not include low-level implementation code unless needed as pseudocode for clarification.
- Do not select an overengineered solution without justification.
- Do not proceed to implementation until the plan has been reviewed and approved.
