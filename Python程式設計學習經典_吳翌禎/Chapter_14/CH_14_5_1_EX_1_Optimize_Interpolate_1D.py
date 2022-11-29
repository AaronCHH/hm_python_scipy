#----------------------------------------------
#   CH_14_5_1_EX_1_Optimize_Interpolate_1D.py   
#----------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as inter
#----- 原始數據
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.exp(-0.2*x)*np.cos(x)
#-------(1) 使用 interp1d 內插
g1 = inter.interp1d(x, y, kind='linear')
g2 = inter.interp1d(x, y, kind='quadratic')
g3 = inter.interp1d(x, y, kind='cubic')
#------(2) 使用 UnivariateSpline 內插
xnew = np.linspace(0, 10, num=41, endpoint=True)
spline1 = inter.InterpolatedUnivariateSpline(x, y)
spline1 = inter.InterpolatedUnivariateSpline(x, y, k=2)
spline1 = inter.InterpolatedUnivariateSpline(x, y, k=3)
ynew_spline1 = spline1(xnew)
ynew_spline2 = spline1(xnew)
ynew_spline3 = spline1(xnew)
#-----(3) 使用輻狀基(RBF) 內插
rbf1 = inter.Rbf(x, y)
ynew_rbf = rbf1(xnew)
#----- 繪圖比較
fig1 = plt.figure(1)
plt.subplot(1,3,1)
plt.plot(x, y, 'o', xnew, g1(xnew), '-', xnew, g2(xnew), '--', xnew, g3(xnew), '-.')
plt.xlabel('x')
plt.grid()
plt.legend(['data', 'linear', 'quadratic', 'cubic'], loc='best')
plt.title('interp1d')
#
plt.subplot(1,3,2)
plt.plot(x, y, 'o', xnew, ynew_spline1, '-', xnew, ynew_spline1, '--', xnew, ynew_spline1, '-.')
plt.xlabel('x')
plt.grid()
plt.legend(['data', 'spline(k=1)', 'spline(k=2)', 'spline(k=3)'], loc='best')   
plt.title('UnivariateSpline')
#
plt.subplot(1,3,3)
plt.plot(x, y, 'o', xnew, ynew_rbf, '-')
plt.xlabel('x')
plt.grid()
plt.legend(['data', 'rbf'], loc='best')   
plt.title('RBF')
#
plt.savefig('CH_14_5_1_EX_1_Interpolate_1D.png')
plt.show()























































	


