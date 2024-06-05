from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-06-05 14:40"
mascara = "%d/%m/%Y %H:%M"
mascara_p = "%Y-%m-%d %H:%M"

#data formatada
print(data_hora_atual.strftime(mascara))

#data convertida
print(datetime.strptime(data_hora_str, mascara_p))
