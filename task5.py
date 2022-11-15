def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


# Проверка кода

a=5
b=3
print(gcd(a, b))  # Должна выйти единица

a=225
b=625
print(gcd(a, b))  # Должно выйти 25
