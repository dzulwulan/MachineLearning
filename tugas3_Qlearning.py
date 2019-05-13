import csv
import math
import random
import numpy as np
import time
Q_tabel =[]
point=[]
Q_Point=[]
l_r = 0.01
# d_r = 10
num_episodes= 100
max_steps_per_episode = 100
# exploration_rate = 1
# max_exploration_rate = 1
# min_exploration_rate = 0.01
# exploration_decay_rate = 0.01
discount_rate = random.uniform(0,1)
with open ('DataTugas3ML2019.txt', 'r') as f:
    for row in csv.reader(f,delimiter='\t') :
        point.append(row)
def create_QPoint(): # 0 = Atas , 1 = bawah , 2 = kiri , 4 = kanan 
    for i in range(len(point[0])):
        for j in range(15):
            Q_Point.append(point[i][j])
            Q_tabel.append([0,0,0,0])

def policy(st):# 0 = Atas , 1 = bawah , 2 = kiri , 3 = kanan
    if((st // 15 == 0) and (st % 15 == 14)): #pojok kiri atas
        act = random.sample([1,2],1)
    elif((st % 15 == 0) and (st // 15 == 0)): #pojok kanan atas
        act = random.sample([1,3],1)
    elif((st % 15 == 0) and (st // 15 == 14)): #pojok kiri bawah
        act = random.sample([0,3],1)
    elif((st % 15 == 14) and (st // 15 == 14)): #pojok kanan bawah
        act = random.sample([0,2],1)
    elif (st // 15 == 0): #bagian atas
        act = random.sample([1,2,3],1)
    elif (st // 15 == 14): #bagian bawah
        act = random.sample([0,2,3],1)
    elif (st % 15 == 0): #bagian samping kiri
        act = random.sample([0,1,3],1)
    elif (st % 15 == 0): #bagian samping kanan
        act = random.sample([0,1,2],1)
    else: 
        act = random.sample([0,1,2,3],1)
    
    return act[0]

def reward_next(act,st):
    reward=0
    if (act == 0): #atas
        reward = Q_Point[st-15]
    elif (act == 1): #bawah
        reward = Q_Point[st+15]
    elif (act == 2):#kiri
        reward = Q_Point[st-1]
    elif (act == 3):
        reward = Q_Point[st+1]
    return int(reward)
def find_newstate(act,st):
    new_state=0
    if (act == 0): #atas
        new_state = st-15
    elif (act == 1): #bawah
        new_state = st+15
    elif (act == 2):#kiri
        new_state = st-1
    elif (act == 3):
        new_state = st+1
    return new_state
create_QPoint()

for ep in range(num_episodes):
    state = 210 #reset posisi agent
    for step in range(max_steps_per_episode):
        #explo_threshold = random.uniform(0,1)
        #if explo_threshold > exploration_rate :
        #    action = np.argmax(Q_tabel[state])
        #else : 
        #    action = policy(state)
        action=policy(state)
        reward_point = reward_next(action,state)
        new_state = find_newstate(action,state)
        Q_tabel[state][action] = Q_tabel[state][action] +(l_r*(reward_point + (discount_rate * max(Q_tabel[new_state]) - Q_tabel[state][action])))
        # Q_tabel[state][action] = ((Q_tabel[state][action])*(1-l_r)) + (l_r*(reward_point + discount_rate * max(Q_tabel[new_state])))
        state = new_state
for i in range(len(Q_tabel)):
    print(Q_tabel[i])
st = 210
while(st != 14):
    print(st) # 0 = Atas , 1 = bawah , 2 = kiri , 3 = kanan
    if((st // 15 == 0) and (st % 15 == 14)): #pojok kiri atas
        act = max(Q_tabel[st][1],Q_tabel[st][2])
    elif((st % 15 == 0) and (st // 15 == 0)): #pojok kanan atas
        act = max(Q_tabel[st][1],Q_tabel[st][3])
    elif((st % 15 == 0) and (st // 15 == 14)): #pojok kiri bawah
        act = max(Q_tabel[st][0],Q_tabel[st][3])
    elif((st % 15 == 14) and (st // 15 == 14)): #pojok kanan bawah
        act = max(Q_tabel[st][0],Q_tabel[st][3])
    elif (st // 15 == 0): #bagian atas
        act = max(Q_tabel[st][1],Q_tabel[st][2],Q_tabel[st][3])
    elif (st // 15 == 14): #bagian bawah
        act = max(Q_tabel[st][0],Q_tabel[st][2],Q_tabel[st][3])
    elif (st % 15 == 0): #bagian samping kiri
        act = max(Q_tabel[st][0],Q_tabel[st][1],Q_tabel[st][3])
    elif (st % 15 == 0): #bagian samping kanan
        act = max(Q_tabel[st][0],Q_tabel[st][1],Q_tabel[st][2])
    else: 
        act = max(Q_tabel[st])
    if (act == Q_tabel[st][0]):
        act = 0
    elif (act == Q_tabel[st][1]):
        act = 1
    elif (act == Q_tabel[st][2]):
        act = 2
    elif (act == Q_tabel[st][3]):
        act = 3
    reward_point = reward_next(act,st)
    print(act)
    st = find_newstate(act,st)
    time.sleep(1)
