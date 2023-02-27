import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box
from numpy.linalg import norm, det
from numpy.random import uniform

def gauss(a, b):
    a = a.copy()
    b = b.copy()

    def forward():
        n=len(b)
        for i in range(n-1):
            for j in range (i+1, n):
                b[j]=b[j]-b[i]*a[j][i]/a[i][i] 
                a[j, i:]=a[j, i:]-a[i, i:]*(a[j][i]/a[i][i]) 
                
    def backward():
        n=len(b)
        x = numpy.zeros(len(b), dtype=float)
        x[n-1]=b[n-1]/a[n-1][n-1]
        for i in range(2, n+1):
            sum=0
            for j in range (n-i+1, n):
                sum=sum+a[n-i][j]*x[j]
            x[n-i]=(b[n-i]-sum)/a[n-i][n-i]
        return x

    forward()
    x = backward()
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4  ],
    [2.0, 1.0, 4.0, 3  ]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))

# Проверим получше
N=100
SMALL = 1e-5

def test_error(gauss):
    while True:
        a = uniform(0.0, 1.0, (N, N))
        b = uniform(0.0, 1.0, (N,  ))

        d = det(a)
        if abs(d) <= SMALL:  
            continue  
        if d < 0.0:  
            a = -a

        try:
            oob_solution = solve_out_of_the_box(a, b)
        except Exception as e:  
            continue  

        sb = a @ oob_solution
        if norm(sb - b, ord=1) > SMALL:
            continue  
        
        break 

    tested_solution = gauss(a, b)
    return norm(tested_solution - oob_solution, ord=1)

print(test_error(gauss))
