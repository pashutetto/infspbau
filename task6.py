def gcd(a, b):
    if a==0:
        return b
    else:
        return gcd(b%a, a)


def egcd(a, b):
    if a==0:
        x=0
        y=1
        return (gcd(a, b), x, y)
    else:
        d, x, y =egcd(b%a, a)
        return(d, y-(b//a)*x, x)


# Проверим код:

a=80
b=144
print(egcd(a, b))  # 16=80*2-144. Тогда x=2, y=-1
