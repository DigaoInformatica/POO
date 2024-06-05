import tkinter as tk
from tkinter import messagebox
from BACK import Sistema, LivroFisico, LivroDigital, Usuario, Reserva
from datetime import datetime

class LoginApp:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema

        self.root.title("Login")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
        self.lbl_username = tk.Label(self.root, text="Usuário:")
        self.lbl_username.grid(row=0, column=0)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1)

        self.lbl_password = tk.Label(self.root, text="Senha:")
        self.lbl_password.grid(row=1, column=0)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1)

        # Buttons
        self.btn_login = tk.Button(self.root, text="Login", command=self.login)
        self.btn_login.grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verificar se é um usuário válido ou funcionário
        if username == "usuario" and password == "senha_usuario":
            messagebox.showinfo("Login", "Login de usuário bem-sucedido!")
            self.root.destroy()
            self.open_main_app("usuario")
        elif username == "funcionario" and password == "senha_funcionario":
            messagebox.showinfo("Login", "Login de funcionário bem-sucedido!")
            self.root.destroy()
            self.open_main_app("funcionario")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

    def open_main_app(self, user_type):
        if user_type == "usuario":
            sistema = Sistema('POO.xlsx', user_type)
            root = tk.Tk()
            app = UserApp(root, sistema)
            root.mainloop()
        elif user_type == "funcionario":
            sistema = Sistema('POO.xlsx', user_type)
            root = tk.Tk()
            app = StaffApp(root, sistema)
            root.mainloop()

class UserApp:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema

        self.root.title("Sistema de Biblioteca - Usuário")

        self.create_widgets()

    def create_widgets(self):
        # Your user interface for regular users goes here
        pass

class StaffApp:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema

        self.root.title("Sistema de Biblioteca - Funcionário")

        self.create_widgets()

    def create_widgets(self):
        # Your user interface for staff goes here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    login_app = LoginApp(root, None)
    root.mainloop()
