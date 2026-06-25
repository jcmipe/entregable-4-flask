# Skill: Pytest testing

## Context

Use this skill when writing, reviewing, or modifying automated tests using pytest.

This skill is especially relevant when:

- creating unit tests.
- creating integration tests.
- testing domain logic.
- testing application use cases.
- testing repositories.
- testing REST endpoints.
- using fixtures.
- using parametrized tests.
- isolating dependencies with mocks or stubs.
- improving existing test readability or maintainability.

This skill complements:

- `ai/rules/testing.md`
- `ai/commands/generate-tests.md`

## Goal

Provide practical guidance for writing clear, deterministic, maintainable, and useful tests with pytest.

The goal is to ensure that pytest tests validate behavior, support refactoring, and provide confidence without coupling tests to implementation details.

## Core principles

- Each test should verify one clear behavior.
- Tests should be easy to read and understand.
- Tests should follow a consistent structure.
- Tests should avoid unnecessary setup.
- Tests should avoid implementation coupling.
- Test data should be explicit and meaningful.
- Fixtures should reduce duplication without hiding important behavior.
- Parametrization should be used for equivalent scenarios.
- Mocks and stubs should isolate external dependencies when appropriate.

## Implementation guidelines

### Test structure

Use a clear arrange, act, assert structure.

```python
def test_<expected_behavior>():
    # arrange

    # act

    # assert
```

Keep each section simple. If setup becomes difficult to understand, extract only the reusable parts into fixtures or factories.

### Naming

Use descriptive test names that explain the behavior being validated.

```python
def test_create_order_with_valid_data_returns_created_order():
    ...
```

Avoid vague names.

```python
def test1():
    ...
```

### Fixtures

Use fixtures to manage reusable setup.

```python
import pytest

@pytest.fixture
def order():
    return Order(id="1", total=100)
```

Prefer fixtures when they improve readability or avoid meaningful duplication.

Avoid overusing fixtures when inline setup would be clearer.

### Parametrization

Use parametrized tests when the same behavior must be validated with multiple inputs.

```python
import pytest

@pytest.mark.parametrize(
    "price, expected",
    [
        (10, 10),
        (0, 0),
    ],
)
def test_calculate_total_returns_expected_value(price, expected):
    assert calculate_total(price) == expected
```

Use parametrization for equivalent scenarios, not for unrelated behaviors.

### Unit tests

Use unit tests for:

- domain entities.
- value objects.
- domain services.
- application use cases.
- pure functions.
- validation logic.

Unit tests should avoid:

- database access.
- network calls.
- file system dependencies unless explicitly required.
- framework startup.
- real external services.

### Integration tests

Use integration tests for:

- repository implementations.
- persistence mappings.
- REST endpoints.
- external adapter behavior.
- configuration and dependency wiring when relevant.

Integration tests may use:

- test databases.
- temporary files.
- controlled local services.
- mocked external systems.

### Mocks and stubs

Use mocks or stubs to isolate dependencies that are outside the behavior under test.

```python
from unittest.mock import Mock

repo = Mock()
repo.save.return_value = None
```

Prefer simple fakes or stubs when they make the test easier to understand.

Avoid mocking domain objects just to reproduce implementation details.

### Assertions

Use clear assertions that verify meaningful behavior.

Avoid weak assertions.

```python
assert result is not None
```

Prefer specific assertions.

```python
assert result.total == 100
```

When validating collections, assert the relevant values explicitly.

### Error testing

Use `pytest.raises` to validate expected exceptions.

```python
import pytest

def test_validate_price_with_negative_value_raises_error():
    with pytest.raises(ValueError):
        validate_price(-1)
```

Only test exceptions that are part of the expected behavior.

### Test data

Keep test data simple and explicit.

Use factories when object creation is repetitive or complex.

Avoid magic values. If a value is meaningful, name it clearly.

### Test organization

Organize tests close to the module, layer, or feature they validate, according to the project structure.

Common patterns include:

```text
tests/
├── unit/
├── integration/
└── e2e/
```

or layer-specific test folders inside each module.

Follow the structure already established by the project.

## Examples

### Domain test example

```python
def test_order_total_is_sum_of_order_lines():
    order = Order(
        lines=[
            OrderLine(price=10, quantity=2),
            OrderLine(price=5, quantity=1),
        ],
    )

    total = order.total()

    assert total == 25
```

### Use case test example

```python
def test_create_order_saves_order_and_returns_identifier():
    repository = Mock()
    repository.save.return_value = "order-1"

    use_case = CreateOrderUseCase(order_repository=repository)

    result = use_case.execute(CreateOrderRequest(customer_id="customer-1"))

    assert result.order_id == "order-1"
    repository.save.assert_called_once()
```

### Parametrized validation example

```python
import pytest

@pytest.mark.parametrize("invalid_price", [-1, -10, -100])
def test_validate_price_with_negative_value_raises_error(invalid_price):
    with pytest.raises(ValueError):
        validate_price(invalid_price)
```

## Avoid anti-patterns

Avoid:

- testing private methods directly.
- depending on test execution order.
- depending on shared mutable state.
- writing tests that only verify mocks.
- mocking the behavior that should actually be tested.
- using real external services in automated tests without explicit justification.
- creating complex test setup for simple behavior.
- using vague assertions.
- writing tests only to increase coverage.
- duplicating implementation logic inside tests.
- coupling tests to internal implementation details.

## Integration with architecture

Pytest tests should follow the project architecture.

Recommended testing focus by layer:

| Layer | Recommended test type | Notes |
|---|---|---|
| Domain | Unit tests | Test business behavior independently |
| Application | Unit tests | Test use case orchestration with mocked ports |
| Infrastructure | Integration tests | Test adapters, repositories, persistence mappings |
| API REST | Integration or controller tests | Test request/response behavior and delegation |
| Boot | Smoke or integration tests | Test wiring only when useful |

Testing rules are defined in:

- `ai/rules/testing.md`

Test generation workflow is defined in:

- `ai/commands/generate-tests.md`

Project-specific testing documentation should be maintained under:

- `docs/testing/`

## When to use this skill

Use this skill when the task requires pytest-specific implementation guidance.

Do not use this skill to define mandatory testing policy. Mandatory testing constraints belong in `ai/rules/testing.md`.
