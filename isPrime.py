# program to tell user if the number is prime or not prime #
num = int(input("enter any number: "))
counter = 2
isPrime = true
while counter < num :
    if num % counter == 0 :
         isPrime = False
              break
counter = counter + 1

if isPrime:
    print("this is a prime number!")
else:
    print(" this is not a prime number!")

