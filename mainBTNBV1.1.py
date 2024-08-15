from tkinter import *
import tkinter.messagebox as tkm
import re


##-----Variables et constantes-----##
BGCOLOR1 = "#000"
FGCOLOR1 = "#fff"
SIZE1 = 13
SIZE2 = 20
SIZE3 = 14
BTNSIZE = 18
BTNHT1 = 80
BTNHT2 = 240
BTNWT1 = 85
BTNWT2 = 75

def is_binary(chaine):
    return bool(re.match("^[01]+$", chaine))
def is_decimal(chaine):
    return bool(re.match("^[0123456789]+$", chaine))
def is_hexa(chaine):
    return bool(re.match("^[0123456789abcdefABCDEF]+$", chaine))
def is_octal(chaine):
    return bool(re.match("^[01234567]+$", chaine))


def clear_():
    bin_entry.delete(0, END)
    lbl_binary.config(text="Bin ")
    lbl_decimal.config(text="Dec ")
    lbl_hexadec.config(text="Hex ")
    lbl_octal.config(text="Oct ")

def insert_(text):
    bin_entry.insert(END, text)


def from_binary(event=None):
    try:

        # bin2other = int(bin_entry.get(),2)
        bin2other = bin_entry.get()
        bin2other = eval(bin2other)
        lbl_binary.config(text="Bin "+ str(bin2other))
        result = int(bin2other, 2)
        lbl_decimal.config(text="Dec "+ result)
        lbl_hexadec.config(text="Hex"+ hex(result)[2:].upper())
        lbl_octal.config(text="Oct "+ oct(result)[2:])
    except Exception:
        bin_entry.delete(0, END)
        raise tkm.showerror("Attention ", "Veuillez Entrer soit 1 ou 0")



root = Tk()
root.title("Calculatrice")
root.geometry("500x460")
root.resizable(False, False)

bin_frame = Frame(root)
bin_frame.configure(bg="#000")
bin_frame.place(x=0,y=0,width=500,height=220)

btn_frame = Frame(root)
btn_frame.place(x=0,y=220,width=500,height=240)
btn_frame.configure(bg="#123")

title_label = Label(bin_frame, text="Programmeur ",fg=FGCOLOR1, bg=BGCOLOR1, font=("Arial",SIZE3,"bold"))
title_label.pack()

bin_entry = Entry(bin_frame, font=('Arial',SIZE1), bg=BGCOLOR1, fg=FGCOLOR1,width=20)
# dec_entry.place(x=120, y=50,width=200, height=30)
bin_entry.pack(pady=15)

lbl_decimal = Label(bin_frame,text="Dec ",fg=FGCOLOR1, bg=BGCOLOR1, font=('Arial',SIZE1))
lbl_decimal.place(x=0,y=120)
lbl_binary = Label(bin_frame,text="Bin ",fg=FGCOLOR1, bg=BGCOLOR1, font=('Arial',SIZE1))
lbl_binary.place(x=0,y=90)
lbl_hexadec = Label(bin_frame,text="Hex ",fg=FGCOLOR1, bg=BGCOLOR1, font=('Arial',SIZE1))
lbl_hexadec.place(x=0,y=150)
lbl_octal = Label(bin_frame,text="Oct ",fg=FGCOLOR1, bg=BGCOLOR1, font=('Arial',SIZE1))
lbl_octal.place(x=0,y=180)


btn1 = Button(btn_frame, text="1",font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("1"))
btn1.place(x=0, y=0, width=BTNWT1, height=BTNHT1)
btn2 = Button(btn_frame,state='disabled', text="2",font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("2"))
btn2.place(x=85, y=0, width=BTNWT1, height=BTNHT1)
btn3 = Button(btn_frame,state='disabled', text="3",font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("3"))
btn3.place(x=170, y=0, width=BTNWT1, height=BTNHT1)
btn4 = Button(btn_frame,state='disabled', text="4", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("4"))
btn4.place(x=0, y=80, width=BTNWT1, height=BTNHT1)
btn5 = Button(btn_frame,state='disabled', text="5", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("5"))
btn5.place(x=85, y=80, width=BTNWT1, height=BTNHT1)
btn6 = Button(btn_frame,state='disabled', text="6", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1, command=lambda:insert_("6"))
btn6.place(x=170, y=80, width=BTNWT1, height=BTNHT1)
btn7 = Button(btn_frame,state='disabled', text="7", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("7"))
btn7.place(x=0, y=160, width=BTNWT1, height=BTNHT1)
btn8 = Button(btn_frame,state='disabled', text="8", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("8"))
btn8.place(x=85, y=160, width=BTNWT1, height=BTNHT1)
btn9 = Button(btn_frame,state='disabled', text="9", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("9"))
btn9.place(x=170, y=160, width=BTNWT1, height=BTNHT1)

btn0 = Button(btn_frame, text="0", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("0"))
btn0.place(x=255,y=0, width=85, height=240)

btnadd = Button(btn_frame, text="+", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("+"))
btnadd.place(x=340,y=0, width=BTNWT1, height=BTNHT1)

btnmin = Button(btn_frame, text="-", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("-"))
btnmin.place(x=340,y=80, width=BTNWT1, height=BTNHT1)

btntime = Button(btn_frame, text="*", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("*"))
btntime.place(x=340,y=160,  width=BTNWT1, height=BTNHT1)

btndiv = Button(btn_frame, text="/", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=lambda:insert_("/"))
btndiv.place(x=425, y=0, width=75, height=BTNHT1)

btnclear = Button(btn_frame, text="CE", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=clear_)
btnclear.place(x=425, y=80, width=75, height=BTNHT1)

btne = Button(btn_frame, text="=", font=('Arial',BTNSIZE),fg=FGCOLOR1, bg=BGCOLOR1,command=from_binary)
btne.place(x=425, y=160, width=BTNWT1, height=BTNHT1)


root.bind("<Return>",from_binary)
root.mainloop()