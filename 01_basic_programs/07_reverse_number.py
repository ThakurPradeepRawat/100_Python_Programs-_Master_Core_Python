"""
Program: Reverse number
Author: Pradeep Rawat
Description: Take a number as input from user than reverse it .
"""
def reverse_number(num):
    reverse_num = 0
    while(num>0):
        rem = num%10
        reverse_num = reverse_num*10 + rem
        num = num//10
    return reverse_num
# user input 
num = int(input("Enter a number :- "))
print("Number = " , num)
print("Reverse number = {}" .format(reverse_number(num)))