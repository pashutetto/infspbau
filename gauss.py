import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def solution(a, b):
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

def max_dev(a, b):
    oob_solution = solve_out_of_the_box(a, b)
    return norm(solution(a,b)-oob_solution, ord=1)


