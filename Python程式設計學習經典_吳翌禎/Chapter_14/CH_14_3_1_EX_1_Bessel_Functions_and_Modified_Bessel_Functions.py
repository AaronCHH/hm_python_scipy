#--------------------------------------------------------------------
#   CH_14_3_1_EX_1_Bessel_Functions_and_Modified_Bessel_Functions.py
#--------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#----- Bessel 函數
x1 = np.linspace(0.01, 10, 100)
x2 = np.linspace(0.1, 10, 100)
x3 = np.linspace(0.4, 10, 100)
x4 = np.linspace(0.9, 10, 100)
x5 = np.linspace(0.1, 3, 30)
x6 = np.linspace(0.4, 3, 30)
Bessel_j0 = spec.j0(x1)
Bessel_j1 = spec.j1(x1)
Bessel_j2 = spec.jn(2, x1)
#
Bessel_y0 = spec.y0(x2)
Bessel_y1 = spec.y1(x3)
Bessel_y2 = spec.yn(2, x4)
#----- Bessel 修正函數
Bessel_i0 = spec.i0(x5)
Bessel_i1 = spec.i1(x5)
#
Bessel_k0 = spec.k0(x5)
Bessel_k1 = spec.k1(x6)
#----- 繪圖
plt.figure(1)
#
plt.subplot(2,2,1)
plt.plot(x1, Bessel_j0, 'b-', lw = 2, label = 'J0')
plt.plot(x1, Bessel_j1, 'b--', lw = 2, label = 'J1')
plt.plot(x1, Bessel_j2, 'b-.', lw = 2, label = 'J2')
plt.xlabel('x')
plt.plot([0, 10], [0, 0], 'k-')
plt.plot([0, 0], [-2, 1], 'k-')
plt.legend(loc = 'best')
#
plt.subplot(2,2,2)
plt.plot(x2, Bessel_y0, 'b-', lw = 2, label = 'Y0')
plt.plot(x3, Bessel_y1, 'b--', lw = 2, label = 'Y1')
plt.plot(x4, Bessel_y2, 'b-.', lw = 2, label = 'Y2')
plt.xlabel('x')
plt.plot([0, 10], [0, 0], 'k-')
plt.plot([0, 0], [-2, 0.5], 'k-')
plt.legend(loc = 'best')
#
plt.subplot(2,2,3)
plt.plot(x5, Bessel_i0, 'b-', lw = 2, label = 'I0')
plt.plot(x5, Bessel_i1, 'b--', lw = 2, label = 'I1')
#
plt.xlabel('x')
plt.plot([0, 3], [0, 0], 'k-')
plt.plot([0, 0], [0, 5], 'k-')
plt.legend(loc = 'best')
#
plt.subplot(2,2,4)
plt.plot(x5, Bessel_k0, 'b-', lw = 2, label = 'K0')
plt.plot(x6, Bessel_k1, 'b--', lw = 2, label = 'K1')
#
plt.xlabel('x')
plt.plot([0, 3], [0, 0], 'k-')
plt.plot([0, 0], [0, 3], 'k-')
plt.legend(loc = 'best')
plt.savefig('CH_14_3_1_EX_1_Bessel and Modified Bessel Functions.png')
plt.show()
#----- 列出 jn(n, k) 的零點
for kk in range(0, 10):
    print('jn_zeros(0,', kk, ') =', spec.jn_zeros(0, 10)[kk])
for kk in range(0, 10):
    print('jn_zeros(1,', kk, ') =', spec.jn_zeros(1, 10)[kk])
for kk in range(0, 10):
    print('jn_zeros(2,', kk, ') =', spec.jn_zeros(2, 10)[kk])
#----- 列出 yn(n, k) 的零點
for kk in range(0, 10):
    print('yn_zeros(0,', kk, ') =', spec.yn_zeros(0, 10)[kk])
for kk in range(0, 10):
    print('yn_zeros(1,', kk, ') =', spec.yn_zeros(1, 10)[kk])
for kk in range(0, 10):
    print('yn_zeros(2,', kk, ') =', spec.yn_zeros(2, 10)[kk])
















































	


