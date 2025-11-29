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

## 🧩 3. Crear y activar un entorno virtual (venv)

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

## ▶️ 5. Levantar el servidor

Ejecutá uvicorn en modo desarrollo:
```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en:

  - http://localhost:8000
  - Documentación automática OpenAPI: http://localhost:8000/docs
  - Documentación ReDoc: http://localhost:8000/redoc

