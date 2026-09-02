from pydantic import BaseModel, Field

class RepoCandidate(BaseModel):
    repo_name: str = Field(
        ..., 
        description="Nombre del repositorio en formato usuario/repo"
    )