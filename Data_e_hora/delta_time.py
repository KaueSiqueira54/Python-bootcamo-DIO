from datetime import timedelta, datetime, date, time

tipo_carro = "g"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "p":
    data_esttimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_esttimada}")
elif tipo_carro == "m":
    data_esttimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_esttimada}")
else:
    data_esttimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou {data_atual} e ficará pronto ás {data_esttimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2024, 3, 25, 19, 26, 23) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())