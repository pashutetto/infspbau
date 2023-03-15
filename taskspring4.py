# Будем вычислять опреденный интеграл (8+2x-x^2) от -2 до 4, который равен 36
import random 

def func(n):
    return 8+2*n-n**2

def integral(n):
    k=0
    for i in range (n):
        x=random.uniform( 1, 4)
        y=random.uniform( 0, 9)
        if y<=func(x):
            k=k+1
    return 2*3*9*k/n

N=10000
print(integral(N))
        