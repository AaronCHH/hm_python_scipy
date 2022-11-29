#----------------------------------------------
#   CH_14_5_2_EX_1_Optimize_Interpolate_2D.py   
#----------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as inter
#-----定義雙變數函數
def func(x, y):
    z = np.exp(-(x**2+y**2))
    return z
x, y = np.mgrid[-1:1:20j, -1:1:20j]
z = func(x, y)
#-----(1) 使用interp2d 內插
g3_interp2d = inter.interp2d(x, y, z, kind='cubic')
#
xnew = np.linspace(-1, 1, 101)
ynew = np.linspace(-1, 1, 101)
znew_interp2d_3 = g3_interp2d(xnew, ynew)
#-----(2) 使用輻狀基 (RBF) 內插
ti = np.linspace(-1.0, 1.0, 100)
XI, YI = np.meshgrid(ti, ti)
rbf1 = inter.Rbf(x, y, z, epsilon=2)
znew_rbf = rbf1(XI, YI)
#----- 繪圖比較
fig1 = plt.figure(1)
#
plt.subplot(1,3,1)
plt.pcolor(x, y, z)
plt.xlabel('x')
plt.ylabel('y')
plt.title('data')
plt.axis('square')
#
plt.subplot(1,3,2)
plt.pcolor(xnew, ynew, znew_interp2d_3)
plt.xlabel('x')
plt.title('interp2d')
plt.axis('square')
#
plt.subplot(1,3,3)
plt.pcolor(XI, YI, znew_rbf)
plt.xlabel('x')
plt.title('RBF')
plt.axis('square')
#
plt.savefig('CH_14_5_2_EX_1_Interpolate_2D.png')
plt.show()























































	


