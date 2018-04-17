import pygame,sys
import numpy as np
import time
# pygame.init()
# screen=pygame.display.set_mode((450,100))
# rect0=pygame.Rect(10,10,100,80)
# rect1=pygame.Rect(120,10,100,80)
# rect2=pygame.Rect(230,10,100,80)
# rect3=pygame.Rect(340,10,100,80)
# rect4=pygame.Rect(10,10,100,80)
# pygame.draw.rect(screen,(100,100,3),rect0)
# pygame.draw.rect(screen,(100,100,3),rect1)
# pygame.draw.rect(screen,(100,100,3),rect2)
# pygame.draw.rect(screen,(100,100,100),rect3)
# pygame.draw.rect(screen,(2,2,200),rect4)
#
# pygame.display.update()


# fps=300
# fclock=pygame.time.Clock()#引入时间对象
class randomwlk():
    def __init__(self):
        self.done=False
        self.screen = pygame.display.set_mode((450, 100))
        self.rect0 = pygame.Rect(10, 10, 100, 80)
        self.rect1 = pygame.Rect(120, 10, 100, 80)
        self.rect2 = pygame.Rect(230, 10, 100, 80)
        self.rect3 = pygame.Rect(340, 10, 100, 80)
        self.rect4 = pygame.Rect(10, 10, 100, 80)
        self.Actions= [np.array([0, 1]).reshape([2, 1]),np.array([1, 0]).reshape([2, 1])]
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect0)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect1)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect2)
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect3)
        pygame.draw.rect(self.screen, (2, 2, 200), self.rect4)

    def show(self):
        pygame.display.update()

    def reset(self):
        self.done = False
        self.rect0 = pygame.Rect(10, 10, 100, 80)
        self.rect1 = pygame.Rect(120, 10, 100, 80)
        self.rect2 = pygame.Rect(230, 10, 100, 80)
        self.rect3 = pygame.Rect(340, 10, 100, 80)
        self.rect4 = pygame.Rect(10, 10, 100, 80)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect0)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect1)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect2)
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect3)
        pygame.draw.rect(self.screen, (2, 2, 200), self.rect4)
        return np.asarray([0,0.1,1,0.1]),0,self.Actions,self.done  #state_,reward,actions,terminal
    def step(self,action,s):
        if s[0] == 1:
            if action==0:
               self.rect4.centerx+=110
               return np.asarray([2,0.2,1,0.2]),-1,self.done
            else:
               self.rect4.centerx-= 110
               return np.asarray([0,0.1,1,0.1]),-1,self.done
        elif s[0]==0:
            if action==0:
                self.rect4.centerx=self.rect4.centerx
                return np.asarray([0,0.1,1,0.1]),-1,self.done
            else:
                self.rect4.centerx+=110
                return np.asarray([1,0.5,1,0.5]),-1,self.done
        else:
            if action==0:
                self.rect4.centerx -=110
                return np.asarray([1,0.5,1,0.5]), -1, self.done
            else:
                self.rect4.centerx += 110
                self.done=True
                return np.asarray([0,0.1,1,0.1]), -1, self.done
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect0)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect1)
        pygame.draw.rect(self.screen, (100, 100, 3), self.rect2)
        pygame.draw.rect(self.screen, (100, 100, 100), self.rect3)
        pygame.draw.rect(self.screen, (2, 2, 200), self.rect4)





#def Action(action,s):
    # if s==1:
    #     if action==1:
    #         return 1
    #     else:
    #         return -1
    # elif action==1:
    #     return -1
    # else:
    #     return 1



# while True:
#     for event in pygame.event.get():#事件返回是一个ｌｉｓｔ
#         if event.type==pygame.QUIT:
#             sys.exit()
#     c=(rect4.centerx+110)<=rect3.centerx
#     if Action()==1&c:
#
#         time.sleep(3)
#         rect4.centerx+=110
#         pygame.draw.rect(screen, (100, 100, 3), rect0)
#         pygame.draw.rect(screen, (100, 100, 3), rect1)
#         pygame.draw.rect(screen, (100, 100, 3), rect2)
#         pygame.draw.rect(screen, (100, 100, 100), rect3)
#         pygame.draw.rect(screen, (2, 2, 200), rect4)
#     pygame.display.update()
#     fclock.tick(fps)  #时间对
