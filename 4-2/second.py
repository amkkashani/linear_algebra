import numpy as np
import copy
def main():
    matrixA= np.array([
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1],
        [-1,-13,-12.3,-1.5]
    ])
    matrixB= np.array([
        [1],
        [0],
        [0],
        [-1]
    ])
    result=matrixB
    temp=copy.deepcopy(matrixB)
    for i in range(3):
        temp=np.dot(matrixA,temp)
        result=np.append(result,temp,axis=1)
    print("ماتریس حاصل")
    print(result)
    result_echlon,rank=echelon(result)
    print("حالت کاهش یافته")
    print(result_echlon)
    print("رنک ماتریس")
    print(len(rank))
    print("نتیجه از این قرار است که جفت ماتریس قابل کنترل میباشد")
def echelon(matrix):
    m, n = matrix.shape
    i, j = 0, 0
    p_r = []
    p_c = []
    p = []
    while i < m and j < n:
        if matrix[i, j] == 0:
            for k in range(i + 1, m):
                if matrix[k, j] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    break
            if matrix[i, j] == 0:
                j += 1
                continue
        for k in range(i + 1, m):
            matrix[k] -= matrix[i] * (matrix[k, j] / matrix[i, j])
        p_r.append(i)
        p_c.append(j)
        p.append((i, j))
        i += 1
        j += 1

    # reduce
    return matrix,p_c






if __name__ == "__main__":
        main()
