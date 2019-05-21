import numpy as np
import copy

def main():
    c = input("insert c vector \n")
    r = input("insert r vector \n")
    c_list = c.split(" ")
    r_list = r.split(" ")
    c_array = []
    r_array = []
    for temp in c_list:
        c_array.append(int(temp))
    for temp in r_list:
        r_array.append(int(temp))

    # print(c_array)
    # print(r_array)

    n = len(r_array)
    matrix = np.zeros((n, n))
    matrix[:, 0] = c_array
    matrix[0, 1:] = r_array[1:]
    # print(matrix)
    for i in range(1,n):
        for j in range(1,n):
            matrix[i, j] = matrix[i - 1, j - 1]
    print(matrix)
    matrix2,zarib=echlon(matrix,n)
    print(matrix2)
    deter=1
    for u in range(n):
        deter*=matrix2[u,u]
    print("determinan",end="")
    print(deter*zarib)

    # # print(matrix)
    # # print(matrix[2,2])
    # pivot = 0
    # for c in range(n):
    #     for x in range(c + 1):
    #         matrix[c, x] = c_array[c - x]
    #     pivot += 1
    # print(matrix)

def echlon(matrix,n):
    # print("**")
    # print(matrix)
    alamat=1
    j=0
    while j<n:
        if(matrix[j,j]!=0):
            for i in range(1,n-j):
                # print(i)
                # print("****")
                # print(matrix[j,j])
                # print(matrix[j,j])
                # print("****")
                zarib=matrix[j+i,j]/matrix[j,j]
                # print(zarib)
                for k in range(n):
                    # print(zarib)
                    # print(matrix[j,k]*zarib)
                    matrix[i+j,k]-=matrix[j,k]*zarib

            j += 1
        else:
            for i in range(1,n-j):
                if matrix[j+i,j]!=0:
                    temp = copy.copy(matrix[j+i,:])
                    matrix[j+i,:]=matrix[j,:]
                    matrix[j,:]=temp
                    alamat*=-1
                    break


    return matrix,alamat




if __name__ == "__main__":
    main()
