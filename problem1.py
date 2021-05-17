def solution(s):
    answer = ''
    i = 0 
    
    while(i < len(s) ) :
        if('0'<=s[i]<='9') :
            answer += s[i]
            i+=1 
        elif s[i] == 'z' : 
            i += 4
            answer += '0'
        elif s[i] == 'o': 
            i +=3 
            answer += '1'
            continue
        elif s[i:i+2] == 'tw':
            i+=3
            answer += '2' 
        elif s[i:i+2] == 'th':
            i+=5
            answer += '3' 
        elif s[i:i+2] == 'fo':
            i+=4
            answer += '4' 
        elif s[i:i+2] == 'fi':
            i+=4
            answer += '5' 
        elif s[i:i+2] == 'si':
            i+=3
            answer += '6' 
        elif s[i:i+2] == 'se':
            i+=5
            answer += '7' 
        elif s[i] == 'e':
            i+=5
            answer += '8' 
        elif s[i] == 'n':
            i+=4
            answer += '9' 

    return answer

print(solution("123"))
