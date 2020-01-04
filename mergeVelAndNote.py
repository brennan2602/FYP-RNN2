import numpy as np

with open('generatedNotes.txt') as f:
    lines = f.readlines()
outString=""
for l in lines:
    if len(l.strip()) != 0:
        outString=outString+l

with open('generatedVel.txt') as f:
    lines = f.readlines()
outString2=""
for l in lines:
    if len(l.strip()) != 0:
        outString2=outString2+l


output=outString.split("\n")
arr=np.zeros((128,len(output)))
print(arr.shape)
j=0
for i in arr.T:
    if output[j].find("#") <0:
        val=output[j]
        #print(val)
        internal=val.split(" ")
        clipped = internal[0:-1]
        for v in clipped:
            index= float(v)
            index=int(index)
            if index>127 or index<1:
                index=0
            i[index]=-1
    j=j+1
output=outString2.split("\n")

l=[]
for i in output:
    val=i.split(" ")
    clipped=val[0:-1]
    vels= np.array(clipped)
    for v in vels:
        v=float(v)
        v=int(v)
        if v> 127 or v < 1:
            v= 0
        l.append(v)
index=0
for i in arr.T:
    for j in range(len(i)):
        if i[j] ==-1:
            i[j]=l[index]
            index+=1
            if index>=len(l):
                index=0
np.savetxt("arrayafter.txt", arr, fmt="%s")