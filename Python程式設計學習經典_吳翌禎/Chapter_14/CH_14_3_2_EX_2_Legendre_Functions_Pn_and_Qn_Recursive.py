#-------------------------------------------------------------
#   CH_14_3_2_EX_2_Legendre_Functions_Pn_and_Qn_Recursive.py   
#-------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#----- 定義函數 Legendre_P(n, x)
def Legendre_P(n, x):
    if n == 0:
        Pn = 1
    elif n == 1:
        Pn = x
    else:
        Pn =(1/n)* ((2*n-1)*x*Legendre_P(n-1, x) - (n-1)* Legendre_P(n-2, x))
    return Pn
#----- 定義函數 Legendre_Q(n, x)
def Legendre_Q(n, x):
    if n == 0:
        Qn = np.log((1.+x)/(1.-x))/2.
    elif n == 1:
        Qn = x*np.log((1.+x)/(1.-x))/2.-1.
    else:
        Qn =(1/n)* ((2*n-1)*x*Legendre_Q(n-1, x) - (n-1)* Legendre_Q(n-2, x))
    return Qn
x = np.linspace(-1., 1., 101)
P0 = np.zeros(101)
P1 = np.zeros(101)
P2 = np.zeros(101)
P3 = np.zeros(101)
P4 = np.zeros(101)
Q0 = np.zeros(101)
Q1 = np.zeros(101)
Q2 = np.zeros(101)
Q3 = np.zeros(101)
Q4 = np.zeros(101)
#----- 計算 P0~P4
for ii in range(0, 101):
    P0[ii] = Legendre_P(0, x[ii])
    P1[ii] = Legendre_P(1, x[ii])
    P2[ii] = Legendre_P(2, x[ii])
    P3[ii] = Legendre_P(3, x[ii])
    P4[ii] = Legendre_P(4, x[ii])
#----- 計算 Q0~Q4
    Q0[ii] = Legendre_Q(0, x[ii])
    Q1[ii] = Legendre_Q(1, x[ii])
    Q2[ii] = Legendre_Q(2, x[ii])
    Q3[ii] = Legendre_Q(3, x[ii])
    Q4[ii] = Legendre_Q(4, x[ii])
#----- 繪圖
plt.figure(1)
ax11 = plt.subplot(2,1,1)
plt.plot(x, P0, 'r-', lw = 2, label = 'n = 0')
plt.plot(x, P1, 'g--', lw = 2, label = 'n = 1')
plt.plot(x, P2, 'b-.', lw = 2, label = 'n =2')
plt.plot(x, P3, 'k-', lw = 2, label = 'n = 3')
plt.plot(x, P4, 'm-', lw = 2, label = 'n = 4')
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1, 2], 'k-')
plt.xlabel('x')
plt.grid()
plt.legend(loc=1)
plt.title('Pn(x)')
plt.axis([-1., 1., -1., 2])
ax11.get_xaxis().set_visible(False)
#
ax12 = plt.subplot(2,1,2)
plt.plot(x, Q0, 'r-', lw = 2)
plt.plot(x, Q1, 'g--', lw = 2)
plt.plot(x, Q2, 'b-.', lw = 2)
plt.plot(x, Q3, 'k-', lw = 2)
plt.plot(x, Q4, 'm-', lw = 2)
plt.title('Qn(x)')
plt.xlabel('x')
plt.plot([-1, 1], [0, 0], 'k-')
plt.plot([0, 0], [-1.5, 1.5], 'k-')
plt.grid()
plt.axis([-1, 1, -1.5, 1.5])
plt.title('Qn(x)')
plt.grid()
plt.savefig('CH_14_3_2_EX_2_Legendre Functions_Pn_and_Qn_Recursive.png')
plt.show()

















































	


