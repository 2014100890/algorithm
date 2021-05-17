def solution(prices):
    answer = []
    len_prices = len(prices)
    for i in range(len_prices-1): 
        standard = prices[i]
        ck = False
        for j in range(i, len_prices) :
            if standard > prices[j] : # 가격 감소하였을 경우 
                answer.append(j-i)
                ck = True
                break
        if not ck : 
            answer.append(len_prices-i-1)   
    answer.append(0)
    return answer
