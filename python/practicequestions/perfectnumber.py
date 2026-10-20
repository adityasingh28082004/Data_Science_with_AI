# check perfect number
# A perfect number is a number equal to the sum of its positive factors, excluding the number itself.
n = int(input("enter the number :"))
total = 0 
for i in range (1 , n):
    if n % i == 0 :
        total = total +i
if total == n :
     print("perfect number")
else:
       print("not perfect number")


    

