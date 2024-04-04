# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip_address = input("Введите адрес: ")
    octets = ip_address.split(".")
    correct_ip = True

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                correct_ip = False
                break
    else:
        correct_ip = False
    if correct_ip:
        break
    print("Неправильный IP-адрес")
first_octets = int(ip_address.split('.')[0])
if ip_address == '0.0.0.0':
    print('unassigned')
elif ip_address == '255.255.255.255':
    print('local broadcast')
elif (first_octets >= 1 and  first_octets <= 223):
    print('unicast')
elif first_octets >= 224 and  first_octets <= 239:
    print('multicast')
else:
    print('unused')