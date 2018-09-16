# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:52:17 2018

@author: TheRealMentor
"""

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt

#Defining given parameters
A_c = 1      #Carrier Amplitude
f_c = 0.4    #Carrier Freq.
f_m = 0.05   #Modulation Freq.

#Defining time periods
T_c = 1/f_c  #Time period of carrier signal
T_m = 1/f_m  #Time period of modulating signal

t = np.arange(0, 200, 0.1)             #Defining the x-axis range

message = np.cos(2*np.pi*f_m*t)           #Defining message signal

#Defining function to create modulated signal
def modulate(message, A_c, f_c, n_u):
    c = A_c*np.cos(2*np.pi*f_c*t)

    mod = (1 + n_u*message)*c
    return mod

#Modulated Signals
sig_1 = modulate(message, A_c, f_c, 0.5)
sig_2 = modulate(message, A_c, f_c, 1)
sig_3 = modulate(message, A_c, f_c, 2)

# Time Domain Plots
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t, message)
plt.title("Message Signal")
plt.xlabel('$t$ (sec)')
plt.ylabel('$m(t)$')

plt.subplot(2,2,2)
plt.plot(t, sig_1)
plt.title("Modulated Signal ( $\mu = 0.5$ )")
plt.xlabel('$t$ (sec)')
plt.ylabel('$s_{1}(t)$')

plt.subplot(2,2,3)
plt.plot(t, sig_2)
plt.title("Modulated Signal ( $\mu = 1$ )")
plt.xlabel('$t$ (sec)')
plt.ylabel('$s_{2}(t)$')

plt.subplot(2,2,4)
plt.plot(t, sig_3)
plt.title("Modulated Signal ( $\mu = 2$ )")
plt.xlabel('$t$ (sec)')
plt.ylabel('$s_{3}(t)$')

plt.tight_layout()
plt.show()


# Frequency Domain Plots
plt.figure(2)
plt.subplot(3,1,1)
ft = np.fft.fft(sig_1)
ft = np.fft.fftshift(ft)
freq = np.fft.fftfreq(len(ft))
plt.plot(freq, np.absolute(ft))
plt.title("Modulated Signal ( $\mu = 0.5$ )")
plt.xlabel('$f$ (Hz)')
plt.ylabel('$S_{1}(f)$')

plt.subplot(3,1,2)
ft = np.fft.fft(sig_2)
ft = np.fft.fftshift(ft)
freq = np.fft.fftfreq(len(ft))
plt.plot(freq, np.absolute(ft))
plt.title("Modulated Signal ( $\mu = 1$ )")
plt.xlabel('$f$ (Hz)')
plt.ylabel('$S_{2}(f)$')

plt.subplot(3,1,3)
ft = np.fft.fft(sig_3)
ft = np.fft.fftshift(ft)
freq = np.fft.fftfreq(len(ft))
plt.plot(freq, np.absolute(ft))
plt.title("Modulated Signal ( $\mu = 2$ )")
plt.xlabel('$f$ (Hz)')
plt.ylabel('$S_{3}(f)$')

plt.tight_layout()
plt.show()
