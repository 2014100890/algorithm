from collections import deque
def solution(n, k, cmd):
    del_li = deque()
    del_append = del_li.append
    del_number = []
    li = deque([i for i in range(n)])
   
    for do_it in cmd : 
        if(do_it[0] == 'D'): # 아래로 내려간다. 
            k += int(do_it[1:])
        elif(do_it[0] == 'C'): 
            del_append([li[k], k])
            del_number.append(li[k])
            del li[k]
            if k == len(li): 
                k -=1 
        elif(do_it[0] == 'U'): 
            k -= int(do_it[1:])  # 여기서 앞으로 가야함 
        elif(do_it[0] == 'Z'):     
            insert_thing = del_li.pop()
            del del_number[-1]
            li.insert(insert_thing[1], insert_thing[0])   
            if (insert_thing[1]<= k ) : 
                k +=1 

    answer = ['O']*n
    del_number = del_number

    for i in del_li : 
        answer[del_li[i][0]] = 'X'

    return ''.join(answer)
   