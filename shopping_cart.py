# Product-- Name, Price, Stock
# Customer-- Name
# CartItems-- Product, Quantity
# Cart-- User, CartItems
# Payment Method-- Credit Card, Bkash, Paypal

# Creating Product Class
class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.__stock = stock
    
    def __str__(self):
        return f"{self.name}-{self.price}tk-{self.__stock}"

# Creating Customer Class
class Customer:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
    
# Cartitem
class CartItems:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity

# Cart
class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []

    def add_to_cart(self,product,quantity):
        self.cart.append(CartItems(product,quantity))

    def calculate_total(self):
        total_price = 0

        for item in self.cart:
           total_price += item.get_total_price()
        
        return total_price

    def display_cart(self):
        print(f'Shopping cart of {self.customer}')

        for item in self.cart:
            print(f"{item.product.name} x {item.quantity} - {item.get_total_price()}tk")        
        
        print(f"Total: {self.calculate_total()}tk")


from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay():
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount}tk using Credit Card")

class Bkash(Payment):
    def pay(self,amount):
        print(f"Paid {amount}tk using Bkash")



laptop = Product('Laptop', 60000, 10)
phone = Product('Android', 25000, 20)

customer_name = input()
name = Customer(customer_name)

name_cart = Cart(name)

name_cart.add_to_cart(laptop,1)
name_cart.add_to_cart(phone,2)

name_cart.display_cart()

credit_card = CreditCard()
credit_card.pay(name_cart.calculate_total())

# bkash = Bkash()
# bkash.pay(name_cart.calculate_total())


