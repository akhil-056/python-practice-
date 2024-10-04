from tkinter import*
from tkinter import ttk
m=Tk()
m.title("Simple tkinter application")
m.geometry("600x600")
m.config(bg="purple")
lab=Label(m,text="Name: ",font=("times new roman",15,"bold"),fg="white",bg="purple")
lab.grid(row=0,column=0, padx=3, pady=5)

ent=Entry(m)
ent.grid(row=0,column=1)

lab1=Label(m,text="Age:",font=("times new roman",15,"bold"),fg="white",bg="purple")
lab1.grid(row=1,column=0,padx=3, pady=5)

sc=Spinbox(m,fg="lightblue",bg="green",from_=0, to=100,width=30)
sc.grid(row=1,column=1,padx=3,pady=5)

lab2=Label(m,text="Favorite fruit",font=("times new roman",15,"bold"),fg="white",bg="purple")
lab2.grid(row=3,column=0,padx=3,pady=5)

comb=ttk.Combobox(m,values=["banana","pineapple","apple","jackfruit"])
comb.grid(row=3,column=1,padx=10)

lab3=Label(m,text="Add Hobby: ",font=("times new roman",15,"bold"),fg="white",bg="purple")
lab3.grid(row=4,column=0,padx=3,pady=5)

e3=Entry(m,bg="lightblue")
e3.grid(row=4,column=1,)
meow=Listbox(m)
meow.grid(row=5,column=1)
def endho():
    selec=meow.curselection()
    if selec:
        meow.delete(selec[0])
def inp():
    name=e3.get()
    meow.insert(0,name)

meow.insert(1,"Hunting")
meow.insert(2,"Fishing")
meow.insert(3,"Climbing")
meow.insert(4,"Leaping")
but=Button(m,text="Add HOBBY",bg="blue",fg="white",command=inp)
but.grid(row=4,column=3)
def show():
    n0.insert(1,"NAME:"+ent.get())
    n0.insert(2,"Age:"+sc.get())
    n0.insert(3,"Fvorite Food:"+comb.get())
but3=Button(m,text="display information",width=20,fg="black", bg="green",command=show)
but3.grid(row=6,column=1,pady=5)
n0=Listbox(m)
n0.grid(row=7,column=1)

m.mainloop()