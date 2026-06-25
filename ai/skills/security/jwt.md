# Skill: JWT authentication in Python

## Context

Use this skill when implementing, reviewing, or modifying JSON Web Token authentication in Python.

This skill is especially relevant when:

- generating JWT access tokens.
- validating JWT access tokens.
- defining token claims.
- protecting REST endpoints.
- mapping authenticated users to application context.
- testing authentication behavior.
- reviewing token-related security risks.

This skill complements:

- `ai/rules/security.md`
- `ai/rules/api.md`
- `ai/rules/testing.md`

## Goal

Provide practical guidance for implementing standard JWT authentication in Python using simple, secure, and maintainable defaults.

The preferred approach is:

- signed JWT access tokens.
- explicit expiration.
- strict validation.
- secure configuration.
- clear authentication error handling.
- no refresh token complexity unless a requirement explicitly introduces it.

This skill does not define an OAuth2, refresh token, token rotation, blacklist, or multi-tenant authentication model.

## Core principles

- Treat JWTs as bearer credentials.
- Validate tokens before trusting any claim.
- Keep signing secrets or keys outside source code.
- Use secure and explicit algorithms.
- Enforce expiration.
- Validate required claims.
- Do not store sensitive data inside JWT payloads.
- Keep authentication logic outside domain logic.
- Keep framework-specific authentication code at the delivery or infrastructure boundary.
- Keep business authorization decisions explicit in application or domain logic when required.

## Implementation guidelines

### Recommended token type

Use JWTs as access tokens.

Recommended properties:

| Property | Recommendation |
|---|---|
| Token type | Bearer access token |
| Expiration | Required |
| Signature | Required |
| Algorithm | Explicitly configured |
| Secret/key location | Secure configuration |
| Sensitive data in payload | Not allowed |
| Refresh tokens | Not included unless required |

### Token location

For REST APIs, clients usually send the token in the `Authorization` header.

```text
Authorization: Bearer <access_token>
```

Do not send JWTs in URLs.

### Claims

Use a small and explicit set of claims.

Recommended claims:

| Claim | Purpose |
|---|---|
| `sub` | Subject or authenticated user identifier |
| `exp` | Expiration time |
| `iat` | Issued-at time |
| `iss` | Issuer, when useful |
| `aud` | Audience, when useful |
| `roles` | Optional role list if needed by the project |

Do not include:

- passwords.
- secrets.
- API keys.
- personal data not required by the API.
- large authorization models.
- infrastructure details.

### Expiration

JWT access tokens must expire.

Use a short expiration appropriate for the application.

Examples:

- 15 minutes.
- 30 minutes.
- 1 hour.

The exact duration must be defined by project requirements or configuration.

### Signing algorithm

Use an explicit algorithm.

For simple internal systems, an HMAC algorithm such as `HS256` may be sufficient when the secret is strong and protected.

For distributed systems or systems where token verification is performed by multiple services, asymmetric algorithms such as `RS256` may be more appropriate.

Do not accept tokens signed with unexpected algorithms.

Do not accept unsigned tokens.

### Configuration

Store JWT configuration outside source code.

Typical configuration values:

```text
JWT_SECRET
JWT_ALGORITHM
JWT_EXPIRATION_MINUTES
JWT_ISSUER
JWT_AUDIENCE
```

Secrets must not be committed to version control.

Use environment variables, secret managers, or another secure configuration mechanism defined by the project.

### Token generation

Token generation should:

- receive an authenticated user identity.
- include only required claims.
- set expiration.
- sign with the configured algorithm.
- avoid embedding sensitive data.

Example:

```python
from datetime import datetime, timedelta, timezone
import jwt

def create_access_token(
    subject: str,
    secret: str,
    algorithm: str,
    expiration_minutes: int,
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,
        "iat": now,
        "exp": now + timedelta(minutes=expiration_minutes),
    }

    return jwt.encode(payload, secret, algorithm=algorithm)
```

### Token validation

Token validation should:

- extract the bearer token.
- verify the signature.
- enforce expiration.
- validate the expected algorithm.
- validate required claims.
- validate issuer and audience when configured.
- reject malformed tokens.
- reject expired tokens.
- reject tokens with missing required claims.

Example:

```python
import jwt

def decode_access_token(
    token: str,
    secret: str,
    algorithm: str,
) -> dict:
    return jwt.decode(
        token,
        secret,
        algorithms=[algorithm],
        options={
            "require": ["sub", "exp"],
        },
    )
```

When issuer or audience are configured:

```python
import jwt

def decode_access_token_with_issuer_and_audience(
    token: str,
    secret: str,
    algorithm: str,
    issuer: str,
    audience: str,
) -> dict:
    return jwt.decode(
        token,
        secret,
        algorithms=[algorithm],
        issuer=issuer,
        audience=audience,
        options={
            "require": ["sub", "exp", "iss", "aud"],
        },
    )
```

### Bearer token extraction

Extract the bearer token carefully.

Example:

```python
def extract_bearer_token(authorization_header: str | None) -> str:
    if not authorization_header:
        raise AuthenticationError("Missing Authorization header.")

    prefix = "Bearer "

    if not authorization_header.startswith(prefix):
        raise AuthenticationError("Invalid Authorization header.")

    token = authorization_header[len(prefix):].strip()

    if not token:
        raise AuthenticationError("Missing bearer token.")

    return token
```

### Error handling

Authentication errors should be translated into API responses without exposing internal details.

Typical mapping:

| Error | HTTP status |
|---|---|
| Missing token | `401 Unauthorized` |
| Malformed token | `401 Unauthorized` |
| Invalid signature | `401 Unauthorized` |
| Expired token | `401 Unauthorized` |
| Missing required claim | `401 Unauthorized` |
| Authenticated but not allowed | `403 Forbidden` |

Do not expose:

- token contents.
- raw library exceptions.
- stack traces.
- signing secrets.
- validation internals.

### Architecture placement

JWT authentication should be placed at the delivery or infrastructure boundary.

Recommended responsibilities:

| Concern | Recommended location |
|---|---|
| Extract Authorization header | API REST layer |
| Decode and validate token | security/auth adapter or infrastructure support |
| Build authenticated user context | application boundary or API mapper |
| Business authorization decisions | application or domain logic when required |
| JWT configuration | boot/config layer |

Domain entities should not depend on JWT libraries or token formats.

### Authorization

JWT authentication proves identity and possibly carries coarse-grained roles or scopes.

Do not assume authentication alone is authorization.

Protected use cases should explicitly check permissions when the requirement demands it.

Role checks should be consistent and testable.

### Testing

Test JWT behavior with automated tests.

Recommended tests:

- token is created with `sub` and `exp`.
- token can be decoded with correct secret and algorithm.
- expired token is rejected.
- malformed token is rejected.
- token signed with wrong secret is rejected.
- missing bearer header is rejected.
- invalid bearer format is rejected.
- missing required claims are rejected.
- protected endpoint rejects unauthenticated requests.
- protected endpoint accepts valid authenticated requests.

Use test secrets, not production secrets.

## Examples

### Authentication flow

```text
HTTP request
  -> API authentication middleware/dependency
    -> extract bearer token
      -> validate JWT
        -> create authenticated context
          -> call application use case
```

### Minimal payload example

```json
{
  "sub": "user-1",
  "iat": 1710000000,
  "exp": 1710001800
}
```

### Role payload example

```json
{
  "sub": "user-1",
  "roles": ["admin"],
  "iat": 1710000000,
  "exp": 1710001800
}
```

Only include roles if the project requires role-based authorization.

### Protected endpoint behavior

```text
GET /profile
Authorization: Bearer <access_token>
```

Possible responses:

```text
200 OK
```

```text
401 Unauthorized
```

```text
403 Forbidden
```

## Avoid anti-patterns

Avoid:

- accepting unsigned JWTs.
- accepting unexpected algorithms.
- disabling expiration validation.
- storing secrets in source code.
- logging JWTs.
- storing passwords or secrets in JWT payloads.
- trusting claims before signature validation.
- using JWT payload as a domain entity.
- putting JWT library code inside the domain layer.
- returning raw token validation errors to API clients.
- implementing refresh tokens without an explicit requirement.
- using long-lived access tokens without justification.
- sending JWTs in URLs.
- duplicating JWT validation logic across controllers.

## Integration with architecture

JWT authentication belongs at the API, infrastructure, or boot boundary depending on framework and project structure.

In the reference architecture:

- API extraction belongs under `code/api_rest/`.
- Token validation support may belong under `code/infrastructure/`.
- Configuration belongs under `code/boot/`.
- Business authorization belongs in application or domain logic when required.

Mandatory security constraints are defined in:

- `ai/rules/security.md`

API behavior must also comply with:

- `ai/rules/api.md`

Testing must comply with:

- `ai/rules/testing.md`

## When to use this skill

Use this skill when the task requires JWT-specific implementation or review guidance in Python.

Do not use this skill to define mandatory security policy. Mandatory security constraints belong in `ai/rules/security.md`.
