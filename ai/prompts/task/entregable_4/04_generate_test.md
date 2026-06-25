# Prompt: generate tests for activity

## Context

Generacion de pruebas automatizadas para la Actividad usando
`ai/commands/generate-tests.md`.

## Input

```text
Act according to `AGENTS.md`.

Use the command:

- `ai/commands/generate-tests.md`

Generate or update tests for:

- `docs/requirements/task/entregable_4/activity.md`

Using the approved plan:

- `ai/plans/task/entregable_4/activity.md`

And the implemented code under:

- `code/`

Apply:

- `ai/rules/testing.md`
- `ai/skills/testing/pytest.md`

Cover use cases, edge cases, and error scenarios.
Do not invent behavior.

Store this prompt under:

- `ai/prompts/task/entregable_4/04_generate_test.md`
```

## Generated output

Se generaron las pruebas automatizadas del Entregable 4:

- `tests/test_app.py`

También se actualizó:

- `README.md`

Comportamientos cubiertos:

- `GET /` responde con código HTTP `200`.
- La respuesta tiene formato JSON.
- El cuerpo contiene únicamente la propiedad `message`.
- El mensaje coincide exactamente con el saludo aprobado, incluidos sus
  caracteres Unicode.

No se añadieron pruebas de persistencia, autenticación, autorización,
integraciones externas, rutas adicionales ni métodos HTTP no definidos porque
están fuera del requisito y del plan aprobado.

No se ejecutó pytest durante esta fase porque
`ai/commands/generate-tests.md` indica que el comando debe proporcionarse para
ejecución manual salvo solicitud explícita de ejecución automática.

## Related requirement

- `docs/requirements/task/entregable_4/activity.md`

## Related plan

- `ai/plans/task/entregable_4/activity.md`

## Test command

```powershell
C:\altia\25_IA\Proyectos\.venv\Scripts\python.exe -m pytest -q
```
