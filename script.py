from datetime import time

#Making the Menus

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{name} menu available from {start} to {end}".format(name = self.name, start = self.start_time, end = self.end_time)
    
    def calculate_bill(self, purchased_items):
        subtotal = 0
        for item in purchased_items:
            subtotal += self.items.get(item,0)
        return subtotal


brunch = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11), time(16))

early_bird = Menu("Early-bird Dinners", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, time(15), time(18))

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, time(17), time(21))

kids = Menu("Kids'", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11), time(21))

#print(brunch)
#print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#Creating the Franchises

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address
    def available_menus(self, time):
        available_list = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_list.append(menu)
        return available_list

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#print(flagship_store)
#print(flagship_store.available_menus(time(12)))
#print(flagship_store.available_menus(time(17)))

# Creating Businesses !

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

takeaarepa = Business("Take a' Arepa", arepas_place)