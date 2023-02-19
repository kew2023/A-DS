from metods import KMP
import wikipedia
import pypandoc
def delcp(x):
    arr = ",<>.[]?!/*&^%$@()_-=+:;"
    for i in arr:
        x = x.replace(i, ' ')
    while "  " in x:
        x = x.replace("  ", " ")
    return x
#Конвертация текста из докс в тхт
essay = pypandoc.convert_file('Рентгеновское излучение.docx', 'plain').lower() #Убираем заглавные буквы
srttest = delcp(essay) #Убираем спецсимволы
arrref = srttest.split() #Общее кол-во слов в реферате
newset = []
for i in range(len(arrref)-2):
    if (arrref[i],arrref[i+1],arrref[i+2]) not in newset: newset.append((arrref[i],arrref[i+1],arrref[i+2]))
mainset = newset #Получение массива уникальных 3-х слов подряд

wikipedia.set_lang("ru") #Язык wiki
origin = wikipedia.page("Рентгеновское излучение").content.lower() #Убираем заглавные буквы с страницы полученной с wiki
srttest = delcp(origin) #Убираем спецсимволы
arrwiki = srttest.split() #Общее кол-во слов в wiki
newset = []
for i in range(len(arrwiki)-2):
    if (arrwiki[i],arrwiki[i+1],arrwiki[i+2]) not in newset: newset.append((arrwiki[i],arrwiki[i+1],arrwiki[i+2]))
patternset = newset #Получение массива уникальных 3-х слов подряд

#Словарь кол-ва символов для каждого сочетания 3-х слов по формуле (Кол-во повторов * кол-символов)
dict = {}
for pattern in patternset:
    dict[' '.join(pattern)] = (KMP(arrref, pattern)*(len(' '.join(pattern))),len(pattern[0])+1,len(pattern[1])+1,len(pattern[2]))


k = 0
dictval = list(dict.values())
last = dictval[0]
k = last[0]
#Исключение ситуации, когда в "ABCD" считались плагиатом "ABC" и "BCD"
for j in range(1,len(dictval)):
    if last[0] != 0:
        k += (dictval[j][0] - (last[1]+last[2]+1))
    else:
        k += dictval[j][0]
    last = dictval[j]
print(k / len(essay)  * 100, "%")