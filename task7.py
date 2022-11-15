import math


def is_simple(a):
    n=math.sqrt(a)  
    n=int(n)
    s=[2]
    for i in range(3, n+1):
        k=0
        for j in range(len(s)):
            if i%s[j]==0:
                k=k+1
            if k==0:
                s.append(i)
    t=0
    for i in range(len(s)):
        if a%s[i]==0:
            t=t+1
    if t==0:
        return True
    else:
        return False


# Проверим код:

print(is_simple(897))  # Число составное
print(is_simple(521))  # Число простое




