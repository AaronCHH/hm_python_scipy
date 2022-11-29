#-------------------------------------
#   CH_14_3_3_EX_1_Gamma_Function.py   
#-------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#----- 計算Gamma 函數
x1 = np.linspace(-5., 3., 100)
Gamma = spec.gamma(x1)
Factorial = spec.gamma(x1+1.)
GammaSign = spec.gammasgn(x1)
LogGamma = spec.loggamma(x1)
#----- 繪圖
fig1 = plt.figure(1)
#
ax1 = plt.subplot(2,2,1)
plt.plot(x1, Gamma, 'b-', lw = 2)
plt.plot([-5, 3], [0, 0], 'k-')
plt.plot([0, 0], [-20, 20], 'k-')
plt.title('gamma')
plt.axis([-5, 3, -2, 5])
ax1.get_xaxis().set_visible(False)
#
ax2 = plt.subplot(2,2,2)
plt.plot(x1, Factorial, 'b-', lw = 2)
plt.plot([-5, 3], [0, 0], 'k-')
plt.plot([0, 0], [-5, 5], 'k-')
plt.title('gamma(x+1)=x!')
plt.axis([-5, 3, -2, 5])
ax2.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(x1, GammaSign, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-5, 5], [0, 0], 'k-')
plt.plot([0, 0], [-5, 5], 'k-')
plt.title('gammasgn')
plt.axis([-5, 3, -2, 5])
#
plt.subplot(2,2,4)
plt.plot(x1, LogGamma, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-5, 3], [0, 0], 'k-')
plt.plot([0, 0], [-5, 5], 'k-')
plt.title('loggamma')
plt.axis([-5, 3, -2, 5])
#
plt.savefig('CH_14_3_3_EX_1_Gamma Function.png')
plt.show()

















































	


