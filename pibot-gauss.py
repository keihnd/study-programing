#Ax = bの解法
#前進消去の途中で対角成分が0になるときは実行できない

import numpy as np


a = np.array([[1.0,2.0],
             [1.0,1.0]])

b = np.array([[3.0],
              [1.0]])


# 後退代入
def back_substitution(a,b):
    beta = 0
    n = a.shape[0]
    for k in list(reversed(range(n))):
        for j in range(k+1,n):
            beta = beta + a[k,j] * b[j]
        b[k] = (b[k] - beta)/ a[k,k]
        beta = 0

    return b


n = a.shape[0]
alpha = 0
for k in range(n-1):
    a_max = abs(a[k,k])
    ip = k
    for j in range(k+1,n):
        if a_max < abs(a[j,k]):
            a_max = abs(a[j,k])
            ip = j
    if a_max < 0.00001:
        print("aは正則でない")
    if ip != k:
        c = a[ip,]
        a[ip,] = a[k,]
        a[k,] = c
        b[k] = b[ip]
    for j in range(k + 1, n):
        alpha = a[j, k] / a[k, k]
        a[j,] = a[j,] - alpha * a[k,]
        b[j] = b[j] - alpha * b[k]

X = back_substitution(a,b)


print(X)

"""
print("与えられた行列は")
print(a)
print("与えられた定数項は")
print(b)
print("です.")
print("解は")
print(gauss_elimination(a,b))
print("となります.")

"""


