# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо
    выполнить на этом интерфейсе
    """
    trunk_config = []
    intf_config = {}
    vlans_str = []
    for intf, vlan in intf_vlan_mapping.items():
        #trunk_config.append(f"interface {intf}")
        #intf_config[intf] = None
        vlans_str = []
        for vlan_str in vlan:
            vlans_str.append(str(vlan_str))
        vlans_str = ','.join(vlans_str)
        #print(f"interface {intf}")
        command_list = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                command_list.append(f"{command} {vlans_str}")
                #print(f"{command} split({vlan})")
            else:
                command_list.append(command)
                #print(command)
        intf_config[intf] = command_list
    return intf_config

print(generate_trunk_config(trunk_config, trunk_mode_template))
