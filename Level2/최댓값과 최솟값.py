def solution(s):
    
    x = s.split(' ')
    list = []
    
    for i in x:
        list.append(int(i))
        
    mi = min(list) 
    ma = max(list)
    
    answer = str(mi) + ' ' + str(ma)
    return answer
