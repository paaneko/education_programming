s = str(input('Введіть рядок: '))
l = list(s.split())
print('Список слів, утворених з рядка:')
print(l)
print('Список слів, довжина яких більша за 3:')
for w in l:
    if len(w)>3:
        print(w)