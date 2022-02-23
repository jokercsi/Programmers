def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        
        # int to binary => format(int, "b")
        # OR operator => | 
        st = format(arr1[i] | arr2[i], "b")
        map = ''
        
        # 앞에 0이 생략되는 binary는 임의로 0을 추가해주기
        if len(st) != n:          
            num = n - len(st) 
            map += " "*num 
        
        #binary를 "#"과 ' 로 바꾸기
        for j in st:
            if j == "1":
                map += "#"
            elif j == "0":
                map += " "
            
        answer.append(map)
        
    return answer
