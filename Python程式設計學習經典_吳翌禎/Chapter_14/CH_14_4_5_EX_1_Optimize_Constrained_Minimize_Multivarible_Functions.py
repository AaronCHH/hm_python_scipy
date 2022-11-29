#--------------------------------------------------------------------
# CH_14_4_5_EX_1_Optimize_Constrained_Minimize_Multivarible_Functions.py
#--------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
#-----定義雙變數函數 f 
def func(x, sign = 1.0):
    f = sign *(x[0]**2 + x[1]**2)
    return f
#-----定義雙變數函數 f 及其導數 df
def func_deriv(x, sign = 1.0):
    dfdx0 = sign * (2.*x[0])
    dfdx1 = sign * (2.*x[1])
    df = np.array([dfdx0, dfdx1])
    return df
#-----限制式
cons = ({'type': 'eq',\
         'fun' : lambda x: np.array([x[0] + x[1] - 2.]),\
         'jac' : lambda x: np.array([1.0, 1.0])})
#------ 計算 (1) 無限制式極小值
min1_unconstrained_SLSQP = opt.minimize(func, [0.0, 0.0], args=(-1.0,), jac=func_deriv, method='SLSQP', options={'disp': True})
#
print('min1_unconstrained_SLSQP = ', min1_unconstrained_SLSQP.x)
#-------計算 (2) 有限制式極小值
min2_constrained_SLSQP = opt.minimize(func, [-0.0, 0.0], args=(-1.0,), jac=func_deriv,
                constraints = cons,method='SLSQP', options={'disp': True})
print('min2_constrained_SLSQP = ', min2_constrained_SLSQP.x)






















































	


