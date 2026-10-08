def display_menu(menu):
  print('-' * 20)
  print('Menu: ')
  print('-' * 20)
  for item in menu.items():
    print(f"{item[0]}: {item[1]}")

def take_order(menu):
    order = {}
    item = input('Enter the item (or done to finish): ').title()

    while item != 'Done':
        if item in menu:
            quantity = int(input(f'Enter the quantity for {item}: '))
            order[item] = quantity
        else:
            print(f'{item} is not in the menu.')

        item = input('Enter the item (or done to finish): ').title()

    return order

def calculate_bill(menu, order):
    total_amount = 0

    for item in order.items():
        item_cost = item[1] * menu[item[0]]
        total_amount += item_cost

    discount = 0
    if total_amount > 1000:
        discount = total_amount * 10 / 100

    return total_amount, discount

def print_bill(menu, order, total_amount, discount, discounted_amount):
    print('-' * 20)
    print('Bill: ')
    print('-' * 20)

    for item in order.items():
        item_cost = item[1] * menu[item[0]]
        print(f"{item[0]} x {item[1]} = {item_cost}")

    print(f'Total Amount: {total_amount}')
    print(f'Discount: {discount}')
    print(f'Discounted Amount: {discounted_amount}')

def main():
    menu = {
        "Idli": 40,
        "Dosa": 60,
        "Vada": 35,
        "Poori": 50,
        "Paneer Butter Masala": 180,
        "Veg Biryani": 150,
        "Chicken Biryani": 220,
        "Fried Rice": 130,
        "Noodles": 120,
        "Manchurian": 140,
        "Gulab Jamun": 60,
        "Ice Cream": 80,
        "Fresh Lime Soda": 50,
        "Coffee": 40,
        "Tea": 30
    }

    display_menu(menu)

    c_order = take_order(menu)

    total_amount, discount = calculate_bill(menu, c_order)

    discounted_amount = total_amount - discount

    print_bill(menu, c_order, total_amount, discount, discounted_amount)

main()  