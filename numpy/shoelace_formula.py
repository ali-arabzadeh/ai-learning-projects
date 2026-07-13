import numpy as np 
import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
ras = list(map(int, data[1:]))
p = np.array(ras).reshape(n, 2)

total_det = 0 
for i in range(n):
    x1 , y1 = p[i]
    x2 , y2 = p[(i+1) % n]
    mat = np.array([[x1 , x2],[y1 , y2]])
    total_det += np.linalg.det(mat)

masahat = abs(total_det) / 2 
print (f"{masahat:.1f}")

