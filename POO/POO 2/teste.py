from BACK import Livro, Usuario, Reserva, Sistema

def mostrar_menu():
    print("\n--- Sistema de Gerenciamento da Biblioteca ---")
    print("1. LIVROS")
    print("2. USUÁRIOS")
    print("3. RESERVAS")
    print("0. SAIR")

def mostrar_menu_livros():
    print("\n--- Menu Livros ---")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Remover Livro")
    print("0. Voltar")

def mostrar_menu_usuarios():
    print("\n--- Menu Usuários ---")
    print("1. Criar Usuário")
    print("2. Listar Usuários")
    print("3. Apagar Usuário")
    print("0. Voltar")

def mostrar_menu_reservas():
    print("\n--- Menu Reservas ---")
    print("1. Adicionar Reserva")
    print("2. Listar Reservas")
    print("3. Remover Reserva")
    print("0. Voltar")

def autenticar_usuario(sistema):
    print("\n--- Login ---")
    while True:
        nome_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        usuario = sistema.autenticar_usuario(nome_usuario, senha)
        if usuario:
            print(f"Bem-vindo, {usuario.nome}!")
            return usuario
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")

def main():
    sistema = Sistema('POO.xlsx')

    usuario_logado = autenticar_usuario(sistema)

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            while True:
                mostrar_menu_livros()
                escolha_livro = input("Escolha uma opção: ")

                if escolha_livro == "1":
                    titulo = input("Título do livro: ")
                    autor = input("Autor do livro: ")
                    genero = input("Gênero do livro: ")
                    tipo = input("Tipo do livro: ")
                    status = input("Status do livro: ")
                    novo_livro = Livro(titulo, autor, genero, tipo, status)
                    sistema.adicionar_livro(novo_livro)
                    print("Livro adicionado com sucesso!")
                    
                elif escolha_livro == "2":
                    sistema.listar('livros')
                    
                elif escolha_livro == "3":
                    titulo = input("Título do livro a ser removido: ")
                    sistema.excluir('livros', titulo)
                    print("Livro removido com sucesso!")
                    
                elif escolha_livro == "0":
                    break
                    
                else:
                    print("Opção inválida!")

        elif escolha == "2":
            while True:
                mostrar_menu_usuarios()
                escolha_usuario = input("Escolha uma opção: ")

                if escolha_usuario == "1":
                    id = input("ID do usuário: ")
                    nome = input("Nome do usuário: ")
                    cpf = input("CPF do usuário: ")
                    senha = input("Senha do usuário: ")
                    tipo = input("Tipo do usuário: (0 = FUNCIONARIO / 1 = USUÁRIO) ")
                    novo_usuario = Usuario(id, nome, cpf, senha, tipo)
                    sistema.adicionar_usuario(novo_usuario)
                    print("Usuário criado com sucesso!")
                    
                elif escolha_usuario == "2":
                    sistema.listar('usuarios')
                    
                elif escolha_usuario == "3":
                    id = input("ID do usuário a ser removido: ")
                    sistema.excluir('usuarios', id)
                    print("Usuário removido com sucesso!")
                    
                elif escolha_usuario == "0":
                    break
                    
                else:
                    print("Opção inválida!")

        elif escolha == "3":
            while True:
                mostrar_menu_reservas()
                escolha_reserva = input("Escolha uma opção: ")

                if escolha_reserva == "1":
                    titulo = input("Título do livro da reserva: ")
                    tipo = input("Tipo do livro da reserva: ")
                    id_usuario = input("ID do usuário para a reserva: ")
                    data_reserva = input("Data de reserva da reserva: ")
                    data_devolucao = input("Data de devolução da reserva: ")
                    nova_reserva = Reserva(titulo, tipo, id_usuario, data_reserva, data_devolucao)
                    sistema.adicionar_reserva(nova_reserva)
                    print("Reserva adicionada com sucesso!")
                    
                elif escolha_reserva == "2":
                    sistema.listar('reservas')
                    
                elif escolha_reserva == "3":
                    titulo = input("Título do livro da reserva a ser removida: ")
                    sistema.excluir('reservas', titulo)
                    print("Reserva removida com sucesso!")
                    
                elif escolha_reserva == "0":
                    break
                    
                else:
                    print("Opção inválida!")

        elif escolha == "0":
            print("Saindo...")
            sistema.salvar()
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
