"""
Program: swap two number
Author: Pradeep Rawat
Description: Take two number as a input from user and swap these numbers without using third variable.
"""
a , b = map(int , input("Enter Two number :- ") .split())
print("Withot swapping numbers are :- {}   ,   {} " .format(a,b))
a= a^b 
b=a^b 
a= a^b 
print("after swapping numbers are :- {}   ,   {} " .format(a,b))