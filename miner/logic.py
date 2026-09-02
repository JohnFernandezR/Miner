def uses_gh_aw(archivos: list[str]) -> bool:
    """
    Recibe una lista de nombres de archivos y verifica si existe
    un par .md y .lock.yml con el mismo nombre base.
    """
    md_bases = {f[:-3] for f in archivos if f.endswith('.md')}
    lock_bases = {f[:-9] for f in archivos if f.endswith('.lock.yml')}
    
    return bool(md_bases.intersection(lock_bases))