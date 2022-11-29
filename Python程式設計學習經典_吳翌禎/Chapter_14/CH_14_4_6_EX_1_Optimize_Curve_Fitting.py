#---------------------------------------------
#   CH_14_4_6_EX_1_Optimize_Curve_Fitting.py   
#---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
#----- 定義函數
def func1(x, a, b):
    f = a * np.exp(b/x)
    return f
def func2(x, para):
    a, b = para
    f = a * np.exp(b/x)
    return f
#----- 定義殘差
def residual(para, y, x):
    res = 0.5*(y - func2(x, para))**2
    return res
#----- 原始數據
x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
y = np.array([6.42, 8.2, 9.58, 9.5, 9.7, 10, 9.93, 9.99, 10.49, 10.59, 10.6, 10.8, 10.6, 10.9, 10.76]) 
#----- 使用曲線調適
param_opt, cov_opt = opt.curve_fit(func1, x, y)
print('param_opt =', param_opt)
#----- 使用最小二乘法
p0 = (10, 1.)
res_lsq = opt.least_squares(residual, p0, args=(y, x))
print('res_lsq.x =', res_lsq.x)
#----- 繪圖
fig1 = plt.figure(1)
plt.plot(x, y, 'bo', label = 'data')
plt.plot(x, func1(x, *param_opt), 'r-',\
     label='fit_1: a=%5.3f, b=%5.3f' % tuple(param_opt))
plt.plot(x, func2(x, res_lsq.x), 'r--', lw = 2,\
         label='fit_2: a=%5.3f, b=%5.3f' % tuple(res_lsq.x))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('CH_14_4_6_EX_1_Curve_Fitting.png')
plt.show()























































	


