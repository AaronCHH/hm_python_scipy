#--------------------------------------------
#   CH_14_4_1_EX_1_Optimize_Root_Finders.py   
#--------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
#----- 定義函數
def func1(x):
    f1 = np.cos(x)-x
    return f1
def func2(x):
    f2 = x**3 + x**2 - 5*x + 3.
    return f2
#----- 求解
solv1_root_obj = opt.root(func1, 0.)
solv1_newton = opt.newton(func1, 0.)
solv1_brentq = opt.brentq(func1, 0., 1.)
solv1_brenth = opt.brenth(func1, 0., 1.)
solv1_ridder = opt.ridder(func1, 0., 1.)
solv1_bisect = opt.bisect(func1, 0., 1.)
#
print('solv1_root_obj.x = ', solv1_root_obj.x)
print('solv1_newton = ', solv1_newton)
print('solv1_brentq = ', solv1_brentq)
print('solv1_brenth = ', solv1_brenth)
print('solv1_ridder = ', solv1_ridder)
print('solv1_bisect = ', solv1_bisect)
#
solv2_root_obj = opt.root(func2, 0.)
solv2_np_root = np.roots([1., 1., -5., 3.])
#
print('solv2_root_obj.x =', solv2_root_obj.x)
print('solv2_np_root =', solv2_np_root)




















































	


