def reverseString(a):
    rev = " "
    counter = len(a) - 1
    while counter >= 0:
        rev = rev + a[counter]
        counter = counter - 1

    return rev

def isPalindrome(a):
    rev = reverseString(a)
    if rev == a:
        return True
    else:
        return False

    name = input("enter name: ")
    password = input(" enter password: ")



    if isPalindrome(name):
        print("This ia a Palindrome!")
    else:
        print("This is not a Plaindrome:(")
        