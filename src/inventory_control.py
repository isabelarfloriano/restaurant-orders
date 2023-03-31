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
            self.inventory[item] -= 1

        self.orders.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        pass
