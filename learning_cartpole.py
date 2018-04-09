import gym
import numpy as np
from REINFORCE_MC_without_Baseline import REINFORCE_Agent
import matplotlib.pyplot as plt
import time

DISPLAY_REWARD_THRESHOLD = 1000
RENDER = False
#创建一个环境
env = gym.make('CartPole-v0')
env.seed(4)
env = env.unwrapped
observetion=env.reset()#状态是4维
print(observetion)
env.render()
print(env.action_space.sample())
print(env.observation_space.shape[0])  #状态是（4，）维
print(env.observation_space.high)
print(env.observation_space.low)

RL = REINFORCE_Agent()
#学习过程
for i_episode in range(20000):
    observation = env.reset()
    while True:
        # if RENDER: env.render()
        env.render()
        #采样动作，探索环境
        #print('huanjing',observetion)
        action = RL.choose_action(observation)
        #print("action",action)
        observation_, reward, done, info = env.step(action)
        #将观测，动作和回报存储起来
        RL.store_transition(observation, action, reward)
        if done:#如果情节结束就进行训练
            ep_rs_sum = sum(RL.ret)
            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.99+ep_rs_sum * 0.01
            if running_reward > DISPLAY_REWARD_THRESHOLD: RENDER = True
            print("episode:", i_episode, "rewards:", int(ep_rs_sum ))
            #每个episode学习一次
            vt = RL.learn()
            # if i_episode == 0:
            #     plt.plot(vt)
            #     plt.xlabel('episode steps')
            #     plt.ylabel('normalized state-action value')
            #     plt.show()
            break#此情节训练完后跳出循环

        #智能体探索一步
        observation = observation_
# #测试过程
for i in range(10):
    observation = env.reset()
    count = 0
    while True:
        # 采样动作，探索环境
        env.render()
        action = RL.greedy(observation)
        #action = RL.choose_action(observation)
        #action = RL.sample_action(observation)
        # print (action)
        # print(action1)
        observation_, reward, done, info = env.step(action)
        if done:
            print(count)
            break
        observation = observation_
        count+=1
        #time.sleep(0.001)
        print (count)





