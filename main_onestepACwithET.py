from one_stepACwithET import onestepAC
from randomwalk import randomwlk
import matplotlib.pyplot as pl
import numpy as np
import pygame
import time
env=randomwlk()
state_,reward,actions,terminal=env.reset()
agent=onestepAC(actions)
Critic=np.zeros(10000)
Actor_left=np.zeros(10000)
Actor_right=np.zeros(10000)
for j in range(30):
    agent.reset()
    for i in range(10000):
        state_, reward, actions, terminal = env.reset()
        # env.show()
        state=state_
        I=1
        print("j",j)
        print('i',i)
        while True:
            action=agent.choose_action(state)
            state_, reward,  terminal = env.step(action,state)
            print(state)
            print('left',agent.actor(0))
            print('right',agent.actor(1))
            agent.train( state, reward, action, state_, I,terminal)
            if terminal==True:
                break
            I=agent.gamma*I
            state=state_


        Critic[i]+=agent.critic([0,0.1,1,0.1])
        Actor_left[i]+=agent.actor(0)
        Actor_right[i]+=agent.actor(1)
pl.figure(1)
pl.plot(Critic/30,'r')
pl.show()
pl.figure(2)
pl.plot(Actor_right/30,'b')
pl.plot(Actor_left/30,'g')
pl.show()



