import typer
import pandas as pd
from typing_extensions import Annotated
from .data import read_repositories
from .github_api import get_workflow_files
from .logic import uses_gh_aw

app = typer.Typer(help="Miner: Identificador de GitHub Agentic Workflows")

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