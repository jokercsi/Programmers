def solution(n):
    answer = 0
    
    binary = bin(n)
    binary = binary[2:]
    count = binary.count("1")
    
    while True:
        n += 1
        binaryNext = bin(n)
        binaryNext = binaryNext[2:]
        if count == binaryNext.count("1"):
            break
            
    answer = n
    return answer
