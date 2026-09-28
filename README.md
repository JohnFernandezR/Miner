# Miner - GitHub Agentic Workflows (GH-AW) Extractor

Miner es una herramienta de línea de comandos (CLI) desarrollada en Python, diseñada para analizar repositorios de GitHub, identificar aquellos que implementan GitHub Agentic Workflows (GH-AW) y extraer su configuración estructurada.

La aplicación procesa repositorios candidatos, descarga los archivos de flujos de trabajo ubicados en `.github/workflows/`, separa el contenido Markdown de sus metadatos (YAML frontmatter) y exporta toda la información en un formato columnar optimizado (Apache Parquet) para su posterior análisis.

## 🚀 Características
* **Extracción Automatizada:** Consulta la API de GitHub para descargar workflows de múltiples repositorios.
* **Procesamiento de Datos:** Separa eficientemente el YAML frontmatter del cuerpo del texto en los archivos Markdown.
* **Exportación a Parquet:** Genera tres datasets relacionales (`repositorios.parquet`, `archivos.parquet`, `frontmatter.parquet`).
* **Análisis Exploratorio (EDA):** Incluye un entorno de Jupyter Notebooks para el análisis y visualización de los datos extraídos.

## 📋 Requisitos
* Python 3.10 o superior.
* Un Personal Access Token (PAT) de GitHub.

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
```bash
git clone (https://github.com/JohnFernandezR/Miner.git)
cd Miner
```

2. **Crear y activar el entorno virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# .venv\Scripts\activate   # En Windows
```

3. **Instalar las dependencias del proyecto:**
```bash
pip install -r requirements.txt
```

4. **Configurar las credenciales:**
Crea un archivo llamado `.env` en la raíz del proyecto (puedes basarte en `.env.example`) y agrega tu token de GitHub sin comillas y sin espacios:
```env
GITHUB_TOKEN=ghp_tu_token_aqui
```

## 💻 Uso de la CLI

Para ejecutar la herramienta y procesar un archivo CSV con la lista de repositorios candidatos, utiliza el punto de entrada principal:

```bash
python main.py candidatos.csv --output repositorios_ghaw.csv
```
*(Nota: Asegúrate de que el archivo CSV de entrada tenga una columna llamada `repo_name` con el formato `usuario/repositorio`).*

## 🧪 Pruebas Automatizadas

El proyecto incluye pruebas unitarias desarrolladas con `pytest` para garantizar el correcto funcionamiento de la lógica de análisis y la separación del YAML frontmatter. Para ejecutarlas, corre el siguiente comando en la raíz del proyecto:

```bash
pytest tests/
```

## 📁 Estructura del Proyecto
* `miner/`: Módulos principales de la aplicación (CLI, lógica de extracción, conexión a la API de GitHub y modelos de datos).
* `tests/`: Directorio de pruebas automatizadas.
* `dataset/`: Carpeta destino donde se guardan los archivos `.parquet` generados.
* `eda/`: Directorio que contiene el Análisis Exploratorio de Datos (Jupyter Notebooks) sobre el dataset final.