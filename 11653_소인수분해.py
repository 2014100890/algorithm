temp = int(input())
div_number = 2


while(temp!=1):
    if(not(temp % div_number)):
        temp = temp/div_number
        print(div_number)
    else:
        div_number+=1
