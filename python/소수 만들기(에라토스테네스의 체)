#에라토스테네스의 체
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def solution(nums):
    answer = 0
    sums = []
    
    for i in range(len(nums)):        
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                sums.append(sum)
    
    print(sums)
    
    
    for i in sums:
        if(isPrime(i)):
            answer += 1
    
    return answer
