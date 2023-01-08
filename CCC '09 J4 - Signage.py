w = int(input())
currentChar = 7
currentLine = ['WELCOME']
lines = []
outputStr = ''
remain = w
remainWords=

words = ['TO','CCC','GOOD','LUCK','TODAY']

for i in words:
    if i == 'TODAY':
        currentLine.append(i)
        lines.append(currentLine)
    elif currentChar + len(i) + 1<=w:
        currentLine.append(i)
        currentChar += len(i)     
    else:
        lines.append(currentLine)
        currentLine = []
        currentChar = 0

print(lines)

        
    
