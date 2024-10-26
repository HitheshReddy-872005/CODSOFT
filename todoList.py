'''creation of a  GUI todo list
    Author: S Hithesh Reddy'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
todoList_root=tk.Tk()
todoList_root.title("ToDo List")
todoList_root.geometry("600x600")
todoList_root.resizable(False,False)
entry_text=tk.StringVar()
tasks_list=[]
def file_function():
    try:
        global tasks_list
        with open("actions.txt","r") as action_file_1:
            tasks=action_file_1.readlines()
            for actions in tasks:
                if(actions!="\n"):
                    tasks_list.append(actions)
                    list_box.insert(END,actions)
    except:
            file=open("actions.txt","w")
            file.close()
def add_data():
    task=entry_text.get()
    task=">>"+task
    if(task==">>"):
        messagebox.showerror("Error",message="please enter your task.")
    else:
        with open("actions.txt","a") as action_file:
            action_file.write(f"{task}\n")
        tasks_list.append(task)
        list_box.insert(END,task)
        entry_text.set("")
def delete_data():
    global tasks_list
    deleteTask=str(list_box.get(ANCHOR))
    if deleteTask in tasks_list:
        tasks_list.remove(deleteTask)
        with open("actions.txt","w") as actions:
            for task in tasks_list:
                actions.write("\n"+task)
        list_box.delete(ANCHOR)
#icon
icon_image=PhotoImage(file="D:\Internship\image.png")
todoList_root.iconphoto(False,icon_image)
#heading
heading=ttk.Label(todoList_root,text="Todo List",font=("Times new roman",30),anchor="center")
heading.pack()
#paragraph
paragraph=ttk.Label(todoList_root,text="Add your tasks",font=("Times new roman",15),anchor="center")
paragraph.pack(pady=10)
#entry box
entry_frame=Frame(todoList_root,width=370,height=40).place(x=70,y=90)
entry_box=tk.Entry(entry_frame,textvariable=entry_text,width=60,bd=0,font=("Times new roman",15)).place(x=70,y=100,width="300",height=35)
#add button
add_button=Button(entry_frame,text="Add task",width=11,height=1,bg="green",font=("Times new roman",14),padx=11,bd=0,activebackground="lightgreen",cursor="hand2",command=add_data).place(x=370,y=100)
#list_frame
list_frame=Frame(todoList_root,bg="white",height=320,width=500).place(x=40,y=160)
list_box=Listbox(list_frame,font=("times new roman",15),width=62,height=14,bg="lightgreen",cursor="hand2")
list_box.place(x=40,y=160)
scroll_bar=Scrollbar(list_frame)
scroll_bar.pack(side=RIGHT,fill=BOTH)
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)
#delete Button
delete_icon=PhotoImage(file="D:\Internship\image copy.png",height=50)
delete_button=Button(todoList_root,image=delete_icon,width=53,height=53,bd=0,pady=13,command=delete_data,cursor="hand2").place(x=260,y=500)
file_function()
todoList_root.mainloop()