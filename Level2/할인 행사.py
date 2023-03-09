"""
10일 -> 회원 자격
할인 제품 -> 하루에 하나씩 구입 가능
회원 등록시 원하는 제품을 모두 할인 받을 수 있는 날짜 구하기
"""
def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    for i, j in zip(want, number):
        want_dict[i] = j
        
    # print(dict)
    accountSale = 10
    skiploop = len(discount) - sum(number) + 1
    
    for i in range(skiploop):
        count = accountSale
        num = len(number)
        dict = want_dict.copy()
        
        for j in range(i, len(discount)):
            if discount[j] in want:
                count -= 1
                dict[discount[j]] -= 1
                if dict[discount[j]] == 0:
                    num -= 1
                if num == 0:
                    answer += 1
                    break
                    
                if count == 0:
                    break

            else:
                #print("break")
                break
    
    return answer
