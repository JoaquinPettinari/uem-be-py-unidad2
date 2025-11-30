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

Contiene los modelos de base de datos usando SQLAlchemy.
Representan las tablas y sus relaciones (usuarios, historial, acciones, etc.).

### 🔌 routers/

Incluye los endpoints de la API.
Cada archivo maneja un conjunto de rutas (por ejemplo: /users, /auth, /search, etc.).

### 📦 schemas/

Define los Pydantic Schemas, utilizados para validar y estructurar la información enviada y recibida por la API.

### ⚙️ services/

Acá vive la lógica de negocio:
consultas a Spotify, manejo de historial, acciones del usuario, etc.
Los routers llaman a estos servicios para mantener el código ordenado.

### 🛠️ utils/

Funciones auxiliares y utilidades comunes (middlewares, helpers, validadores, etc.).

### 🗄️ database.py

Configura la conexión a la base de datos, los motores de SQLAlchemy y la sesión.

### 🚀 main.py

Punto de entrada de la aplicación.
Aquí se crean las instancias de FastAPI y se incluyen los routers.

### 🔑 .env

Archivo con variables de entorno (credenciales, URL de base de datos, etc.).
No se sube al repositorio.

### 💾 app.db

Base de datos SQLite (solo para desarrollo local).

### 📦 requirements.txt

Dependencias del proyecto para instalar con pip.
