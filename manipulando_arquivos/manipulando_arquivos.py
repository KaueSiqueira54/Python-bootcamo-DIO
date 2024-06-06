from pathlib import Path

ROOT_PATH =Path(__file__).parent

#fechando corretemente o arquivo
try:
    with open(ROOT_PATH / "lllorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


#try:
#    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#        arquivo.write("Aprendendo manipular arquivos com python")
#except IOError as exc:
 #   print(f"Erro ao abrir o arquivo {exc}")
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

