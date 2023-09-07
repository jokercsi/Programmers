def solution(n, lost, reserve):
    answer = 0
    
    #input 값 확인
    print("n =", n, ", lost =", lost,", reserve =", reserve)
    
    #일단 리스트를 정렬시키기
    lost.sort()
    reserve.sort()
    
    # [:]는 리스트를 복사
    # 복사를 하지 않으면, for문에서 list.remove()를 할 경우, 전부 돌지 않고 끝나버린다.
    for i in lost[:]:
        for j in reserve:
            # 자신의 운동복 잃어버릴 경우
            if (i == j):
                lost.remove(i)
                reserve.remove(j)
    
    for i in lost[:]:
        for j in reserve:
            if (i + 1 == j) or (i - 1 == j) :
                
                #리스트에 있을경우만 
                if i in lost:
                    lost.remove(i)
                    reserve.remove(j)
                    break

    answer = n - len(lost)

    return answer
