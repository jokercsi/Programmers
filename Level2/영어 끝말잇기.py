def solution(n, words):
    answer = [0,0]

    # [탈락하는 사람 번호, 몇 번째 차례에 탈락]
    # n = 사람 수
    # words = 단어 나열
    # 탈락 안하면 [0,0]
    
    # 중복 확인을 위한 list
    list = []
    
    #마지막 문자 (일단 첫번째 문자 배정)
    lastWord=words[0][0]
    count=0
    for i, word in enumerate(words):
        # num = n번째 사람(틀린 사람)
        num = i%n +1
        
        # 주기 카운트 하기
        if num == 1:
            count += 1
                    
        if lastWord != word[0]:
            answer = [num, count]
            return answer
        
        # list에 중복 단어가 있다면
        if word in list:
            answer = [num, count]
            return answer  
        
        lastWord = word[-1]
        
        list.append(word)
        
    return answer
