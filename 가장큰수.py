def solution(numbers):
    answer = ''
    str_list = list(map(str, numbers)); 
    str_list.sort(key = lambda x : x*3, reverse = True)
    answer = str(int(''.join(str_list)))
    return answer