import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BACK import Sistema, LivroFisico, LivroDigital, Usuario

# Função para adicionar um livro
def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    genero = entry_genero.get()
    tipo = combo_tipo.get()
    
    if tipo == 'Fisico':
        livro = LivroFisico(titulo, autor, genero)
    else:
        livro = LivroDigital(titulo, autor, genero)
    
    sistema.adicionar_livro(livro)
    print(f'Livro {titulo} adicionado.')
    messagebox.showinfo("Sucesso", f'Livro "{titulo}" adicionado.')

# Função para adicionar um usuário
def adicionar_usuario():
    id = int(entry_id.get())
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    senha = entry_senha.get()
    tipo = combo_tipo_usuario.get()

    usuario = Usuario(id, nome, cpf, senha, tipo)
    sistema.adicionar_usuario(usuario)
    print(f'Usuário {nome} adicionado.')
    messagebox.showinfo("Sucesso", f'Usuário "{nome}" adicionado.')

# Função para emprestar um livro
def emprestar_livro():
    titulo = entry_titulo_emprestimo.get()
    id_usuario = int(entry_id_usuario_emprestimo.get())
    
    sistema.emprestar_livro(titulo, id_usuario)
    print(f'Livro {titulo} emprestado ao usuário {id_usuario}.')
    messagebox.showinfo("Sucesso", f'Livro "{titulo}" emprestado ao usuário {id_usuario}.')

# Função para devolver um livro
def devolver_livro():
    titulo = entry_titulo_devolucao.get()
    id_usuario = int(entry_id_usuario_devolucao.get())
    
    sistema.devolver_livro(titulo, id_usuario)
    print(f'Livro {titulo} devolvido pelo usuário {id_usuario}.')
    messagebox.showinfo("Sucesso", f'Livro "{titulo}" devolvido pelo usuário {id_usuario}.')

# Função para listar dados
def listar_dados():
    tipo = combo_lista_tipo.get()
    resultados = sistema.listar(tipo)
    
    if resultados:
        exibir_lista(resultados)
    else:
        messagebox.showinfo("Aviso", f"Nenhum resultado encontrado para o tipo {tipo}.")

# Função para exibir a lista em uma nova janela
def exibir_lista(resultados):
    lista_window = tk.Toplevel(root)
    lista_window.title("Lista")
    
    columns = ("ID", "Título", "Autor", "Gênero", "Tipo")
    tree_lista = ttk.Treeview(lista_window, columns=columns, show='headings')
    tree_lista.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    
    for col in columns:
        tree_lista.heading(col, text=col)
        tree_lista.column(col, width=100)
    
    for resultado in resultados:
        tree_lista.insert("", "end", values=resultado)
    
    vsb_lista = ttk.Scrollbar(lista_window, orient="vertical", command=tree_lista.yview)
    vsb_lista.grid(row=0, column=1, sticky='ns')
    tree_lista.configure(yscrollcommand=vsb_lista.set)

# Inicializa o sistema
sistema = Sistema('POO.xlsx')

# Cria a janela principal
root = tk.Tk()
root.title("Sistema de Biblioteca")

# Cria as guias
tab_control = ttk.Notebook(root)

tab_livros = ttk.Frame(tab_control)
tab_usuarios = ttk.Frame(tab_control)
tab_reservas = ttk.Frame(tab_control)
tab_lista = ttk.Frame(tab_control)

tab_control.add(tab_livros, text='Livros')
tab_control.add(tab_usuarios, text='Usuários')
tab_control.add(tab_reservas, text='Empréstimos e Devoluções')
tab_control.add(tab_lista, text='Lista')

tab_control.pack(expand=1, fill='both')

# Frame para adicionar livros
frame_adicionar_livro = ttk.LabelFrame(tab_livros, text='Adicionar Livro')
frame_adicionar_livro.pack(padx=10, pady=10, fill='x', expand=True)

# Campos de entrada para livros
ttk.Label(frame_adicionar_livro, text="Título:").grid(column=0, row=0, padx=5, pady=5)
entry_titulo = ttk.Entry(frame_adicionar_livro)
entry_titulo.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(frame_adicionar_livro, text="Autor:").grid(column=0, row=1, padx=5, pady=5)
entry_autor = ttk.Entry(frame_adicionar_livro)
entry_autor.grid(column=1, row=1, padx=5, pady=5)

ttk.Label(frame_adicionar_livro, text="Gênero:").grid(column=0, row=2, padx=5, pady=5)
entry_genero = ttk.Entry(frame_adicionar_livro)
entry_genero.grid(column=1, row=2, padx=5, pady=5)

ttk.Label(frame_adicionar_livro, text="Tipo:").grid(column=0, row=3, padx=5, pady=5)
combo_tipo = ttk.Combobox(frame_adicionar_livro, values=['Fisico', 'Digital'])
combo_tipo.grid(column=1, row=3, padx=5, pady=5)

btn_adicionar_livro = ttk.Button(frame_adicionar_livro, text="Adicionar Livro", command=adicionar_livro)
btn_adicionar_livro.grid(column=0, row=4, columnspan=2, pady=10)

# Frame para adicionar usuários
frame_adicionar_usuario = ttk.LabelFrame(tab_usuarios, text='Adicionar Usuário')
frame_adicionar_usuario.pack(padx=10, pady=10, fill='x', expand=True)

# Campos de entrada para usuários
ttk.Label(frame_adicionar_usuario, text="ID:").grid(column=0, row=0, padx=5, pady=5)
entry_id = ttk.Entry(frame_adicionar_usuario)
entry_id.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(frame_adicionar_usuario, text="Nome:").grid(column=0, row=1, padx=5, pady=5)
entry_nome = ttk.Entry(frame_adicionar_usuario)
entry_nome.grid(column=1, row=1, padx=5, pady=5)

ttk.Label(frame_adicionar_usuario, text="CPF:").grid(column=0, row=2, padx=5, pady=5)
entry_cpf = ttk.Entry(frame_adicionar_usuario)
entry_cpf.grid(column=1, row=2, padx=5, pady=5)

ttk.Label(frame_adicionar_usuario, text="Senha:").grid(column=0, row=3, padx=5, pady=5)
entry_senha = ttk.Entry(frame_adicionar_usuario, show="*")
entry_senha.grid(column=1, row=3, padx=5, pady=5)

ttk.Label(frame_adicionar_usuario, text="Tipo:").grid(column=0, row=4, padx=5, pady=5)
combo_tipo_usuario = ttk.Combobox(frame_adicionar_usuario, values=['comum', 'admin'])
combo_tipo_usuario.grid(column=1, row=4, padx=5, pady=5)

btn_adicionar_usuario = ttk.Button(frame_adicionar_usuario, text="Adicionar Usuário", command=adicionar_usuario)
btn_adicionar_usuario.grid(column=0, row=5, columnspan=2, pady=10)

# Frame para gerenciar reservas
frame_gerenciar_reservas = ttk.LabelFrame(tab_reservas, text='Gerenciar Empréstimos e Devoluções')
frame_gerenciar_reservas.pack(padx=10, pady=10, fill='x', expand=True)

# Empréstimo de livros
frame_emprestar_livro = ttk.LabelFrame(frame_gerenciar_reservas, text='Emprestar Livro')
frame_emprestar_livro.pack(padx=10, pady=10, fill='x', expand=True)

ttk.Label(frame_emprestar_livro, text="Título:").grid(column=0, row=0, padx=5, pady=5)
entry_titulo_emprestimo = ttk.Entry(frame_emprestar_livro)
entry_titulo_emprestimo.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(frame_emprestar_livro, text="ID Usuário:").grid(column=0, row=1, padx=5, pady=5)
entry_id_usuario_emprestimo = ttk.Entry(frame_emprestar_livro)
entry_id_usuario_emprestimo.grid(column=1, row=1, padx=5, pady=5)

btn_emprestar_livro = ttk.Button(frame_emprestar_livro, text="Emprestar Livro", command=emprestar_livro)
btn_emprestar_livro.grid(column=0, row=2, columnspan=2, pady=10)

# Devolução de livros
frame_devolver_livro = ttk.LabelFrame(frame_gerenciar_reservas, text='Devolver Livro')
frame_devolver_livro.pack(padx=10, pady=10, fill='x', expand=True)

ttk.Label(frame_devolver_livro, text="Título:").grid(column=0, row=0, padx=5, pady=5)
entry_titulo_devolucao = ttk.Entry(frame_devolver_livro)
entry_titulo_devolucao.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(frame_devolver_livro, text="ID Usuário:").grid(column=0, row=1, padx=5, pady=5)
entry_id_usuario_devolucao = ttk.Entry(frame_devolver_livro)
entry_id_usuario_devolucao.grid(column=1, row=1, padx=5, pady=5)

btn_devolver_livro = ttk.Button(frame_devolver_livro, text="Devolver Livro", command=devolver_livro)
btn_devolver_livro.grid(column=0, row=2, columnspan=2, pady=10)

# Frame para listar dados
frame_lista = ttk.LabelFrame(tab_lista, text='Lista')
frame_lista.pack(padx=10, pady=10, fill='both', expand=True)

ttk.Label(frame_lista, text="Tipo:").grid(column=0, row=0, padx=5, pady=5)
combo_lista_tipo = ttk.Combobox(frame_lista, values=['LIVROS', 'USUARIOS', 'RESERVAS'])
combo_lista_tipo.grid(column=1, row=0, padx=5, pady=5)

btn_listar_dados = ttk.Button(frame_lista, text="Listar Dados", command=listar_dados)
btn_listar_dados.grid(column=0, row=1, columnspan=2, pady=10)

# Executa a janela principal
root.mainloop()
