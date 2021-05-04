# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ips = input("Please enter your IP:" )
    ans = ips.split(".")
    corr = True

    if len(ans) == 4:
        for x in ans:
            if not (x.isdigit() and int(x) in range(256)):
                corr = False
                break
    else:
        corr = False
    if corr:
        break
    print('Неправильный IP-адрес')

oct1 = int(ips.split(".")[0])

if 1 <= oct1 <=223:
    print('unicast')
elif 224 <= oct1 <= 239:
    print('multicast')
elif oct1 == 255:
    print('local broadcast')
elif oct1 == 0:
    print('unassigned')
else:
    print('unused')

