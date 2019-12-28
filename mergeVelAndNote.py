import numpy as np

with open('dataNotes.txt') as f:
    lines = f.readlines()
outString=""
for l in lines:
	if len(l.strip()) != 0:
		outString=outString+l

with open('dataVel.txt') as f:
    lines = f.readlines()
outString2=""
for l in lines:
	if len(l.strip()) != 0:
		outString2=outString2+l

#print(outString)
output=outString.split("\n")
arr=np.zeros((128,len(output)))
print(arr.shape)
j=0
for i in arr.T:
    #print(i)
    #print(output)
    #print(output[j])
    if output[j].find("#") <0:
        val=output[j]
        #print(val)
        internal=val.split(" ")
        clipped = internal[0:-1]
        # if len(clipped)>1:
        #     print(clipped)
        # else:
        #     print(clipped)

        for v in clipped:
            #if v != " ":
            index= float(v)
            index=int(index)
            if index>127 or index<1:
                index=0
            #print(index)
            i[index]=-1
    #print(arr)
    j=j+1
np.savetxt("arraybefore.txt", arr, fmt="%s")
output=outString2.split("\n")
#print(output)
l=[]
for i in output:
    val=i.split(" ")
    clipped=val[0:-1]
    vels= np.array(clipped)
    #newArr=vels.flatten()
    for v in vels:
        #print(v)
        v=float(v)
        v=int(v)
        if v> 127 or v < 1:
            v= 0
        l.append(v)
#print(l)
index=0
for i in arr.T:
    for j in range(len(i)):
        if i[j] ==-1:
            i[j]=l[index]
            index+=1
            if index>=len(l):
                index=0
np.savetxt("arrayafter.txt", arr, fmt="%s")