# Skill: Python development

## Context

Use this skill when writing or modifying Python code.

This skill complements:
- `ai/rules/python-style.md` (style)
- `ai/rules/clean-code.md` (readability)
- `ai/rules/solid.md` (design)

## Goal

Produce idiomatic, maintainable, and testable Python code.

---

## Core principles

- Prefer readability over cleverness.
- Use explicit code instead of implicit behavior.
- Keep code simple and maintainable.

---

## Data modeling

- Use dataclasses for structured data.

Example:

```python 
from dataclasses import dataclass

@dataclass
class Order:
    id: str
    total: float
```
- Use value objects for domain concepts when appropriate.

---

## Functions

- Prefer pure functions when possible.
- Avoid side effects unless necessary.
- Return values instead of modifying global state.

---

## Classes

- Use classes when modeling behavior or state.
- Avoid unnecessary classes for simple logic.
- Keep classes small and focused.

---

## Error handling

- Raise exceptions when errors occur.
- Use specific exception types.
- Do not return error codes.

Example:

```python 
def validate_price(price: float) -> None:
    if price < 0:
        raise ValueError("Price must be non-negative")
```
---

## Dependency handling

- Pass dependencies explicitly (dependency injection).
- Avoid hidden dependencies or global variables.

Example:

```python 
def create_order(repo, order):
    repo.save(order)
```

---

## Working with collections

- Use list comprehensions when simple and readable.
- Prefer clarity over compactness.

---

## Immutability

- Prefer immutable data structures when possible.
- Avoid modifying input parameters.

---

## Configuration

- Use environment variables for configuration.
- Do not hardcode environment-specific values.

---

## Logging

- Use the standard logging library.
- Avoid print statements in production code.

---

## Testing compatibility

- Write code that is easy to test:
  - no hidden dependencies
  - no global state
  - clear inputs and outputs

---

## Avoid anti-patterns

- Avoid mutable default arguments.
- Avoid global state.
- Avoid deep nesting.
- Avoid overly complex list comprehensions.

---

## Integration with architecture

- Domain code must remain independent of frameworks.
- Infrastructure code can use libraries but must be isolated.
- Application layer orchestrates logic.

---

## When to use this skill

Use this skill when:

- writing new Python modules
- refactoring existing code
- implementing use cases
- integrating with external systems
