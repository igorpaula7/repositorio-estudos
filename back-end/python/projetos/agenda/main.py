# Projeto de uma agenda básica, onde o usuário consegue:
# Cadastrar contatos; (Create)
# Listar contatos; (Read)
# Atualizar contatos; (Update)
# Apagar Contatos; (Delete)

import os

contatos = []

def listar_opcoes():
    os.system("clear")
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
    os.system('clear')
    print(subtitulo)

def cadastrar_contato():
    exibir_subtitulo("Cadastrando um contato.")
    registro = {}
    nome = input("Digite o nome do contato a ser cadastrado: ")
    telefone = input("Digite o telefone do contato a ser cadastrado: ")
    registro['Nome'] = nome
    registro['Telefone'] = telefone
    contatos.append(registro)

def listar_contatos():
    exibir_subtitulo("Lista de Contatos:")
    for contato in contatos:
        print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}")
    
    if len(contatos) == 0:
        print("Lista vazia!")

def atualizar_contato():
    exibir_subtitulo("Atualizando um contato: ")
    nome = input("Digite o nome do contato que você deseja alterar o número: ")
    novo_telefone = input("Digite o número correto do contato: ")
    for contato in contatos:
        if contato["Nome"].lower() == nome.lower():
            contato["Telefone"] = novo_telefone

def deletar_contato():
    exibir_subtitulo("Deletando um contato")
    nome = input("Digite o nome do contato a ser deletado: ")
    for contato in contatos:
        if contato["Nome"] == nome:
            indice = contatos.index(contato)
            contatos.pop(indice)

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

    continuar = "sim"

    while continuar in ["sim", "s", "yes", "y"]:
        listar_opcoes()
        escolher_opcao()
        continuar = input("Deseja fazer mais alguma coisa? ").lower()

if __name__ == '__main__':
    main()