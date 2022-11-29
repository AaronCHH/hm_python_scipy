#---------------------------------------------------
#   CH_14_6_1_EX_1_Integrate_Functions_1D_2D_3D.py   
#---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integ
#----- 定義被積分函數
def func1d(x):
    y = 1/x
    return y
#----- 各種1D 積分
I1_quad = integ.quad(func1d, 1., 2.)
I1_fixed_quad = integ.fixed_quad(func1d, 1., 2.)
I1_quadrature = integ.quadrature(func1d, 1., 2.)
I1_romberg = integ.romberg(func1d, 1., 2.)
x1 = np.linspace(1., 2., 9)
y1 = 1/x1
dx1 = (2.-1.)/8.
I1_trapz = integ.trapz(y1, x1)
I1_simps = integ.simps(y1, x1)
I1_romb = integ.romb(y1, dx1)
#
print('I1_quad = ', I1_quad)
print('I1_fixed_Gaussian_quad = ', I1_fixed_quad)
print('I1_Gaussian_quadrature = ', I1_quadrature)
print('I1_romberg = ', I1_romberg)
print('I1_trapz = ', I1_trapz)
print('I1_simps = ', I1_simps)
print('I1_romb = ', I1_romb)
#----- 2D 積分
I2_dblquad = integ.dblquad(lambda x, y: 1., 0, 1., lambda x: 0, lambda x: np.sqrt(1.-x**2))
print('I2_dblquad = ', I2_dblquad)
print('np.pi/4 = ', np.pi/4.)























































	


