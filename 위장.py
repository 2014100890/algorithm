from collections import defaultdict

def solution(clothes):
    
    answer = 0 
    type_list = set()
    clothes_dict = defaultdict(list) 
    
    for i in clothes : 
        type_list.add(i[1])
        clothes_dict[i[1]].append(i[0])
        
    temp_cnt = 0 
    mul_cnt = 1 
    
    for j in clothes_dict :
        cnt = len(clothes_dict[j])
        mul_cnt *= (cnt + 1) 
    
    answer = mul_cnt -1 
    return answer