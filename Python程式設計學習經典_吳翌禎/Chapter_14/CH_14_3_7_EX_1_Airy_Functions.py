#-------------------------------------
#   CH_14_3_7_EX_1_Airy_Functions.py   
#-------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#
x = np.linspace(-15., 5., 200)
#----- 計算 Airy 函數
Ai, Aid, Bi, Bid = spec.airy(x)
#----- 繪圖
fig1 = plt.figure(1)
#
ax1 = plt.subplot(2,2,1)
plt.plot(x, Ai, 'b-', lw = 2)
plt.title('Ai(x)')
plt.plot([-15, 5], [0., 0.])
plt.axis([-15, 5, -1, 1])
plt.legend(loc ='best')
plt.grid()
ax1.get_xaxis().set_visible(False)
#
ax2 = plt.subplot(2,2,2)
plt.plot(x, Bi, 'b-', lw = 2)
plt.title('Bi')
plt.plot([-15, 5], [0., 0.])
plt.axis([-15, 5, -1, 1])
plt.legend(loc ='best')
plt.grid()
ax2.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(x, Aid, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-15, 5], [0., 0.])
plt.title('d(Ai)/dx')
plt.grid()
plt.axis([-15, 5, -2, 2])
#
plt.subplot(2,2,4)
plt.plot(x, Bid, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-15, 5], [0., 0.])
plt.title('d(Bi)/dx')
plt.grid()
plt.axis([-15, 5, -2, 2])
#
plt.savefig('CH_14_3_7_EX_1_Airy_Functions.png')
plt.show()



















































	


