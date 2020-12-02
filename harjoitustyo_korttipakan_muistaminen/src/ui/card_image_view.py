from tkinter import Label, Frame, Button, constants
from PIL import Image, ImageTk
import os

def create_card_image(frame, card, width=250, height=400):
    scriptDir = os.path.dirname(__file__)
    card_path = "./card_images/" + card.card_id() + ".jpg"
    impath = os.path.join(scriptDir, card_path)
    print(impath)
    currentcard = Image.open(impath)
    currentcard = currentcard.resize((width,height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(currentcard)
    img = Label(master=frame, image=render)
    img.image = render
    return img