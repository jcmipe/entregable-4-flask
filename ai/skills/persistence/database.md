# Skill: Database persistence

## Context

Use this skill when designing, implementing, reviewing, or modifying database persistence.

This skill is especially relevant when:

- designing database schemas.
- creating persistence models.
- implementing repository adapters.
- defining database queries.
- adding indexes.
- managing transactions.
- introducing migrations.
- testing database persistence.
- reviewing whether database concerns are properly isolated.

This skill complements:

- `ai/rules/persistence.md`
- `ai/rules/architecture.md`
- `ai/rules/security.md`
- `ai/rules/testing.md`

## Goal

Provide practical guidance for implementing database persistence while keeping database details isolated from domain and application logic.

The goal is to ensure that database access is explicit, testable, secure, maintainable, and aligned with the project architecture.

## Core principles

- Keep database access in the infrastructure layer.
- Access data through repositories or persistence adapters.
- Keep database models separate from domain entities.
- Use explicit mapping between persistence models and domain models.
- Use transactions when consistency requires atomic operations.
- Design schemas for correctness before optimization.
- Optimize only when there is a justified need.
- Test persistence behavior with appropriate integration tests.

## Implementation guidelines

### Reference structure

Database-related code should be placed under infrastructure.

```text
code/infrastructure/src/<project_name>_infrastructure/
├── persistence/
│   ├── models/
│   ├── migrations/
│   └── database.py
├── repositories/
│   └── <entity>_repository.py
└── mappers/
    └── <entity>_persistence_mapper.py
```

Adapt folder names to the technology used by the project, but keep the responsibility separation.

### Persistence models

Define persistence models separately from domain entities.

Persistence models may contain:

- table or collection names.
- column or field mappings.
- indexes.
- storage-specific identifiers.
- database-specific relationships.
- ORM annotations, when an ORM is used.

Persistence models must not contain business behavior.

### Domain mapping

Use explicit mappers between persistence models and domain entities.

```text
database model -> persistence mapper -> domain entity
domain entity -> persistence mapper -> database model
```

Keep mapping logic close to infrastructure unless the project defines a dedicated mapper location.

### Repositories

Repository implementations should expose domain-friendly methods.

Examples:

```python
def save(order: Order) -> OrderId:
    ...
```

```python
def find_by_id(order_id: OrderId) -> Order | None:
    ...
```

Avoid repository methods that leak database implementation details into application or domain code.

```python
def execute_sql(query: str) -> list[dict]:
    ...
```

### Schema design

Use meaningful names for tables, collections, columns, and fields.

Define:

- identifiers.
- required fields.
- relationships.
- uniqueness constraints.
- indexes when justified.
- data types.
- default values when needed.
- audit fields when required by the project.

Prefer clear and normalized structures unless denormalization is justified by a real use case.

### Queries

Queries should retrieve only the data required by the use case.

Use filtering, pagination, and sorting when result sets can grow.

Avoid:

- unnecessary full-table scans.
- N+1 query patterns.
- loading large object graphs without need.
- duplicating query logic across multiple repositories.

### Transactions

Use transactions when multiple operations must be atomic.

Typical cases:

- creating multiple related records.
- updating state and audit data together.
- reserving resources.
- applying financial, inventory, or workflow changes.
- changing several aggregates that must remain consistent.

Keep transaction boundaries clear and as small as practical.

### Migrations

Use migrations when database schema or stored data changes.

Migration documentation should explain:

- what changes.
- why it changes.
- whether existing data is affected.
- whether rollback is possible.
- any compatibility considerations.

Avoid manual undocumented schema changes.

### Error handling

Translate database-specific errors before they cross architectural boundaries.

Examples:

- unique constraint violation -> domain or application conflict.
- missing record -> not found result or domain-specific error.
- connectivity issue -> infrastructure error.

Do not expose raw database errors to API clients.

### Security

Protect database access according to `ai/rules/security.md`.

Recommended practices include:

- parameterized queries.
- least privilege credentials.
- no secrets in source code.
- no sensitive data in logs.
- input validation before persistence.
- encryption or masking when required.
- careful handling of personally identifiable information.

### Testing

Use integration tests for database repositories when behavior depends on the database.

Test:

- successful persistence.
- retrieval by identifier.
- query filters.
- missing data.
- constraints.
- transaction behavior.
- mapping correctness.
- migration behavior when relevant.

Use isolated test data and avoid tests that depend on execution order.

## Examples

### Repository flow

```text
application use case
  -> repository port
    -> infrastructure repository
      -> persistence model
      -> database
```

### Mapping flow

```text
domain entity
  -> persistence mapper
    -> database model
```

```text
database model
  -> persistence mapper
    -> domain entity
```

### Transaction example

```python
def confirm_order(order_id: OrderId) -> None:
    with transaction:
        order = order_repository.find_by_id(order_id)
        order.confirm()
        order_repository.save(order)
        audit_repository.save_confirmation(order_id)
```

The exact transaction mechanism depends on the database technology used by the project.

## Avoid anti-patterns

Avoid:

- direct database access from controllers.
- direct database access from domain services.
- using ORM models as domain entities.
- putting business rules in repository implementations.
- leaking SQL queries into application use cases.
- exposing database errors directly to API clients.
- duplicating persistence queries across unrelated modules.
- creating indexes without a real query need.
- denormalizing without justification.
- changing schemas without migrations or documentation.
- relying on production data for automated tests.

## Integration with architecture

Database persistence belongs to the infrastructure layer.

In the reference architecture, database code should be placed under:

- `code/infrastructure/`

Repository interfaces or persistence ports should be defined outside concrete infrastructure implementations, according to the project architecture.

Application use cases should depend on abstractions, not database implementations.

Project-specific persistence documentation should be maintained under:

- `docs/persistence/`

Mandatory persistence constraints are defined in:

- `ai/rules/persistence.md`

## When to use this skill

Use this skill when the task requires database-specific design or implementation guidance.

Do not use this skill to define mandatory persistence policy. Mandatory persistence constraints belong in `ai/rules/persistence.md`.
