import customtkinter as ctk
def enter_clicked():
  # print("enter clicked")
    name=nameEntry.get()
    password= passwordEntry.get()
    print(name)
    print(password)
    strList = ["Hello", name, "your password is", '*' * len(password)]
    info = ' ' .join(strList)
    infoLabel.configure(text=info)


app = ctk . CTk()
app.title("My Life!")
app.geometry("300x 200")


nameLabel = ctk.CTkLabel(app, text="Name:  ")
nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

passwordLabel = ctk.CTkLabel(app, text="Password:  ")
passwordLabel.grid(row=1, column=0)

passwordEntry = ctk.CTkEntry(app, placeholder_text="Enter your password")
passwordEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text= "Enter:  ", command=enter_clicked)
enterButton.grid(row=2, column= 0)

infoLabel= ctk.CTkLabel(app, text= "  ")
infoLabel.grid(row=4, column=1)

app.mainloop()