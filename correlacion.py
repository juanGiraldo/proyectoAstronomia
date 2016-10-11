import numpy as np
import matplotlib.pyplot as plt
from astroML.correlation import two_point
datos=np.genfromtxt("loadabletxt.csv",usecols=(2,3,4),delimiter=",")
error=np.genfromtxt("standard correlation.1")
media = np.median(datos[:,0])

ii = datos[:,0] > media
HM = datos[ii,1:3]
LM = datos[~ii,1:3]
xerr=0.1#error[:,2]
yerr=0.01#error[:,3]
print np.shape(HM)


bins=np.linspace(1E-4,10.0,30)
cr1=two_point(LM,bins)
cr2=two_point(HM,bins)
plt.figure(1)
plt.plot(cr1,label="masas bajas simulacion")
plt.scatter(error[:,0],error[:,1])
#plt.errorbar(error[:,0],error[:,1],xerr=xerr,yerr=yerr)
plt.plot(cr2,label="masas altas simulacion")
plt.xscale("log")
plt.title("correlacion de masas")
plt.savefig("correlacion_masas_con_error.pdf")
