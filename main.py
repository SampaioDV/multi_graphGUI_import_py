import tkinter as tk
import app

root = tk.Tk()

gui_app = app.App(master=root)

root.mainloop()

project = gui_app.project
