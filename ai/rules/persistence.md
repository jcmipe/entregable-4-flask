# Persistence rules

## Purpose

This file defines mandatory persistence constraints to ensure that data access remains decoupled from domain logic, application logic, delivery mechanisms, and external technologies.

Persistence must be implemented in a way that supports maintainability, testability, data integrity, and future evolution.

## Scope

These rules apply when designing, modifying, reviewing, or generating code related to:

- databases.
- JSON storage.
- file storage.
- repositories.
- persistence models.
- data mappers.
- external data providers used as data sources.
- migrations and stored data evolution.

They apply to all production code under `code/`.

## Core principles

- Persistence must be abstracted behind explicit ports or repository interfaces.
- Domain logic must not depend on persistence technologies.
- Application logic must not depend on concrete persistence implementations.
- Infrastructure must contain concrete persistence implementations.
- Persistence models must be separate from domain entities.
- Data mapping must be explicit.
- Stored data must remain consistent and valid.
- Persistence design must support evolution without unnecessary coupling.

## Mandatory rules

- Domain code must not import persistence frameworks, database clients, file system clients, or external provider clients.
- Domain entities must not be used as persistence models.
- Persistence models must not be used as domain entities.
- API request or response models must not be used as persistence models.
- External provider models must not be used as persistence models unless explicitly isolated inside infrastructure.
- Persistence access must go through repositories, ports, or equivalent abstractions.
- Repository interfaces or persistence ports must be defined outside concrete infrastructure implementations.
- Repository implementations must be placed in the infrastructure layer.
- Controllers or delivery adapters must not access persistence directly.
- Application use cases must not depend on concrete database, file, or external storage implementations.
- Persistence logic must not contain business rules that belong to the domain layer.
- Data transformations between persistence models and domain models must be explicit.
- Stored data must be validated before being persisted when invalid data could compromise consistency.
- Transactions must be used when multiple persistence operations must succeed or fail as a single unit.
- Partial updates that leave data in an inconsistent state must be avoided.
- Persistence errors must be handled and translated appropriately before crossing architectural boundaries.
- Sensitive data must be protected according to `ai/rules/security.md`.
- Persistence behavior must be covered by automated tests according to `ai/rules/testing.md`.
- Persistence design and relevant assumptions must be documented under `docs/persistence/`.

## Additional considerations

Database-specific implementation guidance belongs in:

- `ai/skills/persistence/database.md`

JSON storage implementation guidance belongs in:

- `ai/skills/persistence/json-storage.md`

Project-specific persistence documentation belongs in:

- `docs/persistence/`

Architecture constraints also apply and are defined in:

- `ai/rules/architecture.md`

Security constraints also apply and are defined in:

- `ai/rules/security.md`

Testing constraints also apply and are defined in:

- `ai/rules/testing.md`

Persistence decisions that significantly affect the project should be documented in the appropriate project documentation and, when relevant, as ADRs under:

- `docs/architecture/adr/`

## Rule priority

If there is a conflict between this file and a persistence skill, this rule file takes priority.

If generated code does not comply with these persistence rules, the implementation must be corrected.

If a requirement conflicts with these persistence rules, implementation must stop and the conflict must be clarified before continuing.

Convenience, speed, or framework defaults must not justify coupling domain or application logic to concrete persistence implementations.
