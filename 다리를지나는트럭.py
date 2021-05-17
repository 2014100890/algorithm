def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0 
    truck_on_bridge  = []
    available_weight = weight 
    ck_finish = False

    while not ck_finish : # 남은 트럭이 있고, 종료되지 않았을 때
        if(truck_weights): 
            if(available_weight >= truck_weights[0]):  # 다리에 더 올릴 수 있는 무게가 있다면
                truck_on_bridge.append([truck_weights[0], 0]) # 다리에 트럭을 올린다 
                available_weight -= truck_weights[0]  # 다리에 올릴 수 있는 무게가 줄어든다. 
                truck_weights.pop(0)
        
        time += 1  
        ck_remove = False
        add_weight = 0 
        
        for i in truck_on_bridge : 
            i[1]+=1
            if(i[1] == bridge_length): # 도착했다면
                ck_remove  = True
                add_weight = i[0]   
                
        if(ck_remove) : 
            available_weight += add_weight
            truck_on_bridge.pop(0)
      

        if not truck_on_bridge and not truck_weights: 
            ck_finish = True
            break
    return time +1 
            