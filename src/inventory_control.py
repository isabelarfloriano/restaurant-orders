from track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = TrackOrders()
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, customer, order, day):
        ingredients = self.INGREDIENTS[order]
        for item in ingredients:
            if self.inventory[item] == 0:
                return False
            self.inventory[item] -= 1
        self.orders.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        ingredients_to_buy = {}
        for item, qtd in self.inventory.items():
            qtd_to_buy = self.MINIMUM_INVENTORY[item] - qtd

            if qtd_to_buy > 0:
                ingredients_to_buy[item] = qtd_to_buy
            else:
                ingredients_to_buy[item] = 0

        return ingredients_to_buy

    def get_available_dishes(self):
        dishes_available = set()

        for dish, items in self.INGREDIENTS.items():
            if all(self.inventory[items] > 0
                    for item in items):
                dishes_available.add(dish)

        return dishes_available
