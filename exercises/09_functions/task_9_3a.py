# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):

    access = {}
    trunk = {}

    with open(config_filename, "r") as f:
        for line in f:
            if line.startswith("interface Fast"):
                line_list = line.split()
                intf = line_list[-1]
                access[intf] = 1
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
                del access[intf]
            #elif "switchport mode access" in line:
            #
    access[intf] = 1
    return (access, trunk)

print(get_int_vlan_map('config_sw2.txt'))
