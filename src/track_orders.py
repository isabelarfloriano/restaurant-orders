class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append({
            'client': customer,
            'dish': order,
            'day': day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        requests = []
        for order in self.orders:
            if order['client'] == customer:
                requests.append(order['dish'])
        return max(requests, key=requests.count)

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
