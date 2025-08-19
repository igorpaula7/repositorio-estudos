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
          \n""")
    print("Digite 1 para Cadastrar um contato.")
    print("Digite 2 para Listar os contatos.")
    print("Digite 3 para Atualizar um contato.")
    print("Digite 4 para Apagar um contato.\n")

def exibir_subtitulo(subtitulo):
    terminal.system('clear')
    print(subtitulo)

def cadastrar_contato():
    exibir_subtitulo("Cadastrando um contato.")
    nome = input("Digite o nome do contato a ser cadastrado: ")
    telefone = input("Digite o telefone do contato a ser cadastrado: ")

    cursor.execute("INSERT INTO contatos (nome, telefone) VALUES (?, ?)", (nome, telefone))
    conexao.commit()

def listar_contatos():
    exibir_subtitulo("Lista de Contatos:")

    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conexao.commit()

    print()
    for contato in contatos:
        print(f"ID: {contato[0]} | Nome: {contato[1]} | Telefone: {contato[2]}")
    print()
    
def atualizar_contato():
    exibir_subtitulo("Atualizando um contato: ")
    nome = input("Digite o nome do contato que você deseja alterar o número: ")
    novo_telefone = input("Digite o número correto do contato: ")
    cursor.execute("UPDATE contatos SET telefone = ? WHERE nome = ?", (novo_telefone, nome))
    conexao.commit()

def deletar_contato():
    exibir_subtitulo("Deletando um contato")
    nome = input("Digite o nome do contato a ser deletado: ")
    cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))
    conexao.commit()

def escolher_opcao():

        opcao_escolhida = input("Digite a opção que deseja executar: ")

        if opcao_escolhida == "1":
            cadastrar_contato()
        elif opcao_escolhida == "2":
            listar_contatos()
        elif opcao_escolhida == "3":
            atualizar_contato()
        elif opcao_escolhida == "4":
            deletar_contato()
        else:
            print("\nOpção inválida")
            input("Pressione qualquer tecla para voltar\n")
            listar_opcoes()
            escolher_opcao()

def main():

    criar_banco_de_dados()

    continuar = "sim"

    while continuar in ["sim", "s", "yes", "y", "si", "ye"]:
        listar_opcoes()
        escolher_opcao()
        continuar = input("Deseja fazer mais alguma coisa? ").lower()
    
    conexao.close()

if __name__ == '__main__':
    main()