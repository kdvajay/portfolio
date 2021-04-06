class customer:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.purchases = []
        
    def purchase(self,inventory,product):
        inventory_dict=inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product]>0:
                self.purchases.append(product)
                inventory_dict[product]-=1
            else:
                print('we are out of stock')
        else:
            print('we dont have that product')
            
    def print_purchases(self):
        print("the customer has purchased")
        for item in self.purchases:
            print(item.name)
        

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
        
class inventory:
    def __init__(self):
        self.inventory={}
        
    def add_product(self,product,quantity):
        if product not in self.inventory:
            self.inventory[product]=quantity
        else:
            self.inventory[product]+=quantity
            
    def print_inventory(self):
        for key,value in self.inventory.items():
            print(key.name + ':' +str(value))
        print()
        
        
        

customer1 = customer('joe','joe@gmail.com')
#print(customer1.name)
#print(customer1.email)

apple_watch = product('Apple Watch', 299)
#print(apple_watch.name)
#print(apple_watch.price)

mac = product('Mac', 1999)
#print(mac.name)
#print(mac.price)

inventory1 = inventory()
inventory1.add_product(apple_watch,100)
#inventory.print_inventory()
inventory1.add_product(mac, 498)

inventory1.print_inventory()
customer1.purchase(inventory1,apple_watch)
customer1.purchase(inventory1,mac)
inventory1.print_inventory()
customer1.print_purchases()
