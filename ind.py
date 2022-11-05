#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Вариант 18 (4)

def all_var(arr):
    if len(arr) == 1:
        return [arr]  # терминальная ветвь
    else:
        a = arr[0]  # первый элемент списка
        p = all_var(arr[1:])  # все перестановки хвоста
        r = []  # вставляем a в каждую возможную позицию каждой
        for pp in p:  # перестановки хвоста
            for i in range(len(pp)):
                tmp = pp[0: i] + [a] + pp[i:]
                r.append(tmp)
            r.append(pp + [a])
        return r


if __name__ == '__main__':
    n = int(input("Введите число "))
    print(all_var([i for i in range(1, n + 1)]))