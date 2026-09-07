import yaml

def uses_gh_aw(archivos: list[str]) -> bool:
    """
    Recibe una lista de nombres de archivos y verifica si existe
    un par .md y .lock.yml con el mismo nombre base.
    """
    md_bases = {f[:-3] for f in archivos if f.endswith('.md')}
    lock_bases = {f[:-9] for f in archivos if f.endswith('.lock.yml')}
    
    return bool(md_bases.intersection(lock_bases))

def parse_markdown_file(content: str) -> dict:
    """
    Recibe el texto de un archivo .md y separa el frontmatter del body
    usando YAML directamente para mayor compatibilidad.
    """
    if not content.strip():
        return {"frontmatter": {}, "body": ""}
        
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                return {
                    "frontmatter": fm,
                    "body": parts[2].strip()
                }
            except Exception:
                pass
                
    return {"frontmatter": {}, "body": content}