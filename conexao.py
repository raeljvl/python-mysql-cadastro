import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro"
    )

    if conexao.is_connected():
        print("[SUCESSO] Conectado ao banco 'cadastro'!")
        cursor = conexao.cursor()
        
        # O comando mudou para buscar os dados das pessoas!
        cursor.execute("SELECT * FROM pessoas;")
        
        print("\n--- PESSOAS CADASTRADAS NO BANCO ---")
        resultados = cursor.fetchall()
        
        if not resultados:
            print("Nenhuma pessoa encontrada. Adicione alguem no MySQL Workbench!")
        else:
            for pessoa in resultados:
                print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]} | Nacionalidade: {pessoa[5]}")

except mysql.connector.Error as erro:
    print(f"[ERRO] Erro ao conectar ao MySQL: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\nConexao encerrada com seguranca.")
