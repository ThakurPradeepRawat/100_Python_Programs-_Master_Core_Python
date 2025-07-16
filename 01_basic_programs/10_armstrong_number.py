"""
Program: Armstrong number
Author: Pradeep Rawat
Description: This program takes a number as input from the user and checks if it is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits.
Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
"""
def armstrong(num):
    temp = num
    len_num = len(str(num))
    total_sum = 0 
    while(num>0):
        last_digit = num%10 
        total_sum = total_sum + last_digit**len_num
        num = num//10
    if total_sum == temp :
        return "a armstrong number "
    else:
        return "not a armstrong number"
# main program 
num = int(input("Enter number to check weather is it armstrong or not :"))
print("{} is {} " .format(num, armstrong(num)))

