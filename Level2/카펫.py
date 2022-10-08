# 노란색 네모 만들기 위해 필요한 수
# 제곱들
# 1, 4, 9, ...

# 2와 배수
# 2, 4, 6, 8, 10, ...

def solution(brown, yellow):
    answer = []
    answerlist = []
    
    # 제곱일 경우
    a = yellow ** 0.5    
    
    if a - int(a) == 0:
        answer = [a+2, a+2]
        return answer
    
    # 2의 배수일 경우
    # 약수를 구하자
    for i in range(1, yellow+1):
        if yellow % i == 0:
            answerlist.append(i)
    
    for i in range(0, int(len(answerlist)/2)):
        print(answerlist[-i-1], answerlist[i])
        
        row = answerlist[-i-1] + 2
        column = answerlist[i] + 2
        
        if row * 2 + column * 2 - 4 == brown:
            answer = [row, column]
            return answer
