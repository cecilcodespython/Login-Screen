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


username = Entry(frame,width=20,fg='black',bg='white',font=('Microsoft YaHei UI light',11),border=-2,highlightthickness=0)
username.place(x=30,y=80)
username.insert(0,'Username')
Frame(frame,width=270,height=1,bg='black').place(x=25,y=105)



password = Entry(frame,width=20,fg='black',bg='white',font=('Microsoft YaHei UI light',11),border=-2,highlightthickness=0)
password.place(x=30,y=160)
password.insert(0,'Password')
Frame(frame,width=270,height=1,bg='black').place(x=25,y=190)


Button(frame,width=22,pady=10,text="Log In",bg='#92E3A9',fg='white',border=0).place(x=60,y=204)

label=Label(frame,text="Don't Have An Account? ",bg='white',fg='#92E3A9',font=('Microsoft YaHei UI light',9))
label.place(x=75,y=250)


# 11:14 of the video










root.mainloop()