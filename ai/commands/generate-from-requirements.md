# Command: Generate implementation from requirements

## Purpose

Use this command to generate production-ready implementation code from an approved implementation plan derived from a requirement.

This command is responsible for implementation only. Test generation must be performed separately with `ai/commands/generate-tests.md`.

This command must only be used after the plan has been created, reviewed, and explicitly approved or approved with comments.

## Stage

Implementation

## Preconditions

- A requirement exists under `docs/requirements/`.
- A corresponding approved plan exists under `ai/plans/`.
- All open questions in the plan have been resolved.
- Review comments, if any, have been incorporated as implementation constraints.
- Applicable rules under `ai/rules/` must be available.
- Relevant skills under `ai/skills/` have been identified.
- No code generation must start without an approved plan.

## Inputs

- Requirement file under `docs/requirements/`.
- Approved implementation plan under `ai/plans/`.
- Plan review result, when available.
- Applicable rules under `ai/rules/`.
- Applicable skills under `ai/skills/`.
- Existing code under `code/`.
- Existing documentation under `docs/`.
- Existing prompts under `ai/prompts/`, when relevant.

## Steps

1. Read the approved implementation plan completely.

2. Validate that:
   - all decisions are resolved.
   - no open questions remain.
   - the approach is clearly defined.
   - review comments are understood and enforceable.

3. Identify implementation scope:
   - modules to create or modify.
   - layers impacted: domain, application, infrastructure, api_rest, boot.
   - dependencies required.

4. Map plan design to concrete implementation:
   - classes.
   - functions.
   - modules.
   - folder structure.
   - public interfaces.
   - persistence adapters.
   - facades or entry points required by the requirement.

5. Preserve responsibility separation:
   - do not collapse different domain concepts into a single class or module unless explicitly justified.
   - separate use cases by responsibility.
   - separate repositories or ports by aggregate or persistence responsibility when the domain model requires it.
   - if a unified repository is used, justify why it does not violate single responsibility or architecture rules.

6. Implement by layer:

   Domain:
   - entities.
   - value objects.
   - domain services.
   - repository interfaces or ports.
   - domain exceptions.

   Application:
   - use cases grouped by responsibility.
   - commands or queries if applicable.
   - mappers.
   - application services when needed.
   - facades only when required by the plan or requirement.

   Infrastructure:
   - repository implementations.
   - persistence stores.
   - external integrations.
   - infrastructure mappers.

   API REST, if applicable:
   - controllers.
   - schemas.
   - mappers.

   Boot:
   - configuration.
   - dependency wiring.
   - executable entry points.

7. Ensure:
   - no business logic leaks into controllers, CLI entry points, facades, or repositories.
   - domain is independent from infrastructure.
   - application depends on abstractions, not concrete infrastructure.
   - mapping is explicit.
   - required facade modules delegate to application use cases.
   - persistence access is isolated inside infrastructure.

8. Apply implementation-related rules:
   - architecture.
   - clean code.
   - SOLID.
   - API, when applicable.
   - persistence.
   - security.
   - python style.
   - documentation, when documentation is modified.

9. Use skills only for implementation guidance:
   - do not copy skill content into code.
   - apply patterns only when justified.
   - do not introduce abstractions that are not required by the requirement, plan, or architecture.

10. Reuse existing components when possible.

11. Avoid:
   - duplication.
   - overengineering.
   - unnecessary abstractions.
   - mixing layers.
   - creating test files.

12. Do not generate or modify tests.

   Test generation must be performed separately using:

   - `ai/commands/generate-tests.md`

13. Update documentation only when required by the implementation:
   - README, if required by the requirement.
   - architecture docs, if the implemented structure differs from current documentation.
   - persistence docs, if persistence structure or behavior changes.
   - API docs, if API contracts are implemented or changed.

14. Validate implementation structure:
   - production code is under `code/`.
   - required modules from the requirement exist.
   - required modules respect their assigned responsibility.
   - architecture boundaries are respected.
   - no test files were generated or modified.

15. Provide validation commands for the user to run manually:
   - syntax or compilation command, when applicable.
   - application execution command, when applicable.
   - test command to be used later after `generate-tests.md`.

   Do not execute commands unless the user explicitly asks you to do so.

16. Optionally store prompt under:
   - `ai/prompts/<area>/<requirement-name>.md`

## Output

- Production implementation code under `code/`.
- Updated documentation under `docs/`, only when required.
- Optional prompt record under `ai/prompts/`.
- A summary of files created or modified.
- A summary of architecture decisions applied.
- A list of validation commands for the user to run manually.
- A note confirming that tests were not generated and must be handled with `ai/commands/generate-tests.md`.

## Constraints

- Do not start without an approved plan.
- Do not invent requirements.
- Do not ignore rules.
- Do not bypass architecture.
- Do not mix layers.
- Do not generate test files.
- Do not modify existing test files.
- Do not execute compilation, application, or test commands unless the user explicitly asks for automatic execution.
- Do not generate partial implementations unless the user explicitly requested step-by-step implementation by layer.
- Do not leave TODOs without justification.
