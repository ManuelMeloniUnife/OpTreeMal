import tkinter as tk
import tkinter.ttk as ttk 

#creazione finestra interfaccia
screen = tk.Tk()
screen.geometry("500x500")
screen.title("OpTreeMal")

#implementazione vista gerarchica
treetime = ttk.Treeview(screen)

#creazione colonne
treetime['columns'] = ("Column 2", "Column 3", "Column 4","Column 5")
#formattazione colonne
treetime.column("#0", width=50, minwidth=25)
treetime.column("comlumn 2", width=50, minwidth=25)
treetime.column("comlumn 2", width=50, minwidth=25)
treetime.column("comlumn 2", width=50, minwidth=25)

#definizione titolo colonne


screen.mainloop()  # OR mainloop()

