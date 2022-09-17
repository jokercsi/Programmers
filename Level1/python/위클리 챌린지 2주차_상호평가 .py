def solution(scores):
    answer = ''
    
    list = []
    for j in range(len(scores)):
        for i in range(len(scores)):
            list.append(scores[i][j])
    
        
        list.remove(scores[j][j])
        
        if max(list) >= scores[j][j] and min(list) <= scores[j][j]:
            list.append(scores[j][j])
            
        print(list)
        
        avg = sum(list) / len(list)

        if avg >= 90:
            answer += "A"
        elif avg < 90 and avg >= 80:
            answer += "B"
        elif avg < 80 and avg >= 70:
            answer += "C"
        elif avg < 70 and avg >= 50:
            answer += "D"
        else:
            answer += "F"
        
        list = []
        
    
    return answer
