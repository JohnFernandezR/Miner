import pandas as pd
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