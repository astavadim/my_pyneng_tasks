# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input("Enter ip address: ")
octets = ip_address.split(".")
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Неправильный IP-адрес")
else:
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

