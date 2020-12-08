from tkinter import Frame, constants, Button, messagebox, Entry, Label
from states.gamestate import GameState

class GameSettings:
    def __init__(self,root, handle_show_game_first_view):
        self.root = root
        self.card_number_entry = None
        self.handle_show_game_first_view = handle_show_game_first_view

        self.initialize()
    
    def amount_handler(self):
        """checking that the input is int if not errormessage shown"""
        amount = self.card_number_entry.get()
        try:
            val = int(amount)
            gamestate = GameState(val)
            self.handle_show_game_first_view(gamestate)
            gamestate.print_status()
        except ValueError:
            messagebox.showinfo("VIRHE", "Ole ystävällinen ja syötä kokonaisluku. Kiitos!")

    def initialize(self):
        """asking for amount of cards to be shown and giving the 
        input to amount_handler"""
        self.frame = Frame(master=self.root)
        L1 = Label(master=self.frame, text="Korttien määrä: ")
        L1.grid(row=0, column=0)
        self.card_number_entry = Entry(master = self.frame)
        self.card_number_entry.grid(row=0, column=1)
        start_button = Button(master=self.frame, text="Aloita peli", command=self.amount_handler)
        start_button.grid(padx=5, pady=5, sticky=constants.EW)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
