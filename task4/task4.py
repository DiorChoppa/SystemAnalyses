from io import StringIO
import math
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    for i in graph:
        for j in i:
            j = int(j)
    # 1
    arr1 = []
    for i in graph:
        arr1.append(i[0])
    # 2
    arr2 = []
    for i in graph:
        arr2.append(i[1])
    # 3
    f = graph
    g = graph
    arr3 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] == g[j][0]:
                arr3.append(f[i][0])
    # 4
    arr4 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][1]:
                arr4.append(f[i][1])
    # 5
    arr5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][0]:
                arr5.append(f[i][1])

    result = []
    edges = []
    for x in graph:
        for y in x:
            if y not in edges:
                edges.append(y)
    edges.sort()

    for v in edges:
        result.append([])
    
    for v in edges:
        result[int(v)-1].append(arr1.count(v))
        result[int(v)-1].append(arr2.count(v))
        result[int(v)-1].append(arr3.count(v))
        result[int(v)-1].append(arr4.count(v))
        result[int(v)-1].append(arr5.count(v))

    s = 0
    for j in range(len(edges)):
        for i in range(5):
            if result[j][i] != 0:
                s += (result[j][i] / (len(edges) - 1)) * math.log(result[j][i] / (len(edges) - 1), 2)

    return -s