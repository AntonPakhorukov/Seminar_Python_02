# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# РЕШЕНИЕ 1: ==========================================================================================================================

# n = int(input('Введите натуральное число: '))
# d = dict() # Словарь dict
# for i in range(1, n + 1):
#     d[i] = 3 * i + 1
# for k, v in d.items():
#     print(f'{k}: {v}', end=', ')
   

# РЕШЕНИЕ 2: ==========================================================================================================================

# a = int(input('Введите число: '))
# d = {a: (3*a)+1 for a in range(1, a+1)} # создается словарь 
# print(d)

# РЕШЕНИЕ 3: ==========================================================================================================================

some_dict = {}
n = int(input())
for i in range(1, n + 1):
    some_dict[i] = 3 * i + 1
print(some_dict)




# d = {a: (3*a)+1 for a in range(1, a+1)}
# print(d)
