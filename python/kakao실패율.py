def solution(N, stages):
    answer = []
    
    #dictionary
    dict ={}    

    #N = 전체 스테이지 수
    #stages = 사용자가 멈춤 스테이지

    #stages 정렬
    stages.sort()

    #실패율
    #스테이지에 도달했으나 x클리어 / 스테이지 도달
    mom = len(stages)

    for i in range(1, N+1):    
        count = 0
        for j in stages:
            if i == j:
                count += 1

        #0되는 경우 계산때문에 런타임 에러나니까 if문 사용 
        if count != 0:
            fail = count/mom
            mom -= count
        else:
            fail = 0
            
        dict[i] = fail
        # 실패율이 높은 스테이지 부터 RETURN하기 (내림차순)
        
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)}
    
    answer = list(dict.keys())
    #for key in dict.keys():
    #    answer.append(key)
    return answer
