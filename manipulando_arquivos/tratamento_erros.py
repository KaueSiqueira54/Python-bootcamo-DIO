from pathlib import Path

try:
    arquivo = open("new_meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)

ROOt_PATH = Path(__file__).parent

try:
    arquivo = open(ROOt_PATH / "new-diretorio")
except Exception as exc:
    print(f"não foi possivel abrir o arquivo: {exc}")
