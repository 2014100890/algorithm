def solution(n, computers): 
    visited = [False for i in range(n)]
    answer  = 0 

    def dfs(node_num): 
        visited[node_num] = True
        for new_node in range(n): 
            if computers[node_num][new_node] and not visited[new_node]: 
                dfs(new_node)

    for node_num in range(n) : 
        if not visited[node_num]: 
            dfs(node_num)
            answer += 1 

    return answer 


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))