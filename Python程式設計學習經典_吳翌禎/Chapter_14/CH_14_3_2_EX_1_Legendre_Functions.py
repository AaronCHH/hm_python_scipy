#-----------------------------------------
#   CH_14_3_2_EX_1_Legendre_Functions.py   
#-----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#
x = np.linspace(-1., 1., 100)
#
poly_1 = spec.legendre(1)
P1 = poly_1[1]*x + poly_1[0]
#
poly_2 = spec.legendre(2)
P2 = poly_2[2]*x**2 + poly_2[1]*x + poly_2[0]
#
poly_3 = spec.legendre(3)
P3 = poly_3[3]*x**3 + poly_3[2]*x**2 + poly_3[1]*x + poly_3[0]
#
poly_4 = spec.legendre(4)
P4 = poly_4[4]*x**4 + poly_4[3]*x**3 + poly_4[2]*x**2 + poly_4[1]*x + poly_4[0]
#
plt.figure(1)
#
ax11 = plt.subplot(2,2,1)
plt.plot(x, P1, 'b-', lw = 2)
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1, 1], 'k-')
plt.grid()
plt.title('P1(x)')
ax11.get_xaxis().set_visible(False)
#
ax12 = plt.subplot(2,2,2)
plt.plot(x, P2, 'b-', lw = 2)
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1, 1], 'k-')
plt.title('P2(x)')
plt.grid()
ax12.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(x, P3, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1, 1], 'k-')
plt.title('P3(x)')
plt.grid()
#
plt.subplot(2,2,4)
plt.plot(x, P4, 'b-', lw = 2)
plt.xlabel('x')
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1, 1], 'k-')
plt.title('P4(x)')
plt.grid()
#
plt.savefig('CH_14_3_2_EX_1_Legendre Functions.png')
plt.show()
















































	


