#Метод деления
s = input('Ввод строки: ')
news = []
for i in s:
    news += [ord(i)]
key = ord('я') + 1
for i in range(len(news)):
    news[i] = hex(key % news[i])[2:].zfill(2)
print(' '.join(news))
