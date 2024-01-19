import tkinter as tk
from tkinter import ttk
from user_management import Authentication, Registration
from password_management import PasswordManager


class TkinterGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry('306x160')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root, bg="#282c34")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.loginInput = self.passwordInput = self.info = self._user_id = None
        self._flag = False
        self._create_widgets()
        self.root.bind('<Return>', lambda event: self._authentication())

        self.tree = self.scrollbar = self.style = None

    def _create_widgets(self) -> None:
        if self._flag:
            self._create_table()
            self._feel_table()

            self.serviceInput = tk.Entry(self.frame, width=20)
            self.serviceInput.place(relx=0.04, rely=0.70)
            self.loginInput = tk.Entry(self.frame, width=20)
            self.loginInput.place(relx=0.28, rely=0.70)
            self.passwordInput = tk.Entry(self.frame, width=20)
            self.passwordInput.place(relx=0.52, rely=0.70)
            self.descriptionInput = tk.Entry(self.frame, width=20)
            self.descriptionInput.place(relx=0.76, rely=0.70)

            tk.Label(self.frame, text="service", bg="#282c34", fg='#FFFFFF').place(relx=0.11, rely=0.75)
            tk.Label(self.frame, text="login", bg="#282c34", fg='#FFFFFF').place(relx=0.35, rely=0.75)
            tk.Label(self.frame, text="password", bg="#282c34", fg='#FFFFFF').place(relx=0.57, rely=0.75)
            tk.Label(self.frame, text="description", bg="#282c34", fg='#FFFFFF').place(relx=0.81, rely=0.75)

            tk.Button(self.frame, text="Refresh", command=self._feel_table).place(relx=0.46, rely=0.58)

            tk.Button(self.frame, text="Add", command=self._add_password).place(relx=0.38, rely=0.84)
            tk.Button(self.frame, text="Update", command=self._update_password).place(relx=0.46, rely=0.84)
            tk.Button(self.frame, text="Del", command=self._delete_password).place(relx=0.56, rely=0.84)

        else:
            tk.Label(self.frame, text="Username", bg="#282c34", fg='#FFFFFF').place(relx=0.05, rely=0.2)
            tk.Label(self.frame, text="Password", bg="#282c34", fg='#FFFFFF').place(relx=0.05, rely=0.4)

            self.loginInput = tk.Entry(self.frame, width=25)
            self.loginInput.place(relx=0.30, rely=0.2)
            self.passwordInput = tk.Entry(self.frame, width=25, show='*')
            self.passwordInput.place(relx=0.30, rely=0.4)

            tk.Button(self.frame, text="Log in", command=self._authentication).place(relx=0.35, rely=0.58)
            tk.Button(self.frame, text="Register", command=self._register).place(relx=0.56, rely=0.58)

    def _authentication(self) -> None:
        self._delete_last_widget()
        username = self.loginInput.get()
        password = self.passwordInput.get()

        authentication = Authentication(username, password)
        self._user_id, self._flag = authentication.authenticate_account()

        if self._flag:
            self._delete_last_widget(True)
            self.root.unbind('<Return>')
            self.root.geometry('600x400')
            self._create_widgets()

        else:
            self.info = tk.Label(self.frame, text='Wrong login or password!'.center(86), bg="#282c34", fg='#FFFFFF')
            self.info.place(relx=0, rely=0.75)

    def _register(self) -> None:
        self._delete_last_widget()
        username = self.loginInput.get()
        password = self.passwordInput.get()

        registration = Registration(username, password)
        info = registration.create_account()
        self.info = tk.Label(self.frame, text=info.center(86), bg="#282c34", fg='#FFFFFF')
        self.info.place(relx=0, rely=0.75)

    def _delete_last_widget(self, flag: bool = False) -> None:
        section = slice(None, None) if flag else slice(-1, None)
        for widget in self.frame.winfo_children()[section]:
            if flag or isinstance(widget, tk.Label):
                widget.destroy()

    def _create_table(self) -> None:
        self.style = ttk.Style()
        self.style = self.style.configure("Treeview",
                                          background="#282c34",
                                          foreground="#FFFFFF",
                                          fieldbackground='#282c34'
                                          )

        self.tree = ttk.Treeview(self.frame,
                                 columns=('Service', 'Login', 'Password', 'Description'),
                                 show='headings',
                                 style='Treeview'
                                 )

        self.tree.heading("Service", text="Service")
        self.tree.heading("Login", text="Login")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Description", text="Description")

        self.scrollbar = ttk.Scrollbar(self.frame, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.grid(row=0, column=0, sticky='nsew')
        self.scrollbar.grid(row=0, column=4, sticky='ns')

        for col, width in zip(("Service", "Login", "Password", "Description"), (120, 140, 175, 145)):
            self.tree.column(col, width=width, anchor="center")

    def _feel_table(self) -> None:
        self._clear_table()
        with PasswordManager() as cursor:
            empty_ceil = 10
            for service, login, password, description in cursor.get_passwords(self._user_id):
                self.tree.insert("", "end", values=(f"{service}", f"{login}", f"{password}", f"{description}"))
                empty_ceil -= 1

            while empty_ceil > 0:
                self.tree.insert("", "end", values=(f" ", f" ", f" ", f" "))
                empty_ceil -= 1

    def _clear_table(self) -> None:
        children = self.tree.get_children()
        for item in children:
            self.tree.delete(item)

    def _add_password(self) -> None:
        with PasswordManager() as cursor:
            service_name = self.serviceInput.get()
            login = self.loginInput.get()
            password = self.passwordInput.get()
            description = self.descriptionInput.get()
            cursor.add_password(self._user_id, service_name, login, password, description)

    def _update_password(self) -> None:
        with PasswordManager() as cursor:
            service_name = self.serviceInput.get()
            login = self.loginInput.get()
            password = self.passwordInput.get()
            cursor.update_password(self._user_id, service_name, login, password)

    def _delete_password(self) -> None:
        with PasswordManager() as cursor:
            service_name = self.serviceInput.get()
            login = self.loginInput.get()
            cursor.delete_password(self._user_id, service_name, login)
