def create_orders(customer_name, restaurant_name, total_amount, **extra_details):
    print("Customer:", customer_name)
    print("Restaurant:", restaurant_name)

    if extra_details.get("is_new_customer") == True:
        coupon = "WELCOME50"
        total_amount -= 50
        print("Coupon:", coupon, "-₹50")

    if "tip" in extra_details:
        total_amount += extra_details["tip"]
        print("Tip: ₹", extra_details["tip"])

    print("Other details:")
    for key, value in extra_details.items():
        if key not in ["is_new_customer", "tip"]:
            print(key, ":", value)

    print("Final amount: ₹", total_amount)
    return total_amount

      
create_orders(
    "Aditya",
    "Vrindavan",
    300,
    is_new_customer=True,
    tip=20,
    drink="tea"
)
