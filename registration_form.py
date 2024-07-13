from tkinter import *
import tkinter.messagebox as tmsg
from fpdf import FPDF


root = Tk()
root.geometry("644x345")

def new():
    print("new script is created")


def open():
    print("open script")


def save():
    print("script is saved")


def copy():
    print("script is copied")

def cut():
    print("script is cut")

def delete():
    print("script is deleted")


def help():
    print("i'll help you")
    tmsg.showinfo("HELP","RAM WILL HELP YOU WITH THIS GUI")

def rate():
    print("RATE US")
    value=tmsg.askquestion("WAS YOUR EXPERIENCE GOOF?","give your experience good?")
    if value == "yes":
        msg="greate rate us on appstore"
    else:
        msg="tell us your query"


def browse():
    ans=tmsg.askretrycancel("internet server","connected to net browser")
    if ans:
        print("trying to connect browser")
    else:
        print("no internet connection")



menubar = Menu(root)
m1=Menu(menubar, tearoff=0)
m1.add_command(label="new script",command=new)
m1.add_command(label="open script",command=open)
m1.add_separator()
m1.add_command(label="save",command=save)
m1.add_command(label="print",command=print)

root.config(menu=menubar)
menubar.add_cascade(label="File",menu=m1)

m2=Menu(menubar, tearoff=0)
m2.add_command(label="copy",command=copy)
m2.add_command(label="cut",command=cut)
m2.add_separator()
m2.add_command(label="delete",command=delete)
m2.add_command(label="exit",command=quit)
root.config(menu=menubar)
menubar.add_cascade(label="EDIT",menu=m2)

m3=Menu(menubar, tearoff=0)
m3.add_command(label="HELP",command=help)
m3.add_command(label="RATE",command=rate)
m3.add_separator()
m3.add_command(label="BROWSER",command=browse)

root.config(menu=menubar)
menubar.add_cascade(label="HELP",menu=m3)


Label(root, text="WELCOME TO NIKHIL RESTAURANT", font="Comicsansms 15 bold").grid(column=3)
name=Label(root, text="NAME")
email=Label(root, text="EMAIL")
age=Label(root, text="AGE")
phone=Label(root, text="PHONE")
gender=Label(root, text="GENDER")
paymentmethod=Label(root, text="PAYMENT METHOD")

name.grid(row=1,column=2)
email.grid(row=2,column=2)
age.grid(row=3,column=2)
phone.grid(row=4,column=2)
gender.grid(row=5,column=2)
paymentmethod.grid(row=6,column=2)

namevalue=StringVar()
emailvalue=StringVar()
agevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
paymentmethodvalue=StringVar()
foodservice=IntVar()

nameentry=Entry(root, textvariable=namevalue)
emailentry=Entry(root, textvariable=emailvalue)
ageentry=Entry(root, textvariable=agevalue)

phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
paymentmethodentry=Entry(root, textvariable=paymentmethodvalue)

nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
phoneentry.grid(row=4,column=3)
genderentry.grid(row=5,column=3)
paymentmethodentry.grid(row=6,column=3)


foodservice=Checkbutton(text="want to prebook your meals",variable=foodservice,highlightbackground="red",highlightcolor="red")
foodservice.grid(row=7,column=3)
def getvals():
    print("our team will respond within 24hrs")
    print(f"{namevalue.get(), emailvalue.get(), agevalue.get(), phonevalue.get(), gendervalue.get()}\n")

    document = FPDF()
    document.add_page()
    # font size setting of the page
    document.set_font("Arial", size=15)

    document.cell(230, 10,txt=f"Dear,{namevalue.get()}:you will be notified your seat confirmation at email:{emailvalue.get()}",ln=1,align='L')
    document.cell(230, 10,txt=f"HAVE A NICE DAY,we will also confirm you at your whatsapp:{phonevalue.get()}",ln=2,align='M')
    for i in range(0,8):

        document.cell(200, 10,txt=f"\n",ln=1, align="L")
    document.cell(200, 10, txt=f"THANKS", ln=1, align="L")
    document.output(f"{namevalue.get()}.pdf")
    # creating page format A4 Or A3 Or ...
    document = FPDF(orientation='P', unit='mm', format='A3')
    print("pdf has been created successfully....")

Button(root, text="SUBMIT TO NIKHIL RESTAURANT", command=getvals).grid(row=8,column=3)
root.mainloop()
