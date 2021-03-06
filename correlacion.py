import numpy as np
import matplotlib.pyplot as plt
from astroML.correlation import two_point
datos=np.genfromtxt("loadabletxt.csv",usecols=(2,3,4),delimiter=",")
error=np.genfromtxt("standard correlation.1",dtype='float',skip_header=1)
points=np.genfromtxt("standard correlation.1",dtype='float',skip_header=1)

media = np.median(datos[:,0])

ii = datos[:,0] > media
HM = datos[ii,1:3]
LM = datos[~ii,1:3]
xerr=np.transpose(error[:,2:4])
yerr=np.transpose(error[:,4:])
x=points[:30,0]
y=points[:30,1]


bins=np.linspace(1E-4,10.0,30)
cr1=two_point(LM,bins,method='landy-szalay')
cr2=two_point(HM,bins,method='landy-szalay')
print np.shape(cr1),np.shape(cr2)
plt.figure(1)
plt.plot(cr1,label="masas bajas simulacion")
#plt.scatter(x+5,y)
plt.errorbar(x,y/x,np.abs(xerr),np.abs(yerr),fmt='')
plt.plot(cr2,label="masas altas simulacion")
#plt.xscale("log")
plt.yscale("log")
plt.title("correlacion de masas")
plt.xlabel(r'$s[h^{-1} Mpc]$')
plt.ylabel(r'$\xi(s)$')
plt.legend (loc='best')
plt.savefig("correlacion_masas_con_error2.pdf")
