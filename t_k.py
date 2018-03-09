from Tkinter import *
from PIL import Image, ImageTk
def callback():
	print "click!"
	#print ent.get()
	#print tex.get("2.0",END)
	tex.delete("1.0",END)
	tex.insert("1.0",ent.get())

def hide_show():
    if b1.winfo_viewable():
        b1.grid_remove()
    else:
        b1.grid()


root = Tk()
root.resizable(width=False, height=False)#second step
root.geometry("%dx%d" % (500, 500))#third step
b = Button(root, text="b",width=20,height=5, command=hide_show)#fourth step
#b.pack()#fith step
b.grid(row = 2, column = 2)#6

b1 = Button(root, text="b1", command=callback)
b1.grid(row = 0, column = 0)
#b.place(x=0,y=0)
ent = Entry(root,width=20,bd=3)
ent.grid(row = 1, column = 1)

tex = Text(root,width=40,
          font="Verdana 12",
          wrap=WORD) 
tex.grid(row = 3, column = 1)

label = Label(root, text = "Hello", command = hide_show)
label.pack()


root.mainloop()