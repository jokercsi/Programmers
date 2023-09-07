def solution(absolutes, signs):
    answer = 123456789
    
    for i in range(0,len(signs)):
        if signs[i] == False :
            absolutes[i] = -absolutes[i]
    
    answer = sum(absolutes)
    
    return answer
