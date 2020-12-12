from tkinter import *
import requests
import json

def register():
    global username, password, root
    # Making main window
    root = Tk()
    root.title("Login system")
    #root.minsize(width=400,height=400)
    root.geometry("640x800")
    root.resizable(False, False)
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True,fill=BOTH)

    lblusername = Label(root, text="Put your username in the box beneath", bg="grey", fg='black')
    lblusername.place(relx=0.2, rely=0.20, relwidth=0.62, relheight=0.08)
    username = Entry(root)
    username.place(relx=0.2,rely=0.30, relwidth=0.62, relheight=0.08)

    lblpassword = Label(root, text="Put your password in the box beneath", bg="grey", fg='black')
    lblpassword.place(relx=0.2, rely=0.50, relwidth=0.62, relheight=0.08)
    password = Entry(root)
    password.place(relx=0.2,rely=0.60, relwidth=0.62, relheight=0.08)

    loginscreen = Button(root, text="login page", bg="green", fg="black", command=signin)
    loginscreen.place(relx=0.42,rely=0.75, relwidth=0.1,relheight=0.03)

    button1 = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=registerinfo)
    button1.place(relx=0.38,rely=0.9, relwidth=0.18,relheight=0.08)

    lblregister = Label(root, text="Registration screen", bg="grey", fg='black')
    lblregister.place(relx=0.2, rely=0.05, relwidth=0.62, relheight=0.08)

    root.mainloop()


def registerinfo():

    pwu = {
        "name": username.get(),
        "password": password.get()
    }

    r = requests.post('http://localhost:8000/Register/', data=pwu)
    print(r.text)


def signin():
    root.destroy()
    global username, password, root1
    # Making main window
    root1 = Tk()
    root1.title("Login system")
    #root.minsize(width=400,height=400)
    root1.geometry("640x800")
    root1.resizable(False, False)
    
    Canvas1 = Canvas(root1)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True,fill=BOTH)

    lblusername = Label(root1, text="Put your username in the box beneath", bg="grey", fg='black')
    lblusername.place(relx=0.2, rely=0.20, relwidth=0.62, relheight=0.08)
    username = Entry(root1)
    username.place(relx=0.2,rely=0.30, relwidth=0.62, relheight=0.08)

    lblpassword = Label(root1, text="Put your password in the box beneath", bg="grey", fg='black')
    lblpassword.place(relx=0.2, rely=0.50, relwidth=0.62, relheight=0.08)
    password = Entry(root1)
    password.place(relx=0.2,rely=0.60, relwidth=0.62, relheight=0.08)

    loginscreen = Button(root1, text="Register page", bg="green", fg="black", command=register)
    loginscreen.place(relx=0.4,rely=0.75, relwidth=0.15,relheight=0.03)

    button1 = Button(root1,text="SUBMIT",bg='#d1ccc0', fg='black', command=signininfo)
    button1.place(relx=0.38,rely=0.9, relwidth=0.18,relheight=0.08)

    lblregister = Label(root1, text="Signin screen", bg="grey", fg='black')
    lblregister.place(relx=0.2, rely=0.05, relwidth=0.62, relheight=0.08)

    root.mainloop()

def signininfo():
    pwu = {
        "name": username.get(),
        "password": password.get()
    }

    url = 'http://localhost:8000/Register/?name=' + pwu['name'] + '&password=' + pwu['password']
    print(url)
    r = requests.get(url)
    print(r.text)

register()