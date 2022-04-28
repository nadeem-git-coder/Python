from re import L


tc = int(input())
for _ in range(tc):
    n ,r ,b = list(map(int,input().split()))
    if(r%2==0 and b%2==0):
        print('R'*r//2 + 'B'*b + 'R'*r//2)
    elif(r%2==1):
        print('R'*r//2 + 'B'*b//2 + 'R' + 'B'*b//2 + 'R'*r//2)
    elif(b%2==1):
        print('B'*b//2 + 'R'*r + 'B' + 'R'*r + 'B'*b//2)
    else:
        print('R'*(r//2 +1) + 'B'*b + 'R'*r//2)
