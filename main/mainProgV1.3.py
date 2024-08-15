
from typing import Optional, Tuple, Union
from customtkinter import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkm

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Convertisseur")
        self.geometry("485x460")
        self.resizable(False, False)


        self.menu_z = CTkFrame(self, fg_color="#123",width=485, height=100)
        self.menu_z.place(x=0,y=0)
        self.titre = CTkLabel(self.menu_z,font=("Arial",30), text="Convertisseur")
        self.titre.place(x=155, y=5)
        self.main_frame = CTkFrame(self, width=485, fg_color="#000", height=360)
        self.main_frame.place(x=0, y=100)
        self.btn_frame = CTkFrame(self.main_frame, width=485, height=220)
        self.btn_frame.place(x=0, y=150)
        self.bin_frame = CTkFrame(self.main_frame)
        self.dec_frame = CTkFrame(self.main_frame)
        self.hex_frame = CTkFrame(self.main_frame)
        self.oct_frame = CTkFrame(self.main_frame)

        self.checked = IntVar(value=2)
        self.menu_bin = CTkRadioButton(self.menu_z,variable=self.checked, value=1, text="Bin ",command=self.choose_menu)
        self.menu_bin.place(x=100,y=60)
        self.menu_dec = CTkRadioButton(self.menu_z,variable=self.checked, value=2, text="Dec ",command=self.choose_menu)
        self.menu_dec.place(x=170,y=60)
        self.menu_hex = CTkRadioButton(self.menu_z,variable=self.checked, value=3, text="Hex ",command=self.choose_menu)
        self.menu_hex.place(x=250,y=60)
        self.menu_oct = CTkRadioButton(self.menu_z,variable=self.checked, value=4, text="Oct ",command=self.choose_menu)
        self.menu_oct.place(x=330,y=60)
        
        self.btn1 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="1",font=("",18),height=70,width=80)# command=lambda:insert_("1"))
        self.btn1.place(x=0, y=0)
        self.btn2 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="2",font=("",18),height=70,width=80)# command=lambda:insert_("2"))
        self.btn2.place(x=80, y=0)
        self.btn3 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="3",font=("",18),height=70,width=80)# command=lambda:insert_("3"))
        self.btn3.place(x=160, y=0)
        self.btn4 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="4",font=("",18),height=70,width=80 )# command=lambda:insert_("4"))
        self.btn4.place(x=240, y=0)
        self.btn5 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="5",font=("",18),height=70,width=80)# command=lambda:insert_("5"))
        self.btn5.place(x=320, y=0)
        self.btn6 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="6",font=("",18),height=70,width=80)# command=lambda:insert_("6"))
        self.btn6.place(x=0, y=70)
        self.btn7 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="7",font=("",18),height=70,width=80)# command=lambda:insert_("7"))
        self.btn7.place(x=80, y=70)
        self.btn8 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="8",font=("",18),height=70,width=80)# command=lambda:insert_("8"))
        self.btn8.place(x=160, y=70)
        self.btn9 = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="9",font=("",18),height=70,width=80)# command=lambda:insert_("9"))
        self.btn9.place(x=240, y=70)
        self.btna = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="A",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btna.place(x=320,y=70)

        self.btnb = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="B",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btnb.place(x=0,y=140)
        self.btnc = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="C",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btnc.place(x=80,y=140)
        self.btnd = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="D",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btnd.place(x=160,y=140)
        self.btne = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="E",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btne.place(x=240,y=140)
        self.btnf = CTkButton(self.btn_frame,corner_radius=3,border_width=2, text="F",font=("",18),height=70,width=80) #command=lambda:insert_("0"))
        self.btnf.place(x=320,y=140)

        self.btn0 = CTkButton(self.btn_frame, text="0",corner_radius=3,border_width=2,font=("",18), height=210,width=85) #command=lambda:insert_("0"))
        self.btn0.place(x=400,y=0)



        self.mainloop()

    def choose_menu(self):
        chx = self.checked.get()
        if chx==1:
            self.get_bin_frame()
        elif chx==2:
            self.get_dec_frame()
        elif chx==3:
            self.get_hex_frame()
        elif chx==4:
            self.get_oct_frame()

    def get_bin_frame(self):
        self.dec_frame.place_forget()
        self.hex_frame.place_forget()
        self.oct_frame.place_forget()

        self.bin_frame = CTkFrame(self.main_frame,  fg_color='#f9f9f9')
        self.bin_frame.configure(width=485, height=100)
        self.bin_frame.place(x=0,y=0)
        self.btn2.configure(state="disabled")
        self.btn3.configure(state="disabled")
        self.btn4.configure(state="disabled")
        self.btn5.configure(state="disabled")
        self.btn6.configure(state="disabled")
        self.btn7.configure(state="disabled")
        self.btn8.configure(state="disabled")
        self.btn9.configure(state="disabled")
        self.btna.configure(state="disabled")
        self.btnb.configure(state="disabled")
        self.btnc.configure(state="disabled")
        self.btnd.configure(state="disabled")
        self.btne.configure(state="disabled")
        self.btnf.configure(state="disabled")

    def get_dec_frame(self):
        
        self.bin_frame.place_forget()
        self.hex_frame.place_forget()
        self.oct_frame.place_forget()

        self.dec_frame = CTkFrame(self.main_frame, fg_color='#fff')
        self.bin_frame.configure(width=485, height=100)
        self.dec_frame.place(x=0,y=0)
        self.btna.configure(state="disabled")
        self.btnb.configure(state="disabled")
        self.btnc.configure(state="disabled")
        self.btnd.configure(state="disabled")
        self.btne.configure(state="disabled")
        self.btnf.configure(state="disabled")


    def get_hex_frame(self):
        self.bin_frame.place_forget()
        self.oct_frame.place_forget()
        self.dec_frame.place_forget()

        self.hex_frame = CTkFrame(self.main_frame,  fg_color='#ed124f')
        self.bin_frame.configure(width=485, height=150)
        self.hex_frame.place(x=0,y=0)

    def get_oct_frame(self):
        self.hex_frame.place_forget()
        self.dec_frame.place_forget()
        self.bin_frame.place_forget()

        self.oct_frame = CTkFrame(self.main_frame,  fg_color='#ed00f1')
        self.bin_frame.configure(width=485, height=150)
        self.oct_frame.place(x=0,y=0)
        self.btn8.configure(state="disabled")
        self.btn9.configure(state="disabled")
        self.btna.configure(state="disabled")
        self.btnb.configure(state="disabled")
        self.btnc.configure(state="disabled")
        self.btnd.configure(state="disabled")
        self.btne.configure(state="disabled")
        self.btnf.configure(state="disabled")


app = App()