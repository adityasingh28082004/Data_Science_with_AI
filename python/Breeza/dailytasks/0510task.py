customer_age = int(input("enter customer age :"))
is_customer_a_member = input("is customer a member :")
day_type = input("enter day type :")

if customer_age > 10:
    print("free ticket")
elif is_customer_a_member == "yes":
    print("20%"+ "discount")
elif day_type == "weekday":
    print("30%'"+ " discount")

    print("no discount") 
    