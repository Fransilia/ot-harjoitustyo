from tkinter import Frame, Label, constants

class GameResults:
    def __init__(self,root,gamestate):
        self.root = root
        self.gamestate = gamestate

        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)
        reslut_text = Label(master=self.frame, text="Tulokset")
        reslut_text.grid(row=0, column=0)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
