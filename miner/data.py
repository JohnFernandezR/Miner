import pandas as pd
import os
from .models import RepoCandidate

def read_repositories(csv_path: str) -> list[str]:
    """
    Lee el archivo CSV, valida cada fila usando Pydantic 
    y devuelve una lista de repositorios candidatos.
    """
    df = pd.read_csv(csv_path)
    
    col_name = 'name' if 'name' in df.columns else df.columns[0]
    
    valid_repos = []
    for repo in df[col_name].dropna():
        candidate = RepoCandidate(repo_name=str(repo).strip())
        valid_repos.append(candidate.repo_name)
        
    return valid_repos

def save_to_parquet(data_list: list, output_path: str):
    """
    Recibe una lista de modelos Pydantic y los guarda 
    en un archivo Parquet asegurando la creación del directorio.
    """
    # Si la lista está vacía, no hacemos nada para evitar errores
    if not data_list:
        return

    # Convertimos los objetos Pydantic en diccionarios compatibles con Pandas
    # Usamos model_dump() que es la forma estándar en Pydantic v2
    dicts = [item.model_dump() for item in data_list]
    df = pd.DataFrame(dicts)
    
    # Aseguramos que la carpeta de destino exista antes de guardar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Guardamos usando el motor de PyArrow
    df.to_parquet(output_path, engine='pyarrow', index=False)