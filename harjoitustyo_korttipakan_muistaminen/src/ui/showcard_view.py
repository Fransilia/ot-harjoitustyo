from tkinter import Frame, Button, constants
from PIL import Image, ImageTk
from ui.card_image_view import create_card_image
import os

class ShowCard:
    def __init__(self,root, gamestate, handle_show_answerinput_view):
        self.root = root
        self.gamestate = gamestate
        self.current_card = 0
        self.handle_show_answerinput_view = handle_show_answerinput_view

        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        img = create_card_image(self.frame, self.gamestate.deck[self.current_card])
        img.grid(row=0, column=0)
        next_button = Button(master=self.frame, text="Seuraava", command=self.nextcard_button_pressed)
        next_button.grid(padx=5, pady=5, sticky=constants.EW)

    def nextcard_button_pressed(self):
        if self.current_card < len(self.gamestate.deck)-1:
            self.current_card += 1
            self.destroy()
            self.initialize()
            self.pack()
        else:
            self.destroy()
            self.handle_show_answerinput_view(self.gamestate)


    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

