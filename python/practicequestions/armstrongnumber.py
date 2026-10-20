# check armstrong
# An Armstrong number is a number equal to the sum of its digits,
# each raised to the power of the number of digits.
# the number is known as armstrong if its sum of digits after applying the power 
# equal to the digits is equal to given number
n = int(input("enter the number :"))
original = n
digits = len(str(n))
total = 0
while n > 0:
    digit = n %10 
    total = total+ digit**digits
    n = n//10
if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
