def solution(places):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for place in range(5) : # 전체 공간 
        check_distance = 1 # 거리두기 지키면 1 
        room = [[0]* 5 for i in range(5)]
        
        for row in range(5) : # 한 판 
            for col in range(5): 
                room[row][col] = places[place][row][col]
        
        for row in range(5): 
            for col in range(5): 
                idx = room[row][col]
                if(idx == 'P'):  # 의자일 때 
                    for i in range(4): 
                        ny = row + dy[i] 
                        nx = col + dx[i] 
                        if(ny >= 0 and ny < 5 and nx >= 0 and nx < 5): 
                            if room[ny][nx] == 'P' :  # 근처에 바로 의자가 있을 경우 
                                check_distance = 0
                                print('바로 옆 의자', room[row][col], '현좌표', row, col,'책상좌표', ny, nx, '의자 좌표' , py, px, place)
                            elif room[ny][nx] == 'O' : 
                                for i in range(4): 
                                    py = ny + dy[i]  
                                    px = nx + dx[i]
                                    if(py >= 0 and py < 5 and px >= 0 and px < 5 and (not (py == row and px == col))): 
                                        if(room[py][px] == 'P'): 
                                            check_distance = 0 
                                            # print('건너서의자', room[row][col], '현좌표', row, col,'책상좌표', ny, nx, '의자 좌표' , py, px, place)

                                            break;
        answer.append(check_distance)
    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))