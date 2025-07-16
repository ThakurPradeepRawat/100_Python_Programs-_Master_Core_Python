"""
Program: Prime Number Check
Author: Pradeep Rawat
Description: Checks whether a number is prime or not.
"""
def is_prime(num):
    for i in range(2 , num//2 +1):
        if num%i == 0:
            return "not a prime "
    return "a prime "
num = int(input("Enter a number :- "))
if (num < 2 ):
    print("Enter valid number ('Greater than 2 ')")
else:
    print("{} is {} number " .format(num , is_prime(num)))
