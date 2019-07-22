from Tkinter import *

# switching on "main" window-------------------------------
window=Tk()
window.title("Gates Calculator")

# frame 1 for heading-----------------------------------------
frame=Frame(window)
frame.pack()

heading=Label(frame, text="Welcome to BITWISE OPERATOR", font=("","22"))
heading.pack()

ans=0
bin_ans=0

def onclick():
    myvalue1=int(entry1.get())
    myvalue2=int(entry2.get())
    optionon=myradio.get()
    global ans,bin_ans
    if myvalue2 is None or myvalue1 is None:
        messagebox.showinfo("Empty Values!", "The Values are Empty!")
    else:
        if optionon == 1:
            ans = myvalue1 & myvalue2
            resultstatement.configure(text=ans)
        elif optionon == 2:
            ans = myvalue1 | myvalue2
            resultstatement.configure(text=ans)
        elif optionon == 3:
            ans = ~ myvalue1
            resultstatement.configure(text=ans)
        elif optionon == 4:
            ans = myvalue1 ^ myvalue2
            resultstatement.configure(text=ans)
        elif optionon==5:
            ans = (~(myvalue1 & myvalue2))
            
            resultstatement.configure(text=ans)
        elif optionon == 6:
            ans = (~(myvalue1 | myvalue2))
            resultstatement.configure(text=ans)
        elif optionon==7:
            ans = (~(myvalue1 ^ myvalue2))
            
            resultstatement.configure(text=ans)
        elif optionon==4 or optionon==8:
            ans = myvalue1 ^ myvalue2
            resultstatement.configure(text=ans)

    bin_ans=bin(ans)    

def onclick2():
    myvalue1 = int(entry1.get())
    myvalue2 = int(entry2.get())
    optionon = myradio.get()
    myvalue1_bin=bin(myvalue1)
    myvalue2_bin=bin(myvalue2)
    global ans
    global bin_ans


#Opening New Window--------------------------------------------------------------------------------
    root = Tk()
    root.title("Gates Calculator > Explanation")

    # frame x---------------------------------------------------
    framex = Frame(root)
    framex.pack()

    header = Label(framex, text="Explanation:", fg="green", font=("", "22"))
    header.pack()
    # frame y----------------------------------------------------
    framey = Frame(root, bg="orange")
    framey.pack()

    label1 = Label(framey, text="Your Value A : ", font=("", "14"), bg="orange")
    value = Label(framey, text=myvalue1, fg="white", font=("", "14"), bg="orange")
    label2 = Label(framey, text="Your Value B : ", font=("", "14"), bg="orange")
    value2 = Label(framey, text=myvalue2, fg="white", font=("", "14"), bg="orange")

    binary1 = Label(framey, text="In Binary :", font=("", "14"), bg="orange")
    valuex = Label(framey, text=myvalue1_bin[2:], fg="white", font=("", "14"), bg="orange")
    binary2 = Label(framey, text="In Binary :", font=("", "14"), bg="orange")
    valuey = Label(framey, text=myvalue2_bin[2:], fg="white", font=("", "14"), bg="orange")

    label1.grid(row=0, column=0)
    value.grid(row=1, column=0)
    label2.grid(row=0, column=2)
    value2.grid(row=1, column=2)
    binary1.grid(row=2, column=0)
    valuex.grid(row=3, column=0)
    binary2.grid(row=2, column=2)
    valuey.grid(row=3, column=2)

    # frame z -----------------------------------------------------
    framez = Frame(root)
    framez.pack()

    operation = Label(framez, text="Operation Output (DECIMAL) :", font=("", "13"))
    valuea = Label(framez, text=ans, bg="Blue", fg="white", font=("", "13"))
    operation2 = Label(framez, text="Operation Output (BINARY) :", font=("", "13"))
    if ans>=0:
        valueb = Label(framez, text=bin_ans[2:], bg="Blue", fg="white", font=("", "13"))
    else:
        valueb = Label(framez, text=bin_ans[3:], bg="Blue", fg="white", font=("", "13"))
    operation.grid(row=0, column=0)
    valuea.grid(row=0, column=1)
    operation2.grid(row=1, column=0)
    valueb.grid(row=1, column=1)

    
    root.mainloop()

# frame 2 for body items---------------------------------------
frame2=Frame(window,bg="orange")
frame2.pack()

number1=Label(frame2,text="Value A",bg="blue",fg="white",font=("","12"))
entry1=Entry(frame2)

number2=Label(frame2,text="Value B",bg="blue",fg="white",font=("","12"))
entry2=Entry(frame2)

number1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
number2.grid(row=0,column=2)
entry2.grid(row=0,column=3)

myradio=IntVar()
option1=Radiobutton(frame2,text="AND",value=1,bg="orange",font=("","12"),variable=myradio)
option2=Radiobutton(frame2,text=" OR",value=2,bg="orange",font=("","12"),variable=myradio)
option3=Radiobutton(frame2,text="NOT",value=3,bg="orange",font=("","12"),variable=myradio)
option4=Radiobutton(frame2,text="XOR",value=4,bg="orange",font=("","12"),variable=myradio)
option5=Radiobutton(frame2,text="NAND",value=5,bg="orange",font=("","12"),variable=myradio)
option6=Radiobutton(frame2,text="XNOR",value=6,bg="orange",font=("","12"),variable=myradio)
option7=Radiobutton(frame2,text="NOR",value=7,bg="orange",font=("","12"),variable=myradio)
option8=Radiobutton(frame2,text="XOR",value=8,bg="orange",font=("","12"),variable=myradio)

option1.grid(row=3,column=0,sticky=N)
option2.grid(row=3,column=1)
option3.grid(row=5,column=0,sticky=N)
option4.grid(row=5,column=1)
option5.grid(row=7,column=0,sticky=E)
option6.grid(row=9,column=0)
option7.grid(row=7,column=1)
option8.grid(row=9,column=1)

result=Button(frame2,text="Generate Result",bg="green",fg="white",command=onclick,font=("","12"))
explain=Button(frame2,text="Get Explanation",bg="green",fg="white",font=("","12"),command=onclick2)

result.grid(row=5,column=3)
explain.grid(row=7,column=3)

# frame3 for result---------------------------------------
frame3=Frame(window)
frame3.pack()

solution=Label(frame3,text="Answer : ",fg="green",font=("","22"))
solution.pack(side=LEFT)
resultstatement=Label(frame3,text="Values Empty!",fg="red",font=("","22"))
resultstatement.pack(side=LEFT)

frameend=Frame(window)
frameend.pack()
copyright=Label(frameend,text="Created by: Aditya, Rohit and Sairam",fg="black",font=("","8"))
copyright.pack()

window.mainloop()
