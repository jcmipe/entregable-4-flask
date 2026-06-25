# Entregable 4: Flask, Docker y GitHub Actions

Aplicación web sencilla desarrollada con Python y Flask. Expone una ruta
principal, se empaqueta con Docker y publica su imagen en Docker Hub mediante
GitHub Actions después de ejecutar las pruebas automatizadas.

## Contrato HTTP

```text
GET /
```

Respuesta `200 OK`:

```json
{
  "message": "Hola, esta es la aplicación Flask del Entregable 4."
}
```

La aplicación escucha en `0.0.0.0:5000`.

## Estructura

```text
entregable_4/
├── .github/
│   └── workflows/
│       └── docker-publish.yml
├── code/
│   └── app.py
├── tests/
│   └── test_app.py
├── Dockerfile
├── README.md
└── requirements.txt
```

El código de producción se mantiene bajo `code/` conforme a la gobernanza del
proyecto.

## Requisitos previos

- Python `3.11.15`.
- Entorno virtual disponible en
  `C:\altia\25_IA\Proyectos\.venv`.
- Docker, para construir y ejecutar el contenedor.

## Instalación

Desde PowerShell:

```powershell
cd C:\altia\25_IA\Proyectos\entregable_4
C:\altia\25_IA\Proyectos\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Las dependencias están fijadas a:

- Flask `3.0.3`.
- pytest `8.3.3`.

## Ejecución local

```powershell
python code/app.py
```

La aplicación queda disponible en:

```text
http://localhost:5000/
```

## Pruebas

Las pruebas automatizadas están bajo `tests/` y se ejecutan con:

```powershell
python -m pytest -q
```

La prueba valida el código HTTP `200`, el formato JSON y el mensaje exacto de
la ruta principal, incluidos sus caracteres Unicode.

## Docker

Construir la imagen:

```powershell
docker build -t entregable-4-flask .
```

Ejecutar el contenedor:

```powershell
docker run --rm -p 5000:5000 entregable-4-flask
```

La aplicación queda disponible en `http://localhost:5000/`.

## Pipeline de GitHub Actions

El workflow `.github/workflows/docker-publish.yml` se ejecuta:

- al hacer `push` a la rama `main`;
- manualmente mediante `workflow_dispatch`.

El pipeline:

1. descarga el repositorio;
2. configura Python `3.11.15`;
3. instala las dependencias;
4. ejecuta pytest;
5. construye la imagen Docker;
6. inicia sesión en Docker Hub;
7. publica las etiquetas `latest` y el SHA del commit.

La publicación no continúa si fallan las pruebas o la construcción.

## Secretos de GitHub

Configurar en `Settings > Secrets and variables > Actions`:

- `DOCKERHUB_USERNAME`: usuario de Docker Hub;
- `DOCKERHUB_TOKEN`: token de acceso de Docker Hub con permisos de
  publicación.

Las credenciales no deben almacenarse en el repositorio.

## Imagen publicada

El repositorio de Docker Hub es `entregable-4-flask`.

```text
<usuario-dockerhub>/entregable-4-flask:latest
<usuario-dockerhub>/entregable-4-flask:<sha-del-commit>
```

Descargar y ejecutar la última imagen:

```powershell
docker pull <usuario-dockerhub>/entregable-4-flask:latest
docker run --rm -p 5000:5000 <usuario-dockerhub>/entregable-4-flask:latest
```
