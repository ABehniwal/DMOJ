n = int(input())
line = input()

longestPalindrome = line[0]

for i in range(n):
    for shift in range(n):
        # 1 character in the middle
        if i-shift >= 0 and i+shift<n:
            if line[i-shift] == line[i+shift]:
                if 2*shift + 1 > len(longestPalindrome):
                    longestPalindrome = line[i-shift:i+shift+1]

            else:
                break
    for shift in range(n):
        # 2 characters in the middle
        if i-shift>= 0 and i+1+shift<n:
            if line[i-shift] == line[i+1+shift]:
                if shift*2 + 2 > len(longestPalindrome):
                    longestPalindrome = line[i-shift:i+1+shift+1]

            else:
                break
                
        
        

print(longestPalindrome)
print(len(longestPalindrome))
