#--------------------------------------
#   CH_14_3_6_EX_1_Error_Functions.py   
#--------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#
x1 = np.linspace(-3., 3., 100)
y1 = np.linspace(-1., 1., 100)
y2 = np.linspace(0., 2., 100)
#----- 計算誤差函數
Erf = spec.erf(x1)
Erfc = spec.erfc(x1)
Erfinv = spec.erfinv(y1)
Erfcinv = spec.erfcinv(y2)
#----- 繪圖
fig1 = plt.figure(1)
#
ax1 = plt.subplot(2,2,1)
plt.plot(x1, Erf, 'b-', lw = 2)
plt.title('erf')
plt.plot([-3, 3], [0., 0.])
plt.axis([-3, 3, -1, 1])
plt.legend(loc ='best')
ax1.get_xaxis().set_visible(False)
#
ax2 = plt.subplot(2,2,2)
plt.plot(x1, Erfc, 'b-', lw = 2)
plt.title('erfc')
plt.axis([-3, 3, 0, 2])
plt.legend(loc ='best')
ax2.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(y1, Erfinv, 'b-', lw = 2)
plt.xlabel('y')
plt.plot([-1, 1], [0., 0.])
plt.title('erfinv(y)')
plt.axis([-1, 1, -2, 2])
#
plt.subplot(2,2,4)
plt.plot(y2, Erfcinv, 'b-', lw = 2)
plt.xlabel('y')
plt.plot([0, 2], [0., 0.])
plt.title('erfcinv(y)')
plt.axis([0, 2, -3, 3])
#
plt.savefig('CH_14_3_6_EX_1_Error_Functions.png')
plt.show()


















































	


