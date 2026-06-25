# Skill: REST API design

## Context

Use this skill when designing, reviewing, documenting, or modifying REST APIs.

This skill is especially relevant when:

- creating new REST endpoints.
- changing existing REST endpoints.
- defining request or response schemas.
- defining API error responses.
- defining pagination, filtering, or sorting.
- documenting APIs with OpenAPI.
- reviewing API consistency.
- integrating API controllers with application use cases.

This skill complements:

- `ai/rules/api.md`
- `ai/rules/security.md`
- `ai/rules/testing.md`

## Goal

Provide practical guidance for designing REST APIs that are clear, consistent, maintainable, and suitable for large projects.

The preferred style is classic REST:

- resource-oriented endpoints.
- correct HTTP methods.
- correct HTTP status codes.
- simple JSON payloads.
- explicit error responses.
- documented contracts.

Use enterprise patterns only when they add real value, such as OpenAPI contracts, pagination standards, traceability, and backward compatibility rules.

## Core principles

- Model endpoints around resources.
- Use nouns for resources, not actions.
- Use HTTP methods to express actions.
- Keep responses simple and explicit.
- Keep API models separate from domain and persistence models.
- Prefer predictable conventions over custom endpoint behavior.
- Keep controllers thin.
- Validate input at API boundaries.
- Document stable API contracts.
- Preserve backward compatibility when clients already consume the API.

## Implementation guidelines

### Resource naming

Use plural nouns for collections.

```text
GET /vehicles
GET /vehicles/{vehicleId}
POST /vehicles
PATCH /vehicles/{vehicleId}
DELETE /vehicles/{vehicleId}
```

Avoid action-based endpoints when a resource-oriented design is possible.

```text
POST /createVehicle
POST /vehicle/delete
```

Prefer nested resources only when the relationship is clearly scoped.

```text
GET /vehicles/{vehicleId}/documents
POST /vehicles/{vehicleId}/documents
```

Avoid excessive nesting.

```text
GET /customers/{customerId}/orders/{orderId}/lines/{lineId}/taxes/{taxId}
```

### HTTP methods

Use HTTP methods consistently.

| Method | Use |
|---|---|
| `GET` | Retrieve a resource or collection |
| `POST` | Create a resource or execute a non-idempotent operation |
| `PUT` | Replace a resource |
| `PATCH` | Partially update a resource |
| `DELETE` | Delete or deactivate a resource |

Do not use `GET` for operations that change state.

### HTTP status codes

Use standard status codes.

| Status | Use |
|---|---|
| `200 OK` | Successful retrieval or update with response body |
| `201 Created` | Resource created |
| `202 Accepted` | Request accepted for asynchronous processing |
| `204 No Content` | Successful operation without response body |
| `400 Bad Request` | Invalid request |
| `401 Unauthorized` | Authentication required or invalid |
| `403 Forbidden` | Authenticated but not allowed |
| `404 Not Found` | Resource not found |
| `409 Conflict` | Business or state conflict |
| `422 Unprocessable Entity` | Semantically invalid input, if used by project convention |
| `500 Internal Server Error` | Unexpected server error |

Use one consistent convention for validation errors across the project.

### Request bodies

Use request bodies for `POST`, `PUT`, and `PATCH`.

Example create request:

```json
{
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2024
}
```

Avoid sending large or complex filter objects in `GET` bodies. Use query parameters for normal filtering.

### Response bodies

Return explicit JSON objects.

Example single resource response:

```json
{
  "id": "vehicle-1",
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2024
}
```

For collection responses, use a consistent structure when pagination is required.

```json
{
  "items": [
    {
      "id": "vehicle-1",
      "brand": "Toyota",
      "model": "Corolla"
    }
  ],
  "page": {
    "number": 1,
    "size": 20,
    "totalElements": 125,
    "totalPages": 7
  }
}
```

Do not wrap every response in generic envelopes unless the project explicitly requires it.

Avoid this as a default convention:

```json
{
  "success": true,
  "data": {},
  "errors": []
}
```

### Error format

Use a consistent error format.

Recommended structure:

```json
{
  "code": "VEHICLE_NOT_FOUND",
  "message": "Vehicle not found.",
  "details": [
    {
      "field": "vehicleId",
      "message": "No vehicle exists with the provided identifier."
    }
  ],
  "traceId": "request-123"
}
```

The error response should include:

| Field | Description |
|---|---|
| `code` | Stable machine-readable error code |
| `message` | Human-readable summary |
| `details` | Optional detailed validation or field errors |
| `traceId` | Optional request identifier for troubleshooting |

Do not expose:

- stack traces.
- internal exception class names.
- database errors.
- secrets.
- tokens.
- infrastructure details.

### Validation

Validate request input at the API boundary.

Validation errors should clearly identify:

- invalid field.
- reason.
- expected format or constraint when useful.

Example validation error:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "The request contains invalid fields.",
  "details": [
    {
      "field": "year",
      "message": "Year must be greater than or equal to 1900."
    }
  ],
  "traceId": "request-123"
}
```

### Pagination

Use pagination for collections that can grow.

Recommended query parameters:

```text
GET /vehicles?page=1&size=20
```

Recommended response metadata:

```json
{
  "items": [],
  "page": {
    "number": 1,
    "size": 20,
    "totalElements": 0,
    "totalPages": 0
  }
}
```

Use consistent indexing across the project. If the project uses zero-based pagination, document it clearly.

### Filtering

Use query parameters for simple filters.

```text
GET /vehicles?brand=Toyota&year=2024
```

Use consistent naming and avoid ambiguous parameters.

For complex searches, use a dedicated search endpoint only when query parameters become insufficient.

```text
POST /vehicles/search
```

Use `POST /search` only when the search request has complex structured criteria, not for simple filtering.

### Sorting

Use a consistent sorting format.

Recommended simple format:

```text
GET /vehicles?sort=createdAt,desc
```

For multiple fields:

```text
GET /vehicles?sort=brand,asc&sort=createdAt,desc
```

### Versioning

Do not version APIs unnecessarily.

Use versioning when:

- consumers already exist.
- backward compatibility cannot be preserved.
- external clients depend on stable contracts.
- multiple API contracts must coexist.

Recommended versioning style for larger projects:

```text
/api/v1/vehicles
```

Avoid changing the meaning of existing fields or removing fields without a migration strategy.

### Backward compatibility

Prefer additive changes.

Usually safe:

- adding optional response fields.
- adding optional request fields.
- adding new endpoints.
- adding new enum values only when consumers can tolerate them.

Potentially breaking:

- removing fields.
- renaming fields.
- changing field types.
- changing error formats.
- changing pagination format.
- changing status codes.
- changing required fields.
- changing endpoint semantics.

Document breaking changes and coordinate them with consumers.

### Traceability

When traceability is required, support request or correlation identifiers.

Common headers:

```text
X-Request-Id
X-Correlation-Id
```

Return the trace identifier in error responses when useful.

### OpenAPI

Document public or shared REST APIs with OpenAPI.

The OpenAPI contract should define:

- endpoints.
- HTTP methods.
- request schemas.
- response schemas.
- error schemas.
- status codes.
- authentication requirements.
- pagination parameters.
- filtering and sorting parameters when supported.

The OpenAPI contract should be kept aligned with implementation.

### Controller responsibilities

Controllers should:

- receive HTTP requests.
- validate and map request data.
- call application use cases.
- map application results to API responses.
- return HTTP responses.

Controllers should not:

- contain business rules.
- access repositories directly.
- call external providers directly.
- perform complex orchestration.
- expose persistence models.
- expose domain internals unnecessarily.

### Mapping

Use explicit mapping between:

- API request models and application input models.
- application output models and API response models.
- domain errors and API errors.

Avoid using the same class for API, application, domain, and persistence concerns.

## Examples

### Create resource

```text
POST /vehicles
```

Request:

```json
{
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2024
}
```

Response:

```text
201 Created
Location: /vehicles/vehicle-1
```

```json
{
  "id": "vehicle-1",
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2024
}
```

### Partial update

```text
PATCH /vehicles/vehicle-1
```

Request:

```json
{
  "model": "Corolla Touring Sports"
}
```

Response:

```text
200 OK
```

```json
{
  "id": "vehicle-1",
  "brand": "Toyota",
  "model": "Corolla Touring Sports",
  "year": 2024
}
```

### Delete resource

```text
DELETE /vehicles/vehicle-1
```

Response:

```text
204 No Content
```

### Collection with pagination

```text
GET /vehicles?page=1&size=20&sort=createdAt,desc
```

Response:

```json
{
  "items": [
    {
      "id": "vehicle-1",
      "brand": "Toyota",
      "model": "Corolla"
    }
  ],
  "page": {
    "number": 1,
    "size": 20,
    "totalElements": 125,
    "totalPages": 7
  }
}
```

## Avoid anti-patterns

Avoid:

- action-based endpoint names when resource-oriented names are possible.
- using `GET` for state-changing operations.
- exposing persistence models directly.
- exposing external provider models directly.
- placing business logic in controllers.
- returning inconsistent error formats.
- returning stack traces to clients.
- using generic response envelopes by default.
- changing API contracts without documenting impact.
- hiding all errors behind `500 Internal Server Error`.
- creating versioned APIs without a real compatibility need.
- implementing endpoints before the requirement is clear.

## Integration with architecture

REST APIs belong to the delivery layer.

In the reference architecture, REST code should be placed under:

- `code/api_rest/`

REST controllers should call application use cases located under:

- `code/application/`

Business rules should remain in:

- `code/domain/`

Technical integrations should remain in:

- `code/infrastructure/`

API rules are defined in:

- `ai/rules/api.md`

Project-specific API documentation should be maintained under:

- `docs/apis/`

## When to use this skill

Use this skill when the task requires REST-specific implementation or design guidance.

Do not use this skill to define mandatory API policy. Mandatory API constraints belong in `ai/rules/api.md`.
