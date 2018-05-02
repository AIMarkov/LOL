import numpy as np
import math
from matplotlib import pyplot as pl


# v(s,w)=[w1,w2,]^T[1,1]
class onestepAC(object):
    def __init__(self, Actions):  #??两个问题有两个网络，但是不能保证两个网络同时收敛，并且两个网络必定有一个先收敛
        self.gamma = 0.99
        self.alpha_w = 2 ** (-6)
        self.alpha_theta = 2 ** (-9) #步长一定要小，因为是两个函数逼近，步长太大可能会直接越过收敛值
        self.lambda_w=0.01
        self.lambda_theta=0.01
        self.theta = np.array([0, 0]).reshape([2, 1])
        self.actions = Actions

        self.action_num = range(len(self.actions))
        self.x_left = self.actions[0]
        self.x_right = self.actions[1]
        self.W = np.asarray([0, 0,0,0])
        self.Z_w=np.asarray([0,0,0,0])
        self.Z_theta= np.array([0, 0]).reshape([2, 1])
    def reset(self):
        self.W = np.asarray([0, 0,0,0])
        self.theta = np.array([0, 0]).reshape([2, 1])
        self.Z_w = np.asarray([0, 0, 0, 0])
        self.Z_theta = np.array([0, 0]).reshape([2, 1])

    def critic(self, S):
        V = S[0] * self.W[0] + S[1] * self.W[1]+S[2]*self.W[2]+S[3]*self.W[3]+0.5 #原来不收敛估计就是特征不够至少三个
        return V

    def actor(self, a):
        #print('fenmu:', ( np.exp(np.dot(self.theta.T, self.x_left)) + np.exp(np.dot(self.theta.T, self.x_right))))
        if a == 0:
            return np.exp(np.dot(self.theta.T, self.x_left)) / (
                        np.exp(np.dot(self.theta.T, self.x_left)) + np.exp(np.dot(self.theta.T, self.x_right)))
        else:
            return np.exp(np.dot(self.theta.T, self.x_right)) / (
                        np.exp(np.dot(self.theta.T, self.x_left)) + np.exp(np.dot(self.theta.T, self.x_right)))

    def choose_action(self, S):
        right = self.actor(self.action_num[1])
        N_e = np.random.binomial(1, right)
        if N_e:
            return self.action_num[1]
        else:
            return self.action_num[0]

    def train(self, S, R, A, S_, I,terminal):
        if terminal==True:
            delta = R + self.gamma * 0 - self.critic(S)
        else:
            delta = R + self.gamma * self.critic(S_) - self.critic(S)
        self.Z_w=self.gamma*self.lambda_w*self.Z_w+I*S
        if A==0:
            self.Z_theta=self.gamma*self.lambda_theta*self.Z_theta+I*(
                    self.x_left - (self.actor(0)[0, 0] * self.x_left + self.actor(1)[0, 0] * self.x_right))
        else:
            self.Z_theta = self.gamma * self.lambda_theta * self.Z_theta + I *(
                self.x_right - (self.actor(0)[0, 0] * self.x_left + self.actor(1)[0, 0] * self.x_right))
        self.W = self.W + self.alpha_w* delta * self.Z_w
        self.theta=self.theta+self.alpha_theta*delta*self.Z_theta
