""" Program: Fibonacci Series
 Author: Pradeep Rawat (Revised for efficiency)
 Description: Take a number as an input from the user and print the Fibonacci series up to that many terms.
"""
def print_fibonacci_series(count):
    #Calculates and prints the Fibonacci series in one go.
    a, b = 0, 1  # Initialize the first two numbers

    if count <= 0:
        print("Please enter a positive number.")
        return 

    print("Fibonacci series :- ")
    for i in range(count):
        print(a, end=" --> ")
        # Calculate the next term in the series
        c = a + b
        # Update the values for the next loop
        a = b
        b = c

# --- Main Program ---

num = int(input("Enter the number of terms to print: "))
print_fibonacci_series(num)
