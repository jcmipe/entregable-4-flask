# API rules

## Purpose

This file defines mandatory API constraints for designing, modifying, reviewing, or generating APIs in this project.

APIs must be consistent, predictable, documented, and safe to consume by internal or external clients.

## Scope

These rules apply to:

- REST APIs.
- API controllers.
- request and response schemas.
- API error handling.
- API documentation.
- API versioning.
- API integrations exposed by this project.

They apply to all production API code under `code/`.

## Core principles

- APIs must expose application behavior, not internal implementation details.
- APIs must be consistent across modules.
- APIs must be easy to understand and consume.
- APIs must use HTTP semantics correctly.
- APIs must avoid leaking domain, persistence, or infrastructure internals.
- APIs must be documented with an explicit contract.
- APIs must be designed with backward compatibility in mind when consumers already exist.

## Mandatory rules

- REST APIs must use resource-oriented endpoint names.
- REST APIs must use HTTP methods according to their semantic meaning.
- API endpoints must delegate business behavior to application use cases.
- API controllers must not contain business rules.
- API request models must not be used as domain entities.
- API response models must not be used as domain entities.
- Persistence models must not be exposed directly through APIs.
- External provider models must not be exposed directly through APIs.
- API responses must be explicit and stable.
- API errors must follow a consistent error format.
- API validation errors must be clear and actionable.
- APIs that return collections must define pagination when result size can grow.
- APIs that support filtering or sorting must use consistent parameter naming.
- APIs must not expose sensitive data unless explicitly required and approved.
- APIs must not expose stack traces, internal exception names, secrets, tokens, or infrastructure details.
- Public or shared APIs must be documented using OpenAPI.
- Breaking API changes must be avoided when consumers already exist.
- Breaking API changes must be documented and coordinated when unavoidable.
- API versioning must be used when compatibility cannot be preserved.
- APIs must include traceability support when required by the project, such as request or correlation identifiers.
- API behavior must be covered by automated tests according to `ai/rules/testing.md`.

## Additional considerations

REST-specific implementation guidance belongs in:

- `ai/skills/api/rest/rest-api.md`

Project-specific API documentation belongs in:

- `docs/apis/`

OpenAPI specifications, when present, should be maintained under the project documentation or API contract location defined by the project.

API decisions that affect consumers should be documented in the appropriate project documentation and, when relevant, as ADRs under:

- `docs/architecture/adr/`

## Rule priority

If there is a conflict between this file and an API skill, this rule file takes priority.

If generated code does not comply with these API rules, the implementation must be corrected.

If a requirement conflicts with these API rules, implementation must stop and the conflict must be clarified before continuing.
