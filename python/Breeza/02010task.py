name = input("Enter student name: ")
city = input("Enter city: ")
course = input("Enter course name: ")
fee = float(input("Enter monthly fee (INR): "))
months = int(input("Enter number of months: "))
discount = float(input("Enter discount (%): "))
total_fee = fee * months
discount_amount = total_fee * discount / 100
final_amount = total_fee - discount_amount
gst = final_amount * 18 / 100
grand_total = final_amount + gst



print("==============================")
print("DATAVALLEY ENROLLMENT RECIEPT ")
print("==============================")
print("student   : ", name)
print("city      :", city)
print("course    :", course)
print("------------------------------")
print("monthly fee :" , fee)
print("duration    :", months )
print("total fee   :" , total_fee)
print(f"discount    : {discount_amount}({discount}%) ")
print(f"after discount : {final_amount}")
print(f"GST (18%)    : {gst}")
print("------------------------------")
print(f"GRAND TOTAL    : {grand_total}")
print("==============================")