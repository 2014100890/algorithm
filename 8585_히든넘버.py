cnt = int(input())
temp = input()
result = 0
ck = False 
temp_tot = ''
for i in temp : 
    if(not(i>='A')): # 현재값이 숫자라면 
        print(i)
        if(ck):  # 이전값이 숫자인 경우  
           temp_tot += i 
        else : 
            ck = True
            temp_tot = i
    else: 
        ck = False
        if(len(temp_tot)>0):
            result += int(temp_tot)
            temp_tot = ''

if(temp_tot != ''):
    result += int(temp_tot)

print(result)


