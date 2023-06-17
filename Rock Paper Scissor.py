from tkinter import *
import random
import tkinter.messagebox

root = Tk()
root.geometry('700x700+400+50')
root.iconbitmap(r'icon.ico')
root.title("Rock Paper Scissor")
root.configure(bg='bisque2')

rHandPhotoUser = PhotoImage(file='rock.png')
pHandPhotoUser = PhotoImage(file='paper.png')
sHandPhotoUser = PhotoImage(file='scissor.png')

rHandPhotoComp = PhotoImage(file='rock2.png')
pHandPhotoComp = PhotoImage(file='paper2.png')
sHandPhotoComp = PhotoImage(file='scissor2.png')

Label(root,text="User",font= ('Helvetica 25 bold italic'),height=2,width=10, bg='yellow').place(x=110,y=50)
Label(root,text="Computer",font= ('Helvetica 25 bold italic'),height=2,width=10, bg='yellow').place(x=410,y=50)

def rock():
    yourChoice = 0
    compChoice = random.randint(0,2)
    Button(root,image=rHandPhotoUser, bg='orange').place(x=100,y=150)
    if(compChoice == 0):
        Button(root,image=rHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","It's a Draw")
    if(compChoice == 1):
        Button(root,image=pHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Loose")
    if(compChoice == 2):
        Button(root,image=sHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Won")
def paper():
    yourChoice = 1
    compChoice = random.randint(0,2)
    Button(root,image=pHandPhotoUser, bg='orange').place(x=100,y=150)
    if(compChoice == 0):
        Button(root,image=rHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Won")
    if(compChoice == 1):
        Button(root,image=pHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","It's a Draw")
    if(compChoice == 2):
        Button(root,image=sHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Loose")
def scissor():
    yourChoice = 2
    compChoice = random.randint(0,2)
    Button(root,image=sHandPhotoUser, bg='orange').place(x=100,y=150)
    if(compChoice == 0):
        Button(root,image=rHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Loose")
    if(compChoice == 1):
        Button(root,image=pHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","You Won")
    if(compChoice == 2):
        Button(root,image=sHandPhotoComp, bg='orange').place(x=400,y=150)
        tkinter.messagebox.showinfo("Result","It's a Draw")
        
Button(root,text="Rock",font= ('Helvetica 15 bold italic'),height=2,width=10,command=rock, bg='red').place(x=100,y=500)
Button(root,text="Paper",font= ('Helvetica 15 bold italic'),height=2,width=10,command=paper, bg='red').place(x=300,y=500)
Button(root,text="Scissor",font= ('Helvetica 15 bold italic'),height=2,width=10,command=scissor, bg='red').place(x=500,y=500)

root.mainloop()
