# Documentation rules

## Purpose

Define mandatory documentation constraints to ensure that project documentation is clear, consistent, current, and aligned with the actual state of the system.

This file defines documentation rules only. It must not contain project documentation, functional specifications, API details, architecture decisions, or implementation guides.

## Scope

These rules apply to:

- project documentation under `docs/`.
- architecture documentation.
- API documentation.
- persistence documentation.
- testing documentation.
- dependency documentation.
- requirement documentation.
- ADRs.
- inline code documentation when needed.
- AI-generated documentation.

They apply whenever code, requirements, architecture, APIs, tests, persistence, dependencies, or operational behavior are created or modified.

## Core principles

- Documentation must reflect the current state of the system.
- Documentation must be clear, concise, and useful.
- Documentation must have a single source of truth.
- Documentation must not duplicate rules, skills, or commands.
- Documentation must be updated together with the change it describes.
- Documentation must be understandable without requiring hidden context.
- Documentation must distinguish between requirements, decisions, implementation details, and operational instructions.

## Mandatory rules

- Project documentation must be stored under `docs/`.
- Documentation rules must remain under `ai/rules/documentation.md`.
- Documentation content must not be duplicated inside rules, skills, commands, or agent instructions.
- Rules must reference documentation locations instead of copying documentation content.
- Skills must provide implementation guidance and must not become project documentation.
- Commands must define workflows and must not become project documentation.
- Requirements must be documented under `docs/requirements/`.
- Architecture documentation must be documented under `docs/architecture/`.
- Architecture decisions must be documented as ADRs under `docs/architecture/adr/` when they affect design, structure, dependencies, or long-term maintainability.
- API documentation must be documented under `docs/apis/`.
- Persistence documentation must be documented under `docs/persistence/`.
- Testing documentation must be documented under `docs/testing/` when test strategy, tools, execution, or conventions are relevant.
- Dependency documentation must be documented under `docs/dependencies/` when dependencies are added, removed, or significantly changed.
- Documentation must be updated when related code changes.
- Documentation must be updated when API contracts change.
- Documentation must be updated when persistence structures or data formats change.
- Documentation must be updated when architecture decisions change.
- Documentation must be updated when dependencies change.
- Documentation must not describe functionality that does not exist.
- Documentation must not contain obsolete information.
- Documentation must not contradict requirements, plans, code, or ADRs.
- Documentation must not invent business behavior.
- Documentation must use consistent names for modules, layers, entities, endpoints, and concepts.
- Documentation must clearly mark assumptions, open questions, or pending decisions when they exist.
- Documentation must be reviewed when generated or modified by AI.

## Additional considerations

Documentation should be concise and structured.

When documentation needs examples, examples should be directly related to the project or clearly marked as illustrative.

When a topic is governed by an external reference, such as OWASP or PEP 8, the documentation should reference the external source conceptually and avoid duplicating extensive external content.

Related files:

- `ai/rules/general.md`
- `ai/rules/architecture.md`
- `ai/rules/api.md`
- `ai/rules/persistence.md`
- `ai/rules/testing.md`
- `ai/commands/create-implementation-plan.md`

## Rule priority

If there is a conflict between documentation rules and project documentation, the documentation must be corrected to comply with these rules.

If there is a conflict between documentation and implementation, the source of truth must be determined as follows:

1. Approved requirement.
2. Approved implementation plan.
3. ADR, when the conflict concerns an architecture decision.
4. Current production code.
5. Project documentation.

Documentation must never override approved requirements, approved plans, ADRs, or production code.

Outdated documentation must be corrected or removed.
