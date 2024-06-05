import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BACK import Sistema

def preencher_lista_livros():
    try:
        resultados = sistema.listar('LIVROS')
        
        # Limpa a lista atual antes de adicionar os resultados
        limpar_lista_livros()

        for i, livro in enumerate(resultados, start=1):
            lista_livros.insert("", "end", iid=i, values=livro)

    except Exception as e:
        messagebox.showerror("Erro", f'Erro ao preencher lista de livros: {e}')

def filtrar_lista_livros():
    try:
        filtro = combo_filtro.get().lower()
        valor = entry_valor.get().lower()

        resultados = sistema.listar('LIVROS')
        resultados_filtrados = []

        # Mapeamento de filtros para colunas
        filtro_map = {
            "autor": 1,
            "título": 0,
            "gênero": 2,
            "tipo": 3,
            "status": 4
        }

        coluna = filtro_map.get(filtro)

        if coluna is not None:
            resultados_filtrados = list(filter(lambda livro: valor in livro[coluna].lower(), resultados))
        
        # Limpa a lista atual antes de adicionar os resultados filtrados
        limpar_lista_livros()

        for i, livro in enumerate(resultados_filtrados, start=1):
            lista_livros.insert("", "end", iid=i, values=livro)

    except Exception as e:
        messagebox.showerror("Erro", f'Erro ao filtrar livros: {e}')

def limpar_lista_livros():
    # Limpa a lista de livros
    for item in lista_livros.get_children():
        lista_livros.delete(item)

sistema = Sistema('POO.xlsx')

root = tk.Tk()
root.title("Lista de Livros")

frame_lista_livros = ttk.Frame(root)
frame_lista_livros.pack(fill='both', expand=True, padx=10, pady=10)

combo_filtro = ttk.Combobox(frame_lista_livros, values=["Título", "Autor", "Gênero", "Tipo", "Status"])
combo_filtro.grid(row=0, column=0, padx=5, pady=5)

entry_valor = ttk.Entry(frame_lista_livros)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

btn_filtrar = ttk.Button(frame_lista_livros, text="Filtrar", command=filtrar_lista_livros)
btn_filtrar.grid(row=0, column=2, padx=5, pady=5)

columns = ("Título", "Autor", "Gênero", "Tipo", "Status")
lista_livros = ttk.Treeview(frame_lista_livros, columns=columns, show='headings')
lista_livros.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

for col in columns:
    lista_livros.heading(col, text=col)
    lista_livros.column(col, width=100)

# Preenche a lista de livros inicialmente
preencher_lista_livros()

root.mainloop()

