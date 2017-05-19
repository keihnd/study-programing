#Ax = bの解法
#前進消去の途中で対角成分が0になるときは実行できない

import numpy as np


a = np.array([[1.0,0.0,0.0,1.0],
              [0.0,1.0,0.0,8.0],
              [0.0,2.0,1.0,0.0],
              [3.0,0.0,0.0,1.0]])

b = np.array([[3.0],
              [1.0],
              [2.0],
              [2.0]])

def gauss_elimination(a,b):
    alpha = 0
    n = a.shape[0]

    #前進消去

    for k in range(n-1):
        for j in range(k+1,n):
            alpha = a[j,k] / a[k,k]
            a[j,] = a[j,] - alpha * a[k,]
            b[j] = b[j] - alpha * b[k]

    #後退代入
    beta = 0
    for k in list(reversed(range(n))):
        for j in range(k+1,n):
            beta = beta + a[k,j] * b[j]
        b[k] = (b[k] - beta)/ a[k,k]
        beta = 0

    return b


print("与えられた行列は")
print(a)
print("与えられた定数項は")
print(b)
print("です.")
print("解は")
print(gauss_elimination(a,b))
print("となります.")




"""n = A.ndim  #行列の次元
print(list(range(n-2)))
#前進消去
alpha = 0
x = 0
for k in range(n-1):
    for i in range(k+1,n):
        alpha = - A[i,k]/A[k,k]     #先頭を1に変換
        for j in range(k+1,n):
            A[i,j] = A[i,j] + alpha * A[k,j]    #先頭以外に代入
        b[i] = b[i] + alpha * b[i]      #ｂにも代入


#後退代入
for k in list(reversed(range(n))):
    for j in range(k+1,n):
        b[k] = b[k] - A[k,j] * b[j]
    b[k] = b[k] / A[k,k]

print(b)
print(list(reversed(range(n))))
"""
