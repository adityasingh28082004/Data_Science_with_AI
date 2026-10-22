# check  weather numbere is  primeor not 
num = int(input("enter the number :"))
if num <= 1:
  print("number is not prime ")
else:
  for i in range (2 , num):
    if num % i == 0:
      print("number is not prime")
      break
  else:
      print("number is  prime")