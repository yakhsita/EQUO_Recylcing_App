# Recycling software

from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter import messagebox
import tkinter as tk
# from PIL import Image, ImageTk
# import cv2
# import webbrowser  # pip install pillow
from html.parser import HTMLParser
import time
import random
from datetime import date
from datetime import datetime
import math

root = Tk()
root.title("Recycling Application - Hackathon 2022")
bg_color = 'Black'
root.geometry("1215x700")
root.resizable(0, 0)

# Variable Used
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
# Rate = IntVar()
bill_no = StringVar()
x = random.randint(1000, 9999)
bill_no.set(str(x))

global l
l = []

# Date and Time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# Functions

def show():
    t = clicked.get()
    labels.config(text=optionss[t], font=('times new roman', 18, 'bold'))


def remvcha():
    text = "Choose Mineral"
    if clicked.get() == text:
        messagebox.showinfo('Error', 'Please select mineral')
    else:
        additm()

def remvchg():
    text = "Choose Mineral"
    if clicked.get() == text:
        messagebox.showinfo('Error', 'Please select mineral')
    else:
        gbill()


def additm():
    if type(n_txt.get()) == str:
        try:
            qq = int(n_txt.get())
            if type(int(qq)) != int:
                messagebox.showinfo('Error', 'Please enter quantity!\n(Numeric Value)')
            else:
                t = clicked.get()
                qq = int(n_txt.get())
                if t != 'Choose Mineral':
                    if qq != '':
                        show()
                        tt = optionss[t]
                        # n = Rate.get()
                        m = qq * tt
                        l.append(m)
                        if clicked.get() != '':
                            textarea.insert((10.0 + float(len(l) - 1)), f"{clicked.get()}\t\t{n_txt.get()}\t\t{m}\n")
                        else:
                            messagebox.showinfo('Error', 'Please Select Mineral!')
                    else:
                        messagebox.showinfo('Error', 'Please enter quantity!')
        except:
            messagebox.showinfo('Error', 'Please enter quantity!\n(Numeric Value)')
    else:
        t = clicked.get()
        q = n_txt.get()
        if t != 'Choose Mineral':
            if q != '':
                show()
                tt = optionss[t]
                # n = Rate.get()
                m = n_txt.get() * tt
                l.append(m)
                if clicked.get() != '':
                    textarea.insert((10.0 + float(len(l) - 1)), f"{clicked.get()}\t\t{n_txt.get()}\t\t{m}\n")
                else:
                    messagebox.showinfo('Error', 'Please Select Mineral!')
            else:
                messagebox.showinfo('Error', 'Please enter quantity!')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer/Product details not entered")
    else:
        mis = round((10 / 100) * sum(l))
        textAreaText = textarea.get(10.0, (10.0 + float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END,
                        f"-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t        SUB TOTAL :Rs. {sum(l)}")
        textarea.insert(END, f"\n\t          MISCELLANEOUS CHARGES:Rs. {mis}")
        textarea.insert(END,
                        f"\n-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t    GRAND TOTAL :Rs. {sum(l) - mis}")
        textarea.insert(END,
                        f"\n-------------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n\t\t Address for the recycle dump:")
        textarea.insert(END, f"\n\t\t#245 Church Street, Bangalore")
        textarea.insert(END, f"\n\n\t   THANK YOU FOR PROMOTING RECYCLING")
        textarea.insert(END, f"\n\t\t\tGO GREEN!")


def clear():
    c_name.set('')
    c_phone.set('')
    clicked.set('Choose Mineral')
    # Rate.set(0)
    labels.config(text='-', font=('times new roman', 18, 'bold'))
    welcome()


def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()


def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t              Exotic Recycler's India Pvt. Ltd. ")
    textarea.insert(END, "\n\t\tMG Road, Bangalore-560001")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END, f"\nBill Number\t\t: {bill_no.get()}")
    textarea.insert(END, f"\nDate\t\t: {date.today()}\t     Time: {current_time}")
    textarea.insert(END, f"\nProduct Name \t\t: {c_name.get()}\t          Customer Name: {c_phone.get()}")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------")
    textarea.insert(END, "\nMineral Name\t\tMineral Quantity\t\tTotal Price(INR)")
    textarea.insert(END,
                    f"\n-------------------------------------------------------------------------------------------\n")
    textarea.configure(font='arial 11')


##------------------------------------------- Variables to be placed ------------------------------------------------##

# logo_pic
photo = PhotoImage(file="H:\\Equo\\user&pass_pic.png") # bg_pic
label = tk.Label(image=photo)
label.img = photo
lphoto = PhotoImage(file="H:\\Equo\\ntg.png") # logoooo
llabel = tk.Label(image=lphoto, bd=0)
llabel.img = lphoto

# FirstPage
border = tk.LabelFrame(root, text='Login', bg='ivory', bd=1, font=("Arial", 20))
L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
T1 = tk.Entry(border, width=30, bd=5)
L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
T2 = tk.Entry(border, width=30, show='*', bd=5)

# register
border2 = tk.LabelFrame(root, text='Register', bg='ivory', bd=1, font=("Arial", 20))
l1 = tk.Label(border2, text="Username", font=("Arial Bold", 15), bg="ivory")
t1 = tk.Entry(border2, width=30, bd=5)
l2 = tk.Label(border2, text="Password", font=("Arial Bold", 15), bg="ivory")
t2 = tk.Entry(border2, width=30, show="*", bd=5)
l3 = tk.Label(border2, text="Confirm Password   ", font=("Arial Bold", 15), bg="ivory")
t3 = tk.Entry(border2, width=30, show="*", bd=5)

# SecondPage

Label = tk.Label(root, text='''\nDear User,     

    Thank you for choosing e-Recyclers Recycling Software.\t
    INSTRUCTIONS FOR USING THE APP\t
    1. Enter the name of device that is to be recycled.\t
     2. Select the mineral(s) present in your device from among the following minerals\t
    3. After entering details, click on ADD MINERAL\t
     4. Once your are done with entering all the required details, Click on Generate Bill\t

    NOTE : Click on NEXT to continue.\t

    Thanks & Regards,\t
    Team e-Recyclers \t
    A program by : Nishant V H, Priyanshu Singh and Yakhsita Hansdah\t\n\n''', font=("Arial Bold", 10),
                 bg='ivory', fg='black', bd=10)

# slide1-----------------------------                          ------------------------------
# lable
title = tk.Label(root, pady=2, text="Recycling Software for Smart India Hackathon 2022", bd=12, bg=bg_color,
                 fg='white', font=('times new roman', 25, 'bold'), relief=GROOVE, justify=CENTER)
F1 = tk.Label(root, bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color)
# detail entry
cname_lbl = tk.Label(F1, text='Product Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cname_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7)
cphone_lbl = tk.Label(F1, text='Customer Name ', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
cphone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone, relief=SUNKEN, bd=7)
# lable2
F2 = tk.LabelFrame(root, text='Product Details', font=('times new roman', 18, 'bold'), fg='#ffe4e1', bg=bg_color)
# actual detail abt mineral
itm = tk.Label(F2, text='Mineral Name', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')

# for dropdown
options = [
    "Aluminum",
    "Antimony",
    "Barite",
    "Bauxite",
    "Bentonite",
    "Beryllium",
    "Boron",
    "Cadmium",
    "Chromite",
    "Chromium",
    "Cobalt",
    "Columbium",
    "Copper",
    "Europium",
    "Diamond",
    "Diatomite",
    "Feldspar",
    "Gallium",
    "Germanium",
    "Gold",
    "Graphite",
    "Halite",
    "Indium",
    "Iron",
    "Kaolin",
    "Kyanite",
    "Lanthanides",
    "Lead",
    "Lime",
    "Limestone",
    "Lithium",
    "Manganese",
    "Mercury",
    "Mica",
    "Molybdenum",
    "Nickel",
    "Perlite",
    "Platinum",
    "Quartz",
    "Rhenium",
    "Selenium",
    "Silica",
    "Sillimanite",
    "Silver",
    "Strontium",
    "Talc",
    "Tantalum",
    "Tellurium",
    "Terbium",
    "Titanium",
    "Tin",
    "Trona",
    "Tungsten",
    "Vanadium",
    "Yttrium",
    "Zeolite",
    "Zinc",
    "Zirconium"
]

optionss = {
    "Aluminum": 23,
    "Antimony": 24,
    "Barite": 26,
    "Bauxite": 30,
    "Bentonite": 20,
    "Beryllium": 21,
    "Boron": 22,
    "Cadmium": 29,
    "Chromite": 28,
    "Chromium": 28,
    "Cobalt": 30,
    "Columbium": 27,
    "Copper": 20,
    "Europium": 30,
    "Diamond": 50,
    "Diatomite": 44,
    "Feldspar": 29,
    "Gallium": 24,
    "Germanium": 26,
    "Gold": 35,
    "Graphite": 22,
    "Halite": 25,
    "Indium": 24,
    "Iron": 23,
    "Kaolin": 28,
    "Kyanite": 30,
    "Lanthanides": 22,
    "Lead": 23,
    "Lime": 25,
    "Limestone": 27,
    "Lithium": 28,
    "Manganese": 27,
    "Mercury": 30,
    "Mica": 30,
    "Molybdenum": 27,
    "Nickel": 29,
    "Perlite": 26,
    "Platinum": 39,
    "Quartz": 27,
    "Rhenium": 31,
    "Selenium": 23,
    "Silica": 30,
    "Sillimanite": 28,
    "Silver": 33,
    "Strontium": 30,
    "Talc": 24,
    "Tantalum": 25,
    "Tellurium": 22,
    "Terbium": 25,
    "Titanium": 36,
    "Tin": 27,
    "Trona": 26,
    "Tungsten": 30,
    "Vanadium": 27,
    "Yttrium": 30,
    "Zeolite": 29,
    "Zinc": 25,
    "Zirconium": 30
}

labels = tk.Label(root, text="-", font=('times new roman', 17, 'bold'), bg="white", width=16)

clicked = StringVar()
clicked.set("Choose Mineral") # initial menu text
drop = OptionMenu(F2, clicked, *options)
# clicked.get() is the item choosen
# itm_txt = tk.Label(F2, width=20, textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7)
drop.config(width=32)

rate = tk.Label(F2, text='Mineral Rate per gram', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')
rate_txt = Entry(F2, width=20, font='arial 15 bold', relief=SUNKEN, bd=7)
n = tk.Label(F2, text='Mineral Quantity (in gram)', font=('times new roman', 18, 'bold'), bg=bg_color, fg='#dda0dd')
n_txt = Entry(F2, width=20, font='arial 15 bold', relief=SUNKEN, bd=7)
F3 = Frame(root, relief=GROOVE, bd=10)
# Bill generation area
bill_title = tk.Label(F3, text='Bill Generation Area', font='arial 15 bold', bd=7, relief=GROOVE)
scrol_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scrol_y)


def slide1():
    root['bg'] = 'ivory'
    label.place_forget()
    Label.place_forget()
    Button1.place_forget()
    Button2.place_forget()

    title.pack(fill=X)

    # Product Frames
    F1.place(x=0, y=80, relwidth=1)

    cname_lbl.grid(row=0, column=0, padx=20, pady=5)
    cname_txt.grid(row=0, column=1, padx=10, pady=5)

    cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
    cphone_txt.grid(row=0, column=3, padx=10, pady=5)

    F2.place(x=20, y=180, width=630, height=500)

    itm.grid(row=0, column=0, padx=30, pady=20)
    #itm_txt.place(x=360, y=22)
    drop.place(x=360, y=22)

    rate.grid(row=1, column=0, padx=30, pady=20)
    rate_txt.grid(row=1, column=1, padx=10, pady=20)
    labels.place(x=388, y=304)

    n.grid(row=2, column=0, padx=30, pady=20)
    n_txt.grid(row=2, column=1, padx=10, pady=20)

    # Bill area
    F3.place(x=700, y=180, width=500, height=500)

    bill_title.pack(fill=X)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()
    # Buttons
    btn1 = Button(F2, text='Add Mineral', font='arial 15 bold', command=remvcha, padx=5, pady=10, bg='#8f00ff', width=15)
    btn1.grid(row=3, column=0, padx=10, pady=30)
    btn2 = Button(F2, text='Generate Bill', font='arial 15 bold', command=remvchg, padx=5, pady=10, bg='#8f00ff',
                  width=15)
    btn2.grid(row=3, column=1, padx=10, pady=30)
    # btn2a = Button(root, text='Next', font='arial 15 bold', command=qr, padx=2, pady=3, bg='#76ff7a', width=6)
    # btn2a.place(x=950, y=92)
    btn3 = Button(F2, text='Clear', font='arial 15 bold', padx=5, pady=10, command=clear, bg='#8f00ff', width=15)
    btn3.grid(row=4, column=0, padx=10, pady=30)
    btn4 = Button(F2, text='Exit', font='arial 15 bold', padx=5, pady=10, command=exit, bg='#8f00ff', width=15)
    btn4.grid(row=4, column=1, padx=10, pady=30)


def verify():
    try:
        with open("credential.txt", "r") as f:
            info = f.readlines()
            i = 0
            for e in info:
                u, p = e.split(",")
                if u.strip() == T1.get() and p.strip() == T2.get():
                    i = 1
                    SecondPage()
            if i == 0:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
    except:
        messagebox.showinfo("Error", "Please provide correct username and password!!")
        FirstPage()


def check():
    if t1.get() != "" and t2.get() != "" and t3.get() != "":
        with open("credential.txt", "r") as f:
            info = f.readlines()
            if info == ["\n"]:
                if t2.get() == t3.get():
                    with open("credential.txt", "a") as f:
                        f.write(t1.get() + "," + t2.get() + "\n")
                        messagebox.showinfo("Welcome", "You are registered successfully!!")
                        SecondPage()
                if t2.get() != t3.get():
                    messagebox.showinfo("Error", "Your password didn't get match!!")
            else:
                for e in info:
                    u, p = e.split(",")
                    if u.strip() == t1.get():
                        messagebox.showinfo("Error", "Username Exists!\nEnter a different username.")
                        register()
                    if u.strip() != t1.get():
                        if t2.get() == t3.get():
                            with open("credential.txt", "a") as f:
                                f.write(t1.get() + "," + t2.get() + "\n")
                                messagebox.showinfo("Welcome", "You are registered successfully!!")
                                SecondPage()
                        if t2.get() != t3.get():
                            messagebox.showinfo("Error", "Your password didn't get match!!")
    else:
        messagebox.showinfo("Error", "Please fill the complete field!!")


b1 = tk.Button(border2, text="Submit", bg="#6f2da8", font=("Arial", 15), command=check)


# button variable for Register
def register():
    border.pack_forget()
    L1.place_forget()
    T1.place_forget()
    L2.place_forget()
    T2.place_forget()
    B1.place_forget()
    B2.place_forget()

    border2.pack(fill="both", expand=True, padx=370, pady=225)
    l1.place(x=30, y=10)
    t1.place(x=220, y=10)
    l2.place(x=30, y=60)
    t2.place(x=220, y=60)
    l3.place(x=30, y=110)
    t3.place(x=220, y=110)
    b1.place(x=270, y=153)
    b2.place(x=110, y=153)


"""def ThirdPage():
    vid()

    Button=tk.Button(root, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
    Button.place(x=650, y=450)

    Button=tk.Button(root, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
    Button.place(x=100, y=450)
"""


def logo_pic():
    root['bg'] = 'black'
    llabel.place(x=485, y=165)
    root.after(3000, FirstPage)


def FirstPage():
    llabel.place_forget()
    Label.place_forget()
    Button1.place_forget()
    Button2.place_forget()
    border2.pack_forget()
    l1.place_forget()
    t1.place_forget()
    l2.place_forget()
    t2.place_forget()
    l3.place_forget()
    t3.place_forget()
    b1.place_forget()
    b2.place_forget()

    label.place(x=-2, y=0)
    border.pack(fill="both", expand=True, padx=370, pady=240)
    L1.place(x=64, y=18)
    T1.place(x=194, y=18)
    L2.place(x=64, y=74)
    T2.place(x=194, y=74)

    global B1
    global B2
    B1 = tk.Button(border, text="Sign in", font=("Arial", 15), command=verify)
    B1.place(x=260, y=120)
    B2 = tk.Button(border, text="Register", bg="#e51a4c", font=("Arial", 15), command=register)
    B2.place(x=115, y=120)


Button1 = tk.Button(root, text="Back", font=("Arial", 15), command=FirstPage, bg='ivory', fg='black')
# button variables of Firstpage
Button2 = tk.Button(root, text="Next", font=("Arial", 15), command=slide1, bg='ivory', fg='black')

b2 = tk.Button(border2, text="Login", font=("Arial", 15), command=FirstPage)
# button variable of Register--- since FirstPage needs to be defined first.


def SecondPage():
    border.pack_forget()
    L1.place_forget()
    T1.place_forget()
    L2.place_forget()
    T2.place_forget()
    l1.place_forget()
    t1.place_forget()
    B1.place_forget()
    border2.pack_forget()
    l2.place_forget()
    t2.place_forget()
    l3.place_forget()
    t3.place_forget()
    b1.place_forget()
    B2.place_forget()

    Label.place(x=330, y=180)
    Button1.place(x=490, y=495)
    Button2.place(x=730, y=495)


logo_pic()
root.mainloop()
