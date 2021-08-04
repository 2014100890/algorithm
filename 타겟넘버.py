def solution(numbers, target):
    answer = 0
    total_num = len(numbers)
    def dfs(idx, result): 
        if(idx == total_num): 
            if(result == target): 
                nonlocal answer
                answer += 1 
            return 
        else : 
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
            
    dfs(0, 0)
    return answer