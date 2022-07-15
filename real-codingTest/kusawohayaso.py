import sys

def main(lines):

    # input first line 
    a = lines[0]
    # input second line
    b = lines[1]

    # split input
    line = a.split(" ") 

    n = int(line[0])
    k = int(line[1])
    
    count = 0
    # flag = skip for-loop 
    flag = 0
    
    for i in range(n):
        
        if flag != 0:
            flag -= 1
            continue

        # if found "w", 
        if b[i] == "w":
            continue  
        
        # if found "."
        elif b[i] == ".":
            count += 1
            flag = k - 1

    print(count)
