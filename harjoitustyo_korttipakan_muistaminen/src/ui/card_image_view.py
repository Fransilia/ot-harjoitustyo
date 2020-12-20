import os
from tkinter import Label
from PIL import Image, ImageTk

def create_card_image(frame, card, width=250, height=400):
    """Makes the image for a card """
    script_dir = os.path.dirname(__file__)
    card_path = "./card_images/" + card.card_id() + ".jpg"
    impath = os.path.join(script_dir, card_path)
    print(impath)
    currentcard = Image.open(impath)
    currentcard = currentcard.resize((width,height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(currentcard)
    img = Label(master=frame, image=render)
    img.image = render
    return img
