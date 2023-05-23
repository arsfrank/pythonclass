import customtkinter as ctk

currentText = "0"
num = 0
op = ""

def updateText():
    global currentText
    if len (currentText) == 0:
        currentText="0"

    if len (currentText) > 12:
        currentText= currentText[:12]

    calcLabel.configure(text=currentText)

def addText(str):
    global currentText
    if float (currentText) == 0 and str != '.' and '.' not in currentText:
         currentText = " "

    if '.' in currentText and str == '.':
        return

    currentText = currentText + str
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""
    updateText()

def Back():
    global currentText
    currentText = currentText[0:len(currentText)-1]
    updateText()

def plus_minus():
    global currentText
    if '-' in currentText:
        currentText= currentText.replace('-', '')
    else:
        currentText = '-' + currentText
        updateText()

def calculate():
    global currentText
    global num
    global op

    currentNum = float(currentText)
    result = 0
    if op == '+':
        result = num + currentNum
    elif op == '-':
        result=currentNum-num
    elif op == '*':
        result =currentNum * num
    elif op == '/':
        result = currentNum/num

    num=result
    currentText = str(result)
    updateText()

def operations(str):
    global currentText
    global num
    global op

    if op == "":
        num = float(currentText)
        currentText = "0"
    else:
        calculate()

    if str == '=':
        op = ""
    else:
        op = str
        currentText = "0"

app = ctk.CTk()
app. geometry("350x500")
app.title("Calculator")
app.configure(bg_color="blue", fg_color="teal")

calcFrame = ctk.CTkFrame(master=app, width= 340, height = 70)
calcFrame.grid(row=0, column=0, padx=5, pady= 5)

calcLabel=ctk.CTkLabel(master=calcFrame, text="0", width= 330, height= 70,
                       anchor="e", font=ctk.CTkFont(size= 50),
                       bg_color="White", fg_color="aqua")
calcLabel.grid(row=0, column= 0, padx=5)

btnFrame = ctk.CTkFrame(master=app, width= 340, height = 400)
btnFrame.grid(row=1, column=0, padx=5, pady= 5)

btnCE= ctk.CTkButton(master= btnFrame, text="CE", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                     command = CE)
btnCE.grid(row= 0, column= 0, padx=2, pady=2)



btnBack= ctk.CTkButton(master= btnFrame, text="<--", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                       command=Back)
btnBack.grid(row= 0, column= 1, padx=2, pady=2)



btnPercent= ctk.CTkButton(master= btnFrame, text="%", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal")
btnPercent.grid(row= 0, column= 2, padx=2, pady=2)


btnDivide= ctk.CTkButton(master= btnFrame, text="/", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                         command=lambda: operations("/"))
btnDivide.grid(row= 0, column= 3, padx=2, pady=2)


btnSeven= ctk.CTkButton(master= btnFrame, text="7", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                        command= lambda:addText("7"))
btnSeven.grid(row= 1, column= 0, padx=2, pady=2)


btnEight= ctk.CTkButton(master= btnFrame, text="8", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                        command=lambda: addText("8") )
btnEight.grid(row= 1, column= 1, padx=2, pady=2)


btnNine= ctk.CTkButton(master= btnFrame, text="9", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                       command= lambda:addText("9"))
btnNine.grid(row= 1, column= 2, padx=2, pady=2)

btnx= ctk.CTkButton(master= btnFrame, text="x", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command=lambda: operations("*"))
btnx.grid(row= 1, column= 3, padx=2, pady=2)


btn4= ctk.CTkButton(master= btnFrame, text="4", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("4"))
btn4.grid(row= 2, column= 0, padx=2, pady=2)


btn5= ctk.CTkButton(master= btnFrame, text="5", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("5"))
btn5.grid(row= 2, column= 1, padx=2, pady=2)


btn6= ctk.CTkButton(master= btnFrame, text="6", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("6"))
btn6.grid(row= 2, column= 2, padx=2, pady=2)


btnMinus= ctk.CTkButton(master= btnFrame, text="-", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                        command=lambda: operations("-"))
btnMinus.grid(row= 2, column= 3, padx=2, pady=2)

btn1= ctk.CTkButton(master= btnFrame, text="1", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("1"))
btn1.grid(row= 3, column= 0, padx=2, pady=2)


btn2= ctk.CTkButton(master= btnFrame, text="2", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("2"))
btn2.grid(row= 3, column= 1, padx=2, pady=2)


btn3= ctk.CTkButton(master= btnFrame, text="3", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("3"))
btn3.grid(row= 3, column= 2, padx=2, pady=2)


btnPlus= ctk.CTkButton(master= btnFrame, text="+", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                       command= lambda: operations("+"),
                     fg_color="blue", bg_color="teal")
btnPlus.grid(row= 3, column= 3, padx=2, pady=2)


btnThingie= ctk.CTkButton(master= btnFrame, text="+/-", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal")
btnThingie.grid(row= 4, column= 0, padx=2, pady=2)




btn0= ctk.CTkButton(master= btnFrame, text="0", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                    command= lambda:addText("0"))
btn0.grid(row= 4, column= 1, padx=2, pady=2 )


btnDec= ctk.CTkButton(master= btnFrame, text=".", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                      command= lambda:addText("."))
btnDec.grid(row= 4, column= 2, padx=2, pady=2)


btnEqual= ctk.CTkButton(master= btnFrame, text="=", width=75, height= 65,
                     font= ctk.CTkFont(size = 30),
                     fg_color="blue", bg_color="teal",
                         command=lambda: operations("=") )
btnEqual.grid(row= 4, column= 3, padx=2, pady=2)

app.mainloop()