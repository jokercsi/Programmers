def solution(d, budget):
    answer = 0
        
    #정렬하기 sort
    d.sort()

    #최대로 빌려주기
    for i in d:        
        if budget >= i:
            budget = budget - i
            answer += 1
        else:
            break 

    return answer
