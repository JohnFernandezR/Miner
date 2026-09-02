import os
import httpx
from dotenv import load_dotenv

load_dotenv()

def get_workflow_files(repo_name: str) -> list[str]:
    """
    Consulta la API de GitHub y devuelve una lista con los nombres 
    de los archivos dentro de .github/workflows/.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("Falta configurar GITHUB_TOKEN en el archivo .env")

    url = f"https://api.github.com/repos/{repo_name}/contents/.github/workflows"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        
    if response.status_code != 200:
        return [] 
        
    data = response.json()
    return [item["name"] for item in data if item["type"] == "file"]