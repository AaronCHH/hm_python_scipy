#---------------------------------------------------------
#   CH_14_4_3_EX_1_Optimize_Minimize_Scalar_Functions.py   
#---------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
#----- 定義單變數函數 f
def func1(x):
    f = x**2 - 3 * x + 2.
    return f
#----- 定義單變數函數 f 及其導數 df
def func2(x):
    f = x**2 - 3 * x + 2.
    df = 2.*x - 3.
    return f, df
#------ 使用不同方法求解
min1_Nelder_Mead = opt.minimize(func1, 0., method = 'Nelder-Mead')
min1_Powell = opt.minimize(func1, 0., method = 'Powell')
min1_CG = opt.minimize(func1, 0., method = 'CG')
min1_BFGS = opt.minimize(func1, 0., method = 'BFGS')
min1_Newton_CG = opt.minimize(func2, 0., jac = 'None', method = 'Newton-CG')
min1_L_BFGS_B = opt.minimize(func1, 0., method = 'L-BFGS-B')
min1_TNC = opt.minimize(func1, 0., method = 'TNC')
min1_COBYLA = opt.minimize(func1, 0., method = 'COBYLA')
min1_SLSQP = opt.minimize(func1, 0., method = 'SLSQP')
#-----列出結果
print('min1_Nelder-Mead = ', min1_Nelder_Mead.x)
print('min1_Powell = ', min1_Powell.x)
print('min1_CG = ', min1_CG.x)
print('min1_BFGS = ', min1_BFGS.x)
print('min1_Newton-CG = ', min1_Newton_CG.x)
print('min1_L-BFGS-B = ', min1_L_BFGS_B.x)
print('min1_TNC = ', min1_TNC.x)
print('min1_COBYLA = ', min1_COBYLA.x)
print('min1_SLSQP = ', min1_SLSQP.x)
#-----使用函數極值檢核
min2_scalar = opt.minimize_scalar(func1)
print('min2_scalar =', min2_scalar)





















































	


