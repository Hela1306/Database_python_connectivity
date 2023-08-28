##==============================CRIMINAL RECORD SYSTEM===================================##
##=====================================A.D.M.I.N==============================================##
##===============================IMPORTING REQUIRED MODULES============================##
import mysql.connector
import tkinter as tkin
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
#from PIL import Image, ImageTk
##============================================================================================##
class pro:
    def lol(self):
        self.root=tkin.Tk()
        self.root.title("CRIMINAL RECORD SYSTEM OF CHANDKHEDA")
        self.root.geometry("2000x1000")
        ##================================CREATE DATABASE===================================##
        def db():
            con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#")
            cur=con.cursor()
            query="create database plane"
            cur.execute(query)
            con.commit()
        ##=================================CREATING TABLE===================================##
        def conn():
            con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#",database = "plane")
            cur = con.cursor()
            query = "create table if not exists criminal(cid int primary key,cname char(50), \
                        cmobile VarChar(10), ccrime char(255), csection_applied VarChar(255),\
                        cpunishment VarChar(255), ctotal_cases int, cwanted_level char(255))"
            cur.execute(query)
            con.commit()
        #conn()
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
        ##===============================INSERT NEW RECORD===================================##
        def insert():
                con=mysql.connector.connect(host="localhost",user="root",passwd="MicDrop1234@#",database="plane")
                cur=con.cursor()
                query = "insert into criminal(cid,cname,cmobile,ccrime,csection_applied,cpunishment,\
                            ctotal_cases,cwanted_level) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                poo=(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get())
                cur.execute(query,poo)
                con.commit()
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","New Record Has Been Added")
                clear()
        ##====================================DISPLAYING DATA=================================##
        def show():
            if(self.value==0):
                self.value=3
            else:
                self.rightbodyframe.destroy()
                self.value==3
            self.rightbodyframe = LabelFrame(self.mainframe, bd = 1, width = 1500, height = 1000)
            self.rightbodyframe.pack(side = RIGHT)
            con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#",database = "plane")
            cur = con.cursor()
            query = "select * from criminal"
            cur.execute(query)
            row = cur.fetchall()
            con.close()
            labelrecords=Label(self.rightbodyframe,text="---RECORDS---",font=("Times New Roman",50))
            labelrecords.place(x=240,y=20)
            criminallist = Listbox(self.rightbodyframe, width =100, height =100,
                              font = ('Times New Roman',13, 'bold'))
            for i in range(len(row)):
                criminallist.insert(i,row[i])
                criminallist.insert(i+1,'\n')
            criminallist.place(x =20,y=100)
            
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
            updatebutton=Button(self.rightbodyframe,text="UPDATE",font=("Times New Roman",20),command=update)
            updatebutton.place(x=300,y=500)
            deletebutton=Button(self.rightbodyframe,text="DELETE",font=("Times New Roman",20),command=delete)
            deletebutton.place(x=500,y=500)
            clearbutton=Button(self.rightbodyframe,text="CLEAR",font=("Times New Roman",20),command=clear)
            clearbutton.place(x=700,y=500)
        ##===================================INSERT NEW RECORD==============================##
        def new_record():
            if(self.value==0):
                self.value=3
            else:
                self.rightbodyframe.destroy()
                self.value==3
            self.rightbodyframe = LabelFrame(self.mainframe, bd = 1, width = 1500, height = 1000)
            self.rightbodyframe.pack(side = RIGHT)
            abc()
            insertbutton=Button(self.rightbodyframe,text="ADD",font=("Times New Roman",20),command=insert)
            insertbutton.place(x=200,y=500)
            clearbutton=Button(self.rightbodyframe,text="CLEAR",font=("Times New Roman",20),command=clear)
            clearbutton.place(x=700,y=500)
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
        self.buttonsearch = Button(self.leftbodyframe,text="RECORD MANAGEMENT",font=("Times New Roman",20),
                                   command=search)
        self.buttonnewrecord= Button(self.leftbodyframe,text="ADD RECORD",font=("Times New Roman",20),
                                     command=new_record)
        self.buttonview = Button(self.leftbodyframe,text="SHOW RECORDS",font=("Times New Roman",20),command=show)
        self.buttonclose = Button(self.leftbodyframe,text="CLOSE",font=("Times New Roman",20),command=close)

        self.buttonsearch.place(x=50,y=200)
        self.buttonnewrecord.place(x=50,y=100)
        self.buttonview.place(x=50,y=300)
        self.buttonclose.place(x=50,y=400)
        ##==================================SEARCH RECORDS====================================##
        def find():
            if(len(a.get())!=0):
                con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#",database = "plane")
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
            
            
        ##==================================UPDATING DATA=====================================##
        def update():
            if(len(a.get())!=0):
                con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#",database = "plane")
                cur = con.cursor()
                query="update criminal set cname = %s , cmobile = %s , \
             ccrime = %s , csection_applied = %s , cpunishment = %s , ctotal_cases = %s , cwanted_level = %s \
             where cid = %s"
                poo=(b.get(),c.get(),d.get(),e.get(),f.get(),g.get(),h.get(),a.get())
                cur.execute(query,poo)
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","Record Updated ")
                clear()
            else:
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","All Fields Required")
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
        ##================================DELETING DATA======================================##
        def delete():
            if(len(a.get())!=0):
                con = mysql.connector.connect(host = "localhost", user = "root", passwd = "MicDrop1234@#",database = "plane")
                cur = con.cursor()
                query="delete from criminal where cid = %s"
                cur.execute(query,(a.get(),))
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","Record has been deleted")
                clear()
            else:
                tkinter.messagebox.showinfo("CRIMINAL RECORD SYSTEM","ID is must to delete a record")
##==========^_^=========================^_^=============================^_^=================##
ob=pro()
ob.lol()
