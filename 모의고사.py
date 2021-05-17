def solution(answers):
    real_answer = []
    answer = [0]*4
    total_problems = len(answers)
    number_1 = [1,2,3,4,5] * (int(total_problems / 5)+1)
    number_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (int(total_problems / 8)+1)
    number_3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(total_problems / 10)+1)
    
    for i in range(len(answers)) : 
        if answers[i] == number_1[i]: 
            answer[1] += 1 
        if answers[i] == number_2[i]: 
            answer[2] += 1 
        if answers[i] == number_3[i]: 
            answer[3]+= 1 
            
    max_point = max(answer)
    for i in range(1, 4) :
        if(answer[i] == max_point): 
            real_answer.append(i)
            
        
    return real_answer
