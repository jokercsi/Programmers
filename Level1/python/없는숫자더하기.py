def solution(numbers):
    
    zeroToNine = [0,1,2,3,4,5,6,7,8,9]

    for i in numbers:
        zeroToNine.remove(i)
        
    answer = sum(zeroToNine)
                
    return answer
