import cv2
import time
import numpy as np
import pyautogui as pag

mouseClickPosX = [330, 480, 630]
mouseClickPosY = [355, 505, 655]

checkPixelPos = [[0],                                   #0
                [0],                                    #1
                [104, 312],                             #2
                [70, 209, 348],                         #3
                [52, 156, 260, 364],                    #4
                [40, 125, 210, 295, 380],               #5
                [35, 105, 175, 245, 315, 385],          #6
                [30, 90, 150, 210, 270, 330, 390]]      #7

def compare(a, b):
    for i in range(len(a)):
        if (a[i] != b[i]):
            return False
    return True

def check(inputImg, level):
    a = img[checkPixelPos[level][level-1]][checkPixelPos[level][level-2]]
    b = img[checkPixelPos[level][level-1]][checkPixelPos[level][level-1]]
    found = False
    print ("check")
    same = compare(a, b)
    #print(dif)
    for i in range(level):
        if not found:
            for j in range(level):
                if same:
                    if compare(img[checkPixelPos[level][i]][checkPixelPos[level][j]], a) == False:
                        #print(i, j)
                        pag.click(x = 272 + checkPixelPos[level][j], y = 472 + checkPixelPos[level][i])
                        return
                else:
                    if compare(img[checkPixelPos[level][i]][checkPixelPos[level][j]], a):
                        #print(i, j)
                        pag.click(x = 272 + checkPixelPos[level][level-1], y = 472 + checkPixelPos[level][level-1])
                        return
                    if compare(img[checkPixelPos[level][i]][checkPixelPos[level][j]], b):
                        #print(i, j)
                        pag.click(x = 272 + checkPixelPos[level][level-2], y = 472 + checkPixelPos[level][level-1])
                        return


score = 0
level = 2
while(1):
    img = np.array(pag.screenshot(region = (272, 472, 417, 417)))
    if score > 3:
        level = 3
    if score > 10:
        level = 4
    if score > 20:
        level = 5
    if score > 34:
        level = 6
    if score > 47:
        level = 7
    check(img, level)
    #for i in range(level):
    #    for j in range(level):
    #        img[checkPixelPos[level][i]][checkPixelPos[level][j]] = [0, 0, 0]
    #cv2.imwrite(str(score)+".png", img)
    #print("taken")
    if (level < 7):
        time.sleep(0.23)
    score += 1
    #print(score)
    
                
            

    #pag.click(x = 272 + checkPixelPos5[i], y = 472 + checkPixelPos5[j])
        