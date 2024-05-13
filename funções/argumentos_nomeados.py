def salvar_carro(marca, modelo, ano, placa):
    #salva esses dados no banco de dados
    if 1 == 1:
        print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1990, "ABC-1564")
print(salvar_carro)
#forma mais recomendada, menis chance de erro com usuário declarando onde cada argumento deve estar
salvar_carro(marca="Fiat", modelo="Palio", ano=1998, placa="ABD-5643")
salvar_carro(*({"marca": "Fiat", "modelo": "Palio", "ano" : 1998, "placa" : "ABC-465"}))
