def solution(s):
    answer = ''
    list = []
    
    s = s.lower()
    x = s.split(" ")
    
    
    for i in x:
        answer += i.capitalize() + " "

    answer = answer[:-1]
    
    
    return answer
