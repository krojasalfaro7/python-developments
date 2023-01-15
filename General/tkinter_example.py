import tkinter as tk
win = tk.Tk()
win.title("Hello World")

mylabel = tk.Label(win, text="Hello World", font=("ubuntu", 60, "bold"), fg="red")
mylabel.pack()
win.mainloop()
