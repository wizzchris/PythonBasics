"""
Restaurant owner that only does takeaway
As a restaurant owner I can create food items
As the restaurant owner I can create new customers
As a restaurant owner I can create new orders with food items and a customer
"""

#People Class
class People:
    def __init__(self,name):
        self.name = name

class Worker(People):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

class Customer(People):
    def __init__(self,name, alargy_ingredients, address = None):
        super().__init__(name)
        if address == None:
            self.address = []
        self.__payment_details = {}
        self.alergy_ingredients = alargy_ingredients

    def add_payment_details(self,address, card_num):
        self.__payment_details['address'] = address
        self.__payment_details['card num'] = card_num

    def send_payment_details(self):
        return self.__payment_details

customers = []
james = Customer('James', None, '21 Down Town Abi, London')
customers.append(james)
john = Customer('John', 'Peanuts', 'Hackney, London')
customers.append(john)


#Food Class

class Food_Items:
    def __init__(self, item, price, ingredients = None):
        self.item = item
        self.price = price
        if ingredients == None:
            ingredients = []
        self.ingredients = ingredients

class Side(Food_Items):
    pass

class Main(Food_Items):
    pass

class combos(Food_Items):
    def __init__(self,item,price,list_individual_items = None, ingredients = None):
        super().__init__(item,price,ingredients)
        if list_individual_items == None:
            list_individual_items = []
        self.list_individual_item = list_individual_items

#Food Items
#3 mains, 3 sides, 3 drinks, 3 combos
food_items = []
main1 = Food_Items('Sea Bass', 17.50, ['Fish'])
food_items.append(main1)
main2 = Food_Items('Omelet de Formage Avec Champignon', 9, ['Eggs', 'Cheese', 'Mushrooms'])
food_items.append(main2)
main3 = Food_Items('Fiorentina', 5.50, ['Tomato Sauce', 'Mozzarella', 'Spinich'])
food_items.append(main3)

side1 = Food_Items('Garlic Bread', 4, ['Bread', 'Garlic', 'Oregano'])
food_items.append(side1)
side2 = Food_Items('Garlic Bread With Cheese', 4, ['Bread', 'Garlic', 'Oregano', 'Cheese'])
food_items.append(side2)

drink1 = Food_Items('Water', 2, ['Water'])
food_items.append(drink1)
drink2 = Food_Items('Coke', 3, ['Suger', 'Water', 'Other'])
food_items.append(drink2)
drink3 = Food_Items('Smoothie', 4, ['Orange', 'Carrot', 'Kiwi'])
food_items.append(drink3)

#Orders Class

class Order():
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.status = 'Open'

    def add_items_order(self, item):
        self.items.append(item)
        #Have a method to calc total

#User story
orders = []
order1 = Order(john)
orders.append(order1)
order1.add_items_order(main3)
order1.add_items_order(drink3)

print(order1)
print(order1.items)
for item in order1.items:
    print (item.item, f'${item.price}')

#We want a game to keep running with following options
#As a user i can create a customer
#As a user I can create a food item
#As a user I can list food items
#As a user I can create orders
# As a user I can add items to order
#As a user I can see the total of an order

while True:
    answer = input('Hello, welcome to the nice resturant.\n What would you like to do?\n Type HELP for help and Exit to exit\n').strip().lower()
    if answer == 'help':
        print('The commands are\nHelp for Help\nExit for Exit\nCreate Customer for a new customer\nList Food to list food avilable\nCreate Order\nAdd Item to add item to order\nTotal for total cost')
    elif answer == 'exit':
        break
    elif answer == 'create customer':
        name = input('What is the name of the customer?')
        alargy = input('Any alargys?')
        address = input('What is the address')
        name = Customer(name,alargy,address)
        customers.append(name)


    elif answer == 'list food':
        for food in food_items:
            print(food.item + ' £'+ food.price)


    elif answer == 'create order':
        for customer in customers:
            print(customer.name)
        cust = input('What customer do you want to create an order for?')
        for customer in customers:
            if cust == customer.name:
                cust = Order(customer)
                orders.append(cust)


    elif answer == 'add item':
        for ord in orders:
            print(ord.customer.name)
        ordernum = input('Please pick the order')
        for ord in orders:
            if ordernum == ord.customer.name:
                item = input('What item do you want to add?')
                for food in food_items:
                    if item == food.item:
                        ordernum.add_items_order(food)

    elif answer == 'total':
        ordernum = input('What order do you want to check?')
        for ord in orders:
            if ordernum == ord.customer.name:
                total = 0
                for item in ord.items:
                    total += item.price
                print(total)
























