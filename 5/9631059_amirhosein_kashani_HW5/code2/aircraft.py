import numpy as np
def main():
    satr=input().split()
    b=np.zeros(13)
    # print(b)
    for i in range(13):
        b[i]=float(satr[i])
    A=np.zeros((13,3))
    for i in range(13):
        A[i][0]=1
        A[i][1]=i
        A[i][2]=i*i
    # print(A)
    AT=np.transpose(A)
    # print(AT)
    AT_b=np.dot(AT,b)
    AT_A=np.dot(AT,A)
    print("ضرایب ")
    B=np.linalg.solve(AT_A,AT_b)
    print(B)
    print("در ثانیه ی 4.5")
    print(B[0]*1+B[1]*4.5+B[2]*4.5*4.5)












if __name__ == '__main__':
    main()
