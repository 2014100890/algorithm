from collections import defaultdict

def solution(genres, plays):
  
    genre_dict = defaultdict(int)
    detail_dict = defaultdict(list)
    
    idx = 0
    for genre, play_cnt in zip(genres,plays):
        genre_dict[genre] += play_cnt
        detail_dict[genre].append((idx,play_cnt))
        idx += 1

 
    sorted_genre_dict = sorted(genre_dict.items(), key = (lambda x: x[1]), reverse=True)
  

    answer= [] 
    for genre in sorted_genre_dict :
        
        sorted_song_dict = sorted(detail_dict[genre[0]], key=(lambda x: x[1]), reverse=True)

        answer.append(sorted_song_dict[0][0])
        if(len(sorted_song_dict)> 1 ): 
            answer.append(sorted_song_dict[1][0])
    

    return answer

