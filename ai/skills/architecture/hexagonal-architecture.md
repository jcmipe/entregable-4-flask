# Skill: Hexagonal architecture

## Context

Use this skill when designing, reviewing, or modifying code that follows hexagonal architecture.

This skill is especially relevant when:

- creating a new module.
- adding a new use case.
- integrating persistence.
- integrating external APIs.
- exposing REST endpoints.
- adding CLI, workers, scheduled jobs, or other delivery mechanisms.
- reviewing whether code respects architectural boundaries.

## Goal

Provide practical guidance for applying hexagonal architecture while keeping business logic independent from technical concerns.

The goal is to separate:

- domain logic.
- application orchestration.
- infrastructure adapters.
- delivery adapters.
- bootstrapping and dependency wiring.

## Core principles

- The domain layer contains the business core.
- The application layer orchestrates use cases.
- Ports define what the application needs from external systems.
- Adapters implement those ports using concrete technologies.
- Delivery adapters expose application behavior to the outside world.
- Infrastructure details must remain outside the domain layer.
- Dependencies should point inward.
- Architecture should remain proportional to the requirement.

## Implementation guidelines

### Reference structure

This is the canonical Python structure for this project template:

```text
code/
├── domain/
│   ├── src/
│   │   └── <project_name>_domain/
│   │       ├── entities/
│   │       ├── value_objects/
│   │       ├── services/
│   │       ├── repositories/
│   │       └── exceptions/
│   └── tests/
│
├── application/
│   ├── src/
│   │   └── <project_name>_application/
│   │       ├── use_cases/
│   │       ├── commands/
│   │       ├── queries/
│   │       ├── mappers/
│   │       ├── helpers/
│   │       ├── decorators/
│   │       └── services/
│   └── tests/
│
├── infrastructure/
│   ├── src/
│   │   └── <project_name>_infrastructure/
│   │       ├── persistence/
│   │       ├── repositories/
│   │       ├── external/
│   │       └── mappers/
│   └── tests/
│
├── api_rest/
│   ├── src/
│   │   └── <project_name>_api_rest/
│   │       ├── controllers/
│   │       ├── schemas/
│   │       └── mappers/
│   └── tests/
│
├── boot/
│   ├── src/
│   │   └── <project_name>_boot/
│   │       ├── main.py
│   │       ├── config.py
│   │       └── container.py
│   └── tests/
```

### Dependency direction

Dependencies should follow this direction:

```text
api_rest ─┐
boot     ─┼─> application -> domain
          │
infrastructure -> domain/application ports
```

### Domain layer

The domain layer contains business concepts and business rules.

Recommended contents:

| Element | Location | Description |
|---|---|---|
| Entity | `<project_name>_domain/entities` | Business entity |
| Value object | `<project_name>_domain/value_objects` | Immutable business value |
| Domain service | `<project_name>_domain/services` | Pure domain behavior |
| Repository interface | `<project_name>_domain/repositories` | Persistence abstraction |
| DAO interface | `<project_name>_domain/repositories` | DAO abstraction only when DAO terminology is required |
| Domain exception | `<project_name>_domain/exceptions` | Business exception |

### Application layer

The application layer coordinates business actions.

Recommended contents:

| Element | Location | Description |
|---|---|---|
| Use case | `<project_name>_application/use_cases` | Application action |
| Command | `<project_name>_application/commands` | DDD command, only when DDD is used |
| Query | `<project_name>_application/queries` | DDD query, only when DDD is used |
| Mapper | `<project_name>_application/mappers` | Mapping between application and domain objects |
| Helper | `<project_name>_application/helpers` | Complementary application behavior |
| Decorator | `<project_name>_application/decorators` | Cross-cutting behavior |
| Application service | `<project_name>_application/services` | Coordination support for use cases |

### Infrastructure layer

The infrastructure layer implements technical details.

Recommended contents:

| Element | Location | Description |
|---|---|---|
| Repository implementation | `<project_name>_infrastructure/repositories` | Concrete persistence adapter |
| Persistence model | `<project_name>_infrastructure/persistence` | Database or storage-specific model |
| External service adapter | `<project_name>_infrastructure/external` | Adapter for third-party systems |
| Infrastructure mapper | `<project_name>_infrastructure/mappers` | Mapping between technical and domain objects |

### API REST layer

The API REST layer exposes application behavior through HTTP.

Recommended contents:

| Element | Location | Description |
|---|---|---|
| Controller | `<project_name>_api_rest/controllers` | REST entry point |
| Schema | `<project_name>_api_rest/schemas` | Request and response schema |
| Mapper | `<project_name>_api_rest/mappers` | Mapping between API and application/domain objects |

If the project does not require REST API yet, `code/api_rest/` may exist as a prepared folder without implemented endpoints.

### Boot layer

The boot layer starts the application and wires dependencies.

Recommended contents:

| Element | Location | Description |
|---|---|---|
| Entry point | `<project_name>_boot/main.py` | Application startup |
| Configuration | `<project_name>_boot/config.py` | Runtime configuration |
| Container | `<project_name>_boot/container.py` | Dependency wiring, when needed |

## Examples

### Example dependency flow

```text
REST controller
  -> application use case
    -> domain entity / domain service
    -> repository port
      -> infrastructure repository implementation
```

### Example external integration

```text
application use case
  -> external service port
    -> infrastructure external adapter
      -> third-party API
```

### Example persistence integration

```text
application use case
  -> repository interface
    -> infrastructure repository
      -> persistence model or storage client
```

## Avoid anti-patterns

Avoid:

- putting business logic in controllers.
- putting business logic in repositories.
- using database models as domain entities.
- using API schemas as domain entities.
- importing infrastructure code from the domain layer.
- importing REST framework objects from the application or domain layer.
- creating ports without a real external dependency.
- adding unnecessary abstractions for simple logic.
- mixing bootstrapping code with business logic.
- implementing endpoints before they are required.

## Integration with architecture

This skill supports the mandatory architectural constraints defined in:

- `ai/rules/architecture.md`

Project-specific architecture documentation should be maintained under:

- `docs/architecture/`

Architecture decisions should be documented as ADRs under:

- `docs/architecture/adr/`

Future extensions should be placed according to their responsibility:

| Concern | Recommended location |
|---|---|
| Database support | `code/infrastructure/src/<project_name>_infrastructure/persistence/` |
| Repository implementation | `code/infrastructure/src/<project_name>_infrastructure/repositories/` |
| External API integration | `code/infrastructure/src/<project_name>_infrastructure/external/` |
| Azure integration | `code/infrastructure/src/<project_name>_infrastructure/external/azure/` |
| REST endpoints | `code/api_rest/src/<project_name>_api_rest/` |
| Application orchestration | `code/application/src/<project_name>_application/` |
| Business rules | `code/domain/src/<project_name>_domain/` |

## When to use this skill

Use this skill when the task requires architectural design, code organization, module placement, dependency review, or implementation guidance related to hexagonal architecture.

Do not use this skill to define mandatory policy constraints. Mandatory constraints belong in `ai/rules/architecture.md`.
