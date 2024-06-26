# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = [
"Prefix                {}",
"AD/Metric             {}",
"Next-Hop              {}",
"Last update           {}",
"Outbound Interface    {}",
]
with open('ospf.txt', 'r') as f:
    for line in f:
        line_list = line.split()
        prefix = line_list[1]
        ad = line_list[2]
        nexthop = line_list[4]
        lastupdate = line_list[5]
        intf = line_list[-1]
        #print(f"Prefix {prefix:>27}\nAD/Metric {ad.strip('[]')}")
        print('\n'.join(result).format(prefix,ad.strip('[]'),nexthop.strip(','),lastupdate.strip(','),intf))