# program to check password and make sure it's 8 charectars long
username= input("Enter your name")
password= input("Enter your password")
passwordLength= len(password)
while passwordLength < 8 :
    print("password should be 8 or more characters")
    password=input("Enter your password")
    passwordLength = len(password)
hiddenPassword= '*' * len(password)

print(f"Hello {username} your password is {hiddenPassword}")

