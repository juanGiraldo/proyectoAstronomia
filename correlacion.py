import numpy as np
import matplotlib.pyplot as plt
from astroML.correlation import two_point
datos=np.genfromtxt("loadabletxt.csv",usecols=(2,3,4),delimiter=",")
media = np.median(datos[:,0])

ii = datos[:,0] > media
HM = datos[ii,1:3]
LM = datos[~ii,1:3]
print np.shape(HM)


bins=np.linspace(1E-4,10.0,30)
cr1=two_point(LM,bins)
cr2=two_point(HM,bins)
plt.figure(1)
plt.plot(cr1,label="masas bajas simulacion")
plt.plot(cr2,label="masas altas simulacion")
plt.xscale("log")
plt.title("correlacion de masas")
plt.savefig("correlacion_masas.pdf")
