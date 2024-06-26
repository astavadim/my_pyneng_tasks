# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

filename = argv[1]
filename_out = argv[2]
#filename = 'config_sw1.txt'
#filename_out = 'config_sw1_out.txt'

with open(filename) as f, open(filename_out, 'a') as f_out:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            f_out.write(line)
                #f_out.writelines(line.rstrip() + '\n')
    else:
        f_out.close()


            #print(line.rstrip())
