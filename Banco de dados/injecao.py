import sqlite3

conexao = sqlite3.connect("meubanco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

#forma errada de utilizar consultas
id_cliente = input("informe o id do cliente: ")
#brecha de segurança com format 
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
cliente = cursor.fetchone()
print(dict(cliente))