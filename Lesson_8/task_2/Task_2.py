import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        obj = json.load(f_n)
        obj.get("orders").append({'item': item,
                                  'quantity': quantity,
                                  'price': price,
                                  'buyer': buyer,
                                  'date': date})

    with open('orders.json', 'w') as f_m:
        json.dump(obj, f_m, sort_keys=True, indent=4)


write_order_to_json("monitor", "20", "10000", "Ivanov I.I.", "24.09.2017")
write_order_to_json("headphones", "30", "20000", "Petrov P.P.", "11.01.2018")
