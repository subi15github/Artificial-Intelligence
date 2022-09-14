import math
def fun_Minmax(cd,nodev,maxt,scr,td):
    if(cd==td):
        return scr[nodev]
    if(maxt):
        return max(fun_Minmax(cd+1,nodev*2,False,scr,td),fun_Minmax(cd+1,nodev*2+1,False,scr,td))
    else:
        return min(fun_Minmax(cd+1,nodev*2,True,scr,td),fun_Minmax(cd+1,nodev*2+1,True,scr,td))

scr=[]
x=int(input("Enter total number of leaf nodes: "))
for i in range(x):
    y=int(input("Enter leaf value: "))
    scr.append(y)

td=math.log(len(scr),2)

cd=int(input("Enter current depth value: "))
nodev=int(input("Enter the node value: "))
maxt=True

print("The answer is: ")
answer=fun_Minmax(cd,nodev,maxt,scr,td)
print(answer)