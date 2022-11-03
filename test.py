T = int(input())
for i in range(T):
    A,B,C = map(int,input().split(" "))
    a = A+B
    b = B+C
    c = A+C
    if a %2 ==0 or b %2 ==0:
        print("No")
    else:
        print("Yes")