from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title('Muistipeli :)')

ui = UI(window)
ui.start()

window.mainloop()
