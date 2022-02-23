def solution(n):
    answer = 0
    
    #n(10진법) 
    if n == 0:
        return '0'
    
    nums = []
    #n이 0 아니기 때문에 항상 참
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    num = ''.join(nums)
    
    answer = int(num, 3)
    
    return answer
