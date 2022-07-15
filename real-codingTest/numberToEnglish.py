import sys

d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
    6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
    11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
    15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
    19 : 'nineteen', 20 : 'twenty',
    30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
    70 : 'seventy', 80 : 'eighty', 90 : 'ninety' 
}

t = 1000 #thousand
m = 1000000 #million
b = 1000000000 #billion
tr = 1000000000000 #trillion

def main(lines):

    if not lines[0]:
        print(-1)
    elif lines[0].isalpha():
        print(-1)
    elif lines[0][0] == "0" and lines[0][1] != ".":
        print(-1)

    else:
        num = float(lines[0])

        #소수일 경우
        if num - int(num) != 0:
            print(float_to_eng(num).capitalize())

        #소수가 아닐 경우
        elif num - int(num) == 0:
            print(int_to_en(num).capitalize())


def float_to_eng(num):
    sosu = num - int(num)
    int_num = int(num)
    floatNum = round(sosu, 5)
    return(int_to_en(int_num) + ' point ' + float_separate(floatNum))


def float_separate(num):
    a = []
    float_str = ""

    
    for i in str(num):
      a.append(i)
    #정수 지우기
    a = a[2:] 

    for i in a:
      float_str += d[int(i)] + " "
    return float_str


def int_to_en(num):
    if (num < 20):
        return d[num]

    elif (num < 100):
        if num % 10 == 0: 
          return d[num]
        else: 
          return d[num // 10 * 10] + ' ' + d[num % 10]

    elif (num < t):
        if num % 100 == 0: 
          return d[num // 100] + ' hundred'
        else: 
          return d[num // 100] + ' hundred ' + int_to_en(num % 100)

    elif (num < m):
        if num % t == 0: return int_to_en(num // t) + ' thousand'
        else: return int_to_en(num // t) + ' thousand ' + int_to_en(num % t)

    elif (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million ' + int_to_en(num % m)

    elif (num < tr):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion ' + int_to_en(num % b)



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
