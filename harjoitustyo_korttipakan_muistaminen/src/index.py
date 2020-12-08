from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title('Muistipeli :)')

ui = UI(window)
ui.start()

window.geometry("800x750")

window.mainloop()
