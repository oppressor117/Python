import csv
import re


def write_to_csv(path_to_csv):
    main_data = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
    print(main_data)
    with open(path_to_csv, "w") as file:
        writer = csv.writer(file)
        writer.writerows(main_data)


def get_data(file_list):
    parse_parameters = (re.compile(r'Изготовитель системы:.*'),
                        re.compile(r'Название ОС:.*'),
                        re.compile(r'Код продукта:.*'),
                        re.compile(r'Тип системы:.*'))
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    print(file_list)
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in file_list:
        with open(file_name, "r", encoding="windows-1251") as file:
            text = file.read()
            os_prod_list.append(parse_parameters[0].findall(text)[0].split(':')
                                [1].lstrip())
            os_name_list.append(parse_parameters[1].findall(text)[0].split(':')
                                [1].lstrip())
            os_code_list.append(parse_parameters[2].findall(text)[0].split(':')
                                [1].lstrip())
            os_type_list.append(parse_parameters[3].findall(text)[0].split(':')
                                [1].lstrip())

    for key in range(len(file_list)):
        main_data.append([os_prod_list[key], os_name_list[key],
                          os_code_list[key], os_type_list[key]])
    return main_data


write_to_csv('my_data_report.csv')