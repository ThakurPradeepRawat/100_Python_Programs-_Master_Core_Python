"""
Program: largest of three number
Author: Pradeep Rawat
Description: find the largest number from three numbers .
"""
def largest_three(num1,num2,num3):
    if num1>=num2 and num1>num3 :
        return num1
    elif num2>num1 and num2>=num3:
        return num2 
    elif num3>num2 and num3>=num1 :
        return num3 
    else :
        return "All numbers are equal "
a, b,c = map(int,input("Enter three numbers :- ") .split())
print("Max of {} , {} and {}  is {}" .format(a,b,c,largest_three(a,b,c)))
    