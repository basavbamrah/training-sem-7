# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:00:39 2022

@author: Shubu
"""

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
# back=#efdcc5
conn = mysql.connector.connect(user='root',
                               host='localhost',
                               port=3306,
                               password='')

cur = conn.cursor()
try:
    cur.execute('create database abcde;')
except:
    pass
cur.execute('use abcde;')


class Pro:
    def signup(self):
        # frame=Tk()
        self.root = Tk()
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        # self.root.geometry(f"500x500")

        self.root.geometry(f"{self.w}x{self.h}")
        self.root.title("Signup Page")
        # Headings

        self.l1 = Label(self.root, text="Signup Here", fg="black",
                        font=("Times New Roman", 20, "italic", "bold"))
        self.l1.place(relx=0.40, rely=0.01)

        # Labels
        self.l2 = Label(self.root, text="Username        :", fg="black",
                        font=("Times New Roman", 14, "italic"))
        self.l2.place(relx=0.3, rely=0.22)

        self.l2 = Label(self.root, text="Password        :", fg="black",
                        font=("Times New Roman", 14, "italic"))
        self.l2.place(relx=0.3, rely=0.28)

        self.l2 = Label(self.root, text="Confirm\npassword        :", fg="black",
                        font=("Times New Roman", 14, "italic"))
        self.l2.place(relx=0.3, rely=0.34)

        self.l2 = Label(self.root, text="Gender           :", fg="black",
                        font=("Times New Roman", 14, "italic"))
        self.l2.place(relx=0.3, rely=0.44)

        self.l2 = Label(self.root, text="Email             :", fg="black",
                        font=("Times New Roman", 14, "italic"))
        self.l2.place(relx=0.3, rely=0.50)

        # entry field
        # username

        self.e1 = Entry(self.root, font=("Times New Roman", 14), width=20)
        self.e1.place(relx=0.45, rely=0.22)

        # password

        self.e2 = Entry(self.root, font=("Times New Roman", 14), width=20)
        self.e2.place(relx=0.45, rely=0.28)

        # confirm password

        self.e3 = Entry(self.root, font=("Times New Roman", 14), width=20)
        self.e3.place(relx=0.45, rely=0.36)

        # Gmail

        # Radio Button

        self.v = IntVar()
        self.r1 = Radiobutton(
            self.root, text="Male", variable=self.v, value=0, font=("Times New Roman", 12))
        self.r1.place(relx=0.45, rely=0.43)

        self.r1 = Radiobutton(
            self.root, text="Female", variable=self.v, value=1, font=("Times New Roman", 12))
        self.r1.place(relx=0.50, rely=0.43)

        # Email

        self.e5 = Entry(self.root, font=("Times New Roman", 14), width=20)
        self.e5.place(relx=0.45, rely=0.5)

        # buttons

        self.bt1 = Button(self.root, text="Signup", width=10, bg="#a5ebf4",
                          font=("Times New Roman", 12), command=sig)
        self.bt1.place(relx=0.3, rely=0.60)

        self.bt2 = Button(self.root, text="Already have an account?", width=25, bg="#a5ebf4",
                          font=("Times New Roman", 12), command=fxn)
        self.bt2.place(relx=0.45, rely=0.60)

        self.root.configure(bg="#c5c7ef")

        self.root.mainloop()

    def login(self):
        self.root1 = Tk()
        # self.root1.geometry("500x500")
        self.w1 = self.root1.winfo_screenwidth()
        self.h1 = self.root1.winfo_screenheight()
        # self.root.geometry(f"500x500")
        lst = ['Username : ', 'Password : ']
        a = 0.2
        b = 0.3
        for i in range(2):
            l = Label(self.root1, text=lst[i], fg='black',
                      bg='#f4a5b7',
                      font=("Times New Roman", 14, "italic"))
            l.place(relx=b, rely=a)
            a += 0.08
        self.username = Entry(self.root1, font=(
            "Times New Roman", 14), width=20)
        self.username.place(relx=0.4, rely=0.2)
        self.password = Entry(self.root1, font=(
            "Times New Roman", 14), width=20)
        self.password.place(relx=0.4, rely=0.28)

        self.root1.geometry(f"{self.w1}x{self.h1}")
        self.root1.title("Login Page")

        # Headings

        self.bt1 = Button(self.root1, text="Resgister for new account",
                          bg="#a5ebf4", font=("Times New Roman", 12), command=sign)
        self.bt1.place(relx=0.4, rely=0.36)

        self.bt2 = Button(self.root1, text="Login",
                          bg="#a5ebf4", font=("Times New Roman", 12), command=login_)
        self.bt2.place(relx=0.3, rely=0.36)

        self.root1.configure(bg="#f4a5b7")
        self.root1.mainloop()

    def home_page(self):
        self.root2 = Tk()
        self.root2.mainloop()


obj = Pro()


def sig():
    name = obj.e1.get()
    password = obj.e2.get()
    cpassword = obj.e3.get()
    gender = obj.v.get()
    email = obj.e5.get()
    if gender == 0:
        gender = "male"
    elif gender == 1:
        gender = "Female"
    try:
        cur.execute(
            'create table signup(name varchar(20) primary key,password varchar(20),gender varchar(20),email varchar(20));')
    except:
        pass
    try:
        if password == cpassword:
            cur.execute(
                f"insert into signup values('{name}','{password}','{gender}','{email}');")
        else:
            messagebox.showerror('error', 'Please check your password')
    except:
        messagebox.showerror('error', 'username already exists')
    obj.e1.delete(0, END)
    obj.e2.delete(0, END)
    obj.e3.delete(0, END)
    # obj.r1.delete(0,END)
    obj.e5.delete(0, END)


def login_():
    name = obj.username.get()
    pwd = obj.password.get()
    cur.execute(
        f"select * from signup where name='{name}' and password='{pwd}';")
    val = cur.fetchall()
    if len(val) > 0:
        obj.root1.destroy()
        obj.home_page()
    else:
        messagebox.showinfo('error', 'Username or password incorrect')


def sign():
    obj.root1.destroy()
    obj.signup()


def fxn():
    obj.root.destroy()
    obj.login()


obj.signup()
conn.commit()
conn.close()
