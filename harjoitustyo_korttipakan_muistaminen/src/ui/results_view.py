from tkinter import Frame, Label, constants, Button
from ui.scrollable_frame import ScrollableFrame
from ui.card_image_view import create_card_image

class GameResults:
    def __init__(self,root,gamestate,handle_show_game_settings, handle_show_frontpage_view):
        self.root = root
        self.gamestate = gamestate
        self.handle_show_game_settings = handle_show_game_settings
        self.handle_show_frontpage_view = handle_show_frontpage_view

        self.initialize()

    def initialize(self):
        """first some text to the resultspage"""
        self.frame = Frame(master=self.root)
        reslut_text = Label(master=self.frame, text="Tulokset")
        reslut_text.config(font=("Courier", 44))
        reslut_text.grid(row=0, column=0)
        amount_correct_text = Label(master=self.frame, text="Oikeat arvaukset:")
        amount_correct_text.config(font=("Courier", 20))
        amount_correct_text.grid(row=1, column=0)

        """geting the amount of correct guesses from gamesta class and showing it"""
        correct_amount, comparison = self.gamestate.get_result()
        full_amount = self.gamestate.get_deck_size()
        result_amount_text = Label(master=self.frame, text=(str(correct_amount)+ "/" +str(full_amount)))
        result_amount_text.config(font=("Courier", 20))
        result_amount_text.grid(row=1, column=1)

        """More text on page"""
        theese_wrong_text = Label(master=self.frame, text="Tässä oikea rivi: ")
        theese_wrong_text.config(font=("Courier", 20))
        theese_wrong_text.grid(row=3, column=0)
        player_answers_text = Label(master=self.frame, text="Näin sinä vastasit: ")
        player_answers_text.config(font=("Courier", 20))
        player_answers_text.grid(row=5, column=0)

        sf_correct = ScrollableFrame(self.frame)
        sf_user = ScrollableFrame(self.frame)

        for i in range(len(comparison)):
            """Using scrollable frame to show the right answers
            and guesses (pictures of cards) made by player"""
            is_correct, correct_card, user_card = comparison[i]
            text = "vastasit:\noikein" if is_correct else "vastasit:\nväärin" 
            color = "green" if is_correct else "red"
            img = create_card_image(sf_correct.scrollable_frame, correct_card, 50,100)
            img.grid(row=0, column=i)
            label = Label(master=sf_correct.scrollable_frame, text= text, fg = color)
            label.grid(row=1,column=i)
            img = create_card_image(sf_user.scrollable_frame, user_card, 50,100)
            img.grid(row=0, column=i)
            label = Label(master=sf_user.scrollable_frame, text= text, fg = color)
            label.grid(row=1,column=i)
        sf_correct.grid(row=4, column=0)
        sf_user.grid(row=6, column=0)

        """Buttons for navigation"""
        new_game_button = Button(master=self.frame, text="Uusi peli", command = self.handle_show_game_settings)
        frontpage_button = Button(master=self.frame, text="Päävalikkoon", command = self.handle_show_frontpage_view)
        new_game_button.grid(padx=5, pady=5, sticky=constants.EW)
        frontpage_button.grid(padx=5, pady=5, sticky=constants.EW)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
