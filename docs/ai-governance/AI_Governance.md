# AI Governance

## Purpose

This document defines the standards, structure, and governance model for using AI-assisted software development within the project.

The objective is to:

- Ensure consistency across different AI tools (Codex, Claude, Copilot, etc.).
- Provide a reusable and extensible framework.
- Guarantee software quality, security, and maintainability.
- Enable any developer or team to understand, use, and extend the system.
- Prevent ambiguity and uncontrolled AI behavior.

This governance model is designed to be:

- AI-agnostic.
- Scalable.
- Maintainable.
- Auditable.
- Reproducible.

---

## Repository structure

The repository is organized into three main areas:

- `ai/`: AI operating instructions and governance.
- `docs/`: project documentation and requirements.
- `code/`: production source code.

### AI layer (`ai/`)

Contains all instructions used by AI tools:

- `rules/`: mandatory constraints.
- `commands/`: execution workflows.
- `skills/`: technical knowledge.
- `plans/`: generated implementation plans.
- `prompts/`: stored prompt outputs.

### Documentation layer (`docs/`)

Contains all project documentation:

- requirements.
- architecture.
- domain.
- APIs.
- persistence.
- dependencies.
- testing.
- AI governance.

### Code layer (`code/`)

Contains all production code structured according to the selected architecture, preferably hexagonal architecture when applicable.

---

## Recommended AI governance location

This document should be stored under:

```text
docs/ai-governance/AI_Governance.md
```

### Rationale

- `docs/` is the correct location because this document is project documentation intended for humans and teams.
- `ai/` should contain operational instructions consumed by AI tools.
- `code/` should contain only production code.
- Keeping AI governance under `docs/ai-governance/` makes it auditable, shareable, and easy to maintain.

Recommended structure:

```text
docs/
└── ai-governance/
    ├── AI_Governance.md
    ├── rules.md          # optional future extension
    ├── commands.md       # optional future extension
    └── patterns.md       # optional future extension
```

---

## AI components

The AI system is structured into five main component types.

### Rules (`ai/rules/`)

Rules define mandatory constraints that must always be followed.

Examples:

- architecture rules.
- security rules.
- testing rules.
- clean code rules.
- Python style rules.

Rules answer:

> What must never be violated?

---

### Commands (`ai/commands/`)

Commands define workflows that guide the AI through tasks.

Examples:

- create implementation plan.
- review implementation plan.
- generate code from requirements.
- generate tests.

Commands answer:

> How should tasks be executed?

---

### Skills (`ai/skills/`)

Skills provide technical knowledge and implementation guidance.

Examples:

- Python development.
- REST API design.
- database persistence.
- pytest usage.
- Azure integration.

Skills answer:

> How should something be implemented?

---

### Plans (`ai/plans/`)

Plans contain generated implementation plans.

Plans ensure:

- traceability.
- controlled execution.
- alignment with requirements.
- explicit decision-making before coding.

---

### Prompts (`ai/prompts/`)

Prompts store generated prompts and AI outputs for traceability and reproducibility.

Prompts ensure:

- reproducibility.
- auditability.
- knowledge transfer.
- future review of AI-assisted decisions.

---

## AI workflow

The standard workflow for AI-assisted development is:

1. Define requirement in `docs/requirements/`.
2. Generate implementation plan using:
   - `ai/commands/create-implementation-plan.md`.
3. Review plan using:
   - `ai/commands/review-plan.md`.
4. Select approach and confirm with the user.
5. Decide whether implementation should be generated:
   - step-by-step.
   - all at once.
6. Generate code using:
   - `ai/commands/generate-from-requirements.md`.
7. Decide whether tests should be generated:
   - step-by-step.
   - all at once.
8. Generate tests using:
   - `ai/commands/generate-tests.md`.
9. Store prompts in:
   - `ai/prompts/`.
10. Update documentation in:
   - `docs/`.

At each step, rules under `ai/rules/` must be applied.

---

## Standard structure for AI files

To ensure consistency, maintainability, and compatibility across AI tools, each type of AI file must follow a defined structure.

---

## Rules (`ai/rules/`)

### Purpose

Rules define mandatory constraints that must always be respected.

### Standard structure

Each rule file must include:

1. `Purpose`
   - Explains what the rule enforces.
2. `Scope`
   - Defines when the rule applies.
3. `Core principles`
   - Describes the high-level intent.
4. `Mandatory rules`
   - Lists explicit constraints.
5. `Additional considerations`
   - Optional section for related guidance.
6. `Rule priority`
   - Explains how conflicts are resolved.

### Characteristics

Rule files must:

- be deterministic and explicit.
- avoid ambiguity.
- avoid implementation details.
- avoid workflow steps.
- define constraints that apply across tools and implementations.

### Recommended sections

```md
# <Rule name> rules

## Purpose

## Scope

## Core principles

## Mandatory rules

## Additional considerations

## Rule priority
```

### Rationale

Rules are separated from commands and skills to avoid mixing mandatory constraints with operational workflows or technical knowledge.

This separation helps AI tools apply non-negotiable requirements consistently.

---

## Commands (`ai/commands/`)

### Purpose

Commands define step-by-step workflows to execute tasks.

### Standard structure

Each command file must include:

1. `Purpose`
   - Explains what the command does.
2. `Stage`
   - Indicates where it fits in the AI workflow.
3. `Preconditions`
   - Defines what must exist before execution.
4. `Inputs`
   - Lists required sources of information.
5. `Steps`
   - Provides ordered execution steps.
6. `Output`
   - Defines the expected result.
7. `Constraints`
   - Defines limitations or prohibitions.

### Characteristics

Command files must:

- be procedural.
- guide execution clearly.
- avoid low-level technical explanations.
- avoid duplicating mandatory rules.
- avoid replacing implementation plans.

### Recommended sections

```md
# Command: <command name>

## Purpose

## Stage

## Preconditions

## Inputs

## Steps

## Output

## Constraints
```

### Rationale

Commands provide repeatable workflows. They help AI tools execute tasks consistently without relying on implicit reasoning.

---

## Skills (`ai/skills/`)

### Purpose

Skills provide technical knowledge and implementation guidance.

### Standard structure

Each skill file must include:

1. `Context`
   - Explains when to use the skill.
2. `Goal`
   - Defines what the skill achieves.
3. `Core principles`
   - Lists the key technical concepts.
4. `Implementation guidelines`
   - Explains how to apply the skill.
5. `Examples`
   - Optional but recommended.
6. `Anti-patterns`
   - Explains what to avoid.
7. `Integration with architecture`
   - Explains how the skill fits into the project structure.

### Characteristics

Skill files must:

- be practical.
- provide implementation guidance.
- avoid mandatory policy language when possible.
- avoid defining full workflows.
- avoid duplicating rules.

### Recommended sections

```md
# Skill: <skill name>

## Context

## Goal

## Core principles

## Implementation guidelines

## Examples

## Avoid anti-patterns

## Integration with architecture

## When to use this skill
```

### Rationale

Skills represent reusable technical knowledge. They allow the framework to grow without modifying the core governance model.

---

## Plans (`ai/plans/`)

### Purpose

Plans capture implementation decisions before coding.

### Standard structure

Each implementation plan must include:

- requirement summary.
- scope.
- acceptance criteria.
- assumptions and open questions.
- impact analysis.
- reuse analysis.
- alternative solutions.
- selected approach.
- justification for the selected approach.
- design by layer.
- data flow.
- testing strategy.
- security considerations.
- risks.
- pending user decisions.

### Characteristics

Plans must:

- be complete before implementation starts.
- be reviewed before coding.
- be traceable to requirements.
- identify options and trade-offs.
- avoid implementation before approval.

### Recommended sections

```md
# Implementation plan: <requirement name>

## Requirement summary

## Scope

## Acceptance criteria

## Assumptions and open questions

## Impact analysis

## Reuse analysis

## Alternative solutions

## Selected approach and justification

## Design by layer

## Data flow

## Testing strategy

## Security considerations

## Risks

## Pending user decisions
```

### Rationale

Plans create a human-in-the-loop checkpoint before code generation. This reduces uncontrolled AI behavior and improves traceability.

---

## Prompts (`ai/prompts/`)

### Purpose

Prompts store AI prompts and outputs for traceability and reproducibility.

### Standard structure

Each prompt file should include:

- context.
- input.
- generated output.
- related requirement.
- related plan.
- notes or decisions.

### Characteristics

Prompt files must:

- be stored after execution.
- allow reproducibility.
- avoid sensitive data.
- reference the related requirement or implementation plan.

### Recommended sections

```md
# Prompt: <requirement or task name>

## Context

## Input

## Generated output

## Related requirement

## Related plan

## Notes and decisions
```

### Rationale

Prompt storage supports auditing, future reuse, and knowledge transfer between teams and AI tools.

---

## AI design principles

The governance model is based on the following principles.

### Separation of concerns

Different responsibilities must be isolated:

- rules.
- workflows.
- technical knowledge.
- decisions.
- generated prompts.
- production code.
- project documentation.

This prevents uncontrolled context mixing.

---

### Explicit over implicit

All constraints, expectations, and decisions must be explicitly defined.

AI tools should not infer critical behavior from vague or incomplete instructions.

---

### Determinism

AI-assisted development should be predictable and reproducible.

The same requirement, rules, skills, and plan should produce consistent results.

---

### Traceability

All relevant decisions, plans, and prompts must be stored.

This enables auditing, review, and future maintenance.

---

### Extensibility

The structure must support:

- new technologies.
- new AI tools.
- new workflows.
- new quality gates.
- new infrastructure patterns.

---

### AI-agnostic design

The system must not depend on a single AI provider.

Provider-specific entry points may exist, but they should delegate to common governance files.

Examples:

- Codex: `AGENTS.md`.
- Claude: `CLAUDE.md`.
- GitHub Copilot: `.github/copilot-instructions.md`.

---

### Controlled flexibility

The AI should be guided by rules and workflows without being over-constrained.

The system should support alternatives and trade-offs, but important decisions must be explicit.

---

### Human-in-the-loop

Critical decisions require user confirmation.

This includes:

- selecting between implementation alternatives.
- deciding whether to generate code step-by-step or all at once.
- deciding whether to generate tests step-by-step or all at once.
- approving plans before implementation.

---

## Extending the AI framework

When adding a new technical area such as database, Azure, REST API, CI/CD, Sonar, observability, messaging, or another AI tool:

1. Add mandatory constraints under `ai/rules/` only if they apply generally.
2. Add technical implementation guidance under `ai/skills/`.
3. Add reusable workflows under `ai/commands/` only if the action is repeated.
4. Add generated implementation plans under `ai/plans/`.
5. Add generated prompts under `ai/prompts/`.
6. Add human-readable project documentation under `docs/`.
7. Keep production code under `code/`.

### Example: adding Sonar

Recommended files:

```text
ai/rules/code-quality.md
ai/skills/code-quality/sonar.md
docs/quality/sonar.md
```

### Example: adding CI/CD

Recommended files:

```text
ai/rules/ci-cd.md
ai/skills/devops/ci-cd.md
docs/devops/ci-cd.md
```

---

## Governance checks

Before accepting AI-generated output, verify:

- The requirement exists in `docs/requirements/`.
- A plan exists in `ai/plans/` for non-trivial work.
- The plan has been reviewed.
- The selected approach is explicit.
- Code is generated only under `code/`.
- Documentation is generated only under `docs/`.
- AI instructions are kept under `ai/`.
- Tests are included.
- Test coverage target is at least 80%.
- Security rules are applied.
- OWASP practices are considered where applicable.
- Prompt output is stored under `ai/prompts/`.

---

## References and justification

This governance model is aligned with documented best practices and official references.

### AI coding agent instructions

- OpenAI Codex — Custom instructions with `AGENTS.md`:
  - https://developers.openai.com/codex/guides/agents-md
  - Justification: Codex supports `AGENTS.md` as a repository-level instruction file. This supports using `AGENTS.md` as the common root entry point for AI coding agents.

- AGENTS.md open format:
  - https://agents.md/
  - Justification: Provides a simple open format for guiding coding agents, described as a predictable place to provide context and instructions.

- OpenAI Codex — Agent Skills:
  - https://developers.openai.com/codex/skills
  - Justification: Supports the concept of packaging task-specific instructions and resources as reusable skills.

### Prompt engineering and context structuring

- Anthropic — Prompt engineering overview:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
  - Justification: Supports the use of clear instructions, structured context, examples, roles, and prompt chaining.

- Anthropic — Effective context engineering for AI agents:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - Justification: Supports organizing and managing context intentionally for agentic workflows.

### GitHub Copilot customization

- GitHub Copilot — Adding repository custom instructions:
  - https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
  - Justification: Supports repository-level custom instructions for Copilot.

- GitHub Copilot — Custom instructions:
  - https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions
  - Justification: Explains how custom instructions guide Copilot behavior and how prompt files can define reusable task prompts.

- GitHub Copilot — Custom instructions support:
  - https://docs.github.com/en/copilot/reference/custom-instructions-support
  - Justification: Provides reference information about custom instruction support across Copilot environments.

### Security

- OWASP Secure Coding Practices Quick Reference Guide:
  - https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
  - Justification: Provides technology-agnostic secure coding practices that can be integrated into the development lifecycle.

- OWASP Secure Coding Practices stable checklist:
  - https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/
  - Justification: Includes secure coding checklist areas such as input validation, authentication, access control, error handling, data protection, database security, and file management.

- OWASP API Security Project:
  - https://owasp.org/API-Security/
  - Justification: Provides API-specific security risks and best practices.

- OWASP API Security Top 10 2023:
  - https://owasp.org/API-Security/editions/2023/en/0x11-t10/
  - Justification: Provides the current API Security Top 10 risk categories.

### Software architecture and engineering principles

- Separation of concerns:
  - Used as a general software architecture principle to separate AI instructions, documentation, and production code.

- Dependency inversion:
  - Used to keep high-level business logic independent from infrastructure and technical implementations.

- Hexagonal architecture:
  - Used to separate domain/application logic from infrastructure, APIs, persistence, cloud services, and external systems.

- Clean code and SOLID principles:
  - Used to improve maintainability, readability, testability, and extensibility.

### Testing and quality

- Automated testing:
  - Used to validate generated behavior and reduce regression risk.

- Test coverage threshold:
  - The framework uses a minimum 80% coverage target as a practical quality gate for affected code.

- Deterministic tests:
  - Required to avoid flaky or environment-dependent results.

---

## Maintenance policy

This document must be updated when:

- a new AI tool is introduced.
- a new mandatory rule category is added.
- a new command workflow is added.
- a new reusable skill is added.
- repository structure changes.
- security, testing, or architecture governance changes.

Changes to this document should be reviewed before being adopted by teams.
