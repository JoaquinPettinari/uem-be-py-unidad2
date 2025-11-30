## 📁 Estructura del Proyecto

Este backend está construido con FastAPI, organizado de forma modular para mantener el código limpio, escalable y fácil de mantener.
A continuación se describe cada carpeta y archivo principal:
```bash
app.
├── models/
├── routers/
├── schemas/
├── services/
├── utils/
├── database.py
├── main.py
├── .env
├── app.db
├── requirements.txt
```

### 🧩 models/

Contiene los modelos de base de datos usando [SQLAlchemy]([**SQLAlchemy**](https://www.sqlalchemy.org)).
Representan las tablas y sus relaciones (usuarios, historial, acciones, etc.).

### 🔌 routers/

Incluye los endpoints de la API.
Cada archivo maneja un conjunto de rutas (por ejemplo: /users, /spotify).

### 📦 schemas/

Define los Pydantic Schemas, utilizados para validar y estructurar la información enviada y recibida por la API.

### ⚙️ services/

Acá vive la lógica de la aplicación:
consultas a Spotify, manejo de historial, acciones del usuario, etc.
Los routers llaman a estos servicios para mantener el código ordenado.

### 🛠️ utils/

Funciones auxiliares y utilidades comunes.

### 🗄️ database.py

Configura la conexión a la base de datos, los motores de SQLAlchemy y la sesión.

### 🚀 main.py

Punto de entrada de la aplicación.
Aquí se crean las instancias de FastAPI y se incluyen los routers.

### 🔑 .env

Archivo con variables de entorno (credenciales, etc.).
No se sube al repositorio.

### 💾 app.db

Base de datos SQLite (solo para desarrollo local).

### 📦 requirements.txt

Dependencias del proyecto para instalar con pip.

--
## 🧭 Recorrido del Código (Cómo funciona todo junto)

El punto de entrada del proyecto es **main.py**, donde se crea la aplicación con **FastAPI** y se registran todas las rutas definidas en la carpeta **routers/**. 
Cada ruta delega su lógica a un archivo dentro de **services/**, que contiene las funciones que realmente ejecutan las operaciones (búsquedas de Spotify, creación de usuarios, acciones, etc.). 
Estos servicios reciben y devuelven datos estructurados mediante los **Schemas de Pydantic**, ubicados en la carpeta **schemas/**, que se encargan de validar y tipar correctamente la información. 
Finalmente, toda la persistencia se maneja mediante los modelos de **SQLAlchemy** en **models/**. 

Se utiliza SQLAlchemy porque permite trabajar la base de datos usando ORM, evitando escribir SQL manualmente y facilitando cambiar de motor (SQLite, PostgreSQL, MySQL, etc.) sin modificar la lógica; además ofrece relaciones, migraciones y un manejo más seguro y expresivo que interactuar directamente con MySQL u otros motores mediante consultas crudas.


## 🚧 Limitaciones y Posibles Mejoras

Aunque el proyecto cumple con los objetivos propuestos y presenta una arquitectura sólida, existen algunas áreas donde se podrían introducir mejoras:

- Autorización limitada: el proyecto no implementa autenticación real de usuarios (OAuth2, JWT, sesiones, etc.). Actualmente asume que el user_id es confiable.
- Dependencia del flujo [Client Credentials](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow) de Spotify: este flujo no permite obtener información personalizada del usuario de Spotify, solo acceso a contenidos públicos. Para funcionalidades más avanzadas se requeriría OAuth completo.
- Validaciones básicas: aunque se usan enums y Pydantic, aún faltan validaciones más estrictas (tipos, rangos, formatos).
- Base de datos local: se utiliza SQLite por simplicidad, lo cual no es ideal para producción. No soporta concurrencia alta ni escalabilidad.
- Errores genéricos: algunas respuestas de error del backend podrían ser más descriptivas y consistentes.
- Servicios sin tests automatizados: actualmente no hay cobertura de tests unitarios o de integración.

## 📝 Conclusiones y Observaciones

El proyecto presenta una arquitectura organizada y modular que facilita su mantenimiento y escalabilidad. 
El flujo completo (desde **main.py** hasta los modelos) permite separar responsabilidades de forma clara: 
- Las rutas manejan las solicitudes
- Los servicios ejecutan la lógica de la aplicación
- Los schemas validan los datos y los modelos representan la base de datos.

Gracias a **SQLAlchemy**, el manejo de la persistencia es flexible y seguro, evitando escribir SQL manual y permitiendo cambiar fácilmente de motor de base de datos en el futuro. 
La integración con Spotify se realiza a través del flujo de Client Credentials, manteniendo las claves seguras mediante variables de entorno. 

Esta estructura permite añadir funcionalidades nuevas, validaciones y endpoints sin generar problemas de acoplamiento o duplicación de código.
