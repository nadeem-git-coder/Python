tc = int(input())
for _ in range(tc):
    n = int(input())
    if(n>=1900):
        print("Division 4")
    elif(n>=1600 and n<=1899):
        print("Division 3")
    elif(n>=1400 and n<=1599):
        print("Division 2")
    elif(n<=1399):
        print("Division 1")


from collections import Counter
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int,input().split()))
    d = Counter(arr)
    val = max(d.values())
    if(val <=1):
        print(-1)
    else:
        for key,value in d.items():
            if(value == val):
                print(key)
   