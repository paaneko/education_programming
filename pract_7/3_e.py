s = str(input('Введіть рядок: '))
l = list(s.split(' '))

ll = []
for sl in l:
    w = sl.strip(':;.,!?')
    if w != '':
        ll.append(w)

print('Список слів, у яких перша і остання літери однакові:')
for w in ll:
    if len(w) > 1 and w[0] == w[-1]:
        print(w)