# Entregable 4: guía de uso y verificación

Esta documentación acompaña al requisito
[`activity.md`](activity.md) y describe el estado implementado del Entregable 4.

## Resultado

La solución incluye:

- aplicación Flask en `code/app.py`;
- prueba automatizada en `tests/test_app.py`;
- dependencias fijadas en `requirements.txt`;
- imagen definida mediante `Dockerfile`;
- pipeline en `.github/workflows/docker-publish.yml`;
- publicación en GitHub y Docker Hub.

Enlaces:

- GitHub: <https://github.com/jcmipe/entregable-4-flask>
- Docker Hub: <https://hub.docker.com/r/jcmira/entregable-4-flask>

## Contrato HTTP

La aplicación escucha en `0.0.0.0:5000` y expone:

```text
GET /
```

Respuesta `200 OK`:

```json
{
  "message": "Hola, esta es la aplicación Flask del Entregable 4."
}
```

## Requisitos

- Python `3.11.15`.
- Entorno virtual:
  `C:\altia\25_IA\Proyectos\.venv`.
- Docker Desktop para construir o ejecutar la imagen.

Dependencias fijadas:

- Flask `3.0.3`;
- pytest `8.3.3`.

## Ejecución local

Desde PowerShell:

```powershell
cd C:\altia\25_IA\Proyectos\entregable_4
C:\altia\25_IA\Proyectos\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python code/app.py
```

La aplicación estará disponible en:

```text
http://localhost:5000/
```

## Pruebas automatizadas

Ejecutar:

```powershell
python -m pytest -q
```

La prueba comprueba:

- estado HTTP `200`;
- respuesta JSON;
- propiedad `message`;
- saludo literal definido por el requisito, incluidos sus caracteres Unicode.

El valor esperado se declara dentro de la prueba para que un cambio accidental
del mensaje de producción provoque un fallo verificable.

Resultado verificado:

```text
1 passed
```

## Docker local

Construir:

```powershell
docker build -t entregable-4-flask .
```

Ejecutar:

```powershell
docker run --rm -p 5000:5000 entregable-4-flask
```

## Imagen publicada

Descargar y ejecutar la etiqueta estable:

```powershell
docker pull jcmira/entregable-4-flask:latest
docker run --rm -p 5000:5000 jcmira/entregable-4-flask:latest
```

El pipeline publica:

- `jcmira/entregable-4-flask:latest`;
- `jcmira/entregable-4-flask:<sha-del-commit>`.

La imagen `latest` fue descargada y verificada mediante una petición HTTP al
contenedor.

## CI/CD

El workflow se activa:

- con cada `push` a `main`;
- manualmente mediante `workflow_dispatch`.

Secuencia:

1. descarga el repositorio;
2. configura Python;
3. instala dependencias;
4. ejecuta pytest;
5. construye la imagen Docker;
6. inicia sesión en Docker Hub;
7. publica las etiquetas `latest` y SHA.

Los secretos configurados en GitHub Actions son:

- `DOCKERHUB_USERNAME`;
- `DOCKERHUB_TOKEN`.

Sus valores no se almacenan en el repositorio.

## Verificación final

Se ha comprobado:

- ejecución local de Flask;
- prueba pytest satisfactoria;
- construcción de la imagen Docker;
- ejecución y respuesta del contenedor local;
- ejecución satisfactoria del workflow;
- publicación en Docker Hub;
- descarga y ejecución de la imagen publicada.
