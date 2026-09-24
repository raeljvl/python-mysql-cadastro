import mysql.connector

# Configuração ajustada para o WampServer (porta 3306 e sem senha)
CONFIG_MYSQL = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',        # Senha padrão do WampServer é vazia
    'database': 'cadastro'
}

def cadastrar_usuario():
    print("___ DIGITE OS DADOS PARA CADASTRO ___\n")

    nome = input("Digite seu nome: ").title()
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ").strip().upper()
    peso = float(input("Digite seu peso: ").replace(",", "."))
    altura = float(input("Digite sua altura: ").replace(",", "."))
    cpf = input("Digite seu CPF (apenas números): ")

    return {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "peso": peso,
        "altura": altura,
        "cpf": cpf
    }

def salvar_no_mysql(usuario):
    try:
        conexao = mysql.connector.connect(**CONFIG_MYSQL)
        cursor = conexao.cursor()

        # Corrigido: Apontando para a tabela 'usuario'
        sql = """
            INSERT INTO usuario (nome, idade, sexo, peso, altura, cpf)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        dados = (
            usuario["nome"],
            usuario["idade"],
            usuario["sexo"],
            usuario["peso"],
            usuario["altura"],
            usuario["cpf"]
        )

        cursor.execute(sql, dados)
        conexao.commit()
        print("\n✅ Usuário cadastrado e sincronizado no MySQL com sucesso!")

    except mysql.connector.Error as erro:
        print(f"\n❌ Erro ao salvar no MySQL: {erro}")
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def listar_usuarios():
    try:
        conexao = mysql.connector.connect(**CONFIG_MYSQL)
        cursor = conexao.cursor()

        # Corrigido: Apontando para a tabela 'usuario'
        cursor.execute("SELECT * FROM usuario;")
        registros = cursor.fetchall()

        print("\n================ DADOS REGISTRADOS NO NOVO BANCO ================")
        if not registros:
            print("Nenhum registro encontrado.")
        else:
            for linha in registros:
                print(f"Nome: {linha[0]} | Idade: {linha[1]} | Sexo: {linha[2]} | Peso: {linha[3]}kg | Altura: {linha[4]}m | CPF: {linha[5]}")
        print("==================================================================")

    except mysql.connector.Error as erro:
        print(f"\n❌ Erro ao consultar a tabela: {erro}")
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# --- EXECUÇÃO DO TESTE ---
novo_usuario = cadastrar_usuario()
salvar_no_mysql(novo_usuario)
listar_usuarios()