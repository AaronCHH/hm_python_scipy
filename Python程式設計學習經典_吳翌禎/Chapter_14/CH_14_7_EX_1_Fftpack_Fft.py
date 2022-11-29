#--------------------------------
#   CH_14_7_EX_1_Fftpack_Fft.py   
#--------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
#----- 定義函數
def func(t, k1, k2):
   y = np.sin(k1 * 2.0*np.pi*t) + 0.5*np.sin(k2 * 2.0*np.pi*t)
   return y
#----- 定義樣本點
N = 600
#----- 樣本間距及樣本點
T = 1.0 / 800.0
t = np.linspace(0.0, N*T, N)
k1 = 40.
k2 = 120.
#----- 執行fft
yt = func(t, k1, k2)
yf = fftpack.fft(yt)
f = np.linspace(0.0, 1.0/(2.0*T), N//2)
#----- 繪圖
fig1 = plt.figure(1)
plt.plot(f, 2.0/N * np.abs(yf[0:N//2]), 'b-', lw = 2)
plt.xlabel('f')
plt.ylabel('yf(f)')
plt.grid()
plt.savefig('CH_14_7_EX_1_Fftpack_Fft.png')
plt.show()

























































	


