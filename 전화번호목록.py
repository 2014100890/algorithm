def solution(phone_book):
    answer = True
    ck_answer = False
    phone_book.sort()
    
    for i in range(len(phone_book)-1): 
        A_number = phone_book[i]
        B_number = phone_book[i+1]
        
        if(len(A_number) > len(B_number)): 
            A_number, B_number = B_number, A_number


        for idx in range(len(A_number)): 
            if A_number[idx] != B_number[idx] : 
                ck_answer = True
                break
            if(idx == len(A_number)-1): 
                if(A_number[idx] == B_number[idx]):  
                    answer = False
                return answer

    return answer

