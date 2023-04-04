import yaml

dict_yaml = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
             'items_price': {'computer': '200€-1000€', 'printer': '100€-300€', 'keyboard': '5€-50€', 'mouse': '4€-7€'},
             'items_quantity': 4}

with open('file.yaml', 'w') as f_n:
    yaml.safe_dump(dict_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f:
    obj = yaml.safe_load(f)
print(obj)
