
try:
    n = int(input())
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
except ValueError as e:
    print("Invalid djbheg")
except ArithmeticError:
    print("Arithmetic Error")
except TypeError:
    print("TypeError")
