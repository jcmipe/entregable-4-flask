# Prompt: implement plan for activity

## Context

Implementacion de la Actividad usando `ai/commands/generate-from-requirements.md`
despues de la revision del plan con resultado `approved with comments`.

## Input

```text
Act according to `AGENTS.md`.

Use the command:

- `ai/commands/generate-from-requirements.md`

Implement the requirement:

- `docs/requirements/task/entregable_4/activity.md`

Using the approved plan:

- `ai/plans/task/entregable_4/activity.md`

Apply all applicable rules under `ai/rules/`.
Use relevant skills under `ai/skills/`.

Do not invent requirements.
Do not bypass the approved plan.
Update documentation if required.

Store this prompt under:

- `ai/prompts/task/entregable_4/03_implement_plan.md`
```

## Generated output

Se implementó la fase de producción del Entregable 4 conforme al requisito y
al plan aprobado.

Archivos creados:

- `code/app.py`
- `requirements.txt`
- `Dockerfile`
- `.dockerignore`
- `.github/workflows/docker-publish.yml`
- `README.md`

Decisiones aplicadas:

- Aplicación Flask ubicada en `code/app.py`.
- Ruta `GET /` con respuesta JSON y propiedad `message`.
- Escucha en `0.0.0.0:5000`.
- Python fijado a `3.11.15`.
- Dependencias fijadas a `Flask==3.0.3` y `pytest==8.3.3`.
- Imagen basada en `python:3.11.15-slim`.
- Workflow activado por `push` a `main` y `workflow_dispatch`.
- Pruebas configuradas como puerta previa a la construcción y publicación.
- Publicación en
  `<usuario-dockerhub>/entregable-4-flask:latest` y en la etiqueta del SHA.
- Credenciales consumidas mediante `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`.
- Documentación de ejecución local, Docker, CI/CD y secretos añadida al
  `README.md`.

No se generaron ni modificaron tests porque
`ai/commands/generate-from-requirements.md` exige que esa actividad se realice
separadamente mediante `ai/commands/generate-tests.md`.

No se ejecutaron la aplicación, pytest ni Docker porque el comando de
implementación exige proporcionar los comandos de validación para ejecución
posterior, salvo solicitud explícita de ejecución automática.

## Related requirement

- `docs/requirements/task/entregable_4/activity.md`

## Related plan

- `ai/plans/task/entregable_4/activity.md`

## Validation commands

```powershell
C:\altia\25_IA\Proyectos\.venv\Scripts\python.exe -m py_compile code\app.py
C:\altia\25_IA\Proyectos\.venv\Scripts\python.exe code\app.py
C:\altia\25_IA\Proyectos\.venv\Scripts\python.exe -m pytest -q
docker build -t entregable-4-flask .
docker run --rm -p 5000:5000 entregable-4-flask
```

## Notes

La implementación queda preparada para la fase posterior de generación de
tests. Hasta que exista `tests/test_app.py`, el paso pytest del workflow no
debe considerarse validado.
