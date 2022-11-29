#--------------------------------------------
#   CH_14_6_2_EX_1_Integrate_ODE_Solvers.py   
#--------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integ
#----- 定義狀態方程式
def state(Z, t, omega, ):
    q1, q2 = Z
    dZdt = [q2, -omega**2*q1]
    return dZdt
#
g = 9.81
L = 1.
omega = np.sqrt(g/L)
Z0 = [0.1, 0.]
t = np.linspace(0., 10., 101)
#----- 微分方程數值解
sol_odeint = integ.odeint(state, Z0, t, args =(omega,))
#----- 微分方程嚴密解
q1_exact = 0.1*np.cos(omega*t)
q2_exact = -0.1*omega*np.sin(omega*t)
#----- 繪圖比較
fig1 = plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t, sol_odeint[:, 0], 'b--', label='odeint')
plt.plot(t, q1_exact, 'r-', label='exact')
plt.ylabel(r'$\theta$')
plt.grid()
plt.legend(loc=1)
#
plt.subplot(2,1,2)
plt.plot(t, sol_odeint[:, 1], 'b-')
plt.plot(t, q2_exact, 'r-')
plt.xlabel('t')
plt.ylabel(r'$d(\theta/dt$')
plt.grid()
#
plt.savefig('CH_14_6_2_EX_1_ODE_Solvers.png')
plt.show()
























































	


