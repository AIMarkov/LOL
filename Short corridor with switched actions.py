import xlsxwriter
import numpy as np
S=[0,1,2,3]
stateValue=[0.5,0.5,0.5,0.5]
reward=-1
epsilon=0.1
startstate=1
run=range(500)
book=xlsxwriter.Workbook('data')
sheet=book.add_worksheet('data')
k=0
for i in S:
    sheet.write(k,i,'状态'+str(i))
k+=1
for i in run:#(1-epsilon/2)right
    for s in S:
        if s==3:
            break
        elif s==1:
            stateValue[s]=(1-epsilon/2)*(reward+stateValue[s-1])+(epsilon/2)*(reward+stateValue[s+1])
        elif s==0:
            stateValue[s]=(1-epsilon/2)*(reward+stateValue[s+1])+(epsilon/2)*(reward+stateValue[s])
        elif s==2:
            stateValue[s] = (1 - epsilon / 2) * (reward + stateValue[s + 1]) + (epsilon / 2) * (reward + stateValue[s-1])
        sheet.write(k,s,stateValue[s])
    k=k+1
print(stateValue)

for i in S:
    sheet.write(k,i,'状态'+str(i))
k+=1
for i in run:#(1-epsilon/2)left
    for s in S:
        if s==3:
            break
        elif s==1:
            stateValue[s]=(1-epsilon/2)*(reward+stateValue[s+1])+(epsilon/2)*(reward+stateValue[s-1])
        elif s==0:
            stateValue[s]=(1-epsilon/2)*(reward+stateValue[s])+(epsilon/2)*(reward+stateValue[s+1])
        elif s==2:
            stateValue[s] = (1 - epsilon / 2) * (reward + stateValue[s - 1]) + (epsilon / 2) * (reward + stateValue[s+1])
        sheet.write(k,s,stateValue[s])
    k+=1
print(stateValue)


sheet.write(k,0,'probobilityOfright')
sheet.write(k,1,'状态'+str(0))
probobility=np.arange(0.02,0.99,0.01)  #right
k+=1
for E in probobility:
    for i in run:#(epsilon)right
        for s in S:
            if s==3:
                break
            elif s==1:
                stateValue[s]=(E)*(reward+stateValue[s-1])+(1-E)*(reward+stateValue[s+1])
            elif s==0:
                stateValue[s]=(E)*(reward+stateValue[s+1])+(1-E)*(reward+stateValue[s])
            elif s==2:
                stateValue[s] = (E) * (reward + stateValue[s + 1]) + (1-E) * (reward + stateValue[s-1])
    sheet.write(k,0,E)
    sheet.write(k,1,stateValue[0])
    k=k+1


book.close()


