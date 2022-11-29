#--------------------------------------------------------------------
#  CH_14_4_2_EX_1_Optimize_Root_Finders_Simultaneous_Nonlinear_Eqs.py
#--------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
#----- 定義二變量純量函數 f 及其導數 df
def func(x):
    f = [x[0] - np.sin(x[0]+x[1]),\
         x[1] - np.cos(x[0]-x[1]) ]
    df = np.array([[1. - np.cos(x[0]+x[1]), -np.cos(x[0]+x[1])],\
                   [np.sin(x[0]-x[1]), 1. - np.cos(x[0]-x[1])]])
    return f, df
#----- 求解
solv1_root_hybr_obj = opt.root(func, [1, 1], jac=True, method='hybr')
solv1_root_lm_obj = opt.root(func, [1, 1], jac=True, method='lm')
#
print('solv1_root_hybr_obj.x = ', solv1_root_hybr_obj.x)
print('solv1_root_lm_obj.x = ', solv1_root_lm_obj.x)





















































	


