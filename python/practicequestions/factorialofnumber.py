# factorial of number
# The factorial of a positive integer is the product of all integers from 1 up to that number.
n = int(input("enter the number :"))
fact = 1 
for i in range (1 , n+1 ):
    fact = fact * i
print("factorial :", fact)
