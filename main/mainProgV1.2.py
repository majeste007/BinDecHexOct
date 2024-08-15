import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm
import re


SIZE1 = 12
FGCOLOR = "#fff"
BGCOLOR = "#123"
BGCOLOR1 = "#091821"
BGCOLOR2 = "#2f4f4f"
BGCOLOR3 = "#D2691E"
FGCOLOR1 = "#fffafa"
FGCOLOR2 = "#696969"
FGCOLOR3 = "#fff"
def is_binary(chaine):
    return bool(re.match("^[01]+$", chaine))
def is_decimal(chaine):
    return bool(re.match("^[0123456789]+$", chaine))
def is_hexa(chaine):
    return bool(re.match("^[0123456789abcdefABCDEF]+$", chaine))
def is_octal(chaine):
    return bool(re.match("^[01234567]+$", chaine))






def radio_selected():
    selected = getChx.get()
    if selected==1:
        dec_frame.place_forget()
        hex_frame.place_forget()
        oct_frame.place_forget()
        bin_frame.place(x=0,y=140,width=500,height=370)
    elif selected==2:
        bin_frame.place_forget()
        oct_frame.place_forget()
        hex_frame.place_forget()
        dec_frame.place(x=0,y=140,width=500,height=370)
    elif selected==3:
        bin_frame.place_forget()
        dec_frame.place_forget()
        oct_frame.place_forget()
        hex_frame.place(x=0,y=140,width=500,height=370)
    elif selected==4:
        bin_frame.place_forget()
        dec_frame.place_forget()
        hex_frame.place_forget()
        oct_frame.place(x=0,y=140,width=500,height=370)

def from_binary(event=None):
    if is_binary(bin_entry.get()):
        dec2other = int(bin_entry.get(),2)
        lbl_decimal_r = tk.Label(bin_frame,text=dec2other, font=('Arial',SIZE1))
        lbl_decimal_r.place(x=105, y=50)
        lbl_hexadec_r = tk.Label(bin_frame,text=hex(dec2other)[2:].upper(), font=('Arial',SIZE1))
        lbl_hexadec_r.place(x=105, y=70)
        lbl_octal_r = tk.Label(bin_frame,text=oct(dec2other)[2:], font=('Arial',SIZE1))
        lbl_octal_r.place(x=105, y=90)
    else:
        bin_entry.delete(0, END)
        raise tkm.showerror("Attention ", "Veuillez Entrer soit 1 ou 0")

def from_decimal(event=None):
    if is_decimal(dec_entry.get()):
        entre = int(dec_entry.get())
        lbl_binary_r = tk.Label(dec_frame,text=bin(entre)[2:] ,font=('Arial',SIZE1))
        lbl_binary_r.place(x=105, y=50)
        lbl_hexadec_r = tk.Label(dec_frame,text=hex(entre)[2:].upper(), font=('Arial',SIZE1))
        lbl_hexadec_r.place(x=105, y=70)
        lbl_octal_r = tk.Label(dec_frame,text=oct(entre)[2:], font=('Arial',SIZE1))
        lbl_octal_r.place(x=105, y=90)

    else:
        dec_entry.delete(0, END)
        raise tkm.showerror("Attention ", "Veuillez donner un Entier")
def from_hexadec(event=None):
    if is_hexa(hex_entry.get()):
        hex2other = int(hex_entry.get(),16)
        lbl_binary_r = tk.Label(hex_frame,text=bin(hex2other)[2:] ,font=('Arial',SIZE1))
        lbl_binary_r.place(x=105, y=50)
        lbl_decimal_r = tk.Label(hex_frame,text=hex2other, font=('Arial',SIZE1))
        lbl_decimal_r.place(x=105, y=70)
        lbl_octal_r = tk.Label(hex_frame,text=oct(hex2other)[2:], font=('Arial',SIZE1))
        lbl_octal_r.place(x=105, y=90)
    else:
        hex_entry.delete(0, END)
        raise tkm.showerror("Attention ", "Entrée invalide")
    
def from_octal(event=None):
    if is_octal(oct_entry.get()):
        oct2other = int(oct_entry.get(),8)
        lbl_binary_r = tk.Label(oct_frame,text=bin(oct2other)[2:] ,font=('Arial',SIZE1))
        lbl_binary_r.place(x=105, y=50)
        lbl_decimal_r = tk.Label(oct_frame,text=oct2other, font=('Arial',SIZE1))
        lbl_decimal_r.place(x=105, y=70)
        lbl_hexadec_r = tk.Label(oct_frame,text=hex(oct2other)[2:].upper(), font=('Arial',SIZE1))
        lbl_hexadec_r.place(x=105, y=90)

    else:
        oct_entry.delete(0, END)
        raise tkm.showerror("Attention ", "Entrée invalide")
    



def darkMode():
    pass

def lightMode():
    pass




root = tk.Tk()
root.title("Convertisseur de nombres")
root.geometry("500x320")
root.resizable(False, False)

menu_bar = tk.Menu(root)
th_choice = IntVar(value=1)
display_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Affichage', menu=display_menu)
display_menu.add_radiobutton(label='Mode Sombre',indicatoron=True,variable=th_choice, value=2 ,command=darkMode)
display_menu.add_radiobutton(label='Mode clair',indicatoron=True,variable=th_choice, value=1 ,command=lightMode)


help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Aide', menu=help_menu)
root.config(menu=menu_bar)


title_label = tk.Label(root, text="Convertiseur de nombre ", font=("Arial",20,"bold"))
title_label.pack()



zone_1 = tk.LabelFrame(root)
zone_1.place(x=0,y=50,width=500, height=80)
lbl_choice = tk.Label(zone_1, text="Choisissez un systeme",font=("Sans Serif", 12))
lbl_choice.place(x=150, y=1)

getChx = IntVar(value=2)
lbl_bin = tk.Radiobutton(zone_1, text="Bin", variable=getChx,command=radio_selected,value=1,font=("Sans Serif", 12))
lbl_bin.place(x=75,y=30, width=70)
lbl_dec = tk.Radiobutton(zone_1, text="Dec", variable=getChx,command=radio_selected,value=2,font=("Sans Serif", 12))
lbl_dec.place(x=150,y=30,  width=70)
lbl_hexa = tk.Radiobutton(zone_1, text="Hex", variable=getChx,command=radio_selected,value=3,font=("Sans Serif", 12))
lbl_hexa.place(x=225,y=30,  width=70)
lbl_oct = tk.Radiobutton(zone_1, text="Oct", variable=getChx,command=radio_selected,value=4,font=("Sans Serif", 12))
lbl_oct.place(x=300,y=30,  width=70)


# base 2
bin_frame = tk.Frame(root)
bin_entry = tk.Entry(bin_frame, font=('Arial', '13'))
bin_entry.place(x=120, y=15,width=150, height=25)
val_btn = tk.Button(bin_frame, text="Convertir", font=('Arial',SIZE1), command=from_binary)
val_btn.place(x=280, y=15, height=25)
lbl_decimal = tk.Label(bin_frame,text="Decimal ", font=('Arial',SIZE1), fg='#123') 
lbl_decimal.place(x=0,y=50)
lbl_hexadec = tk.Label(bin_frame,text="Hexadecimal ", font=('Arial',SIZE1), fg='#123') 
lbl_hexadec.place(x=0,y=70)
lbl_octal = tk.Label(bin_frame,text="Octal", font=('Arial',SIZE1), fg='#123') 
lbl_octal.place(x=0,y=90)

#  base 8
oct_frame = tk.Frame(root)
oct_entry = tk.Entry(oct_frame, font=('Arial', '13'))
oct_entry.place(x=120, y=15,width=150, height=25)
val_btn = tk.Button(oct_frame, text="Convertir", font=('Arial',SIZE1), command=from_octal)
val_btn.place(x=280, y=15, height=25)
lbl_binary = tk.Label(oct_frame,text="Binaire ", font=('Arial',SIZE1), fg='#123') 
lbl_binary.place(x=0,y=50)
lbl_decimal = tk.Label(oct_frame,text="Decimal ", font=('Arial',SIZE1), fg='#123') 
lbl_decimal.place(x=0,y=70)
lbl_hexadec = tk.Label(oct_frame,text="Hexadecimal", font=('Arial',SIZE1), fg='#123') 
lbl_hexadec.place(x=0,y=90)

# base 16
hex_frame = tk.Frame(root)
hex_entry = tk.Entry(hex_frame, font=('Arial', '13'))
hex_entry.place(x=120, y=15,width=150, height=25)
val_btn = tk.Button(hex_frame, text="Convertir",font=('Arial',SIZE1), command=from_hexadec)
val_btn.place(x=280, y=15, height=25)
lbl_binary = tk.Label(hex_frame,text="Binaire ",font=('Arial',SIZE1), fg='#123') 
lbl_binary.place(x=0,y=50)
lbl_decimal = tk.Label(hex_frame,text="Decimal ", font=('Arial',SIZE1), fg='#123') 
lbl_decimal.place(x=0,y=70)
lbl_octal = tk.Label(hex_frame,text="Octal ", font=('Arial',SIZE1), fg='#123') 
lbl_octal.place(x=0,y=90)


#  base 10
dec_frame = tk.Frame(root)
dec_frame.place(x=0,y=140,width=500,height=370)
dec_entry = tk.Entry(dec_frame, font=('Arial', '13'))
dec_entry.place(x=120, y=15,width=150, height=25)
val_btn = tk.Button(dec_frame, text="Convertir", font=('Arial',SIZE1), command=from_decimal)
val_btn.place(x=280, y=15, height=25)
lbl_binary = tk.Label(dec_frame,text="Binaire ", font=('Arial',SIZE1), fg='#123')
lbl_binary.place(x=0,y=50)
lbl_hexadec = tk.Label(dec_frame,text="Hexadecimal ", font=('Arial',SIZE1), fg='#123')
lbl_hexadec.place(x=0,y=70)
lbl_octal = tk.Label(dec_frame,text="Octal", font=('Arial',SIZE1), fg='#123')
lbl_octal.place(x=0,y=90)







root.mainloop()