# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
conf = argv[1]

ignore = ["duplex", "alias", "configuration"]

f = open(conf, 'r')
f.seek(0)
for line in f:
    line_list = line.split()
    for word in ignore:
        if word in line_list:
            break
        elif line.startswith('!'):
            break
    else:
        print(line.strip('\n'))
