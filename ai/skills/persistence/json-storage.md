# Skill: JSON storage

## Context

Use this skill when implementing, reviewing, or modifying persistence based on JSON files.

This skill is especially relevant when:

- implementing lightweight persistence without a database.
- creating infrastructure repositories backed by JSON files.
- persisting domain entities to local files.
- loading seed or configuration-like data from JSON.
- testing file-based persistence behavior.
- replacing temporary JSON persistence with a future database implementation.

This skill complements:

- `ai/rules/persistence.md`
- `ai/rules/architecture.md`
- `ai/rules/security.md`
- `ai/rules/testing.md`

## Goal

Provide practical guidance for implementing JSON file persistence while keeping file handling, JSON serialization, and storage details isolated inside the infrastructure layer.

The goal is to make JSON persistence simple, explicit, testable, and replaceable.

## Core principles

- Keep JSON and file-system concerns inside infrastructure.
- Do not leak raw JSON dictionaries into domain logic.
- Keep JSON schemas simple and documented.
- Use explicit mapping between JSON data and domain entities.
- Handle missing, empty, and invalid files predictably.
- Use atomic writes when data loss or corruption would be risky.
- Treat JSON persistence as a storage adapter, not as business logic.

## Implementation guidelines

### Reference structure

JSON storage code should be placed under infrastructure.

```text
code/infrastructure/src/<project_name>_infrastructure/
├── persistence/
│   └── json/
│       └── <entity>_json_store.py
├── repositories/
│   └── <entity>_json_repository.py
└── mappers/
    └── <entity>_json_mapper.py
```

Adapt names to the project, but keep responsibilities separated.

### Responsibilities

A JSON repository should:

- implement the repository or persistence port required by the application.
- coordinate reading and writing through the JSON store.
- use mappers to convert between JSON data and domain entities.
- hide file paths, JSON structures, and file-system details from callers.

A JSON store should:

- read files.
- write files.
- handle file existence checks.
- handle encoding.
- isolate low-level file-system operations.

A JSON mapper should:

- convert JSON-compatible dictionaries to domain entities.
- convert domain entities to JSON-compatible dictionaries.
- keep transformation rules explicit.

### JSON schema

Keep the JSON structure simple and stable.

Example:

```json
{
  "items": [
    {
      "id": "employee-1",
      "name": "Ana",
      "department": "IT"
    }
  ]
}
```

Document the schema under:

- `docs/persistence/`

Avoid storing data in a shape that is difficult to validate or migrate.

### Reading data

Handle expected file states explicitly.

Typical cases:

- file exists and contains valid JSON.
- file does not exist.
- file exists but is empty.
- file exists but contains invalid JSON.
- file exists but does not match the expected schema.

The desired behavior for each case should be explicit in code and tests.

### Writing data

Use atomic writes when data loss or corruption would be risky.

A common strategy is:

```text
write to temporary file
flush and close temporary file
replace original file with temporary file
```

Avoid partially written files when persistence correctness matters.

### Mapping

Do not pass raw dictionaries across application or domain boundaries.

Preferred flow:

```text
JSON file
  -> JSON store
    -> JSON mapper
      -> domain entity
```

```text
domain entity
  -> JSON mapper
    -> JSON store
      -> JSON file
```

### Validation

Validate data before creating domain entities when invalid JSON content could break business invariants.

Validate:

- required fields.
- field types.
- allowed values.
- identifiers.
- collection structure.

Do not silently ignore invalid data unless the requirement explicitly defines that behavior.

### Concurrency

JSON files are not a good default for high-concurrency writes.

If concurrent access is possible, define a strategy such as:

- file locks.
- single writer process.
- append-only model.
- migration to a database.
- explicit limitation documented in `docs/persistence/`.

Do not assume JSON file writes are safe under concurrent access.

### Testing

Test JSON persistence behavior with temporary files or isolated test directories.

Test:

- missing file behavior.
- empty file behavior.
- invalid JSON behavior.
- invalid schema behavior.
- successful read behavior.
- successful write behavior.
- mapping from JSON to domain.
- mapping from domain to JSON.
- atomic write behavior when implemented.

Avoid tests that depend on real project data files.

## Examples

### Repository flow

```text
application use case
  -> repository port
    -> JSON repository
      -> JSON store
      -> JSON mapper
```

### JSON mapper example

```python
def to_domain(data: dict) -> Employee:
    return Employee(
        id=EmployeeId(data["id"]),
        name=data["name"],
        department=data["department"],
    )
```

```python
def to_json(employee: Employee) -> dict:
    return {
        "id": str(employee.id),
        "name": employee.name,
        "department": employee.department,
    }
```

### Missing file behavior example

```python
def read_items(path: Path) -> list[dict]:
    if not path.exists():
        return []

    content = path.read_text(encoding="utf-8")

    if not content.strip():
        return []

    return json.loads(content)["items"]
```

The exact behavior must match the project requirement.

## Avoid anti-patterns

Avoid:

- using raw dictionaries as domain objects.
- parsing JSON inside domain services.
- writing files directly from application use cases.
- exposing file paths through domain APIs.
- mixing mapping logic with business logic.
- silently ignoring invalid JSON.
- relying on a JSON file for high-concurrency writes without safeguards.
- using JSON storage as a hidden database without documenting limitations.
- testing JSON persistence against real production files.
- hardcoding absolute file paths in repositories.

## Integration with architecture

JSON storage belongs to the infrastructure layer.

In the reference architecture, JSON persistence code should be placed under:

- `code/infrastructure/`

Application use cases should depend on repository interfaces or persistence ports, not JSON implementations.

Project-specific JSON schema and persistence assumptions should be documented under:

- `docs/persistence/`

Mandatory persistence constraints are defined in:

- `ai/rules/persistence.md`

## When to use this skill

Use this skill when the task requires JSON-storage-specific implementation guidance.

Do not use this skill to define mandatory persistence policy. Mandatory persistence constraints belong in `ai/rules/persistence.md`.
