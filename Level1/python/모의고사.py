def solution(answers):
    answer = []

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]

    list = [0,0,0]

    for i in range(len(answers)):
        c1 = i % 5
        c2 = i % 8
        c3 = i % 10

        if answers[i] == one[c1]:
            list[0] += 1
        if answers[i] == two[c2]:
            list[1] += 1
        if answers[i] == thr[c3]:
            list[2] += 1

    max_num = max(list)

    for i in range(len(list)): 
        if max_num == list[i]:
            answer.append(i+1)

    return answer
