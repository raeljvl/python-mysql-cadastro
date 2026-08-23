import mysql.connector

try:
    # 1. Conectando ao banco
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro"
    )

    if conexao.is_connected():
        cursor = conexao.cursor()
        
        print("--- TELA DE CADASTRO ---")
        
        # 2. Coletando os dados pelo teclado do Python
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ")
        peso = float(input("Digite o peso (ex: 75.5): "))
        altura = float(input("Digite a altura (ex: 1.75): "))
        nacionalidade = input("Digite a nacionalidade: ")

        # 3. Preparando o comando SQL com placeholders (%s) por segurança
        comando_sql = """
        INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade) 
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        dados_pessoa = (nome, idade, sexo, peso, altura, nacionalidade)

        # 4. Executando o comando
        cursor.execute(comando_sql, dados_pessoa)
        
        # MUITO IMPORTANTE: Salva as alterações no banco de dados de verdade
        conexao.commit()
        
        print(f"\n[SUCESSO] {nome} foi cadastrado corretamente no banco!")

except mysql.connector.Error as erro:
    print(f"[ERRO] Falha ao cadastrar: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexao encerrada.")
