from miner.logic import uses_gh_aw, parse_markdown_file

def test_usa_gh_aw():
    archivos = ['report.md', 'report.lock.yml', 'otro_archivo.txt']
    assert uses_gh_aw(archivos) == True

def test_solo_md():
    archivos = ['report.md', 'script.py']
    assert uses_gh_aw(archivos) == False

def test_solo_yml():
    archivos = ['report.lock.yml', 'README.md']
    assert uses_gh_aw(archivos) == False

def test_nombres_distintos():
    archivos = ['report.md', 'other.lock.yml']
    assert uses_gh_aw(archivos) == False

def test_parse_markdown_file():
    # Un string simple y directo que nuestra nueva lógica dividirá perfectamente
    contenido_prueba = "---\nname: triage-agent\ntype: issues\n---\n# Instrucciones\nEste es el cuerpo."
    
    resultado = parse_markdown_file(contenido_prueba)
    
    assert resultado["frontmatter"]["name"] == "triage-agent"
    assert resultado["frontmatter"]["type"] == "issues"
    assert "# Instrucciones" in resultado["body"]
    assert "Este es el cuerpo" in resultado["body"]