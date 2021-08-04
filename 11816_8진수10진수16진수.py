temp = input()
result = 0 
if(temp[0:2] == '0x'):
    print(int(temp, 16))
elif(temp[0] == '0'):
    print(int(temp, 8))
else:
    print(temp)
