import numpy as np
import matplotlib.pyplot as plt
from astroML.correlation import two_point
datos=np.genfromtxt("loadabletxt.csv",usecols=(2,3,4),delimiter=",")
mean=np.mean(datos[0],0)
LM=np.zeros((0,2))#low mass
HM=np.zeros((0,2))#hi mass

for i in xrange(np.shape(datos)[1]):
    if i==0:
        if datos[i][0]<=mean:
            LM=datos[i][1:]
        else:
            HM=datos[i][1:]
    else:
        if datos[i][0]<=mean:
            LM=np.append(LM,datos[i][1:],axis=0)
        else:
            HM=np.append(HM,datos[i][1:],axis=0)
#end for
bins=np.linspace(0,1,300)
cr1=two_point(LM,bins)
cr2=two_point(HM,bins)
plt.figure(1)
plt.plot(cr1,label="masas bajas simulacion")
plt.plot(cr2,label="masas altas simulacion")
plt.xscale("log")
plt.title("correlacion de masas")
plt.savefig("correlacion de masas.pdf")
