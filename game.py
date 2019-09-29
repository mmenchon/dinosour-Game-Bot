print("Dinosaur Game Bot")
from PIL import ImageGrab, ImageOps
from numpy import  *
import pyautogui
import time

class Coord():
    replayBtn = (480,500)
    dinousaur = (120,500)
    #x = 240 coord x to check tree
    #y = 560 coord y to check bird
def restartGame():
    pyautogui.click(Coord.replayBtn)

def pressUp():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Coord.dinousaur[0]+ 200, Coord.dinousaur[1], Coord.dinousaur[0]+260, Coord.dinousaur[1]+50)
    #print(box)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    # print(a.sum())
    return a.sum()  
 
def Main():
    restartGame() 
    while True:
        if (imageGrab() != 3033):
            pressUp()
            time.sleep(0.001)

Main()
