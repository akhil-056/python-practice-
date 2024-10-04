from tkinter import*
m=Tk()
def hello():
    name=my_labe.get()
    greeting="hello"+name
    greet="plese enter a valid name"
    if name!="":
        done.configure(text=greeting)
    elif name=="":
        done.configure(text=greet)
m.configure(bg="black")
m.geometry("313x313")

my_labe=Entry(m,text=" ",font=("Arial",24),fg="black",bg="lavender")
my_labe.pack(padx=5,pady=5)

done=Label(m,text="Enter name",font=("Arial",24),fg="black",bg="lavender")
done.pack(padx=5,pady=5)
fun=Button(m,text="submit",font=("Arial",24),fg="black",bg="lavender",command=hello)
fun.pack(padx=5,pady=5)
m.mainloop()