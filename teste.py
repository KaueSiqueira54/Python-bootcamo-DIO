def validate_numero_telefone(phone_number):
    phone_number = ["(XX) 9XXXX-XXXX"]
    if len(phone_number) != 15:
      return "Número de telefone inválido."
    if phone_number[0] !="(" or phone_number[9] != "-":
      return "Número de telefone inválido"
    for i in [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]:
      if not phone_number[i].isdigit():
        return "Número de telefone inválido."
      if phone_number[1] == "0":
        return "Número de telefone inválido."
      if phone_number[4] != "9":
        return "Número de telefone inválido."
    return "Número de tefone válido."

phone_number = (input("Numero de telefone"))
print(validate_numero_telefone(phone_number))
print(len(phone_number))