# Plan de implementación: actividad del Entregable 4

## Metadatos

- **Estado:** `approved`.
- **Área:** `task/entregable_4`.
- **Requisito:** `docs/requirements/task/entregable_4/activity.md`.
- **Ruta del plan:** `ai/plans/task/entregable_4/activity.md`.
- **Prompt inicial:** `ai/prompts/task/entregable_4/01_create_plan.md`.
- **Prompt de refinamiento:** `ai/prompts/task/entregable_4/01b_refine_plan.md`.
- **Modo de trabajo:** planificación completada; implementación aprobada para la
  fase posterior.

## Resumen del requisito

Crear una aplicación web sencilla con Python y Flask que exponga `GET /` en el
puerto `5000` y devuelva el saludo:

```text
Hola, esta es la aplicación Flask del Entregable 4.
```

La aplicación debe poder ejecutarse en local y dentro de Docker. El proyecto
debe incluir pruebas automatizadas con pytest y un workflow de GitHub Actions
que ejecute las pruebas, construya la imagen Docker y la publique en Docker Hub
mediante los secretos `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`.

El resultado debe quedar documentado para permitir la instalación, ejecución,
prueba, construcción de la imagen, publicación y uso de la imagen publicada.

## Alcance

### Incluido

- Aplicación Flask con la ruta pública `GET /`.
- Respuesta JSON con el mensaje de saludo especificado bajo la propiedad
  `message`.
- Escucha en `0.0.0.0:5000` para permitir la ejecución local y en contenedor.
- Código de producción ubicado en `code/app.py`.
- Python `3.11.15` en local, CI y Docker.
- Dependencias fijadas a `Flask==3.0.3` y `pytest==8.3.3`.
- Prueba automatizada de la ruta principal:
  - código HTTP `200`;
  - contenido JSON;
  - propiedad `message` con el saludo esperado.
- Dockerfile basado en una imagen oficial de Python.
- Construcción y ejecución local de la imagen Docker.
- Workflow `.github/workflows/docker-publish.yml` con estas etapas:
  - descarga del repositorio;
  - preparación de Python;
  - instalación de dependencias;
  - ejecución de pytest;
  - construcción de la imagen;
  - autenticación en Docker Hub mediante secretos;
  - publicación de la imagen.
- Publicación de la etiqueta `latest` con el formato
  `<usuario-dockerhub>/entregable-4-flask:latest`.
- Publicación adicional de una etiqueta inmutable asociada a
  `${{ github.sha }}`, alineada con el proyecto de referencia.
- Activación del workflow mediante:
  - `push` a la rama `main`;
  - `workflow_dispatch`.
- README con instrucciones de instalación, ejecución, pruebas, Docker,
  configuración de secretos y uso de la imagen publicada.
- Generación completa de la implementación en una única fase posterior.
- Generación completa de las pruebas en una única fase posterior.

### Fuera de alcance

- Persistencia o bases de datos.
- Autenticación y autorización de usuarios.
- Endpoints adicionales, incluido `/health`.
- Despliegue automático del contenedor en un proveedor cloud.
- Azure Container Registry, Azure Container Instances u otros registros
  distintos de Docker Hub.
- Lógica de dominio o casos de uso adicionales al saludo solicitado.
- Versionado de API, paginación, filtros o esquemas de entrada.
- Nuevas dependencias no exigidas por el requisito.

## Criterios de aceptación

1. Existe una aplicación Python basada en Flask.
2. `GET /` responde con código HTTP `200`.
3. La respuesta tiene formato JSON y contiene:
   `{"message": "Hola, esta es la aplicación Flask del Entregable 4."}`.
4. La aplicación puede iniciarse en local usando el entorno virtual indicado.
5. La aplicación escucha en el puerto `5000`.
6. El código de producción está ubicado en `code/app.py`.
7. Local, CI y Docker utilizan Python `3.11.15`.
8. `requirements.txt` fija `Flask==3.0.3` y `pytest==8.3.3`.
9. La imagen se construye correctamente a partir de un Dockerfile con una
   imagen base oficial de Python.
10. El contenedor expone la aplicación mediante el mapeo del puerto `5000`.
11. `pytest` ejecuta una prueba que valida el código `200`, el formato JSON y
    el saludo.
12. El workflow se activa con `push` a `main` y manualmente mediante
    `workflow_dispatch`.
13. El workflow ejecuta las pruebas antes de construir y publicar la imagen.
14. El workflow usa `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN` sin incluir sus
    valores en el repositorio.
15. El workflow publica
    `<usuario-dockerhub>/entregable-4-flask:latest` en Docker Hub.
16. El workflow publica también
    `<usuario-dockerhub>/entregable-4-flask:${{ github.sha }}`.
17. El README explica cómo instalar, ejecutar, probar, construir y ejecutar el
    contenedor, configurar los secretos y descargar la imagen publicada.
18. El repositorio público contiene todos los artefactos requeridos para
    revisar la solución.

## Supuestos y decisiones resueltas

### Supuestos explícitos del requisito

- Se utilizará el entorno virtual
  `C:\altia\25_IA\Proyectos\.venv`.
- La aplicación se desarrollará en
  `C:\altia\25_IA\Proyectos\entregable_4`.
- Flask y pytest son las únicas dependencias mínimas solicitadas.
- El puerto de la aplicación y del contenedor es `5000`.
- Docker Hub es el registro de imágenes objetivo.
- El proyecto
  `C:\altia\25_IA\Proyectos\flask-github-actions-acr-aci` se usa solo como
  referencia.

### Decisiones aplicadas

- `GET /` devolverá JSON con una única propiedad `message` y el saludo exacto
  del requisito.
- Se utilizará Python `3.11.15`, versión verificada en
  `C:\altia\25_IA\Proyectos\.venv`.
- Se fijarán las versiones instaladas actualmente:
  - `Flask==3.0.3`;
  - `pytest==8.3.3`.
- El workflow se activará con los mismos eventos del proyecto de referencia:
  - `push` a `main`;
  - `workflow_dispatch`.
- El repositorio de Docker Hub será `entregable-4-flask`.
- Se publicarán las dos etiquetas usadas por el proyecto de referencia:
  - `latest`, requerida por la actividad;
  - `${{ github.sha }}`, para trazabilidad de cada construcción.
- El código de producción se ubicará en `code/app.py`, resolviendo el conflicto
  de estructura a favor de las reglas de arquitectura.
- La implementación se generará completa de una vez.
- Las pruebas se generarán completas de una vez.
- El plan queda aprobado antes de generar código.

No quedan preguntas abiertas para iniciar la implementación.

## Análisis de impacto

### Archivos y áreas previstos

| Área | Impacto previsto |
| --- | --- |
| Producción | Nuevo punto de entrada Flask en `code/app.py`. |
| API HTTP | Nueva ruta pública `GET /` con respuesta JSON, sin parámetros ni autenticación. |
| Dependencias | Python `3.11.15`, `Flask==3.0.3` y `pytest==8.3.3`. |
| Pruebas | Nueva prueba pytest de la ruta principal. |
| Contenedorización | Nuevo `Dockerfile` y contexto de construcción. |
| CI/CD | Nuevo workflow `.github/workflows/docker-publish.yml`. |
| Seguridad | Uso de secretos de GitHub para credenciales de Docker Hub. |
| Documentación | Nuevo `README.md` operativo del entregable. |
| Persistencia | Sin impacto. |
| Dominio | Sin reglas de negocio ni entidades que modelar. |

### Contratos afectados

- Contrato HTTP nuevo:
  - método: `GET`;
  - ruta: `/`;
  - respuesta satisfactoria: `200`;
  - contenido: saludo especificado;
  - formato: JSON;
  - propiedad: `message`.
- Contrato de ejecución:
  - puerto interno: `5000`;
  - código de producción: `code/app.py`;
  - Python: `3.11.15`;
  - arranque mediante Python y Flask.
- Contrato de CI/CD:
  - secretos `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`;
  - nombre de imagen `entregable-4-flask`;
  - eventos `push` a `main` y `workflow_dispatch`;
  - etiquetas `latest` y `${{ github.sha }}`.

### Compatibilidad y migraciones

- No existe código funcional previo en el proyecto, por lo que no se prevén
  incompatibilidades con consumidores existentes.
- No hay modelos persistentes, datos ni migraciones.
- Las rutas de ejecución, pruebas y Docker deberán apuntar expresamente a
  `code/app.py`.

## Análisis de reutilización

El proyecto de referencia permite reutilizar conceptos y estructura de forma
selectiva:

- creación de la instancia Flask y uso del cliente de pruebas de Flask;
- escucha en `0.0.0.0:5000`;
- orden básico del Dockerfile: base, directorio de trabajo, dependencias,
  copia, exposición y arranque;
- uso de pytest para validar el endpoint;
- secuencia de GitHub Actions: checkout, preparación de Python, dependencias,
  pruebas y construcción Docker.

No deben copiarse los siguientes elementos porque no forman parte del
requisito:

- endpoint `/health`;
- respuesta y textos referidos a Azure;
- dependencias adicionales como Gunicorn;
- autenticación o publicación en Azure Container Registry;
- despliegue en Azure Container Instances;
- secretos, nombres de recursos y pasos específicos de Azure.

No existen componentes propios del proyecto actual que puedan reutilizarse,
porque todavía no hay código de producción, pruebas ni workflows del
entregable.

## Soluciones alternativas

### Alternativa A: estructura literal del requisito

Crear `app.py`, `requirements.txt`, `Dockerfile`, `README.md` y `tests/` en la
raíz, siguiendo el árbol indicado en el requisito.

**Ventajas**

- Coincide literalmente con la estructura solicitada.
- Minimiza rutas, configuración y complejidad.
- Facilita la ejecución `python app.py`.

**Inconvenientes**

- Incumple la regla obligatoria que exige código de producción bajo `code/`.
- No puede seleccionarse sin modificar o exceptuar explícitamente dicha regla.

### Alternativa B: estructura mínima compatible con la gobernanza

Ubicar la aplicación en `code/app.py` y mantener en la raíz los artefactos
operativos y documentales que correspondan, adaptando imports, Dockerfile,
pruebas y comandos del README.

**Ventajas**

- Respeta la regla de ubicación del código de producción.
- Mantiene una solución pequeña y proporcional a un único endpoint.
- Evita introducir capas, puertos o abstracciones sin comportamiento de
  negocio.

**Inconvenientes**

- No coincide con el árbol mínimo literal del requisito, pero aplica la
  decisión expresa de respetar la ubicación obligatoria bajo `code/`.

### Alternativa C: arquitectura hexagonal completa

Separar boot, API REST, aplicación y dominio bajo `code/`, siguiendo la
estructura de la skill de arquitectura hexagonal.

**Ventajas**

- Ofrece separación estricta y capacidad de crecimiento.
- Se alinea con la arquitectura de referencia del gobierno del proyecto.

**Inconvenientes**

- Añade módulos sin responsabilidades reales para un saludo constante.
- Incrementa el coste de configuración, imports, pruebas y Docker.
- Contradice el principio de evitar sobreingeniería para este alcance.

## Enfoque recomendado y justificación

Se selecciona y aprueba la **Alternativa B**.

La alternativa mantiene el código de producción bajo `code/`, como exigen las
reglas, y aplica una arquitectura mínima: un adaptador HTTP Flask y su
arranque, sin crear capas vacías. No hay dominio, persistencia, integraciones
de negocio ni casos de uso que justifiquen una arquitectura hexagonal
completa.

La decisión expresa de utilizar `code/app.py` resuelve el conflicto de
gobernanza y obliga a adaptar Dockerfile, pruebas, imports y README a esa ruta.

## Patrones y principios aplicables

- **Application Factory:** no se considera necesaria para el alcance actual;
  solo debería incorporarse si la implementación necesita separar creación y
  ejecución de la aplicación para facilitar configuración o pruebas.
- **Adapter HTTP:** Flask actúa como mecanismo de entrega HTTP.
- **Pipeline CI:** secuencia ordenada con pruebas como puerta previa a la
  construcción y publicación.
- **Separación de configuración y secretos:** las credenciales se inyectan
  desde GitHub Secrets.

No se proponen repositorios, servicios de dominio, inyección de dependencias,
DTO, mappers ni otros patrones porque no resuelven un problema presente en el
requisito.

## Diseño por capa

### Dominio

- Sin impacto.
- No se crearán entidades, objetos de valor, servicios, repositorios ni
  excepciones de dominio.

### Aplicación

- Sin caso de uso independiente: el comportamiento consiste únicamente en
  devolver un saludo constante.
- No se crearán comandos, consultas, mappers ni servicios de aplicación.

### Infraestructura

- Sin persistencia ni integraciones externas de ejecución.
- Docker y GitHub Actions se tratarán como infraestructura operativa del
  proyecto, no como lógica de aplicación.

### API REST

- Definir `GET /`.
- No aceptar parámetros ni cuerpo.
- Responder con estado `200`.
- Devolver JSON con la propiedad `message` y el saludo exigido.
- Mantener el controlador sin lógica adicional.
- No añadir versionado, autenticación, paginación ni endpoints no solicitados.
- No añadir propiedades JSON adicionales no requeridas.

### Boot

- Crear la instancia Flask y registrar la ruta.
- Arrancar escuchando en `0.0.0.0` y puerto `5000` cuando se ejecute el punto
  de entrada.
- Mantener el arranque compatible con local y Docker.
- Ubicar el punto de entrada en `code/app.py`.

### Contenedorización

- Usar una imagen base oficial de Python `3.11.15` en variante slim.
- Definir un directorio de trabajo.
- Copiar e instalar `requirements.txt`.
- Copiar los archivos necesarios de la aplicación.
- Exponer `5000`.
- Ejecutar el punto de entrada Flask mediante Python.
- No añadir dependencias ni servidores de aplicación no exigidos.

### CI/CD

- Crear `.github/workflows/docker-publish.yml`.
- Ejecutar las pruebas antes de construir y publicar.
- Construir usando el Dockerfile del repositorio.
- Autenticarse en Docker Hub sin imprimir ni almacenar credenciales.
- Construir la referencia de imagen a partir de
  `DOCKERHUB_USERNAME` y `entregable-4-flask`.
- Activarse con `push` a `main` y `workflow_dispatch`.
- Publicar las etiquetas `latest` y `${{ github.sha }}`.

## Flujo de datos

### Petición HTTP

1. Un cliente envía `GET /` al puerto `5000`.
2. Flask enruta la petición al manejador de la ruta principal.
3. El manejador crea un objeto JSON con la propiedad `message`.
4. Flask devuelve el JSON con código HTTP `200`.

No existe acceso a dominio, persistencia ni servicios externos.

### Pipeline

1. GitHub Actions obtiene el código.
2. Configura Python.
3. Instala las dependencias declaradas.
4. Ejecuta pytest.
5. Si las pruebas terminan correctamente, construye la imagen Docker.
6. Autentica contra Docker Hub mediante secretos.
7. Etiqueta la misma imagen como `latest` y `${{ github.sha }}`.
8. Publica ambas etiquetas.
9. Si cualquier etapa falla, las etapas dependientes no deben continuar.

## Estrategia de pruebas

### Pruebas automatizadas requeridas

- Prueba de integración ligera con el cliente de pruebas de Flask:
  - realizar `GET /`;
  - comprobar código `200`;
  - comprobar que la respuesta es JSON;
  - comprobar que `message` contiene el saludo exacto.

### Escenarios relevantes

- Ruta principal disponible.
- Mensaje correcto, incluida su codificación en UTF-8.
- Ejecución repetible sin red, Docker Hub ni servicios externos.

### Escenarios de error y límites

- Un cambio accidental de ruta debe hacer fallar la prueba.
- Un cambio accidental del saludo debe hacer fallar la prueba.
- Un error al importar o crear la aplicación debe impedir la ejecución de las
  pruebas y bloquear el pipeline.
- Credenciales ausentes o inválidas deben provocar un fallo controlado en la
  fase de autenticación o publicación, sin exponer los valores.

### Tipos de prueba no necesarios

- No se requieren pruebas de persistencia, dominio, autenticación ni
  integraciones cloud.
- No se requieren pruebas end-to-end contra Docker Hub.
- Una prueba de humo del contenedor sería adicional, pero no está exigida y no
  debe incorporarse sin aprobación.

### Cobertura y ejecución

- Objetivo mínimo: al menos `80 %` de cobertura del código afectado, conforme
  a `ai/rules/testing.md`.
- Los tests deben ejecutarse localmente y en GitHub Actions mediante pytest.
- Todas las pruebas se generarán en una única etapa, después de implementar la
  aplicación y antes de completar el workflow.

## Consideraciones de seguridad

- No almacenar el usuario, token ni otras credenciales de Docker Hub en el
  repositorio.
- Consumir `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN` mediante GitHub Secrets.
- Evitar mostrar secretos en comandos, logs o mensajes de error.
- Limitar los permisos del workflow a los estrictamente necesarios.
- No aceptar entradas externas en `GET /`; no existe superficie de validación
  de parámetros en el alcance actual.
- No activar el modo debug de Flask en la ejecución prevista para Docker.
- No exponer trazas internas al cliente.
- Mantener las dependencias declaradas de forma explícita y sin paquetes no
  utilizados.
- Considerar el Dockerfile y las acciones de terceros del workflow como
  componentes de la cadena de suministro.

## Impacto documental

### README del proyecto

Debe documentar:

- objetivo y estructura del entregable;
- requisitos previos;
- uso del entorno virtual indicado;
- instalación de dependencias;
- ejecución local y URL;
- ejecución de pytest;
- construcción y ejecución de Docker;
- configuración de `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN`;
- comportamiento del workflow;
- nombre de la imagen y etiquetas publicadas;
- descarga y ejecución de la imagen desde Docker Hub.

### Documentación adicional

- No se prevé documentación de persistencia.
- No se justifica un ADR para la aplicación en sí.
- La documentación debe usar `code/app.py` en todos los comandos y ejemplos.
- El contrato JSON de la única ruta se documentará en el README; no se añadirá
  una especificación OpenAPI porque el requisito no define una API pública o
  compartida para terceros.

## Manejo de errores y casos límite

- Si Flask no puede iniciar, el proceso debe terminar con error observable.
- Si pytest falla, el workflow debe detenerse antes de construir la imagen.
- Si la construcción Docker falla, no debe intentarse la publicación.
- Si faltan secretos o Docker Hub rechaza la autenticación, el workflow debe
  fallar sin revelar credenciales.
- Si falla la publicación, el workflow debe marcarse como fallido.
- El saludo debe conservar correctamente caracteres Unicode.
- La aplicación debe enlazarse a `0.0.0.0`, no solo a `127.0.0.1`, para ser
  accesible desde fuera del contenedor.

## Riesgos

| Riesgo | Impacto | Mitigación planificada |
| --- | --- | --- |
| Diferencia entre el árbol del requisito y `code/app.py` | Los comandos literales del requisito no funcionarían sin adaptación | Mantener rutas coherentes en Dockerfile, tests y README |
| Desalineación de Python entre local, CI y Docker | Resultados distintos entre entornos | Fijar Python `3.11.15` en los tres entornos |
| Etiqueta SHA no exigida expresamente | Añade una publicación adicional | Mantenerla por la decisión de alineación con el ejemplo y conservar `latest` como etiqueta requerida |
| Copiar elementos del proyecto de referencia fuera de alcance | Añade complejidad y requisitos no solicitados | Reutilizar solo patrones mínimos y excluir Azure, `/health` y Gunicorn |
| Publicar `latest` sobrescribe la etiqueta mutable | Puede reemplazar la versión anterior | Limitar la publicación automática a `push` sobre `main`; mantener `workflow_dispatch` como ejecución manual |
| Uso de credenciales con permisos excesivos | Aumenta el impacto de una filtración | Usar un token de Docker Hub con el menor alcance posible |

## Secuencia propuesta de implementación

La implementación aprobada se generará completa de una vez:

1. Crear la estructura mínima aprobada con `code/app.py`.
2. Implementar el punto de entrada Flask y `GET /` con respuesta JSON.
3. Declarar Python `3.11.15`, `Flask==3.0.3` y `pytest==8.3.3`.
4. Generar todas las pruebas pytest del contrato HTTP.
5. Ejecutar las pruebas localmente.
6. Crear el Dockerfile y validar construcción y ejecución local.
7. Crear el workflow con `push` a `main`, `workflow_dispatch`, pruebas previas
   y publicación de etiquetas `latest` y SHA.
8. Completar el README con los comandos y secretos requeridos.
9. Revisar trazabilidad contra todos los criterios de aceptación.

## Decisiones pendientes del usuario

No quedan decisiones pendientes para iniciar la implementación aprobada.

## Trazabilidad

| Elemento del requisito | Sección del plan |
| --- | --- |
| Aplicación Flask y ruta `/` | Alcance, criterios de aceptación y diseño de API REST |
| Saludo esperado | Resumen, criterios de aceptación y estrategia de pruebas |
| Puerto `5000` | Criterios, boot, contenedorización y flujo de datos |
| Ejecución local | Alcance e impacto documental |
| Dockerfile | Diseño de contenedorización |
| pytest | Estrategia de pruebas |
| GitHub Actions | Diseño CI/CD y flujo del pipeline |
| Docker Hub | Alcance, seguridad y diseño CI/CD |
| Secretos requeridos | Contratos y consideraciones de seguridad |
| README | Impacto documental |
| Verificación del entregable | Criterios de aceptación y secuencia propuesta |

## Ruta de almacenamiento

Este plan se almacena en:

```text
ai/plans/task/entregable_4/activity.md
```

El plan queda aprobado para la fase posterior de implementación completa y
generación completa de pruebas, sin generar código ni tests durante este
refinamiento.
