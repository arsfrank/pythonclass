import customtkinter as ctk
def enter_clicked():
  # print("enter clicked")
    name=nameEntry.get()
    address= AddressEntry.get()
    print(name)
    print(address)
    strList = [name, address]
    info = '\n' .join(strList)
    infoLabel.configure(text=info)


app = ctk . CTk()
app.title("My Life!")
app.geometry("300x 200")


nameLabel = ctk.CTkLabel(app, text="Name:  ")
nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

nameLabel.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
nameEntry.grid(row=0, column=1)

addressLabel = ctk.CTkLabel(app, text="Address:  ")
addressLabel.grid(row=1, column=0)

AddressEntry = ctk.CTkEntry(app, placeholder_text="Enter your address")
AddressEntry.grid(row=1, column=1)

enterButton = ctk.CTkButton(app, text= "Enter:  ", command=enter_clicked)
enterButton.grid(row=2, column= 0)

infoLabel= ctk.CTkLabel(app, text= "  ")
infoLabel.grid(row=4, column=1)

app.mainloop()