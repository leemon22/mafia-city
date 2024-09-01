from pathlib import Path

for archivo in Path("./resultados").glob("*"):
    if archivo.is_file():
        archivo.unlink()
