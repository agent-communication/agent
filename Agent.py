import random
import numpy as np
print("あああ")

WORLD_NUM = 10
WORLD_SCALE = 100 * WORLD_NUM
MOVE_SCALE = 5

def get_near_adresses(address):
    nears = []
    for i in range(address[0] - 1, address[0] + 1):
        for j in range(address[1] - 1, address[1] + 1):
            nears.append([i, j])
    return nears
    
def move_limitation(coo):
    coo=coo*(coo>=0)
    if coo[0] > WORLD_SCALE:
        coo[0] = WORLD_SCALE
    if coo[1] > WORLD_SCALE:
        coo[1] = WORLD_SCALE   
    return coo



class voice():
    def __init__(self, words):
        self.information = [] * 2


class Agent():
    def __init__(self):
        self.coo = np.random.uniform(low=0, high=WORLD_SCALE, size=2)
        self.address = (self.coo/100).astype('int32')
    def invoice(self, invoice):
        0
        
    def outvoice(self):
        0
    
    def move(self, degree, scale): # scale must be [0, 1]
        if scale < 0:
            scale = 0
        elif scale > 1:
            scale = 1
        self.coo = self.coo+np.array([MOVE_SCALE * scale * np.cos(degree), MOVE_SCALE * scale * np.sin(degree)])
        self.coo = move_limitation(self.coo)
        
    def get_coo(self):
        return self.coo
        
    def see(self, agents):
        count = 0
        for agent in agents:
            for address in get_near_adresses(agent.address):
                if address == agent.address:
                    count += 1
                    break


pos = []
                
agents = [Agent() for i in range(10)]
for i in range(100):
    pos_in=[]
    for agent in agents:
        agent.invoice(0)
        agent.outvoice()
        agent.move(1,1)
        pos_in.append(agent.get_coo())
    pos.append(pos_in)
        
from tkinter import *

cnt = 0 
root = Tk()
c0 = Canvas(root, width = WORLD_SCALE, height = WORLD_SCALE)
c0.pack(expand = True, fill = BOTH)

ovals = [c0.create_oval(pos[cnt][i][0]-1,pos[cnt][i][1]-1,pos[cnt][i][0]+1,pos[cnt][i][1]+1,fill = 'red') for i in range(len(pos[0]))]

def draw_oval(cnt):
    global pos
    [c0.coords(ovals[i],pos[cnt][i][0]-1,pos[cnt][i][1]-1,pos[cnt][i][0]+1,pos[cnt][i][1]+1) for i in range(len(pos[0]))]
        
def show():
    global cnt
    cnt += 1
    draw_oval(cnt)
    if cnt == 99:
        return
    root.after(30, show)
show()
root.mainloop()

