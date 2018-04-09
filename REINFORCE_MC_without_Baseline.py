#交叉熵上面是没有问题的但是可能Gt的运算上面有问题，此外，关于Gt为何归一化
import numpy as np
from torch.autograd import Variable
import torch.nn as nn
import torch

class NNnet(nn.Module):
    def __init__(self):
        super(NNnet,self).__init__()
        self.module_net()

    def module_net(self):
        self.layer1 = nn.Sequential(nn.Linear(4, 10), nn.ReLU())
        self.layer2 =nn.Sequential(nn.Linear(10,5),nn.Tanh())
        self.layer3 = nn.Sequential(nn.Linear(5,2))

    def forward(self, obs):
        y = self.layer1(obs)
        y = self.layer2(y)
        y = self.layer3(y)
        return y


#传入的是一串轨迹和

class REINFORCE_Agent:
    def __init__(self):
        self.mod=NNnet()
        self.obs=[]
        self.acts=[]
        self.ret=[]

    def store_transition(self,o,a,r):
        self.obs.append(o)
        self.acts.append(a)
        self.ret.append(r)

    # def Loss(self,y1,y2,G):
    #     loss1=nn.CrossEntropyLoss(y1,y2)  #交叉熵作为分类输入是（N,c）二维，target是1维的
    #     #print("loss1",loss1)
    #     #loss=loss1*G
    #     return loss

    def learn(self):
        print("actions:",len(self.acts))
        print("reward:",len(self.ret))
        Loss = nn.CrossEntropyLoss(reduce=False)
        x=Variable(torch.Tensor(self.obs))
        y=Variable(torch.LongTensor(self.acts))
        trainer=torch.optim.Adam(self.mod.parameters(),lr=1e-3)
        #forward
        out=self.mod(x)
        #backward
        # print("self.calulate_reutrun)",self.calulate_reutrun))
        Gt=Variable(torch.FloatTensor(self.calulate_reutrun()))  #一定是变量才能求grad
        loss=torch.mean(Loss(out,y)*Gt)
        #print("loss:", loss*100)
        trainer.zero_grad()
        loss.backward()
        trainer.step()
        self.obs,self.ret,self.acts=[],[],[]
        return Gt
    def choose_action(self,obsver):
        self.mod.eval()
        obsver=Variable(torch.Tensor(obsver))
        prob_weight=self.mod.forward(obsver)
        #print("prob_weight:",prob_weight)
        prob=prob_weight.data.numpy()
        prob=np.exp(prob[0])/sum(np.exp(prob))
        born=np.random.binomial(1,prob)
        if born==1:
            return 0
        else:
            return 1
    def greedy(self,obsver):
        self.mod.eval()
        obsver = Variable(torch.Tensor(obsver))
        prob_weight = self.mod.forward(obsver)
        prob = prob_weight.data.numpy()
        prob_weight0 =np.exp(prob[0])/sum(np.exp(prob))
        prob_weight1=np.exp(prob[1])/sum(np.exp(prob))
        if prob_weight0>=prob_weight1:
            return 0
        else:
            return 1
    def calulate_reutrun(self):
        root=0
        Return=np.zeros_like(self.ret)
        for i in reversed(range(0,len(self.ret))):
            root=root*0.99+self.ret[i]
            Return[i]=root
            Return -= np.mean(Return)
            Return /= np.std(Return)
        return Return







