def fibonacci(n): #Функция возвращающая массив из n чисел фибоначчи
    a,b = 1,0
    arr = []
    for i in range(n):
        a, b = b, a+b
        arr += [str(a)]
    return arr

def naive(line = '', findLine = ''): #Наивный поиск - просто проход по всей длинне и break при ошибке
    lenLine = len(line)
    lenFindline = len(findLine)
    counter = 0
    for i in range(lenLine - lenFindline + 1):
        flag = True
        for j in range(lenFindline):
            if line[i+j] != findLine[j]:
                flag = False
                
                break
            
                
        if flag == True:        
            counter += 1

    return counter

def hash(a=0,b=0,line=''): #Хэш-функция (может быть любой, но от нее зависит эффективность алгоритма)
    hashstr = ''
    for i in line[a:b]:
        hashstr += str(ord(i))
    return int(hashstr)

def RabinCarp(line = '', findLine = ''): #Сравнивает хэш строк, после чего идет наивный поиск
    counter = 0
    lenLine = len(line)
    lenFindline = len(findLine)
    for i in range(lenLine-lenFindline+1):
        flag = True
        hashLine = hash(i,i+lenFindline,line)
        hashFind = hash(0,lenFindline,findLine)
        if hashLine == hashFind:
            for j in range(lenFindline):
                if line[i+j] != findLine[j]:
                    flag = False
                    break   
            if flag == True:        
                counter += 1
    return counter 

def BoyerMoore(line='', findline=''): #
    lenLine = len(line)
    lenFindLine = len(findline)
    counter = 0
    skip = 0
    for i in range(0,lenLine-(lenFindLine-1)):
        if skip > 0: #Сдвиг (возможно более удачная реализация c помощью while, вместо for)
            skip -= 1
            continue
        a = line[i:i+lenFindLine] #Срез
        error,skip = predproc(a,findline) #Сама проверка справа налево, возвращающая результат проверки и сдвиг 
        if error == True: counter += 1 #Если ошибок не было, то увеличиваем счетчик
    return counter
        
def predproc(a,b):
    if a: #Если не пустой идет рекурсия, иначе все число пройдено
        if a[-1] == b[-1]: #Проверка правых букв, если равны, то в рекурсию
            t = predproc(a[:-1],b[:-1])
            if t[0] == False:
                return False,t[1] #Возвращение по рекурсии с индексом буквы
            else:
                return True,t[1] #Возвращение без ошибки
        else: return False,b.rfind(a[-1]) #Если буквы не сошлись - возвращает индекс буквы в оставшейся части шаблона 
    return True, 0

def prefix(s):
    arr = [0]*len(s)
    for i in range(2,len(s)+1): #Префикс-функция(1) = 0, поэтому сразу начинаем с 2
        news = s[:i]
        k = 0
        for j in range(len(news)):
            if news[:j+1] == news[-1-j:] and j+1 != len(news):
                k = j+1 #Длина префикса
        arr[i-1] = k
    return arr

def KMP(line,findline):      
    p, l = len(findline), len(line) #Длины строк
    i, j = 0, 0 #Индексы
    counter = 0 
    pi = prefix(findline) #Вычисление префикса шаблона
    while i < l: 
        if line[i] == findline[j]:
            i += 1
            j += 1
            if j == p: #Схожая строка
                counter += 1
                j = 0
        else:
            if j > 0:
                j = pi[j - 1] #Сдвиг
            else:
                i += 1

    return counter
        