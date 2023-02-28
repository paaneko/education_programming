s = input('Введіть рядок: ')
words = s.split()

print('Список слів, довжина яких більше за 3:')
for w in words:
    if len(w.strip(',.;:!?"\' ')) > 3:
        print(w.strip(',.;:!?"\' '))