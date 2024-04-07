from tkinter import*
import datetime 
import sqlite3
from tkinter import messagebox

date = datetime.datetime.now()
date= date.strftime("%Y-%m-%d")

conn=sqlite3.connect ('phonebook.db')
cur = conn.cursor() 

class Phonebook(object):
    def __init__(self, master):
        self.master = master
        top = Frame(master, height=150, bg='#14635f', bd=8, relief=GROOVE)
        top.pack(fill='x')
        self.bottom = Frame(master, height=540, bg='skyblue', bd=8, relief=GROOVE)
        self.bottom.pack(fill='x')
        heading = Label(top, text='My Phonebook App', font='arial 40 bold', bg='#14635f', fg='skyblue')
        heading.place(x=70, y=30)
        date1 = Label(top, text="Today's date: " + date, font='arial 15 bold', bg='#14635f')
        date1.place(x=370, y=100)
        self.login_design()


    def login_design(self):
        f1 = Frame(self.bottom, height=340, width=390, bg='pink', bd=15, relief=GROOVE)
        f1.place(x=120, y=40)
        f2 = Frame(f1, height=300, width=350, bd=8, relief=GROOVE)
        f2.place(x=6, y=6)
        Label (f2,text = 'Login Page', font = 'arial 25 bold', fg = 'blue',).place(x=80,y=10)
        
        Label (f2, text='User Name', font='arial 18 bold').place (x=10, y=90) 
        self.name_e=Entry (f2, bd=3)
        self.name_e.place (x=150, y=90, height=28, width=170)
        Label (f2, text=' Password', font='arial 18 bold').place(x=10,y=150)
        self.pwd_e=Entry (f2, bd=3)
        self.pwd_e.place (x=150, y=150, height=28, width=170) 
        
        btn1=Button (f2, width=7, text='Login',font='arial 13 bold', bd=4, relief = GROOVE, bg= 'pink')
        btn1.place (x=140, y=200) 

        btn2=Button (f2, height=2, width = 13, text='Change Password',font='arial 7 bold', bd=4, relief = GROOVE, bg= 'red',command=self.Change_design)
        btn2.place (x=5, y=250)


    def login(self):
        n = self.name_e.get()
        p = self.pwd_e.get()
        
        result = cur.execute("select * from login").fetchone()
        name = result[0]
        pwd = result[1]

        if n != '' and p != '':

            if name == n and pwd == p:
                messagebox.showinfo("Success", "Login Successful")
            else:
                messagebox.showerror("Error", "Invalid Username and Password")
        else:
            messagebox.showinfo("Information", "Enter Username and Password")


    def Change_design(self):
        f1 = Frame(self.bottom, height=340, width=390, bg='red', bd=15, relief=GROOVE)
        f1.place(x=120, y=40)
        f2 = Frame(f1, height=300, width=350, bd=8, relief=GROOVE)
        f2.place(x=6, y=6)
        Label (f2,text = 'Change Password', font = 'arial 20 bold', fg = 'blue',).place(x=50,y=10)
        
        Label (f2, text='User Name', font='arial 15 bold').place (x=10, y=70) 
        self.name_e=Entry (f2, bd=3)
        self.name_e.place (x=170, y=70, height=28, width=150)

        Label (f2, text='Old Password', font='arial 15 bold').place (x=10, y=110) 
        self.oldpwd_e=Entry (f2, bd=3)
        self.oldpwd_e.place (x=170, y=110, height=28, width=150) 

        Label (f2, text='New Password', font='arial 15 bold').place (x=10, y=150) 
        self.newpwd_e=Entry (f2, bd=3)
        self.newpwd_e.place (x=170, y=150, height=28, width=150)

        btn1=Button (f2, width=7, text='Change',font='arial 13 bold', bd=4, relief = GROOVE, bg= 'red', command = self.change_password)
        btn1.place (x=140, y=200) 

        btn2=Button (f2, height=2, width = 13, text='Login',font='arial 7 bold', bd=4, relief = GROOVE, bg= 'pink', command = self.login_design)
        btn2.place (x=5, y=250)


    def change_password(self):
        n = self.name_e.get()
        o_p = self.oldpwd_e.get()
        n_p = self.newpwd_e.get()

        result = cur.execute("select * from login").fetchone()
        name = result[0]
        pwd = result[1]

        if n != '' and o_p != '' and n_p !='' :

            if name == n and pwd == o_p:
                cur.execute("Update Login set password = ? and password = ?",(n_p,o_p))
                conn.commit()
                messagebox.showinfo("Success", "Password Chnanged")
            else:
                messagebox.showerror("Error", "Invalid Username and Old Password")
        
        else:
            messagebox.showinfo("Information", "Fillup all field")




def main() :
    win = Tk()
    app = Phonebook(win)
    win.title('Myphonebookapp')
    win.geometry('650x570+300+100')
    win.resizable(False, False)
    win.mainloop()
    
main()


                
                