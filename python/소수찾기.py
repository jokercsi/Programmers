def solution(n):
    answer = 0
    list = []

    for i in range(1, n+1):
        count = 0
        for j in range(1, i):
            #1로만 나눠지는 숫자 찾기 (약수 갯수 구하기)
            if i % j == 0:
                count += 1
            
            if count > 1:
                break
        
        if count == 1:
            list.append(i)
            
    answer = len(list)
    return answer
