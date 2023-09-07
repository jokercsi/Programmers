def solution(n):
    answer = 0
    
    if n % 2 == 0:
        # 약수 구하기
        for i in range(1, n+1):
            if n % i == 0 and i % 2 == 1:
                answer += 1           

    else:
        for i in range(1, n+1):
            # 나머지 구하기
            x,z = divmod(n,i)
            print(x,z)
            if z == 0:
                answer += 1
                
    print(answer)
    return answer

#   {1, 3, 5, 15}
#   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#   1 2 3 4 5
#         4 5 6
#               7 8
#                                    15

# {1, 2}
#  2

# {1, 2, 4}
# 4
  
# {1, 2, 4, 8, 16}
# 16

# {1, 2, 5, 10}
# 1 2 3 4
# 10
