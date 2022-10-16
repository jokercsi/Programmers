def solution(s):
    answer = -1    
    pivot = ""
    lis = list(s)
    
    window = []
    
    while len(lis) > 1:
        for i, char in enumerate (lis):

            if char == pivot:
                window.append(lis.pop(i))
                window.append(lis.pop(i-1))

            pivot = char        
        
        if len(window) == 0:
            window.clear()
            return 0
    
