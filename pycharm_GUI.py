from tkinter import *
class MyWindow:
    def __init__(self,window):
        self.lbl = Label(window, text = "Simple Calculator")
        self.lbl.place(x=75, y =75)
        self.lbl1 = Label(window,text = "Number 1:",fg="blue")
        self.lbl1.place(x=80,y=100)
        self.txt1 = Entry(window,bd = 2)
        self.txt1.place(x=150,y=100)

        self.lbl2 = Label(window, text = "Number 2:", fg = "orange")
        self.lbl2.place(x=80, y=150)
        self.txt2 = Entry(window, bd = 5)
        self.txt2.place(x=150,y=150)

        self.btn1= Button(window,text = "Add", command=self.add)
        self.btn1.place(x=80,y=200)
        self.btn2 = Button(window, text = "Subract")
        self.btn2.place(x=120,y=200)
        self.btn2.bind('<Button-1>', self.sub)
        self.btn3 = Button(window,text= "Multiply")
        self.btn3.place(x=180, y=200)
        self.btn3.bind('<Button-1>',self.mul)
        self.btn4 = Button(window,text = "Divide", command=self.div)
        self.btn4.place(x =250,y=200)


        self.txt3 = Entry(window)
        self.txt3.place(x = 100,y =250)

        self.lbl3 = Label(window,text="Gender",fg="blue")
        self.lbl3.place(x=100,y=300)

        var = IntVar()

        self.r1 = Radiobutton(window,text="Male",variable=var,value=1,command=self.sel)
        self.r1.place(x=100,y=320)
        self.r2 = Radiobutton(window,text="Female",variable=var,value=2,command=self.sel)
        self.r2.place(x=150,y=320)

        self.lbl4 = Label(window,text = "Choose all fruits that you eat")
        self.lbl4.place (x=100,y=350)
        self.lbl5 = Label(window, text="Choose all fruits that you eat")
        self.lbl5.place(x=100, y=370)
        self.chkbox= Checkbutton(window,text = "apple")
        self.chkbox.place(x=100,y=370)
        self.chkbox2 = Checkbutton(window,text = "banana")
        self.chkbox2.place(x=150,y=370)
        self.chkbox3 = Checkbutton(window,text="orange")
        self.chkbox3.place(x=200,y=370)
    def add(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1+num2
        self.txt3.insert(END, str(result))

    def sub(self,event):
        self.txt3.delete(0,'end')
        num1=int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self,event):
        self.txt3.delete(0,'end')
        num1=int(self.txt1.get())
        num2=int(self.txt2.get())
        result = num1*num2
        self.txt3.insert(END,str(result))


    def div(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

    def sel(self):
        var = IntVar()
        selection = "You selected this option"+ str(var.get())
        self.lbl5.config(text = selection)


window = Tk()
mywin=MyWindow(window)
window.geometry("500x400+10+20")
window.title("Python Project")
window.mainloop()
