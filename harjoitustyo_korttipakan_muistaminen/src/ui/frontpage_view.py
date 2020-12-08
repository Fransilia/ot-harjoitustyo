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
        login_button = Button(master=self.frame, text="Kirjaudu", command = self.handle_show_login_view)
        info_button = Button(master=self.frame, text ="Tietoja", command = self.info_view)
        start_button = Button(master=self.frame, text="Aloita", command = self.handle_show_game_settings)

        start_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        info_button.grid(padx=5, pady=5, sticky=constants.EW)
        
    def info_view(self):
        lines = ["Tämä on muistipeli sovellus.", "Pelin tavoite on muistaa korttipakan kortit järjestyksessä.", "Paina aloita ja valitse korttien määrä aloittaaksesi."]
        messagebox.showinfo("Tietoja", "\n".join(lines) )

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
