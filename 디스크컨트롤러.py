import heapq
def solution(jobs):
    answer = 0
    start = -1 
    now = 0    
    jobs_todo = []
    heapq.heapify(jobs_todo)
    cnt_todo = len(jobs)
    finish_cnt = 0
    heapq.heapify(jobs)
    
    while finish_cnt < cnt_todo : 
        while jobs : 
            # start : 전의 작업의 시작 시각
            # now : 전 수행 작업의 종료 시각 
            # 전 작업 사이에 시작할 수 있었던 일들을 넣어준다. 
            job = jobs[0]
            if start<job[0]<=now : 
                # 소요시간이 짧은 것 부터 넣기
                heapq.heappush(jobs_todo, [job[1], job[0]])
                heapq.heappop(jobs)
            else : 
                break

        if(jobs_todo) :
            current_job = heapq.heappop(jobs_todo)
             # 작업을 진행 한만큼 현재 시간을 늘려주어야함 
            start = now
            now += current_job[0] # 소요시간 더해줌 
            answer += now - current_job[1]
            finish_cnt += 1
    
        else : 
            now += 1   
            
    return int(answer/cnt_todo)