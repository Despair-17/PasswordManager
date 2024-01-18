import tkinter as tk
from user_management import Authentication, Registration


class TkinterGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry('306x160')
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(self.root, bg="#282c34")
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame.winfo_children()

        self.loginInput = self.passwordInput = self.info = self._user_id = None
        self._flag = False
        self._create_widgets()
        self.root.bind('<Return>', lambda event: self._authentication())

    def _create_widgets(self) -> None:
        if not self._flag:
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
            self.root.geometry('600x400')
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


root = tk.Tk()
gui = TkinterGUI(root)
root.mainloop()
# self.canvas = tk.Canvas(self.root, width=200, height=200)
# self.canvas.pack()
