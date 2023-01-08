def cnvrt_dcml_to_bnry(num):
    ''' Converts a number from decimal to binary '''
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        power = 0
        while (2**power) <= num:
            power += 1
        power -= 1
        
        return 10**power + cnvrt_dcml_to_bnry(num-(2**power))
        
n = int(input())

for i in range(n):
    string = str(cnvrt_dcml_to_bnry(int(input())))
    if len(string) % 4 != 0:
        string = str(0)*(4 - (len(string) % 4)) + string
    output = ''
    if len(string) == 4:
        print(string)
    else:
        for i in range(0,len(string)-3,4):
            output += string[i:i+4] + ' '
        output.strip()
        print(output)
        
