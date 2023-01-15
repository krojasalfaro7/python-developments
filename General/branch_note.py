import tkinter as tk
from tkinter import ttk


def init_window():

    win = tk.Tk()
    win.title("Branch Note")
    win.geometry("600x350")

    tree = ttk.Treeview(height=20, columns=('#0', '#1', '#2'))
    tree.place(x=0, y=0)
    tree.column('#0', width=40)
    tree.heading('#0', text='ID', anchor=tk.CENTER)
    tree.heading('#1', text='Name', anchor=tk.CENTER)
    tree.column('#1', width=360)
    tree.heading('#2', text='On develop?', anchor=tk.CENTER)
    tree.column('#2', width=100)
    tree.heading('#3', text='On production?', anchor=tk.CENTER)
    tree.column('#3', width=100)
    return win

# name_branch = tk.StringVar()
# on_develop = tk.BooleanVar()
# on_production = tk.BooleanVar()
#
# name_branch.set("")
# on_develop.set(False)
# on_production.set(False)


if __name__ == '__main__':
    init_window().mainloop()
