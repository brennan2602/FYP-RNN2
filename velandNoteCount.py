import numpy as np
import matplotlib.pyplot as plt

with open('dataNotes.txt') as f:
    lines = f.readlines()
outString1=""
for l in lines:
	if len(l.strip()) != 0:
		outString1=outString1+l
notes=outString1.split("\n")

with open('dataVel.txt') as f:
    lines = f.readlines()
outString2=""
for l in lines:
	if len(l.strip()) != 0:
		outString2=outString2+l
velocities=outString2.split("\n")

def getCount(file):
    l=[]
    Arr=np.zeros(128)
    for i in file:
        val=i.split(" ")
        clipped=val[0:-1]
        values= np.array(clipped)
        for v in values:
            #print(v)
            v=float(v)
            v=int(v)
            if v> 127 or v < 1:
                v= 0
            l.append(v)
    #print(l)
    for v in l:
        Arr[v]=Arr[v]+1
    print(Arr)
    return Arr
noteSpread=getCount(notes)
velSpread=getCount(velocities)
fig1 = plt.figure(1)
x = np.arange(128)
plt.bar(x, height= velSpread)
#plt.xticks()

fig2 = plt.figure(2)
x = np.arange(128)
plt.bar(x, height= noteSpread)
#plt.xticks()
fig1.show()
fig2.show()

plt.show()
