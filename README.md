# 🚀 Backend – Setup desde cero (Windows)

Este documento explica cómo levantar el proyecto desde cero después de clonar el repositorio.  
Los pasos están pensados para un usuario externo que no conoce el entorno.

---

## ✅ 1. Requisitos previos

Antes de empezar, asegurate de tener instalado:

- **Python 3.10+**
- **Git**
- **pip** (incluido con Python)
- **Virtualenv** (opcional, pero recomendado)

---

## 📥 2. Clonar el repositorio

```bash
git clone https://github.com/JoaquinPettinari/uem-be-py-unidad2

cd uem-be-py-unidad2
```

## 🚀 Levantar aplicación con Docker Compose

Este proyecto se puede levantar fácilmente usando Docker Compose, sin necesidad de instalar Python ni dependencias en tu máquina local.

### 1️⃣ Requisitos

[Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado en tu sistema (incluye Docker Compose).

Para verificar la instalación:
```bash
docker compose version
```

### 2️⃣ Levantar la aplicación.

Desde la raíz del proyecto (donde está docker-compose.yml), ejecuta:
```bash
docker compose up --build
```

Si vas a utilizar esta opción, es importante que solamente leas la parte de las credenciales de Spotify.

## 🐢 3. Crear y activar un entorno virtual (venv, sin Docker Compose)

Crear el entorno virtual:
```bash
python -m venv venv

// Activar el entorno virtual (Windows):
venv\Scripts\activate
// En mac
source venv/bin/activate
```

Si todo va bien, deberías ver algo así al inicio de tu consola:
```bash
(venv) C:\ruta\proyecto/uem-be-py-unidad2
```

## 📦 4. Instalar dependencias

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 🧩 5. Configuración del archivo .env

Para que la aplicación pueda conectarse correctamente a Spotify y a la base de datos, necesitás configurar tus variables de entorno.
En este repositorio vas a encontrar un archivo llamado: 

```bash
.env.copy
```

### 🎧 ¿De dónde sacar las credenciales de Spotify?

1. Entrá a https://developer.spotify.com/dashboard
2. Creá una app nueva.
3. Copiá el Client ID y el Client Secret.
4. Pegalos en tu archivo .env.

### 🔧 Cómo crear tu archivo .env
Copiá el archivo de ejemplo:
```bash
cp .env.copy .env
```

Reemplaza los valores por los tuyos
```bash
SPOTIFY_CLIENT_ID=tu_client_id_de_spotify
SPOTIFY_CLIENT_SECRET=tu_client_secret_de_spotify
```

## ▶️ 6. Levantar el servidor
Ejecutá uvicorn en modo desarrollo:
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en:

  - http://localhost:8000
  - Documentación automática OpenAPI: http://localhost:8000/docs
  - Documentación ReDoc: http://localhost:8000/redoc

## Entrega del proyecto:

[Explicación del código, estructura del proyecto y conclusiones](https://github.com/JoaquinPettinari/uem-be-py-unidad2/blob/main/explicación_código.md)





