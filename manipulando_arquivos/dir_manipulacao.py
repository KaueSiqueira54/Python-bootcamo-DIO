import os
import shutil
from pathlib import Path

#criando uma nova pasta/diretorio na pasta atual
ROOt_PATH = Path(__file__).parent
#os.mkdir(ROOt_PATH / "novo-diretorio")

#criando novo arquivo na pasta atual
#arquivo.open(ROOTH_PATH / "novo-arquivo.txt")
#arquivo.close()

#alternado nome do arquivo
#os.rename(ROOt_PATH / "novo.txt", ROOt_PATH / "alterado.txt")

#removendo arquivo
#os.remove(ROOt_PATH / "alterado.txt")

#movendo arquivo para a pasta novo diretorio
shutil.move(ROOt_PATH / "novo.txt", ROOt_PATH / "novo-diretorio" / "novo.txt")
