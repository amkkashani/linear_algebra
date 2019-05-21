import numpy as np
from fractions import Fraction as frac


def main():
    print("یه اینتر اضافه آخرش بزنید")
    print("insirt A")
    satr = [frac(x) for x in input().split()]
    matrix = np.array(satr)
    loghat = []
    satr = [frac(x) for x in input().split()]
    while len(satr) != 0:
        matrix = np.vstack((matrix, satr))
        satr = [frac(x) for x in input().split()]
    matrix_reduce, p, p_r, p_c = echelon(matrix)
    print("ماتریس کاهش یافته ی سطری")
    print(matrix_reduce.astype(str))
    free_c = [c for c in range(matrix.shape[1]) if c not in p_c]
    null = []
    for col in free_c:
        v = np.zeros((matrix.shape[1], 1))
        v[col] = 1
        for piv in p:
            v[piv[1], 0] = -1 * matrix_reduce[piv[0], col]
        null.append(v)
    print("پایه های فضای پوچ")
    for b in null:
        print(b)
        print("#####")
    print("مختصات بقیه ی بردار ها بر اساس بردار پایه")
    for free in free_c:
        zarib = np.zeros((len(p_r), 1))
        for row in p_r:
            zarib[row] = matrix_reduce[row, free]
        print(zarib)
        print("====")


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
    print("پایه های فضای ستونی")
    for x in p_r:
        temp=matrix[:,x].reshape((m,1))
        print(temp.astype(str))
        print("---")
    print("پایه های فضای سطری")
    for y in p_c:
        print(matrix[y,:].astype(str))

    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77")

    p_r.reverse()
    p_c.reverse()
    for piv in p:
        matrix[piv[0]] /= matrix[piv[0], piv[1]]
        for k in range(piv[0]):
            matrix[k] -= matrix[piv[0]] * matrix[k, piv[1]]
    p_r.reverse()
    p_c.reverse()
    return matrix, p, p_r, p_c


if __name__ == "__main__":
    main()
