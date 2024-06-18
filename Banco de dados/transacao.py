import sqlite3

conexao = sqlite3.connect("meubanco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Teste5", "teste@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)", (2, "Teste4", "teste@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Um erro aconteceu! {exc}")
    conexao.rollback()
#pode ser assim tambem
#finally:
 #   conexao.commit()



