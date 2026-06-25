# Architecture rules

## Purpose

This file defines mandatory architectural constraints that must be followed when designing, modifying, or generating code for this project.

## Scope

These rules apply to all production code under `code/`, all architecture-related decisions, and all AI-assisted implementation tasks.

They must be applied together with:

- `ai/rules/solid.md`
- `ai/rules/clean-code.md`
- `ai/rules/testing.md`
- `ai/rules/security.md`

## Core principles

The project must follow a clear separation of responsibilities between:

- domain logic.
- application orchestration.
- infrastructure adapters.
- delivery adapters.
- application bootstrapping.

The preferred architecture is hexagonal architecture when applicable.

Dependencies must point inward, keeping business logic independent from technical details.

## Mandatory rules

- Production code must be placed under `code/`.
- Project documentation must be placed under `docs/`.
- AI operational instructions must be placed under `ai/`.
- Business logic must not depend on infrastructure, delivery mechanisms, frameworks, databases, file systems, or external APIs.
- Application logic may depend on domain logic.
- Infrastructure adapters may depend on application and domain abstractions.
- Delivery adapters must delegate to application use cases and must not contain business rules.
- Bootstrapping code must be isolated from business logic.
- Dependency wiring must not be placed inside domain logic.
- Framework-specific code must not leak into the domain layer.
- Persistence-specific models must not be used as domain entities.
- API schemas or request/response models must not be used as domain entities.
- New modules must respect the architectural boundaries defined by the selected architecture.
- If hexagonal architecture is used, the implementation guidance must follow `ai/skills/architecture/hexagonal-architecture.md`.

## Additional considerations

Implementation details, reference folder structures, naming conventions, and examples must be documented in skills or project documentation, not in this rule file.

Architecture decisions that are specific to this project should be documented under `docs/architecture/`.

Relevant architecture decisions should be captured as ADRs under `docs/architecture/adr/`.

## Rule priority

If there is a conflict between this file and a skill, this rule file takes priority.

If there is a conflict between architecture rules and generated code, the code must be corrected to comply with these rules.

If a requirement appears to violate these rules, implementation must stop and the conflict must be clarified before continuing.
