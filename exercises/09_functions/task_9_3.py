# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):

    access = {}
    trunk = {}

    with open(config_filename, "r") as f:
        for line in f:
            if line.startswith("interface"):
                line_list = line.split()
                intf = line_list[-1]
                #intf_dict = access.setdefault(intf)
                #print (intf)
            elif "switchport access vlan" in line:
                line_list = line.split()
                vlan = line_list [-1]
                access[intf] = int(vlan)
            elif "switchport trunk allowed vlan" in line:
                #line_list = line.split()
                #vlans = line_list[-1].split(',')
                #vlans_int = []
                #for vl in vlans:
                #    vlans_int.append(int(vl))
                #trunk[intf] = vlans_int
                trunk[intf] = [int(vl) for vl in line.split()[-1].split(',')]
    return (access, trunk)

print(get_int_vlan_map('config_sw1.txt'))
