from miner.logic import uses_gh_aw

def test_usa_gh_aw():
    """Prueba cuando existen ambos archivos con el mismo nombre."""
    archivos = ['report.md', 'report.lock.yml', 'otro_archivo.txt']
    assert uses_gh_aw(archivos) == True

def test_solo_md():
    """Prueba cuando solo existe el archivo Markdown."""
    archivos = ['report.md', 'script.py']
    assert uses_gh_aw(archivos) == False

def test_solo_yml():
    """Prueba cuando solo existe el archivo compilado."""
    archivos = ['report.lock.yml', 'README.md']
    assert uses_gh_aw(archivos) == False

def test_nombres_distintos():
    """Prueba cuando existen ambos pero no comparten el nombre base."""
    archivos = ['report.md', 'other.lock.yml']
    assert uses_gh_aw(archivos) == False