import os
import uuid
import typer
import pandas as pd
from typing_extensions import Annotated

# 1. Importaciones unificadas al principio del archivo
from .data import read_repositories, save_to_parquet
from .github_api import get_workflow_files, get_file_content
from .logic import uses_gh_aw, parse_markdown_file
from .models import Repository, WorkflowFile, FrontmatterProperty

# 2. Inicializamos la aplicación UNA SOLA VEZ
app = typer.Typer(help="Miner: Identificador y Extractor de GitHub Agentic Workflows")

# 3. Comando de la Tarea 2
@app.command()
def process(
    input_csv: Annotated[str, typer.Argument(help="Archivo CSV con los repositorios candidatos")],
    output: Annotated[str, typer.Option("--output", "-o", help="Archivo CSV de salida")]
):
    """
    Lee un CSV de candidatos, consulta a GitHub y genera un nuevo CSV
    únicamente con los repositorios que usan GH-AW.
    """
    typer.echo(f"Leyendo repositorios desde {input_csv}...")
    repos = read_repositories(input_csv)
    
    gh_aw_repos = []
    
    with typer.progressbar(repos, label="Consultando GitHub") as progress:
        for repo in progress:
            files = get_workflow_files(repo)
            
            if uses_gh_aw(files):
                gh_aw_repos.append(repo)
                
    typer.echo(f"\n¡Análisis completado! Se encontraron {len(gh_aw_repos)} repositorios usando GH-AW.")
    typer.echo(f"Generando archivo de salida: {output}...")
    
    df_final = pd.DataFrame({'repo_name': gh_aw_repos})
    df_final.to_csv(output, index=False)
    
    typer.echo("¡Proceso finalizado exitosamente!")

# 4. Comando de la Tarea 3
@app.command()
def extract(
    input_csv: Annotated[str, typer.Argument(help="Archivo CSV filtrado (resultado de Tarea 2)")],
    output_dir: Annotated[str, typer.Option("--out-dir", "-d", help="Carpeta donde se guardarán los archivos Parquet")] = "dataset"
):
    """
    Extrae el contenido de los archivos .md y genera un dataset relacional en formato Parquet.
    """
    typer.echo(f"Leyendo repositorios confirmados desde {input_csv}...")
    repos = read_repositories(input_csv)
    
    repos_data = []
    files_data = []
    frontmatter_data = []
    
    with typer.progressbar(repos, label="Extrayendo y modelando datos") as progress:
        for repo_name in progress:
            repo_id = repo_name
            repos_data.append(Repository(repo_id=repo_id, repo_name=repo_name))
            
            archivos = get_workflow_files(repo_name)
            md_files = [f for f in archivos if f.endswith('.md')]
            
            for md_file in md_files:
                file_path = f".github/workflows/{md_file}"
                content = get_file_content(repo_name, file_path)
                
                if not content:
                    continue
                    
                parsed_data = parse_markdown_file(content)
                file_id = f"{repo_id}/{md_file}"
                
                files_data.append(WorkflowFile(
                    file_id=file_id,
                    repo_id=repo_id,
                    file_name=md_file,
                    body=parsed_data["body"]
                ))
                
                for key, value in parsed_data["frontmatter"].items():
                    fm_id = str(uuid.uuid4())
                    frontmatter_data.append(FrontmatterProperty(
                        fm_id=fm_id,
                        file_id=file_id,
                        key=str(key),
                        value=str(value)
                    ))
                    
    typer.echo(f"\nGuardando dataset en la carpeta '{output_dir}'...")
    save_to_parquet(repos_data, os.path.join(output_dir, "repositorios.parquet"))
    save_to_parquet(files_data, os.path.join(output_dir, "archivos.parquet"))
    save_to_parquet(frontmatter_data, os.path.join(output_dir, "frontmatter.parquet"))
    
    typer.echo("¡Extracción y modelado completados con éxito!")