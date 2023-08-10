import numpy as np
cost=np.array([40,20,30])
qu=np.array([2,3,1])
dis=8
tax=7
for i in range(len(cost)):
    tot=cost*qu
    tot1=tot-tot*(dis/100)
    tot2=tot1+tot1*(tax/100)
    total=sum(tot2)
    

print("total purchased amount after discount and tax added :",total)
