from tkinter import*
m=Tk()
mylabel=Label(m,text="Gates Institute Of Technology",font=("Times New Roman",24,"bold",),bg="purple",fg="grey",padx=40,pady=70)
mylabel.pack()
my_button=Entry(m,text="Login ID",font=("forte",15,"bold"),bg="white",fg="black",cursor="hand2")
ma_t=Button(m,text="passpword",font=("ravie",13,),bg="black",fg="white",padx=9,pady=5,cursor="hand2")
my_button.pack(pady=9,side=RIGHT)
ma_t.pack(side="left")
mat=Button(m,text="LOgin Id",font=("Times New Roman",20,"bold"),bg="red")
mat.pack(padx=2,side=LEFT)

m.mainloop()
