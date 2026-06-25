# SOLID rules

## Purpose
Define strict object-oriented design constraints.

## Scope
Applies to all object-oriented code.

## Core principles
- SRP, OCP, LSP, ISP, DIP must guide design decisions.

## Mandatory rules
- Each class must have a single responsibility.
- Classes must not change for multiple reasons.
- Extend behavior via composition over inheritance when possible.
- Subclasses must not break parent behavior.
- Interfaces must be small and focused.
- High-level modules must not depend on low-level modules.
- Use dependency injection for external dependencies.
- Avoid concrete dependencies inside domain/application layers.

## Additional considerations
Related:
- `ai/rules/architecture.md`

## Rule priority
SOLID principles override convenience-based design decisions.
