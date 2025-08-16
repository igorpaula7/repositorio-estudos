import os as terminal
import sqlite3 as sqlite

conexao = sqlite.connect("agenda.db")
cursor = conexao.cursor()

def criar_banco_de_dados():
    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  telefone TEXT NOT NULL)''')
    
def listar_opcoes():
    terminal.system("clear")
    print("""
░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░
██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗
███████║██║░░██╗░█████╗░░██╔██╗██║██║░░██║███████║
██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║
██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║
╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝
          """)
    print("Digite 1 para Cadastrar um contato.")
    print("Digite 2 para Listar os contatos.")
    print("Digite 3 para Atualizar um contato.")
    print("Digite 4 para Apagar um contato.")
    print()

def exibir_subtitulo(subtitulo):
    terminal.system('clear')
    print(subtitulo)

def cadastrar_contato():
    exibir_subtitulo("Cadastrando um contato.")
    nome = input("Digite o nome do contato a ser cadastrado: ")
    telefone = input("Digite o telefone do contato a ser cadastrado: ")

    cursor.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", (nome, telefone))

def listar_contatos():
    exibir_subtitulo("Lista de Contatos:")

    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    
    print()
    for contato in contatos:
        print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")
    print()
    
def atualizar_contato():
    exibir_subtitulo("Atualizando um contato: ")
    nome = input("Digite o nome do contato que você deseja alterar o número: ")
    novo_telefone = input("Digite o número correto do contato: ")
    cursor.execute("UPDATE contatos SET telefone = ? WHERE nome = ?", (novo_telefone, nome))

def deletar_contato():
    exibir_subtitulo("Deletando um contato")
    nome = input("Digite o nome do contato a ser deletado: ")

    cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))

def escolher_opcao():

    try:
        opcao_escolhida = int(input("Digite a opção que deseja executar: "))
        match opcao_escolhida:
            case 1:
                cadastrar_contato()
            case 2:
                listar_contatos()
            case 3:
                atualizar_contato()
            case 4:
                deletar_contato()
            case _:
                print("Opção inválida")
    except:
        print("Digite uma opção válida")

def main():

    criar_banco_de_dados()

    continuar = "sim"

    while continuar in ["sim", "s", "yes", "y", "si", "ye"]:
        listar_opcoes()
        escolher_opcao()
        continuar = input("Deseja fazer mais alguma coisa? ").lower()
    
    conexao.commit()
    conexao.close()

if __name__ == '__main__':
    main()