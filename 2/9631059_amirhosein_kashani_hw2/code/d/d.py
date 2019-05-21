import numpy as np
import copy
import math

def main():
    h5=hilbert_maker(5)
    h10=hilbert_maker(10)
    h15=hilbert_maker(15)
    h20=hilbert_maker(20)
    A5=myinverse(h5)
    A10=myinverse(h10)
    A15=myinverse(h15)
    A20=myinverse(h20)
    A_inverseh5=np.linalg.inv(h5)
    A_inverseh10=np.linalg.inv(h10)
    A_inverseh15=np.linalg.inv(h15)
    A_inverseh20=np.linalg.inv(h20)


    print("A*A_prim h5")
    print(np.matmul(h5, A5))
    print("A*A_inverse h5")
    print(np.matmul(h5,A_inverseh5))

    print("A*A_prim h10")
    print(np.matmul(h10, A10))
    print("A*A_inverse h10")
    print(np.matmul(h10, A_inverseh10))

    print("A*A_prim h15")
    print(np.matmul(h15, A15))
    print("A*A_inverse h15")
    print(np.matmul(h15, A_inverseh15))

    print("A*A_prim 20")
    print(np.matmul(h20, A20))
    print("A*A_inverse 20")
    print(np.matmul(h20, A_inverseh20))

def myinverse(matrix):
    n=int(math.sqrt(matrix.size))
    l, u = lu_finder(matrix)
    # print("L*******************************")
    # print(l)
    # print("U********************************")
    # print(u)
    javab = None
    for i in range(n):
        temp = np.zeros((n, 1))
        temp[i, 0] = 1
        if javab is None:
            javab = solution_complete_LU(l, u, temp)
        else:
            javab = np.c_[javab, solution_complete_LU(l, u, temp)]
    print("معکوس ماتریس")
    print(javab)
    return javab


def hilbert_maker(n):
    result=np.zeros((n,n),float)
    for i in range(n):
        for j in range(n):
            result[i,j]=1/(1+j+i)
    return result




def lu_finder(A):
    try:
        if A.shape[0] != A.shape[1]:
            print("is not square")
    except:
        if(A.shape[0]==1):
            print("okeye")
        else:
            print("is not square")
    size = int(math.sqrt(A.size))
   # print(size)
    l = np.zeros((size, size))
    u = copy.copy(A)
    for i in range(size - 1):
        zarib = u[i, i]
        #print(zarib)
        l[i, i] = 1
        for v in range(i + 1, size):
            l[v, i] = u[v, i] / zarib
        j = i + 1
        pivot = i
        while (j < size):
            zarib2 = u[j, i] / u[pivot, i]
            for t in range(size):
                u[j, t] = u[j, t] - u[pivot, t] * zarib2
            j += 1
    l[size - 1, size - 1] = 1
  #  print(l)
   # print(u)
    return l, u


def LUsolve_forward_substitution(lu, b):
    n = lu.shape[0]
    y = np.zeros((n), float)
    for i in range(0, n):  #  - Eq. (3.5)
        s = b[i]
        for j in range(0, i):
            s = s - lu[i, j] * y[j]
        y[i] = s
    return y
def LUsolve_backward_substitution(lu, b):
    n = lu.shape[0]
    x = np.zeros((n), float)
    for i in range(n - 1, -1, -1):  #   - Eq. (3.6)
        s = b[i]
        for j in range(i + 1, n):
            s = s - lu[i, j] * x[j]
        x[i] = s / lu[i, i]
    return x

def solution_complete_LU(l,u,b):
    temp=LUsolve_forward_substitution(l,b)
    return LUsolve_backward_substitution(u,temp)


if __name__ == "__main__":
    main()
