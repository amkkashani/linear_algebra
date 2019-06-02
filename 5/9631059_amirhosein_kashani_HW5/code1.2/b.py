import numpy as np
from fractions import Fraction as frac
import random


def main():
    
    matrix=np.zeros((25,25))
    random.seed(2);
    for i in range(25):
        for j in range(25):
            a = random.random()*10
            matrix[i][j]=a
    first=np.zeros((25,1))
    for i in range(25):
        first[i]=random.random()
    print("matrix x0")
    print(first)
    a=50
    print("a=",end=" ")
    print(a)
    yeke=np.identity(25)*a
    zaribY=np.subtract(matrix,yeke)
    for i in range(150):
        Y=np.linalg.solve(zaribY,first)
        s=Y.max()
        first=Y/s
    print("vk")
    print(a+1/s)
    print("xk")
    print(first)





if __name__ == "__main__":
    main()