import csv


path_to_file = 'data/orders_1.csv'

def read_csv_orders(path_to_file):
    all_orders = []
    meals = set()
    week_days = set()
    try:
        with open(path_to_file, 'r') as file:
            read = csv.reader(file)
            for client, order, day in read:
                all_orders.append({
                    client,
                    order,
                    day
                })
                meals.add(order)
                week_days.add(day)
        return (all_orders, meals, week_days)
    except FileNotFoundError:
        if not path_to_file.endswith('.csv'):
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    data = read_csv_orders(path_to_file)
    print(data[0])
    print(data[2])
    print(data[1])
    print('fim.')

analyze_log(path_to_file)