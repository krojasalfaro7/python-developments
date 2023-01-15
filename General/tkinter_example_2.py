from tkinter import ttk
from tkinter import *

root = Tk()
columns = ("Items", "Values")
Treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  #

Treeview.column("Items", width=200, anchor='center')
Treeview.column("Values", width=200, anchor='center')

Treeview.heading("Items", text="Items")
Treeview.heading("Values", text="Values")

Treeview.pack(side=LEFT, fill=BOTH)

name = ['Item1', 'Item2', 'Item3']
ipcode = ['10', '25', '163']
for i in range(min(len(name), len(ipcode))):
    Treeview.insert('', i, values=(name[i], ipcode[i]))


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


def set_cell_value(event):
    for item in Treeview.selection():
        item_text = Treeview.item(item, "values")
        column = Treeview.identify_column(event.x)
        row = Treeview.identify_row(event.y)
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    entryedit = Text(root, width=10 + (cn - 1) * 16, height=1)
    entryedit.place(x=16 + (cn - 1) * 130, y=6 + rn * 20)

    def saveedit():
        Treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()

    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    okb.place(x=90 + (cn - 1) * 242, y=2 + rn * 20)


def newrow():
    name.append('to be named')
    ipcode.append('value')
    Treeview.insert('', len(name) - 1, values=(name[len(name) - 1], ipcode[len(name) - 1]))
    Treeview.update()
    newb.place(x=120, y=(len(name) - 1) * 20 + 45)
    newb.update()


Treeview.bind('<Double-1>', set_cell_value)
newb = ttk.Button(root, text='new item', width=20, command=newrow)
newb.place(x=120, y=(len(name) - 1) * 20 + 45)

for col in columns:
    Treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(Treeview, _col, False))


root.mainloop()