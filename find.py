def depth(graph, start, end, way = [], visited = set()):
    visited.add(start)
    way.append(start)

    #print(way,start) 
    if start == end: return way
    #print(start,visited)
    for next in graph[start]:
        #print("Предполагаемый путь :",start,next,visited)

        if next not in visited:
            #print("Путь :",start,next,visited)
            print(start,next,way)
            t = depth(graph, next, end, way, visited)
            #print(start,next,t,'t') #
            if t: #- /
                return way
    way.pop()
    return False

graf = {
    "A" : ['B','C'],
    "B" : ['A','D','E','F'],
    "C" : ['A','G','H'],
    "D" : ['B'],
    "E" : ['B'],
    "F" : ['B'],
    "G" : ['C'],
    "H" : ['C']
}

print('Поиск в глубину')
t = depth(graf, 'A','H')
print(t)
print('\n')
