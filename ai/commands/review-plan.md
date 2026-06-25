# Command: Review implementation plan

## Purpose

Use this command to review an implementation plan before any code generation.

This command ensures that the plan is complete, consistent, feasible, and aligned with project rules and architecture.

It acts as a quality gate between planning and implementation.

## Stage

Review

## Preconditions

- A requirement exists under `docs/requirements/`.
- A corresponding implementation plan exists under `ai/plans/`.
- The plan has been generated using `create-implementation-plan.md`.
- Applicable rules under `ai/rules/`, including:
  - `ai/rules/plans.md`
- Relevant skills under `ai/skills/` can be consulted if needed.
- No implementation must start before the plan is reviewed.

## Inputs

- Requirement file under `docs/requirements/`.
- Implementation plan under `ai/plans/`.
- Applicable rules under `ai/rules/`.
- Applicable skills under `ai/skills/`.
- Existing code under `code/`, when relevant.
- Existing documentation under `docs/`.

## Steps

1. Read the requirement completely.

2. Read the implementation plan completely.

3. Validate requirement alignment:
   - the plan reflects the requirement.
   - no requirement is missing.
   - no extra functionality is introduced.

4. Validate completeness:
   - scope is defined.
   - acceptance criteria are covered.
   - assumptions are listed.
   - open questions are identified or resolved.
   - all impacted layers are considered.

5. Validate architecture alignment:
   - domain, application, infrastructure separation is respected.
   - dependencies follow correct direction.
   - no layer mixing is proposed.
   - no business logic is placed in controllers or infrastructure.

6. Validate plan structure:
   - correct location under `ai/plans/`
   - correct naming convention
   - correct alignment with requirement name
   - correct area classification
   according to:  `ai/rules/plans.md`   

7. Validate design quality:
   - responsibilities are well defined.
   - naming is clear.
   - reuse is maximized.
   - no unnecessary abstractions.
   - no obvious duplication.

8. Validate alternative analysis:
   - alternatives are considered.
   - selected approach is justified.

9. Validate testing strategy:
   - unit tests are defined.
   - integration tests are defined where needed.
   - edge cases are covered.
   - error scenarios are covered.
    according to:
       - `ai/rules/testing.md`

10. Validate security considerations:
   - input validation is considered.
   - authentication/authorization is considered if needed.
   - sensitive data handling is addressed.
   - OWASP risks are considered where applicable.

11. Validate documentation impact:
    - affected documentation is identified.
    - API documentation is considered.
    - ADRs are proposed when needed.

12. Validate risks:
    - risks are identified.
    - risks are realistic and relevant.

13. Validate implementation feasibility:
    - plan is implementable.
    - no missing critical information.
    - no hidden dependencies.

14. Identify issues:
    - missing elements.
    - inconsistencies.
    - risks not addressed.
    - unclear decisions.

15. Classify issues:
    - blocking (must be resolved before implementation).
    - non-blocking (can be improved later).

16. Provide recommendations:
    - required fixes.
    - suggested improvements.
    - optional optimizations.

17. Determine outcome:
    - approved
    - approved with comments
    - rejected (requires changes)

18. If rejected:
    - specify required changes clearly.
    - do not proceed to implementation.

19. If approved:
    - confirm readiness for implementation.

## Output

A structured review report including:

- summary of evaluation.
- requirement alignment result.
- completeness assessment.
- architecture validation.
- design validation.
- testing validation.
- security validation.
- documentation validation.
- identified issues (blocking / non-blocking).
- recommendations.
- final decision (approved / approved with comments / rejected).

## Constraints

- Do not generate production code.
- Do not modify the plan directly.
- Do not ignore inconsistencies.
- Do not approve incomplete plans.
- Do not assume missing requirements.
- Do not proceed to implementation if blocking issues exist.
