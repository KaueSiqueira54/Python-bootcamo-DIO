import sqlite3

conexao = sqlite3.connect("meubanco.sqlite")
cursor = conexao.cursor()

#Criando tabelas CRATE TABLE
def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARSHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

#Inserindo registror INSERT INTO
def inserindo_registros(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()

#atualizando dados UPDATE
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

#Excluindo um registro DELETE FROM
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

#Inserindo muitos EXECUTEMANY
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()

def recuperar_clientes(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

cliente = recuperar_clientes(cursor, 3)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
#dados a serem inseridos com executemany
#dados = [
###   ("refinaldo", "guas@gmail.com"),
 #   ("mel", "guivc@gmail.com"),
  #  ("amin", "guias@gmail.com"),
 #   ("adji", "guicd@gmail.com"),
#] 
#inserir_muitos(conexao, cursor, dados)
#atualizar_registro(conexao, cursor, "Kaue Siqueira", "Kaue54@gmail.com", 1)
#atualizar_registro(conexao, cursor, "Giovana", "Gi@gmail.com", 2)
#excluir_registro(conexao, cursor, 2)