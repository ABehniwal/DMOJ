lowest = 201
lowestCity = ''

city = ''

while city != "Waterloo":
    city,temp = input().split()
    if int(temp) < lowest:
        lowest = int(temp)
        lowestCity = city

print(lowestCity)
    
