import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkm

FGCOLOR = "#fff"
BGCOLOR = "#123"


def convert_from_decimal(event=None):
    try:
        entre = int(decimal_entry.get())
        binary_label.config(
            text="Binaire \n".upper() + bin(entre)[2:],
            justify="center",
            background=BGCOLOR,
            foreground=FGCOLOR,
        )
        octal_label.config(
            text="Octal \n".upper() + oct(entre)[2:],
            justify="center",
            background=BGCOLOR,
            foreground=FGCOLOR,
        )
        hex_label.config(
            text="Hexadecimal \n".upper() + hex(entre)[2:].upper(),
            justify="center",
            background=BGCOLOR,
            foreground=FGCOLOR,
        )

    except Exception:
        raise tkm.showerror("Attention ", "Veuillez donner un Entier")


window = tk.Tk()
window.title("Convertisseur de nombres")
window.geometry("420x360")
window.minsize(360, 280)
window["bg"] = BGCOLOR
# window.resizable(False, False)


lbl = tk.Label(
    window, text=" CONVERTISSEUR ", width=20, background=BGCOLOR, foreground=FGCOLOR
)
lbl.grid(row=0, columnspan=2)

dec_label = tk.Label(
    window, text="Entrez un entier  ", background=BGCOLOR, foreground=FGCOLOR
)
dec_label.grid(row=1, column=0)

decimal_entry = tk.Entry(window)
decimal_entry.grid(row=1, column=1)

convert_button = tk.Button(
    window,
    border=1,
    text="Convertir",
    background=BGCOLOR,
    foreground=FGCOLOR,
    command=convert_from_decimal,
)
convert_button.grid(row=2, column=0)


binary_label = tk.Label(
    window, text="Binaire".upper(), background=BGCOLOR, foreground=FGCOLOR
)
binary_label.grid(row=4, column=0)

hex_label = tk.Label(
    window, text="Hexadécimal".upper(), background=BGCOLOR, foreground=FGCOLOR
)
hex_label.grid(row=4, column=1)

octal_label = tk.Label(
    window, text="Octal".upper(), background=BGCOLOR, foreground=FGCOLOR
)
octal_label.grid(row=4, column=2)

window.bind("<Return>", convert_from_decimal)
window.mainloop()
