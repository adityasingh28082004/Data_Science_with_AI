orders = [
    {'order_id': 'ORD101', 'customer': 'Aarav Sharma', 'city': 'Hyderabad', 'price': 1499, 'quantity': 2},
    {'order_id': 'ORD102', 'customer': 'Priya Reddy', 'city': 'Bengaluru', 'price': 799, 'quantity': 1},
    {'order_id': 'ORD103', 'customer': 'Rohit Iyer', 'city': 'Chennai', 'price': 2999, 'quantity': 3},
    {'order_id': 'ORD104', 'customer': 'Ananya Patel', 'city': 'Mumbai', 'price': 499, 'quantity': 5},
    {'order_id': 'ORD105', 'customer': 'Vikram Nair', 'city': 'Kochi', 'price': 1299, 'quantity': 1},
    {'order_id': 'ORD106', 'customer': 'Sneha Gupta', 'city': 'Delhi', 'price': 3499, 'quantity': 2},
    {'order_id': 'ORD107', 'customer': 'Karthik Rao', 'city': 'Hyderabad', 'price': 999, 'quantity': 4},
    {'order_id': 'ORD108', 'customer': 'Divya Singh', 'city': 'Pune', 'price': 1799, 'quantity': 1}],
    
def calculate_discount(total):
    discount =0
    if total >= 10000:
        discount= 15
    elif total >= 5000 and total <=9999:
        discount = 10
    elif total >= 2000  and total <=4999:
                discount = 5
    return total * discount/100

print(calculate_discount(10000))
print(calculate_discount(8000))
print(calculate_discount(4000))
print(calculate_discount(1500))
