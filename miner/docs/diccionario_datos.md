# Documentación del Dataset: GitHub Agentic Workflows

## Diagrama Entidad-Relación

```mermaid
erDiagram
    REPOSITORIOS {
        string repo_id PK
        string repo_name
    }
    ARCHIVOS {
        string file_id PK
        string repo_id FK
        string file_name
        string body
    }
    FRONTMATTER {
        string fm_id PK
        string file_id FK
        string key
        string value
    }

    REPOSITORIOS ||--o{ ARCHIVOS : "contiene"
    ARCHIVOS ||--o{ FRONTMATTER : "posee"