"""
Program: even or add
Author: Pradeep Rawat
Description: find number is even or odd
"""
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number :- "))
print("{} is a {} number" .format(num , even_odd(num)))