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
    first[0]=1
    print(first)
    s=None
    for i in range(30):
        first=np.dot(matrix,first)
        maximum = first.max()
        first /= maximum
        # for j in range(25):
        #     first[j][1]
    print("*************************")
    print(first)
    print("**************")
    print(maximum)




if __name__ == "__main__":
    main()