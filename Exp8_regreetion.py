#Linear Regression 2,4
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

x= np.array([1,2,3,4,5,6],dtype=float)
y = np.array([4,5,8,9,1,14],dtype=float)
y2= y.copy()
y2[-1]=18

for name, score in [("Original",y),("Modified",y2)]:
    xm,ym= np.mean(x), np.mean(score)
    m= np.sum((x-xm)*(score-ym)) / sum ((x-xm)**2)
    c= ym-m*xm
    pred= c+ m*x
    r2= 1 - np.sum ((score-pred)**2) / np.sum ((score- ym)**2)

    print ('\n',name,'Data')
    print('\nSlope= ',round(m,4))
    print('\nIntercept= ',round(c,4))
    print('\nR2= ',round(r2,4))
    print('\nPredict at 7 hours= ',round(c+m*7,4))

    if name == "Original":
        m1,c1 =m, c
    else:
        m2,c2 =m, c

plt.scatter(x,y,label="Original")
plt.scatter(x,y2,label="Modified",marker="x")
plt.plot(x,c1+m1*x,label="Original line")
plt.plot(x,c2+m2*x,label="Modified line")
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()

