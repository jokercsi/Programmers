def solution(array, commands):
    answer = []
    
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]

        print(i , j , k)

        #2번째 부터 5번째
        first = array[i-1:j]

        #뽑은 뒤 정렬
        first.sort()

        #세번째 index
        answer.append(first[k-1])
    
    return answer
