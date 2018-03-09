#first call
from Tkinter import *

def printer(event):
     print ("'Hello World!'")

root = Tk()
but = Button(root)
but["text"] = "Print"
but.bind("<Button-1>",printer)
but.pack()
root.mainloop()

#OOP way
from tkinter import *
 
class But_print:
     def __init__(self):
          self.but = Button(root)
          self.but["text"] = "Печать"
          self.but.bind("<Button-1>",self.printer)
          self.but.pack()
     def printer(self,event):
          print ("Как всегда очередной 'Hello World!'")
 
root = Tk()
obj = But_print()
root.mainloop()

#more deep way
from tkinter import *
 
root = Tk()
 
but = Button(root,
          text="Это кнопка", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
 
but.pack()
root.mainloop()

#label
lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
lab.pack()
#string field
ent = Entry(root,width=20,bd=3)
ent.delete(1.0,END)
ent.insert(END,"Обслуживание клиентов на втором этаже")
ent.get()
ent.pack()
#text field
tex = Text(root,width=40,
          font="Verdana 12",
          wrap=WORD) 
tex.get("1.0",END)

ent.grid(row=0,column=0,padx=20)
but.grid(row=0,column=1)
tex.grid(row=0,column=2,padx=20,pady=10)