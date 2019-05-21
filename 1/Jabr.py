import numpy as np


def main():
    n = int(input("input n \n"))
    squre_arr = np.zeros((n, n))

    sotoni = np.zeros((n, 1))
    # print(squre_arr)
    # print(sotoni)
    for i in range(n):
        x = input();
        satr = x.split(" ")
        for j in range(n):
            # print(float(satr[j]))
            squre_arr[i][j] = float(satr[j])

    for i in range(n):
        sotoni[i, 0] = float(input())
    print(squre_arr)
    print(sotoni)

    # now we have 2 matrix

    # now we want to concatinate that
    print("augmented")
    augment = np.hstack((squre_arr, sotoni))
    print(augment)
    print("####")
    ##calculat of matrix
    for i in range(n):
        j = i+1
        while (j != n):
            sefr_konandesatri(n + 1, i, j, augment)
            j += 1
        print(augment)
    print("now we have echlone form")
    for i in range(n-1,-1,-1):
        j= i -1
        while(j!=-1):
            sefr_konandesatri(n+1,i,j,augment)
            j-=1
        reserve=augment[i,i]
        print("*********")
        print(i)
        print(reserve)
        print("********")
        for z in range(n+1):
            augment[i,z]/=reserve
        print(augment)
    print(augment)
    for i in range(n):
        print("a"+(i+1).__str__()+" =",end="")
        print(round(augment[i,n],3))

def sefr_konandesatri(tool, satr1, satr2, arr):
    numberPivot = None
    for i in range(tool):
        if arr[satr1, i] != 0:
            pivot = arr[satr1, i]
            numberPivot = i
            break
    # print(arr[satr1, numberPivot])
    if(arr[satr1, numberPivot]==0):
         return
    zarib = arr[satr2, numberPivot] / arr[satr1, numberPivot]
    for i in range(tool):
        # print(arr[satr2, i] - arr[satr1, i] * zarib)
        arr[satr2, i] =round(float(arr[satr2, i] - arr[satr1, i] * zarib),5)


if __name__ == "__main__":
    main()
