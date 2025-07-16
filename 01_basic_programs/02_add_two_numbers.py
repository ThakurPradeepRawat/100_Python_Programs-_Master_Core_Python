"""
Program: Add two number
Author: Pradeep Rawat
Description: Take two number as a input from user and print sum of these two numbers.
"""
# function for sum or two numbers 
def sum_of_two_numbers():
    a = int(input("Enter first number :- "))
    b = int(input ("Enter Second number :-"))
    print("Sum of {} and {} is {}" .format(a,b,a+b))
sum_of_two_numbers() # function call