def check_cycle(node):
    ''' Checks if there is a path '''
    global visited
    visited[node] = True
    
    for vertex in graph[node]:
        if visited[vertex]:
            return False
        if not check_cycle(vertex):
            return False
    visited[node] = False
    return True

numStudents = int(input())
numConnections = int(input())
graph = [[] for i in range(numStudents+1)]
visited = [False for i in range(numStudents+1)]

possible = True

for i in range(numConnections):
    stu1,stu2 = map(int,input().split())
    graph[stu1].append(stu2)

for i in range(1,numStudents+1):
    if not check_cycle(i):
        possible = False
        break
    
if possible:
    print("Y")
else:
    print("N")

