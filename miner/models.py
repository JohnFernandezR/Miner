from pydantic import BaseModel, Field

class RepoCandidate(BaseModel):
    repo_name: str = Field(
        ..., 
        description="Nombre del repositorio en formato usuario/repo"
    )

class Repository(BaseModel):
    repo_id: str
    repo_name: str

class WorkflowFile(BaseModel):
    file_id: str
    repo_id: str
    file_name: str
    body: str

class FrontmatterProperty(BaseModel):
    fm_id: str
    file_id: str
    key: str
    value: str