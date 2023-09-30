from tkinter import *

def click (event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "Ans":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

            scvalue.set(value)
            screen.update()


    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

            scvalue.set(value)
            screen.update()



    elif text == "C":
        scvalue.set("")
        screen.update()
        pass

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()
root.geometry("600x600")
root.title("Simple Calculator By Isha Suman")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font ="Dubai 40 bold")
screen.pack(fill=X,ipadx=8 , pady=10,padx=10)

f = Frame(root , bg="black")
b = Button(f, text="C", padx=35 , pady=22 , font = "Dubai 20 bold")
b.pack(side=LEFT, padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="Ans", padx=30 , pady=22 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="%", padx=30 , pady=22 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="/", padx=36 , pady=22 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="black")
b = Button(f, text="7", padx=39 , pady=20 , font = "Dubai 20 bold")
b.pack(side=LEFT, padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="8", padx=39 , pady=20 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="9", padx=39 , pady=20 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="*", padx=36 , pady=22 , font = "Dubai 25 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="black")
b = Button(f, text="4", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT, padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="5", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="6", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="-", padx=38 , pady=19 , font = "Dubai 28 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="black")
b = Button(f, text="1", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT, padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="2", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="3", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="+", padx=38 , pady=19 , font = "Dubai 25 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg="black")
b = Button(f, text="00", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT, padx=20 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text="0", padx=38 , pady=19 , font = "Dubai 20 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>",click)


b = Button(f, text=".", padx=38 , pady=19 , font = "Dubai 25 bold")
b.pack(side=LEFT , padx=10 , pady=5)
b.bind("<Button-1>",click)

b = Button(f, text="=", padx=38 , pady=19 , font = "Dubai 25 bold")
b.pack(side=LEFT , padx=20 , pady=5)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()