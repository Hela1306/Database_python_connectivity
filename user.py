##==============================CRIMINAL RECORD SYSTEM===================================##
##=======================================U.S.E.R===============================================##
##===============================IMPORTING REQUIRED MODULES============================##
import mysql.connector
import tkinter as tkin
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
#from PIL import Image, ImageTk
##============================================================================================##
class anime:
    def naruto(self):
        self.root=tkin.Tk()
        self.root.title("CRIMINAL RECORD SYSTEM OF CHANDKHEDA")
        self.root.geometry("2000x1000")
        ##=====================================CLOSE BUTTON=================================##
        def close():
            close = tkinter.messagebox.askyesno("CRIMINAL RECORD SYSTEM","Do you want to exit the program?")
            if close > 0:
                self.root.destroy()
                return
        ##===========================================FIELDS===================================##
        def abc():
            global a,b,c,d,e,f,g,h
            labelcid=Label(self.rightbodyframe,text="ID",font=("Times New Roman",20))
            labelcid.place(x=50,y=50)
            labelcom=Label(self.rightbodyframe,text="(Compulsary)",font=("Times New Roman",16))
            labelcom.place(x=79,y=50)
            entrycid=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycid.place(x=250,y=50)
            a=entrycid
            labelcname=Label(self.rightbodyframe,text="NAME",font=("Times New Roman",20))
            labelcname.place(x=50,y=100)
            entrycname=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycname.place(x=250,y=100)
            b=entrycname
            labelcmobile=Label(self.rightbodyframe,text="MOBILE",font=("Times New Roman",20))
            labelcmobile.place(x=50,y=150)
            entrycmobile=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycmobile.place(x=250,y=150)
            c=entrycmobile
            labelccrime=Label(self.rightbodyframe,text="CRIME",font=("Times New Roman",20))
            labelccrime.place(x=50,y=200)
            entryccrime=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entryccrime.place(x=250,y=200)
            d=entryccrime
            labelcsection_applied=Label(self.rightbodyframe,text="SECTIONS",font=("Times New Roman",20))
            labelcsection_applied.place(x=50,y=250)
            entrycsection_applied=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycsection_applied.place(x=250,y=250)
            e=entrycsection_applied
            labelcpunishment=Label(self.rightbodyframe,text="PUNISHMENT",font=("Times New Roman",20))
            labelcpunishment.place(x=50,y=300)
            entrycpunishment=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycpunishment.place(x=250,y=300)
            f=entrycpunishment
            labelctotal_cases=Label(self.rightbodyframe,text="TOTAL CASES",font=("Times New Roman",20))
            labelctotal_cases.place(x=50,y=350)
            entryctotal_cases=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entryctotal_cases.place(x=250,y=350)
            g=entryctotal_cases
            labelcwanted_level=Label(self.rightbodyframe,text="LEVEL",font=("Times New Roman",20))
            labelcwanted_level.place(x=50,y=400)
            entrycwanted_level=Entry(self.rightbodyframe,width=45,font=("Times New Roman",20))
            entrycwanted_level.place(x=250,y=400)
            h=entrycwanted_level
        ##====================================DISPLAYING DATA=================================##
        def show():
            if(self.value==0):
                self.value=3
            else:
                self.rightbodyframe.destroy()
                self.value==3
            self.rightbodyframe = LabelFrame(self.mainframe, bd = 1, width = 1500, height = 1000)
            self.rightbodyframe.pack(side = RIGHT)
            con = mysql.connector.connect(host = "localhost", user = "root", passwd = "root",database = "plane")
            cur = con.cursor()
            query = "select * from criminal"
            cur.execute(query)
            row = cur.fetchall()
            con.close()
            labelrecords=Label(self.rightbodyframe,text="---RECORDS---",font=("Times New Roman",50))
            labelrecords.place(x=240,y=20)
            criminallist = Listbox(self.rightbodyframe, width =100, height =100,
                              font = ('Times New Roman',13, 'bold'))
            criminallist.place(x =20,y=100)
            for i in range(len(row)):
                criminallist.insert(i,row[i])
                criminallist.insert(i+1,'\n')
        ##===============================SEARCH LEFT BUTTON===================================##
        def search():
            if(self.value==0):
                self.value=1
            else:
                self.rightbodyframe.destroy()
                self.value==1
            self.rightbodyframe = LabelFrame(self.mainframe, bd = 1, width = 1500, height = 1000)
            self.rightbodyframe.pack(side = RIGHT)
            abc()
            searchbutton=Button(self.rightbodyframe,text="SEARCH",font=("Times New Roman",20),command=find)
            searchbutton.place(x=100,y=500)
            clearbutton=Button(self.rightbodyframe,text="CLEAR",font=("Comic Sans",20),command=clear)
            clearbutton.place(x=600,y=500)
        ##==============================CREATE THE MAINFRAME================================##
        self.mainframe = Frame(self.root)
        self.mainframe.grid()
        #=============================== CREATE THE HEADFRAME=================================##
        self.headframe = Frame(self.mainframe, bd = 1,width=1000,height=20)
        self.headframe.pack(side = TOP)
        self.Ctitle = Label(self.headframe, font = ('Calibri(head)', 50, 'bold'), fg = 'red',
                            text ='CRIMINAL RECORD SYSTEM                                                                                                                     ')
        self.Ctitle.grid()
        ##============================CREATE THE LEFT BODYFRAME==============================##
        self.leftbodyframe = Frame(self.mainframe, bd = 1, width = 400, height = 1000)
        self.leftbodyframe.pack(side = LEFT)
        ##============================CREATE THE RIGHT BODYFRAME============================##
        self.rightbodyframe =Frame(self.mainframe, bd = 1, width = 1600, height = 1000)
        self.rightbodyframe.pack(side = RIGHT)
        self.value=0
        ##=============================ADD BUTTONS TO OPERATION FRAME=====================##
        self.buttonsearch = Button(self.leftbodyframe,text="RECORD MANAGEMENT",font=("Times New Roman",18),
                                   command=search)
        self.buttonview = Button(self.leftbodyframe,text="SHOW RECORDS",font=("Times New Roman",20),command=show)
        self.buttonclose = Button(self.leftbodyframe,text="CLOSE",font=("Times New Roman",20),command=close)
        self.buttonsearch .place(x=100,y=100)
        self.buttonview.place(x=100,y=200)
        self.buttonclose.place(x=100,y=300)
        ##==================================SEARCH RECORDS====================================##
        def find():
            if(len(a.get())!=0):
                con = mysql.connector.connect(host = "localhost", user = "root", passwd = "rootllllllllll",database = "plane")
                cur = con.cursor()
                cur.execute(" select * from criminal where cid = %s",(a.get(),))
                row = cur.fetchall()
                con.commit()
                con.close()
                if(len(row)==0):
                    tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","No Such Record Found")
                    clear()
                else:
                    lo=[]
                    for i in row[0]:
                        lo.append(i)
                    del row[0]
                    row.append(lo)
                    for i in row:
                        b.insert(0,i[1])
                        c.insert(0,i[2])
                        d.insert(0,i[3])
                        e.insert(0,i[4])
                        f.insert(0,i[5])
                        g.insert(0,i[6])
                        h.insert(0,i[7])
            elif(a.get()==""):
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","Id is Complusary to perform search operation ")
            
        ##=======================================CLEAR FIELDS===================================##
        def clear():
            a.delete(0,END)
            b.delete(0,END)
            c.delete(0,END)
            d.delete(0,END)
            e.delete(0,END)
            f.delete(0,END)
            g.delete(0,END)
            h.delete(0,END)
##==========^_^=========================^_^=============================^_^=================##
#ob=anime()
#ob.naruto()
