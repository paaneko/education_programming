s = str(input('Enter a string: '))
words = s.split()
result = []
for word in words:
    word = word.strip('.,!?:;-')
    if len(word) % 2 == 0 and word[0].isdigit():
        result.append(word)
print('Words of even length that start with a digit:')
print(result)