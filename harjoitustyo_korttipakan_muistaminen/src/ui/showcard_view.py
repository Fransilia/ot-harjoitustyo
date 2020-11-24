from tkinter import *
from PIL import Image, ImageTk
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
        scriptDir = os.path.dirname(__file__)
        card_path = "./card_images/" + self.gamestate.deck[self.current_card].card_id() + ".jpg"
        impath = os.path.join(scriptDir, card_path)
        print(impath)
        currentcard = Image.open(impath)
        currentcard = currentcard.resize((250,400), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(currentcard)
        img = Label(master=self.frame, image=render)
        img.image = render
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

