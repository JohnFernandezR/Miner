# Análisis Exploratorio de Datos (EDA) - Miner

Este directorio contiene los notebooks del análisis exploratorio del dataset de GitHub Agentic Workflows.

## Dataset Publicado
El dataset estructurado se encuentra publicado en Hugging Face:
** https://huggingface.co/datasets/JFernandez2026/miner-gh-aw-dataset **

## Ubicación de los Archivos Parquet
Para ejecutar los notebooks localmente, los archivos Parquet extraídos (`repositorios.parquet`, `archivos.parquet`, `frontmatter.parquet`) deben estar ubicados en la carpeta `dataset/` en la raíz del proyecto (es decir, en la ruta `../dataset/` relativa a estos notebooks).

## Instalación e Inicio de JupyterLab
Para reproducir el entorno, abre una terminal en la raíz del proyecto y ejecuta:

```bash
# 1. Activar el entorno virtual
source .venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt
pip install jupyterlab pandas matplotlib seaborn fastparquet

# 3. Iniciar JupyterLab
jupyter lab