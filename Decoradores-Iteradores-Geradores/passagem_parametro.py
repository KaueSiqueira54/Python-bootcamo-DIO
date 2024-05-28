def mensagem(nome):
    print("executando nome")
    return f"oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá, tudo bom {nome}?"

def executar(funcao, nome):
    print("Executando a executar")
    return funcao(nome)

print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Nilo"))
