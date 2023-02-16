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
        requests = set()
        customer_requests = set()
        for order in self.orders:
            if order['client'] == customer:
                customer_requests.add(order['dish'])
            requests.add(order['dish'])
        return requests.difference(customer_requests)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        customer_days = set()
        for order in self.orders:
            if order['client'] == customer:
                customer_days.add(order['day'])
            days.add(order['day'])
        return days.difference(customer_days)

    def get_busiest_day(self):
        days = {}
        busiest_day = self.orders[0]['day']
        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1
            if days[order['day']] > days[busiest_day]:
                busiest_day = order['day']
        return busiest_day

    def get_least_busy_day(self):
        days = {}
        least_day = self.orders[0]['day']
        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1
            if days[order['day']] < days[least_day]:
                least_day = order['day']
        return least_day
