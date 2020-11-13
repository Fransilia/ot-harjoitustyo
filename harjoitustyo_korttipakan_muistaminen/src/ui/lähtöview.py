from tkinter import Frame

class GameSettings:
    def __init__(self,root):
        self.root = root

        self.initialize()

    def initialize(self):
        self.frame = Frame(master=self.root)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()
