# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
list_words = []

vl = input('Введите номер влан: ')
vl = int(vl)

with open("CAM_table.txt") as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            list_words.append([int(vlan), mac, interface])
            list_words.sort()
for vlan, mac, interface in list_words:
    if vl == vlan:
        print(f"{vlan:<9}{mac:20}{interface}")