def solution(s):
    stack = []
    
    s = list(s)

    for i in s:
        if not stack:  # 만약 stack이 비여있다면
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
            continue
        else:
            stack.append(i)
        
    if not stack:
        return 1
    else:
        return 0
