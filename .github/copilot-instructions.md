# Copilot instructions

## Purpose

This file defines how GitHub Copilot must behave when generating code in this project.

## Instructions

Copilot must follow the governance model defined in:

- AGENTS.md

Copilot must not:

- generate code without an approved implementation plan
- bypass the workflow defined in AGENTS.md
- ignore rules under ai/rules/
- invent requirements or behavior not defined in requirements or plans

Copilot must:

- respect the project architecture
- follow coding standards
- generate tests when required
- maintain consistency with existing code

If there is a conflict between Copilot suggestions and project governance:

- governance rules always take priority
