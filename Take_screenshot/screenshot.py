#Needed packages
import random

import numpy as np
import cv2
import pyautogui
import os

#take screenshot using pyautogui
image = pyautogui.screenshot()

#since the pyautogui takes as a PIL(pillow) and in RGB we need to convert it to numpy array and BGR
#so we can write it to the disk
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

#writing it to the disk using opencv
cv2.imwrite("test.png",image)

rd=random.randrange(1,10000)
os.rename("test.png","test2_copy"+str(rd)+".png")
