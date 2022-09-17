import datetime

def solution(a, b):
    answer = ''
    
    x = datetime.datetime(2016, a, b)
    print(x.year)
    print(x.month)    
    date = x.strftime("%a")
    answer = date.upper()
    
    return answer
