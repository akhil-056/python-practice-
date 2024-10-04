from tkinter import*
import time
m=Tk()

def bye(hmt,gap,msg):   
    for x in range(hmt):
        time.sleep(gap)
        print(f"sending message:{msg}")
    lab_2.delete(0,END)
    ent1.delete(0,END)
    ent2.delete(0,END)

m.configure(bg="purple")
lab=Label(m,text="Msg Times:",font=("Times New Roman",24,"bold"),width=13,bg="purple",fg="black")
lab.grid(row=0,column=0,padx=5,pady=5,sticky="e")
lab_2=Entry(m,text="",font=("Times New Roman",24,"bold"),bg="white",fg="black")
lab_2.grid(row=0,column=1,padx=5,pady=5,sticky="w")
fun=Label(m,text="Msg Gaps:",font=("Times New Roman",24,"bold"),bg="purple",width=13,fg="black")
fun.grid(row=1,column=0,padx=5,pady=5,sticky="e")
ent1=Entry(m,text="",font=("Times New Roman",24,"bold"),bg="white",fg="black")
ent1.grid(row=1,column=1,padx=5,pady=5,sticky="w")
lab1=Label(m,text="Message:",font=("Times New Roman",24,"bold"),width=13,bg="purple",fg="black")
lab1.grid(row=2,column=0,padx=5,pady=5,sticky="e")
ent2=Entry(m,text="",font=("Times New Roman",24,"bold"),bg="white",fg="black")
ent2.grid(row=2,column=1,padx=5,pady=5,sticky="e")
ent3=Button(m,text="submit",font=("Times New Roman",24,"bold"),bg="purple",fg="black",command=lambda:bye(int(lab_2.get()),int(ent1.get()),str(ent2.get())))
ent3.grid(row=3,column=1,padx=5,pady=5,sticky="e")
m.mainloop()