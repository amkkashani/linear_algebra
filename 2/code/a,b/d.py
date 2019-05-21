import numpy as np
import copy
import math

def main():
    n = int(input("insirt n \n"))
    matrix = np.zeros((n, n))
    for i in range(n):
        satr = input().split(" ")
        j = 0
        for x in satr:
            matrix[i, j] = int(x)
            j += 1
    print(matrix)
    lu_finder(matrix)

    print("insirt b matrix")
    b=np.zeros((n,1))
    for i in range(n):
        b[i][0]=int(input())
    l,u = lu_factor(matrix)
    print("L*******************************")
    print(l)
    print("U********************************")
    print(u)
    javab=solution_complete_LU(l,u,b)
    print("پاسخ نهایی")
    print(javab)


def lu_factor(A):
    try:
        if A.shape[0] != A.shape[1]:
            print("is not square")
            quit()

    except:
        if(A.shape[0]==1):
            print("okeye")
        else:
            print("is not square")
            quit()
    size = int(math.sqrt(A.size))
    print(size)
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
   # print(l)
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
    x = np.zeros((n,1), float)
    for i in range(n - 1, -1, -1):  #   - Eq. (3.6)
        s = b[i]
        for j in range(i + 1, n):
            s = s - lu[i, j] * x[j]
        x[i,0] = s / lu[i, i]
    return x

def solution_complete_LU(l,u,b):
    temp=LUsolve_forward_substitution(l,b)
    return LUsolve_backward_substitution(u,temp)





if __name__ == "__main__":
    main()
