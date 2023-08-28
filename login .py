##============================CRIMINAL RECORD SYSTEM=====================================##
##==================================LOG IN FORM=============================================##
##=============================IMPORTING MODULES=========================================##
from admin import *
from user import *
import tkinter
from tkinter import *
import tkinter.messagebox
#import mysql.connector
#from PIL import ImageTk, Image
##============================================================================================##
class project:
    def login(self):
        self.root=tkinter.Tk()
        self.root.title("CRIMINAL RECORD SYSTEM OF CHANDKHEDA")
        self.root.geometry("2000x1000")
        #self.mypic = ImageTk.PhotoImage(Image.open("login.jpeg"))
        #self.mylabel = Label(image = self.mypic)
        #self.mylabel.grid()
        ##====================================LOGIN BUTTON======================================##
        def click():
            y=self.t1.get()
            u=y.isdigit()
            wo=len(y)
            io=self.t2.get()
            a=self.username.get()
            if(io=="lockin"and wo==4 and u==True and a==1):
                ob=pro()
                ob.lol()
            elif(io=="getin"and wo==4 and u==True and a==2):
                ob=anime()
                ob.naruto()
            else:
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","SOMETHING'S WRONG WITH THE INPUT")
            clear()
        ##=================================CREATING TABLE===================================##
        def conn():
            con = mysql.connector.connect(host = "localhost", user = "root", passwd = "root",database = "plane")
            cur = con.cursor()
            query = "create table if not exists police (batch_number int(4))"
            cur.execute(query)
            con.commit()
        #conn()
        ##============================FOR CANCEL BUTTON=======================================##
        def close():
            close = tkinter.messagebox.askyesno("CRIMINAL RECORD SYSTEM","Do you want to exit the program?")
            if close > 0:
                self.root.destroy()
                return
        ##====================================CLEAR==============================================##
        def clear():
            self.t1.delete(0,END)
            self.t2.delete(0,END)
            self.username.set(0)
        ##===========================LABELS,ENTRIES,BUTTONS==================================##
        ##====================================LABELS============================================##
        self.username=IntVar()
        self.k=Label(self.root,text="LOGIN FORM",font=("Comic Sans",30))
        self.k.place(x=620,y=130)
        self.u=Label(self.root,text="USER NAME",font=("Comic Sans",20))
        self.u.place(x=500,y=225)
        self.v=Label(self.root,text="BATCH NUMBER",font=("Comic Sans",20))
        self.v.place(x=500,y=300)
        self.p=Label(self.root,text="PASSWORD",font=("Comic Sans",20))
        self.p.place(x=500,y=375)
        ##=================================RADIOBUTTONS======================================##
        self.t=Radiobutton(self.root,text="ADMIN",variable=self.username,value=1,font=("Comic Sans",20))
        self.t.place(x=800,y=225)
        self.t3=Radiobutton(self.root,text="USER",variable=self.username,value=2,font=("Comic Sans",20))
        self.t3.place(x=1000,y=225)
        ##===================================ENTRIES===========================================##
        self.t1=Entry(self.root,width=10,font=("Comic Sans",20))
        self.t1.place(x=800,y=300)
        self.t2=Entry(self.root,width=10,font=("Comic Sans",20),show="*")
        self.t2.place(x=800,y=375)
        ##===================================BUTTONS==========================================##
        self.b=Button(self.root,text="LOG IN",font=("Comic Sans",20),command=click)
        self.b.place(x=600,y=450)
        self.b1=Button(self.root,text="CANCEL",font=("Comic Sans",20),command=close)
        self.b1.place(x=800,y=450)
##================^_^=====================^_^============================^_^=================##
po=project()
po.login()
##=============================================================================================##
##=============================================================================================##

