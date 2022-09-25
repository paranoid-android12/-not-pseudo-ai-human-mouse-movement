from PIL import ImageGrab
import pyautogui
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

last = 0
initial = True
sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)
last = []
points  = []
x = 0
y = 0
def wind_mouse(start_x, start_y, dest_x, dest_y, G_0=9, W_0=3, M_0=25, D_0=12, move_mouse=lambda x,y: None):
    '''
    WindMouse algorithm. Calls the move_mouse kwarg with each new step.
    Released under the terms of the GPLv3 license.
    G_0 - magnitude of the gravitational fornce
    W_0 - magnitude of the wind force fluctuations
    M_0 - maximum step size (velocity clip threshold)
    D_0 - distance where wind behavior changes from random to damped
    '''
    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=np.hypot(dest_x-start_x,dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random()*3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + np.random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        start_x += v_x
        start_y += v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            #This should wait for the mouse polling interval
            move_mouse(current_x:=move_x,current_y:=move_y)
    return current_x,current_y

cur_pos = pyautogui.position()


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

#RESET POINTS AND INITIALIZE MOVE

def click():
    global points
    global last
    points = []
    cur_pos = pyautogui.position()
    wind_mouse(cur_pos[0], cur_pos[1], x, y, move_mouse=lambda x, y: points.append([x, y]))
    print(x)
    last = points[-1]
    for idx, i in enumerate(points):
        rand_idx = random.randint(4, 7)
        if (idx % rand_idx) == 0:
            pyautogui.moveTo(i[0], i[1], random.uniform(0.01, 0.08))
    pyautogui.moveTo(last[0], last[1])

#BATTLE ARENA
def ba():
    global points

    flip = random.randint(1, 2)
    global x, y
    x = random.randint(922, 1140)
    y = random.randint(840, 885)

    click()

    if flip == 2:
        x = random.randint(922, 1140)
        y = random.randint(840, 885)
        click()
    pyautogui.moveTo(last[0], last[1])
    time.sleep(random.uniform(0.1,0.4))
    pyautogui.click()
    print("BA")
    bam()

def bam():
    global points
    time.sleep(random.uniform(0.6, 1.2))
    global x, y
    x = random.randint(722, 1026)
    y = random.randint(733, 774)
    click()
    pyautogui.moveTo(last[0], last[1])
    time.sleep(random.uniform(0.4, 0.7))
    pyautogui.click()

    time.sleep(random.uniform(0.9, 1.2))
    x = random.randint(813, 950)
    y = random.randint(710, 760)
    click()
    time.sleep(random.uniform(1.2, 1.5))
    pyautogui.click()
    pyautogui.moveTo(last[0], last[1])
    time.sleep(random.uniform(0.4, 0.7))


    fite()

def fite():
    global points
    flip = random.randint(1, 8)
    global x, y
    if flip >= 7:
        x = random.randint(900, 983)
        y = random.randint(867, 899)
        click()
        time.sleep(random.uniform(0.1, 0.4))
        pyautogui.click()
    else:
        x = random.randint(900, 983)
        y = random.randint(867, 899)
        points = []
        cur_pos = pyautogui.position()
        wind_mouse(cur_pos[0], cur_pos[1], x, y, move_mouse=lambda x, y: points.append([x, y]))
        last = points[-1]
        for idx, i in enumerate(points):
            rand_idx = random.randint(6, 9)
            if (idx % rand_idx) == 0:
                pyautogui.moveTo(i[0], i[1], random.uniform(0.01, 0.08))
        pyautogui.moveTo(last[0], last[1])
        time.sleep(random.uniform(2.1, 2.9))
        pyautogui.click()
    time.sleep(random.uniform(2.1, 2.9))
    px = ImageGrab.grab().load()
    col = px[1724, 373]
    while col == (74, 174, 238):
        px = ImageGrab.grab().load()
        col = px[1724, 373]
        pyautogui.click()
        flip = random.randint(1,2)
        if flip == 1:
            click()
        time.sleep(random.uniform(1.7, 2.0))
        px = ImageGrab.grab().load()
        col = px[1724, 373]


    time.sleep(random.uniform(0.4, 1.2))
    x = random.randint(923, 994)
    y = random.randint(680, 708)
    click()
    pyautogui.click()
    initialize()



def initialize():
    while initial:
        px = ImageGrab.grab().load()
        col = px[1724, 373]
        if col == (105, 104, 107):
            ba()

initialize()