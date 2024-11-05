import os 
import mysql.connector

#Conexão com o Banco de Dados 
conexaoDB = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "senai",
    database= "materialize"
)

#Função para cadastrar produtos no almoxerifado
def cadastrar_produto():
    imprimir_header() 
    print("*** Cadastro de Material ***")
    
    #Informações do Material: 
    nomeMaterial = input("Informe o nome do Material: ")
    funcionalidade = input("Digite a funcionalidade: ")

    try:
    #Informação para o ESTOQUE
        quantidade = int(input("Insira a quantidade no estoque: "))
    except ValueError:
        print("Erro! A quantidade deve ser um valor númerico")
        return #Voltará para o Menu


    #Validação 
    if (not nomeMaterial) or (not funcionalidade) or (quantidade < 0):
        print("Erro! Todos os campos devem ser preenchidos e a quantidade não pode ser negativa!")
        return

    if len(nomeMaterial) > 45:
        print("Erro! O nomeMaterial do material é maior que 45 caracteres!")
        return

    
    #Comando SQL para inserir na Tabela Estoque 
    comandoSQL_estoque = f'INSERT INTO Estoque (quantidade) VALUES ({quantidade})'
    

    try:
        cursorDB = conexaoDB.cursor()

        #Inserimos a quantidade no estoque
        cursorDB.execute(comandoSQL_estoque)

        #A função lastrowid captura o ID do estoque recém-criado
        idEstoque = cursorDB.lastrowid

        #comandoSQL para inserir na Tabela Material
        comandoSQL = f'INSERT INTO Material (nomeMaterial, Funcionalidade, idEstoque) VALUES ("{nomeMaterial}", "{funcionalidade}", {idEstoque})'
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()

    except mysql.connector.Error as erro:
        print(f"Erro! Falha ao cadastrar: {erro}")

    print("*** OK! Material e estoque cadastrados com sucesso! ***")
    cursorDB.close()


def listar_produtos():
    imprimir_header()  # Cabeçalho
    print("*** Lista de Materiais ***")

    try:
        cursorDB = conexaoDB.cursor()
        # Corrigindo a consulta SQL para incluir a coluna 'quantidade'
        cursorDB.execute('''
            SELECT 
                material.idMaterial, 
                material.nomeMaterial, 
                material.funcionalidade, 
                Estoque.quantidade
            FROM Material 
            JOIN Estoque ON material.idEstoque = Estoque.idEstoque;
        ''')
        resultados = cursorDB.fetchall()

        if not resultados:
            print("Não há produtos cadastrados!")
        else:
            for material in resultados:
                # Acessando a quantidade diretamente do resultado
                print(f"ID: {material[0]} -  NOME: {material[1]} - FUNCIONALIDADE: {material[2]} - QUANTIDADE: {material[3]}")

    except mysql.connector.Error as Erro:
        print(f"Erro! Falha ao listar: {Erro}")
    cursorDB.close()


# Funçao para selecionar o material apartir do seu id
def get_material(id_material):
    imprimir_header() #Cabeçalho
    cursorDB = conexaoDB.cursor()
    # Coamndo SQL para selecionar os materiais pegando o ID
    comandoSQL = f'SELECT * FROM Material WHERE idMaterial = {idMaterial}'
    cursorDB.execute(comandoSQL)
    resultado = cursorDB.fetchone()
    cursorDB.close()
    return resultado

# Função para excluir o material
def excluir_material(id_material):
    imprimir_header() #Cabeçalho
    # verifica se o material existe
    material = get_material(id_material)

    if not material: 
        return {"error": f"Material com o ID {id_material} não encontrado!"}

    try:
        cursorDB = conexaoDB.cursor()
        # Coamndo SQL para deletar o material 
        comandoSQL = f"DELETE FROM Material WHERE id_material = {id_material}"
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
        cursorDB.close()
        return {"message": "Material excluído com sucesso!"}
    
    except mysql.connector.Error as Erro:
        return {"error": f"Erro ao excluir o material: {Erro}"}

def imprimir_header():
    os.system('cls')
    print("- " * 20)
    print("*** SISTEMA PAPELARIA ***")
    print("- " * 20)
    return

# Programa Principal
while True:
    imprimir_header()
    print("MENU - Informe a opção desejada: ")
    print("1 - Cadastrar produto")
    print("2 - Alterar quantidade")
    print("4 - Mostrar todos os produtos")
    print("5 - Excluir um produto")
    print("6 - Sair")

    opcao = input("Informe a opção desejada: ")

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '3':
        altera_preco()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        excluir_produto()
    elif opcao == '6':
        break
    else:
        print("Opção inválida!")      

    os.system('pause')

print("SISTEMA ENCERRADO!")
conexaoDB.close()