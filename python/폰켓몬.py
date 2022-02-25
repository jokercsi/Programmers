def solution(nums):
    answer = 0
    limit = len(nums)/2
    newNums = []
    
    #중복제거!!!! for문으로 해결하기, 중복은 set으로도 해결가능 
    for value in nums: 
        if value not in newNums: 
            newNums.append(value)

    print(newNums)
    
    if limit < len(newNums):
        answer = limit
    elif limit > len(newNums):
        answer = len(newNums)
    elif limit == len(newNums):
        answer = limit
    
    return answer
