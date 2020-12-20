from tkinter import Radiobutton, StringVar, IntVar, Frame, Button, constants, Label
from entities.card import Suit, Card

class GameAnswers:
    def __init__(self,root, gamestate, handle_show_result_view, handle_show_frontpage_view):
        self.root = root
        self.gamestate = gamestate
        self.suit_var = StringVar()
        self.num_var = IntVar()
        self.handle_show_result_view = handle_show_result_view
        self.handle_show_frontpage_view = handle_show_frontpage_view

        self.initialize()

    def sel_suit(self):
        print("You selected: " + str(self.suit_var.get()))

    def sel_num(self):
        print("You selected: " + str(self.num_var.get()))

    def next(self):
        """ takes the players guess and adds it to list.
        Takes next guess of goes to resultpage if all guesses are made. """
        suit = Suit(self.suit_var.get())
        card = Card( self.num_var.get(),suit)
        print("going to next page with card: ", card.card_id())
        self.gamestate.add_answer(card)
        if self.gamestate.all_answers_done():
            self.handle_show_result_view(self.gamestate)
            return
        self.destroy()
        self.initialize()
        self.pack()

    def initialize(self):
        """radiobuttons for asking the player which suit the card is"""
        self.frame = Frame(master=self.root)
        radio_button_heart = Radiobutton(master=self.frame, text="Hertta", variable = self.suit_var, value= Suit.HEART.value, command=self.sel_suit)
        radio_button_heart.grid(row=0, column=1)
        radio_button_diamond = Radiobutton(master=self.frame, text="Ruutu", variable = self.suit_var, value= Suit.DIAMOND.value, command=self.sel_suit)
        radio_button_diamond.grid(row=0, column=2)
        radio_button_spade = Radiobutton(master=self.frame, text="Pata", variable = self.suit_var, value= Suit.SPADE.value, command=self.sel_suit)
        radio_button_spade.grid(row=0, column=3)
        radio_button_club = Radiobutton(master=self.frame, text="Risti", variable = self.suit_var, value= Suit.CLUB.value, command=self.sel_suit)
        radio_button_club.grid(row=0, column=4)

        """radiobuttons for asking player which number the card is"""
        for i in range(1,14):
            radio_button = Radiobutton(master=self.frame,text=str(i),variable = self.num_var, value=i, command=self.sel_num)
            radio_button.grid(row=1, column=i)

        select_button = Button(master=self.frame, text="Lukitse valinta", command=self.next)
        select_button.grid(padx=5, pady=5, sticky=constants.EW)
        warning_text = Label(master=self.frame, text="Paina mikäli haluat luovuttaa:")
        warning_text.config(font=("Courier", 10))
        warning_text.grid(row=6, column=0)
        give_up_button = Button(master=self.frame, text="Lopeta peli", command=self.handle_show_frontpage_view)
        give_up_button.grid(padx=5, pady=5, sticky=constants.EW)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
