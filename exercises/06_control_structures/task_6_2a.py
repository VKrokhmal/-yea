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
ip_address = input("введите ip-адрес: ")
conv = ip_address.split(".")
correct_addr = True

if len(conv) != 4:
    correct_addr = False
else:
    for x in conv:
        if not (x.isdigit() and int(x) in range(256)):
            correct_addr = False
            break
if not correct_addr:
    print('Неправильный IP-адрес')
else:
    oct1 = int(ip_address.split(".")[0])

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



