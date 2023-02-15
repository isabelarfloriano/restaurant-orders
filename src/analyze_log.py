import csv


path_to_file = 'data/orders_1.csv'

def read_csv_orders(path_to_file):
    all_orders = []
    meals = set()
    week_days = set()
    try:
        with open(path_to_file, 'r') as file:
            read = csv.reader(file)
            for client, dish, day in read:
                all_orders.append({
                    'client': client,
                    'dish': dish,
                    'day': day
                })
                meals.add(dish)
                week_days.add(day)
        return (all_orders, meals, week_days)
    except FileNotFoundError:
        if not path_to_file.endswith('.csv'):
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def most_requested_by_maria(all_orders):
    requests = []
    for order in all_orders:
        if order['client'] == 'maria':
            requests.append(order['dish'])
    return max(requests, key=requests.count)


def qty_hamburguer_by_arnaldo(all_orders):
    count_requests = 0
    for order in all_orders:
        if order['client'] == 'arnaldo' :
            if order['dish'] == 'hamburguer':
                count_requests += 1
    return count_requests


def never_requested_by_joao(all_orders, meals):
    requests = set()
    for order in all_orders:
        if order['client'] == 'joao' :
            requests.add(order['dish'])
    return meals.difference(requests)


def days_joao_never_went(all_orders, week_days):
    days = set()
    for order in all_orders:
        if order['client'] == 'joao' :
            days.add(order['day'])
            print('------', order['day'])
    print(week_days.difference(days))
    return week_days.difference(days)

def analyze_log(path_to_file):
    [all_orders, meals, week_days] = read_csv_orders(path_to_file)
    
    most_requested_by_maria(all_orders)
    qty_hamburguer_by_arnaldo(all_orders)
    never_requested_by_joao(all_orders, meals)
    days_joao_never_went(all_orders, week_days)
    print('fim.')
    # print(all_orders)
    print(meals)
    print(week_days)

analyze_log(path_to_file)