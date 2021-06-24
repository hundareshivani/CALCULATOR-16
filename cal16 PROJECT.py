import tkinter
from tkinter import *

exp = " "
def click(num):
    global exp
    exp+=str(num)
    text.set(exp)

def equalclick():
    global exp
    sum=str(eval(exp))
    text.set(sum)
    exp=" "


def clear ():
    global exp
    exp = " "
    text.set(" ")



if __name__ == "__main__":




    cal=Tk()
    cal.title("CALCUULATOR APP 2020")
    exp=" "
    text= StringVar()

cal.configure(bg="cyan")
cal.geometry("365x370")
Display=Entry(cal, font=("canbara", 20 , "bold"), textvariable=text, bd=30 , bg="lightpink1")
Display.grid(columnspan=4)

bt7= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="7", command = lambda : click(7) )
bt7.grid(row=1 , column=0)

bt8= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="8", command = lambda : click(8) )
bt8.grid(row=1 , column=1)

bt9= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="9", command = lambda : click(9) )
bt9.grid(row=1 , column=2)

Add= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="+" , command = lambda : click("+"))
Add.grid(row=1 , column=3)

bt4= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="4", command = lambda : click(4) )
bt4.grid(row=2 , column=0)

bt5= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="5" , command = lambda : click(5))
bt5.grid(row=2 , column=1)

bt6= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="6" , command = lambda : click(6))
bt6.grid(row=2 , column=2)

Subtract= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="-" , command = lambda : click("-"))
Subtract.grid(row=2 , column=3)

bt1= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="1" , command = lambda : click(1))
bt1.grid(row=3 , column=0)

bt2= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="2" , command = lambda : click(2))
bt2.grid(row=3 , column=1)

bt3= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="3" , command = lambda : click(3))
bt3.grid(row=3 , column=2)

Multiply= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="*" , command = lambda : click("*"))
Multiply.grid(row=3 , column=3)

bt0= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="0" ,  command = lambda : click(0))
bt0.grid(row=4 , column=0)

btClear= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="C" , command = clear )
btClear.grid(row=4 , column=1)

btEqual= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="=" , command = equalclick )
btEqual.grid(row=4 , column=2)

Division= Button (cal, fg="black", bd=8, padx=16, font=("canbara", 20 , "bold"), text="/" , command = lambda : click("/"))
Division.grid(row=4 , column=3)

cal.mainloop()