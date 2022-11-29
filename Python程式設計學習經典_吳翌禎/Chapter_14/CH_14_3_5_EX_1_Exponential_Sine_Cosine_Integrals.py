#--------------------------------------------------------
#   CH_14_3_5_EX_1_Exponential_Sine_Cosine_Integrals.py   
#--------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#
x1 = np.linspace(0., 2., 100)
x2 = np.linspace(0., 15., 100)
#-----計算指數積分
Expi = spec.expi(x1)
Expn_1 = spec.expn(1, x1)
Expn_2 = spec.expn(2, x1)
Expn_5 = spec.expn(5, x1)
#----- 計算正弦與餘弦積分
Si, Ci = spec.sici(x2)
#----- 繪圖
ax11 = plt.subplot(2,2,1)
plt.plot(x1, Expn_1, 'b-', lw = 2, label = 'expn(1, x)')
plt.plot(x1, Expn_2, 'b--', lw = 2, label = 'expn(2, x)')
plt.plot(x1, Expn_5, 'b-.', lw = 2, label = 'expn(5, x)')
plt.grid()
plt.title('expn(n, x)')
plt.legend(loc='best')
ax11.get_xaxis().set_visible(False)
#
ax12 = plt.subplot(2,2,2)
plt.plot(x1, Expi, 'b-', lw = 2, label = 'K(0.1, phi)')
plt.plot([0.,2.], [0., 0.], 'k-')
plt.title('expi(x)')
plt.grid()
ax12.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(x2, Si, 'b-', lw = 2)
plt.plot([0., 15], [0., 0.], 'k-')
plt.xlabel('x')
plt.grid()
plt.title('Si(x)')
plt.axis([0, 15, -2, 2])
#
plt.subplot(2,2,4)
plt.plot(x2, Ci, 'b-', lw = 2)
plt.plot([0., 15], [0., 0.], 'k-')
plt.xlabel('x')
plt.grid()
plt.title('Ci(x)')
plt.axis([0, 15, -1, 1])
#
plt.savefig('CH_14_3_5_EX_1_Exponential_Sine_Cosine_Integrals.png')
plt.show()


















































	


