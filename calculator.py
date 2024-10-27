'''creating a GUI based calculator.
Author: S Hithesh Reddy'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox
calculator_root=tk.Tk()
calculator_root.geometry("600x600")
calculator_root.resizable(False,False)
calculator_icon=PhotoImage(file="D:\Internship\image copy 2.png")
calculator_root.iconphoto(False,calculator_icon)
text=StringVar()
new_text=""
def action(number):
    global new_text
    new_text+=number
    text.set(new_text) 
def calculate():
    try:
        global new_text
        result=eval(text.get())
        new_text=str(result)
        text.set(result)
    except ZeroDivisionError:
        messagebox.showerror("Error","division by zero is invalid")
    except SyntaxError:
        messagebox.showerror("Error","please enter a valid syntax")
def clear():
    global new_text
    new_text=""
    text.set(new_text)
#main frame
calculator_frame=Frame(calculator_root,width=600,height=600,bd=0,bg="grey").place(x=0,y=0)
#display frame
calculator_display_frame=Frame(calculator_frame,bg="white",bd=0,width=562,height=245).place(x=15,y=15)
#entry_box
data_entry_box=Entry(calculator_display_frame,bd=0,font=("Times New Roman",35),width=21,bg="white",textvariable=text).place(x=21,y=205)
number_frame=Frame(calculator_root,background="white",height=297,width=399,bd=0).place(x=15,y=280)
operation_frame=Frame(calculator_root,background="white",height=297,width=147,bd=0).place(x=430,y=280)
#number buttons
button_8=Button(number_frame,text="8",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("8")).place(x=155,y=288)
button_7=Button(number_frame,text="7",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("7")).place(x=23,y=288)
button_9=Button(number_frame,text="9",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("9")).place(x=284,y=288)
button_4=Button(number_frame,text="4",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("4")).place(x=23,y=358)
button_5=Button(number_frame,text="5",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("5")).place(x=155,y=358)
button_6=Button(number_frame,text="6",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("6")).place(x=284,y=358)
button_1=Button(number_frame,text="1",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("1")).place(x=23,y=435)
button_2=Button(number_frame,text="2",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("2")).place(x=155,y=435)
button_3=Button(number_frame,text="3",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("3")).place(x=284,y=435)
button_c=Button(number_frame,text="c",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=clear).place(x=23,y=508)
button_0=Button(number_frame,text="0",height=1,width=7,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("0")).place(x=155,y=508)
button_equal=Button(number_frame,text="=",height=1,width=7,bg="orange",font=("times new rooman",20),activebackground="orange",cursor="hand2",command=calculate).place(x=284,y=508)
#operation buttons
button_div=Button(number_frame,text="/",height=1,width=8,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("/")).place(x=435,y=288)
button_mul=Button(number_frame,text="*",height=1,width=8,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("*")).place(x=435,y=358)
button_sub=Button(number_frame,text="-",height=1,width=8,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("-")).place(x=435,y=435)
button_add=Button(number_frame,text="+",height=1,width=8,bg="grey",font=("times new rooman",20),activebackground="grey",cursor="hand2",command=lambda:action("+")).place(x=435,y=508)
calculator_root.mainloop()
