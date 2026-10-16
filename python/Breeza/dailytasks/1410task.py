class product():
    def __init__(self , product_id :int,name:str,price:float,quantity:int,category:str):
        self.product_id= product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_product(self):
        print("Product ID :", self.product_id)
        print("Name:", self.name)
        print(f"Price: {self.price:.2f}")
        print("Quantity:", self.quantity)
        print("Category:", self.category)

    def add_to_cart(self,purchase_quantity):
        if self.quantity >= purchase_quantity:
         self.quantity-= purchase_quantity
         print(f"{purchase_quantity} item is added to cart")
         
        else:
          print("No suffcient stock")

    def calculate_total(self, purchase_quantity ,price ):
       total = purchase_quantity * self.price
       return(total)
    
    def apply_discount(self,total ):
      discount_rate = 10 or 5
      if total>= 5000:
         discount_rate =  total*discount_rate/100
      elif total>=2000 :
         discount_rate =total*discount_rate/100
      else:
         print("no discount")
      return(discount_rate) 
product1= product(101,'wireless headphones', 2500, 20, 'electronics')
product1.display_product()
purchase_quantity= 4

product1.add_to_cart(purchase_quantity)

total = product1.calculate_total(purchase_quantity, 2500)

# print("Total amount:", total)
discount = product1.apply_discount(total)

print("Total amount:", total)
print("Discount:", discount)



     
               





        









