import sys
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from tkinter.constants import *
from tkinter import font
import os.path
from PIL import Image, ImageTk
from functools import partial
_location = os.path.dirname(__file__)
import interface_support
_bgcolor = 'skyblue1'
_fgcolor = 'black'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
        top is the toplevel containing window.'''
        top.geometry("350x250+660+210")
        #top.minsize(120, 1)
        #top.maxsize(3844, 1061)
        #top.resizable(1,  1)
        top.title("Detail's Wakfu")
        #top.configure(background="#d9d9d9")
        #top.configure(highlightbackground="#d9d9d9")
        #top.configure(highlightcolor="#000000")
        self.top = top
        self.Listbox1 = tk.Listbox(self.top)
        self.Listbox1.place(relx=0.0, rely=0.0, relheight=0.76
                , relwidth=1.008)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(exportselection="0")
        grande_police = font.Font(family="Segoe UI", size=18, weight="bold")
        self.Listbox1.configure(font=grande_police)
        self.Listbox1.configure(foreground="black")
        self.Listbox1.configure(highlightbackground="skyblue1")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#d9d9d9")
        self.Listbox1.configure(selectforeground="black")
        self.optionmenu_var = ctk.StringVar(value="Damage")
        self.OptionMenu1 = ctk.CTkOptionMenu(self.top, values=["Damage", "Heal", "Shield"], command=interface_support.switchButton, height=26, width=106, variable=self.optionmenu_var)
        self.OptionMenu1.place(relx=0.017, rely=0.778)
        self.optionmenu_var2 = ctk.StringVar(value="Options")
        self.Parametres = ctk.CTkOptionMenu(self.top, values=["Reset", "Export Data", "Import Data"], command=interface_support.open_settings, height=26, width=106, variable=self.optionmenu_var2)
        self.Parametres.place(relx=0.796, rely=0.911)
        # self.Menubutton2 = tk.Menubutton(self.top)
        # self.Menubutton2.place(relx=0.796, rely=0.911, relheight=0.056
        #          , relwidth=0.176)
        # self.men54_m = tk.Menu(self.Menubutton2,tearoff=0,background=_bgcolor)
        # self.Menubutton2.configure(activebackground="#d9d9d9")
        # self.Menubutton2.configure(activeforeground="black")
        # self.Menubutton2.configure(anchor='w')
        # self.Menubutton2.configure(background="#d9d9d9")
        # self.Menubutton2.configure(disabledforeground="#a3a3a3")
        # self.Menubutton2.configure(foreground="#000000")
        # self.Menubutton2.configure(highlightbackground="#d9d9d9")
        # self.Menubutton2.configure(highlightcolor="#000000")
        # self.Menubutton2.configure(indicatoron="1")     
        # self.Menubutton2.configure(menu=self.men54_m)
        # self.Menubutton2.configure(padx="5")
        # self.Menubutton2.configure(pady="4")
        # self.Menubutton2.configure(relief="raised")
        # self.Menubutton2.configure(compound='left')
        # self.Menubutton2.configure(text='''Options''')
        # self.men54_m.add_command(compound='left'
        #         ,font="-family {Segoe UI} -size 9", label='Reset', command=interface_support.resetButton)
        # self.men54_m.add_command(compound='left'
        #         ,font="-family {Segoe UI} -size 9", label='Export Data', command=interface_support.extractdata)
        # self.men54_m.add_command(compound='left'
        #         ,font="-family {Segoe UI} -size 9", label='Import Data', command=interface_support.importdata)

def start_up():
    interface_support.main()
if __name__ == '__main__':
    interface_support.main()