orders =      [
    {'order_id': 'ORD101', 'customer': 'Aarav Sharma', 'city': 'Hyderabad', 'price': 1499, 'quantity': 2},
    {'order_id': 'ORD102', 'customer': 'Priya Reddy', 'city': 'Bengaluru', 'price': 799, 'quantity': 1},
    {'order_id': 'ORD103', 'customer': 'Rohit Iyer', 'city': 'Chennai', 'price': 2999, 'quantity': 3},
    {'order_id': 'ORD104', 'customer': 'Ananya Patel', 'city': 'Mumbai', 'price': 499, 'quantity': 5},
    {'order_id': 'ORD105', 'customer': 'Vikram Nair', 'city': 'Kochi', 'price': 1299, 'quantity': 1},
    {'order_id': 'ORD106', 'customer': 'Sneha Gupta', 'city': 'Delhi', 'price': 3499, 'quantity': 2},
    {'order_id': 'ORD107', 'customer': 'Karthik Rao', 'city': 'Hyderabad', 'price': 999, 'quantity': 4},
    {'order_id': 'ORD108', 'customer': 'Divya Singh', 'city': 'Pune', 'price': 1799, 'quantity': 1}]

def get_order_list_from_city(order_list,city):
    order_ids = []
    for order in order_list:
     if order["city"] == city:
        order_ids.append (order["order_id"])
    return order_ids
result= get_order_list_from_city(orders,"Hyderabad")
print(result)
    