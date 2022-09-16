from logging import root
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Login Screen")
root.geometry("825x500+300+200")
root.config(bg='white')
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,height=350,width=350,bg='white')
frame.place(x=480,y=50)

heading = Label(frame,text="Login",bg='white',fg='#92E3A9',font=('Microsoft YaHei UI light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    username.delete(0,'end')

def on_leave(e):
    name = username.get()
    if name == "":
        username.insert(0,'username')




username = Entry(frame,width=20,fg='black',bg='white',font=('Microsoft YaHei UI light',11),border=-2,highlightthickness=0)
username.place(x=30,y=80)
username.insert(0,'Username')
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave)
Frame(frame,width=270,height=1,bg='black').place(x=25,y=105)

def on_enter(e):
    password.delete(0,'end')

def on_leave(e):
    name = password.get()
    if name == "":
        password.insert(0,'password')


password = Entry(frame,width=20,fg='black',bg='white',font=('Microsoft YaHei UI light',11),border=-2,highlightthickness=0)
password.place(x=30,y=140)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
Frame(frame,width=270,height=1,bg='black').place(x=25,y=170)

def li_message():
    user_name = username.get()
    messagebox.showinfo(title="Log In",message=f"Hello {user_name},You're Logged in")


Button(frame,width=22,pady=10,text="Log In",bg='#92E3A9',fg='white',border=0,command=li_message).place(x=60,y=204)

label=Label(frame,text="Don't Have An Account? ",bg='white',fg='black',font=('Microsoft YaHei UI light',9))
label.place(x=65,y=260)


sign_up = Button(frame,width=4,height=2,cursor='hand2',text="Sign Up",border=-2,bg='white',fg='black',highlightthickness=0)
sign_up.place(x=220,y=250)








root.mainloop()