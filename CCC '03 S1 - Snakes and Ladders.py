current = 1

while True:
    roll = int(input())
    if roll == 0:
        print("You Quit!")
        break
    if current + roll <= 100:
        current += roll
        if current == 100:
            print("You are now on square 100")
            print("You Win!")
            break
        elif current == 9:
            current = 34
        
        elif current == 40:
            current = 64
          
        elif current == 54:
            current = 19
       
        elif current == 67:
            current = 86

        elif current == 90:
            current = 48
            
        elif current == 99:
            current = 77
    

    print("You are now on square " + str(current))
