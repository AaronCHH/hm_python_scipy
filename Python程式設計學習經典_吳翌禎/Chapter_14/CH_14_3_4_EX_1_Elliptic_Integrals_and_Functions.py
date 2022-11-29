#-------------------------------------------------------
#   CH_14_3_4_EX_1_Elliptic_Integrals_and_Functions.py   
#-------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special as spec
#
phi1 = np.linspace(0., np.pi/2, 100)
m1 = np.linspace(0., 1., 100)
#----- 計算橢圓積分
EllipKinc_m01 = spec.ellipkinc(0.1, phi1)
EllipKinc_m05 = spec.ellipkinc(0.5, phi1)
EllipKinc_m10 = spec.ellipkinc(1.0, phi1)
#
EllipEinc_m01 = spec.ellipeinc(0.1, phi1)
EllipEinc_m05 = spec.ellipeinc(0.5, phi1)
EllipEinc_m10 = spec.ellipeinc(1.0, phi1)
#
EllipK = spec.ellipk(m1)
#
EllipE = spec.ellipe(m1)
#----- 繪圖
fig1 = plt.figure(1)
#
ax11 = plt.subplot(2,2,1)
plt.plot(phi1, EllipKinc_m01, 'b-', lw = 2, label = 'K(0.1, phi)')
plt.plot(phi1, EllipKinc_m05, 'b--', lw = 2, label = 'K(0.5, phi)')
plt.plot(phi1, EllipKinc_m10, 'b-.', lw = 2, label = 'K(1.0, phi)')
plt.title('ellipkinc(m, phi)')
plt.grid()
plt.legend(loc ='best')
ax11.get_xaxis().set_visible(False)
#
ax12 = plt.subplot(2,2,2)
plt.plot(phi1, EllipEinc_m01, 'b-', lw = 2, label = 'E(0.1, phi)')
plt.plot(phi1, EllipEinc_m05, 'b--', lw = 2, label = 'E(0.5, phi)')
plt.plot(phi1, EllipEinc_m10, 'b-.', lw = 2, label = 'E(1.0, phi)')
plt.grid()
plt.title('ellipeinc(m, phi)')
plt.legend(loc='best')
ax12.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(m1, EllipK, 'b-', lw = 2)
plt.xlabel('m')
plt.grid()
plt.title('ellipk(m)')
plt.axis([0, 1, 0, 4])
#
plt.subplot(2,2,4)
plt.plot(m1, EllipE, 'b-', lw = 2)
plt.xlabel('m')
plt.grid()
plt.title('ellipe(m)')
plt.axis([0, 1, 0, 2])
#
plt.savefig('CH_14_3_4_EX_1(a)_Elliptic Integrals.png')
plt.show()
#----- Jacobi Elliptic Functions
m2 = np.linspace(0., 0.9, 3)
u = np.linspace(0, 20, 201)
sn, cn, dn, phi = spec.ellipj(u[:, None], m2[None, :])
#----- 繪圖
fig2 = plt.figure(2)
#
ax21 = plt.subplot(2,2,1)
plt.plot(u, sn[:, 0], 'b-', lw = 2, label = 'm = 0.')
plt.plot(u, sn[:, 1], 'b--', lw = 2, label = 'm = 0.45')
plt.plot(u, sn[:, 2], 'b-.', lw = 2, label = 'm = 0.9')
#plt.plot([0, 20], [0, 0], 'k-')
plt.title('sn')
plt.grid()
plt.axis([0, 20, -1.2, 1.2])
ax21.get_xaxis().set_visible(False)
#
ax22 = plt.subplot(2,2,2)
plt.plot(u, cn[:, 0], 'b-', lw = 2, label = 'm = 0.')
plt.plot(u, cn[:, 1], 'b--', lw = 2, label = 'm = 0.45')
plt.plot(u, cn[:, 2], 'b-.', lw = 2, label = 'm = 0.9')
#plt.plot([0, 20], [0, 0], 'k-')
plt.grid()
plt.title('cn')
plt.axis([0, 20, -1.2, 1.2])
ax22.get_xaxis().set_visible(False)
#
plt.subplot(2,2,3)
plt.plot(u, dn[:, 0], 'b-', lw = 2, label = 'm = 0.')
plt.plot(u, dn[:, 1], 'b--', lw = 2, label = 'm = 0.45')
plt.plot(u, dn[:, 2], 'b-.', lw = 2, label = 'm = 0.9')
plt.grid()
plt.xlabel('u')
plt.title('dn')
plt.axis([0, 20, 0, 1.2])
#
plt.subplot(2,2,4)
plt.plot(u, phi[:, 0], 'b-', lw = 2, label = 'm = 0.')
plt.plot(u, phi[:, 1], 'b--', lw = 2, label = 'm = 0.45')
plt.plot(u, phi[:, 2], 'b-.', lw = 2, label = 'm = 0.9')
plt.grid()
plt.xlabel('u')
plt.title('phi')
plt.legend(loc='best')
plt.axis([0, 20, 0, 20])
#
plt.savefig('CH_14_3_4_EX_1(b)_Jacobi Elliptic Functions.png')
plt.show()


















































	


