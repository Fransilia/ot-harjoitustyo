from tkinter import Frame, constants, Button, messagebox

class Frontpage:

    def __init__(self, root, handle_show_login_view, handle_show_game_settings):
        self.root = root
        self.frame = None
        self.handle_show_login_view = handle_show_login_view
        self.handle_show_game_settings = handle_show_game_settings
        
        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        A = Button(master=self.frame, text="Kirjaudu", command = self.handle_show_login_view)
        B = Button(master=self.frame, text ="tietoja", command = self.info_view)
        C = Button(master=self.frame, text="Aloita", command = self.handle_show_game_settings)

        C.grid(padx=5, pady=5, sticky=constants.EW)
        A.grid(padx=5, pady=5, sticky=constants.EW)
        B.grid(padx=5, pady=5, sticky=constants.EW)
        
    def info_view(self):
        messagebox.showinfo("Tietoja", "Tämä on muistipeli sovellus.")

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
