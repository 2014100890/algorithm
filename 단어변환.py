from collections import deque 
answer = 51

def solution(begin, target, words):
    global answer 
    number_words = len(words)
    len_word = len(begin)
    visited = [False for i in range(number_words)]
    word_queue = deque()
    
    def bfs() : 
        global answer
        while word_queue : 
            now_point = word_queue.pop()
            now_word = now_point[0]
            now_count = now_point[1]

            if(now_word == target) :                 
                answer = now_count
                return                

            for word_idx in range(number_words): 
                if not visited[word_idx]: 
                    temp_word = words[word_idx]
                    wrong_cnt = 0 
                    for str_idx in range(len_word): 
                        if now_word[str_idx] != temp_word[str_idx] :
                            wrong_cnt += 1 
                        if(wrong_cnt > 2) : 
                            break
                    if wrong_cnt == 1 : 
                        word_queue.append([temp_word, now_count+1])
                        visited[word_idx] = True

        
    for word_idx in range(number_words):
        if not visited[word_idx]: 
            temp_word = words[word_idx]
            wrong_cnt = 0 
            for str_idx in range(len_word): 
                if begin[str_idx] != temp_word[str_idx] :
                    wrong_cnt += 1 
                if(wrong_cnt > 2) : 
                    break
            if wrong_cnt == 1 : 
                word_queue.append([temp_word, 1])
                visited[word_idx] = True
                   
    bfs()
    if(answer == 51) : 
        answer = 0 
        
    return answer