from tkinter import *
m=Tk()
m.title("Registration form")

def hello():
    entry.delete(1,END)
    entry1.delete(1,END)
    enty1.delete(1,END)
    enty2.delete(1,END)
    enty3.delete(1,END)
    enty4.delete(1,END)
    enty5.delete(1,END)
    enty6.delete(1,END)
    enty7.delete(1,END)
    
    lab=Label(m,text="You have Successfully Registered",font=("Times New Roman",25,"bold"),bg="brown",fg="white")
    lab.grid(row=14,column=0,columnspan=3,sticky="snew")
m.geometry("615x560")
m.configure(bg="lightblue")

label=Label(m,text="Registration Form",font=("Times New Roman",30,"bold"),bg="green",fg="white")
label.grid(row=0, column=0, columnspan=2, padx="5", pady="5", sticky="nsew")

label1=Label(m,text="Fill out the form carefully for registration",font=("Inter",15),bg="lightblue",fg="blue")
label1.grid(row=1,column=0,sticky="w",padx="10",pady="10")

label2=Label(m,text="Student Name",font=("Inter",11),bg="lightblue",fg="black")
label2.grid(row=2,column=0,sticky="w",padx="10",pady="10")

entry=Entry(m,textvariable=(),font=("Inter",11))
entry.grid(row=3,column=0,padx="10",pady="3",sticky="nsew")
entry1=Entry(m,textvariable=(),font=("Inter",11))
entry1.grid(row=3,column=1,padx="10",pady="3",sticky="nsew")

labe1=Label(m,text="First Name",font=("Inter",8),bg="lightblue",fg="green")
labe1.grid(row=4,column=0,sticky="w",padx="10",pady="3")
labe2=Label(m,text="Last Name",font=("Inter",8),bg="lightblue",fg="green")
labe2.grid(row=4,column=1,sticky="nsew",padx="10",pady="3")

labe4=Label(m,text="Date of Birth",font=("Inter",11),bg="lightblue",fg="black")
labe4.grid(row=5,column=0,sticky="w",padx="10",pady="5")
labe5=Label(m,text="Gender",font=("Inter",11),bg="lightblue",fg="black")
labe5.grid(row=5,column=1,sticky="nsew",padx="10",pady="5")

enty1=Entry(m,textvariable=(),font=("Inter",10))
enty1.grid(row=6,column=0,padx="10",pady="5",sticky="nsew")
enty2=Entry(m,textvariable=(),font=("Inter",10))
enty2.grid(row=6,column=1,padx="10",pady="5",sticky="nsew")


labe6=Label(m,text="E-Mail Address",font=("Inter",11),bg="lightblue",fg="black")
labe6.grid(row=7,column=0,sticky="w",padx="10",pady="5")
labe7=Label(m,text="Mobile Number",font=("Inter",11),bg="lightblue",fg="black")
labe7.grid(row=7,column=1,sticky="nsew",padx="10",pady="5")

enty3=Entry(m,textvariable=(),font=("Inter",10))
enty3.grid(row=8,column=0,padx="10",pady="5",sticky="nsew")
enty4=Entry(m,textvariable=(),font=("Inter",10))
enty4.grid(row=8,column=1,padx="10",pady="5",sticky="nsew")


labe8=Label(m,text="Address",font=("Inter",11),bg="lightblue",fg="black")
labe8.grid(row=9,column=0,sticky="w",padx="10",pady="5")
enty5=Entry(m,textvariable=(),font=("Inter",10))
enty5.grid(row=10,column=0,padx="10",pady="5",sticky="nsew")


labe9=Label(m,text="College Name",font=("Inter",11),bg="lightblue",fg="black")
labe9.grid(row=11,column=0,sticky="w",padx="10",pady="5")
labe10=Label(m,text="State/Province",font=("Inter",11),bg="lightblue",fg="black")
labe10.grid(row=11,column=1,sticky="nsew",padx="10",pady="5")


enty6=Entry(m,textvariable=(),font=("Inter",10))
enty6.grid(row=12,column=0,padx="10",pady="5",sticky="nsew")
enty7=Entry(m,textvariable=(),font=("Inter",10))
enty7.grid(row=12,column=1,padx="10",pady="5",sticky="nsew")

button=Button(m,text=("Submit"),font=("Inter",15,"bold"),bg="green",fg="white",command=hello)
button.grid(row=13,padx="60",sticky="se")
m.mainloop()