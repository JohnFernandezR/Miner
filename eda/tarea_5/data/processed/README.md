# Evolución de GitHub Agentic Workflows (Tarea 5)

Este directorio contiene el análisis exploratorio sobre la evolución histórica y las modificaciones de los repositorios que implementan GitHub Agentic Workflows, utilizando el dataset GHAW-H.

## Estructura del Directorio
* **`01_preparacion_y_agregaciones.ipynb`**: Notebook que calcula las diferencias de longitud de código entre versiones, mide el tiempo transcurrido entre modificaciones y genera agregaciones a nivel de archivo y mes.
* **`02_boxplots_y_evolucion.ipynb`**: Notebook que carga los datos procesados para visualizar mediante boxplots y gráficos de líneas la evolución temporal de los flujos de trabajo.
* **`data/`**: Carpeta donde se deben ubicar los archivos originales del dataset GHAW-H.
* **`data/processed/`**: Carpeta generada automáticamente donde se guardan los archivos Parquet procesados resultantes del primer notebook.

## Reproducción del Entorno

Para ejecutar estos notebooks, sitúate en la raíz del proyecto (la carpeta principal de `Miner`) y ejecuta los siguientes comandos en tu terminal:

```bash
# 1. Activar el entorno virtual
source .venv/bin/activate

# 2. Instalar las dependencias necesarias
pip install jupyterlab pandas pyarrow matplotlib seaborn fastparquet

# 3. Iniciar JupyterLab
jupyter lab