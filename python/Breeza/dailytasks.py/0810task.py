numbers = [8,7,10,4,5,6,8,9]
#largest = max(numbers)
#print(largest)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest value:", largest)
    

