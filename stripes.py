import numpy as np
import matplotlib.pyplot as plt

r=31.8/2
a=90-72.5 #degree
h=20

print "radius = ",r
print "angle = ",a," degree"
print "height = ",h

X = np.linspace(0,(2*np.pi+1)*r,num=300)
Yu = r*np.tan(a/180*np.pi)*(1-np.cos(X/r))
Yo = r*np.tan(a/180*np.pi)*(1-np.cos(X/r))+h

fig=plt.figure(figsize=(16,7))
ax=fig.add_subplot(111)

ax.set_xlim(0,(2*np.pi+1)*r)
ax.set_aspect(1)
#plt.subplots_adjust(left=0.0, bottom=0.0, right=1.0, top=1.0, wspace=0.0, hspace=0.0)

plt.plot(X,Yu)
plt.plot(X,Yo)
plt.show()
