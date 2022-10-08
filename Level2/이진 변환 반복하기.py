def solution(s):
    answer = []
    countZero = 0
    count = 0
    
    while True:
        countZero += s.count("0")
        count += 1
        s = s.replace("0", "")
        b = str(bin(len(s)))
        s = b[2:]
        if s == "1":
            break
            
    answer = [count, countZero]

    
    return answer
