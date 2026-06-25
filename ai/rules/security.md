# Security rules

## Purpose

This file defines mandatory security constraints for designing, modifying, reviewing, or generating code in this project.

Security must be considered by default in all production code, especially in authentication, authorization, input validation, persistence, APIs, logging, configuration, and external integrations.

## Scope

These rules apply to:

- application code.
- API endpoints.
- authentication mechanisms.
- authorization checks.
- persistence.
- logging.
- configuration.
- secrets.
- external integrations.
- generated code.
- AI-assisted implementation tasks.

They apply to all production code under `code/`.

## Core principles

- Security must be applied by default, not as an afterthought.
- Sensitive data must be protected.
- Secrets must never be hardcoded.
- Inputs must be validated before use.
- Access must be explicitly controlled.
- Error handling must not leak internal details.
- Logs must not expose secrets or sensitive data.
- Dependencies and integrations must be treated as potential attack surfaces.
- Security decisions must be explicit and documented when they affect the project.

## Mandatory rules

- Secrets must not be stored in source code.
- Secrets must not be committed to version control.
- Credentials, tokens, API keys, private keys, passwords, and connection strings must be provided through secure configuration mechanisms.
- Sensitive data must not be logged.
- Authentication tokens must not be logged.
- Stack traces must not be exposed to API clients.
- Internal exception names must not be exposed to API clients.
- Infrastructure details must not be exposed to API clients.
- All external input must be validated before being used.
- API request validation must be enforced at API boundaries.
- Authorization checks must be performed before protected actions.
- Authentication and authorization concerns must not be bypassed for convenience.
- Passwords must never be stored in plain text.
- Passwords must be hashed using an appropriate password hashing algorithm when password storage is required.
- JWT tokens must be signed using secure algorithms and validated before trust.
- JWT expiration must be enforced.
- JWT claims must be validated according to the project requirements.
- Unsafe deserialization must be avoided.
- SQL queries must be parameterized when SQL is used.
- File paths provided by users must be validated and constrained before file access.
- Error messages must be useful but must not reveal sensitive implementation details.
- Security-sensitive configuration must be documented without exposing secret values.
- Security-relevant behavior must be covered by automated tests according to `ai/rules/testing.md`.
- Dependencies used for security-sensitive behavior must be maintained and appropriate for production use.
- Security reviews must consider OWASP Top 10 risks when implementing or modifying exposed APIs, authentication, authorization, persistence, file handling, or external integrations.

## Additional considerations

JWT-specific implementation guidance belongs in:

- `ai/skills/security/jwt.md`

API security must also follow:

- `ai/rules/api.md`

Persistence security must also follow:

- `ai/rules/persistence.md`

Testing requirements must also follow:

- `ai/rules/testing.md`

Project-specific security documentation should be maintained under:

- `docs/security/`

Security decisions that significantly affect the project should be documented in the appropriate project documentation and, when relevant, as ADRs under:

- `docs/architecture/adr/`

## Rule priority

If there is a conflict between this file and a security skill, this rule file takes priority.

If generated code does not comply with these security rules, the implementation must be corrected.

If a requirement conflicts with these security rules, implementation must stop and the conflict must be clarified before continuing.

Convenience, speed, or temporary implementation must not justify insecure defaults.
