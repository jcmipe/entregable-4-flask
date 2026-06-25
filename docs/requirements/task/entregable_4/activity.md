# Entregable 4: Aplicación Flask contenerizada con Docker y pipeline CI/CD

## 1. Descripción del proyecto

Este proyecto corresponde al **Entregable 4** del Programa Avanzado en Inteligencia Artificial para Programar. El objetivo principal es crear una aplicación web sencilla desarrollada con **Python y Flask**, empaquetarla en un contenedor mediante **Docker** y automatizar su construcción, prueba y publicación mediante un pipeline de integración continua con **GitHub Actions**.

La aplicación expondrá un endpoint principal en la ruta `/`, que devolverá un mensaje de saludo. Además, se incluirán pruebas automatizadas con `pytest` para verificar que la aplicación responde correctamente antes de construir y publicar la imagen Docker.

El proyecto se desarrollará en la carpeta local:

```text
C:\altia\25_IA\Proyectos\entregable_4
```

Como referencia de estructura y configuración se tomará el proyecto de ejemplo disponible en:

```text
C:\altia\25_IA\Proyectos\flask-github-actions-acr-aci
```

El entorno virtual ya disponible para trabajar será:

```text
C:\altia\25_IA\Proyectos\.venv
```

## 2. Objetivos de la actividad

Los objetivos de esta actividad son:

- Crear una aplicación web simple en Python utilizando Flask.
- Empaquetar la aplicación en un contenedor Docker para garantizar su portabilidad.
- Definir un archivo `Dockerfile` que permita construir la imagen de la aplicación de forma reproducible.
- Automatizar el ciclo de construcción, prueba y publicación de la imagen mediante GitHub Actions.
- Subir la imagen generada a Docker Hub.
- Documentar correctamente el proyecto, incluyendo las instrucciones necesarias para ejecutarlo en local y mediante Docker.

## 3. Requisitos funcionales

La aplicación deberá cumplir los siguientes requisitos funcionales:

1. Debe estar desarrollada en Python utilizando el framework Flask.
2. Debe exponer una ruta principal `/`.
3. Al acceder a la ruta `/`, la aplicación debe devolver un mensaje de saludo.
4. La aplicación debe poder ejecutarse localmente desde el entorno virtual existente.
5. La aplicación debe poder ejecutarse dentro de un contenedor Docker.
6. Deben incluirse pruebas automatizadas que permitan comprobar que la ruta principal responde correctamente.

## 4. Requisitos técnicos

El proyecto deberá incluir, como mínimo, los siguientes archivos:

```text
entregable_4/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── docker-publish.yml
```

### 4.1. Aplicación Flask

El archivo `app.py` contendrá la aplicación Flask. La aplicación deberá escuchar en el puerto `5000` y estar preparada para ejecutarse tanto en local como dentro de Docker.

Ejemplo de comportamiento esperado:

```text
GET http://localhost:5000/
```

Respuesta esperada:

```text
Hola, esta es la aplicación Flask del Entregable 4.
```

### 4.2. Dependencias del proyecto

El archivo `requirements.txt` deberá contener las dependencias necesarias para ejecutar la aplicación y las pruebas:

```text
Flask
pytest
```

Si se desea fijar versiones concretas, se podrá utilizar una versión equivalente a la instalada en el entorno virtual del proyecto.

### 4.3. Dockerfile

El archivo `Dockerfile` deberá cumplir los siguientes requisitos:

- Utilizar una imagen base oficial de Python.
- Copiar el código fuente de la aplicación dentro del contenedor.
- Instalar las dependencias desde `requirements.txt`.
- Exponer el puerto `5000`.
- Configurar el comando de arranque de la aplicación Flask.

Ejemplo de estructura esperada:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## 5. Ejecución en local

Para ejecutar la aplicación en local, se utilizará el entorno virtual ya existente:

```powershell
cd C:\altia\25_IA\Proyectos\entregable_4
C:\altia\25_IA\Proyectos\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Una vez iniciada la aplicación, se podrá acceder desde el navegador a:

```text
http://localhost:5000/
```

## 6. Ejecución con Docker

Para construir la imagen Docker de la aplicación, se ejecutará el siguiente comando desde la carpeta del proyecto:

```powershell
docker build -t entregable-4-flask .
```

Para ejecutar el contenedor:

```powershell
docker run -p 5000:5000 entregable-4-flask
```

La aplicación estará disponible en:

```text
http://localhost:5000/
```

## 7. Pruebas automatizadas

Se incluirá una prueba con `pytest` para validar que la aplicación responde correctamente en la ruta principal `/`.

Ejemplo de ejecución local:

```powershell
pytest
```

La prueba deberá comprobar que:

- La respuesta HTTP tiene código `200`.
- El contenido devuelto contiene el mensaje de saludo esperado.

## 8. Pipeline de integración continua con GitHub Actions

El proyecto incluirá un workflow de GitHub Actions en la ruta:

```text
.github/workflows/docker-publish.yml
```

El pipeline deberá realizar las siguientes etapas:

1. Descargar el código del repositorio.
2. Preparar el entorno de ejecución.
3. Instalar dependencias.
4. Ejecutar las pruebas automatizadas con `pytest`.
5. Construir la imagen Docker a partir del `Dockerfile`.
6. Iniciar sesión en Docker Hub utilizando secretos configurados en GitHub.
7. Publicar la imagen Docker en Docker Hub.

## 9. Secretos necesarios en GitHub

Para poder subir la imagen a Docker Hub desde GitHub Actions, será necesario configurar los siguientes secretos en el repositorio de GitHub:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

Estos secretos se configurarán desde:

```text
Settings > Secrets and variables > Actions > New repository secret
```

El secreto `DOCKERHUB_USERNAME` contendrá el nombre de usuario de Docker Hub.

El secreto `DOCKERHUB_TOKEN` contendrá un token de acceso generado desde Docker Hub.

## 10. Publicación de la imagen Docker

La imagen se publicará en Docker Hub con un nombre similar al siguiente:

```text
<usuario-dockerhub>/entregable-4-flask:latest
```

Una vez publicada, podrá descargarse y ejecutarse desde cualquier equipo con Docker instalado:

```powershell
docker pull <usuario-dockerhub>/entregable-4-flask:latest
docker run -p 5000:5000 <usuario-dockerhub>/entregable-4-flask:latest
```

## 11. Verificación del entregable

Para comprobar que el entregable es correcto, se verificará lo siguiente:

- El repositorio público contiene el código fuente de la aplicación.
- Existe un archivo `Dockerfile` funcional.
- Existe un archivo `requirements.txt` con las dependencias necesarias.
- Existe un workflow de GitHub Actions en formato YAML.
- El pipeline ejecuta las pruebas antes de construir la imagen.
- La imagen Docker se construye correctamente.
- La imagen se publica correctamente en Docker Hub.
- La aplicación responde correctamente al acceder a la ruta `/`.
- El archivo `README.md` incluye instrucciones claras de ejecución.

## 12. Entrega final

La entrega consistirá en un enlace a un repositorio público de GitHub que contenga:

- Código fuente de la aplicación Flask.
- Archivo `Dockerfile`.
- Archivo `requirements.txt`.
- Archivo del pipeline de GitHub Actions en formato `.yml` o `.yaml`.
- Carpeta de pruebas automatizadas.
- Archivo `README.md` con la descripción del proyecto y las instrucciones de ejecución.

El repositorio deberá permitir revisar la solución completa y comprobar que la aplicación puede ejecutarse correctamente tanto en local como en Docker.

## 13. Criterios de evaluación cubiertos

Este proyecto cubre los criterios indicados en la rúbrica de la actividad:

| Criterio | Descripción |
| --- | --- |
| Creación del Dockerfile | Se define un Dockerfile estructurado y funcional. |
| Configuración del pipeline | Se incluye un pipeline con etapas claras de prueba, construcción y publicación. |
| Automatización de pruebas | Se incorporan pruebas con pytest ejecutadas dentro del pipeline. |
| Subida y despliegue del contenedor | La imagen se publica en Docker Hub y puede ejecutarse desde Docker. |
| Documentación | El README incluye instrucciones detalladas para instalar, ejecutar, probar y desplegar la aplicación. |
