import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pylab import *
import pyautogui,sys,math
import matplotlib.image as mpimg
from tkinter import *
from collections import defaultdict
from heapq import *

x_clickPosition = 0
y_clickPosition = 0

def on_press(event):
    print("Your position:" ,event.button,event.xdata, event.ydata)
    global x_clickPosition
    x_clickPosition = event.xdata
    global y_clickPosition
    y_clickPosition = event.ydata
    chooseCanteen()
    return event.xdata, event.ydata


def clickPosition():
    print("Please click your position in the map")
    fig = plt.figure()
    img=mpimg.imread('canteen.jpeg')  #get image
    imgplot = plt.imshow(img)
    plt.imshow(img, animated= True)
    fig.canvas.mpl_connect('button_press_event', on_press)
    plt.show()






canteenName=["Ananda Kitchen","North Hill Food Court","North Indian Cuisine","Canteen9"\
             "Canteen2","Canteen1","NTU NorthSpine Plaza","Peach Garden","NIE Canteen","Food Court 16","Food Court 13","Canteen 14"]

# canteenPositionX={'Ananda Kitchen':(2146.84677,225.0823),'North Hill Food Court':(2235.1371,240.8484),'North Indian Cuisine':(1781.0726,480.4935),'Canteen9':(1686.4758,638.1548),\
#                'Canteen2':(1733.7742,1360.2435),'Canteen1':(1831.5241,1685.0258),'NTU NorthSpine Plaza':(863.4838,1612.5016),'Peach Garden':(708.9758,1580.9693),\
#               'NIE Canteen':(258.0645,1300.3322),'Food Court 16':(882.4032,994.4693),\
#                 'Food Court 13':(907.6290,748.5177),'Canteen 14':(1122.0483,559.3241)}#get canteen position coordinate

#def canteenPosition():

canteenPositionX={'Ananda Kitchen':2146.84677,'North Hill Food Court':2235.1371,'North Indian Cuisine':1781.0726,'Canteen9':1686.4758,\
               'Canteen 2':1733.7742,'Canteen 1':1831.5241,'NTU NorthSpine Plaza':863.4838,'Peach Garden':708.9758,\
              'NIE Canteen':258.0645,'Food Court 16':882.4032,\
                'Food Court 13':907.6290,'Canteen 14':1122.0483}#get canteen position xcoordinate

canteenPositionY={'Ananda Kitchen':225.0823,'North Hill Food Court':240.8484,'North Indian Cuisine':477.34032,'Canteen9':638.1548,\
               'Canteen 2':1360.2435,'Canteen 1':1685.0258,'NTU NorthSpine Plaza':1612.5016,'Peach Garden':1580.9693,\
              'NIE Canteen':1300.3322,'Food Court 16':994.4693,\
                'Food Court 13':748.5177,'Canteen 14':559.3241}#get canteen position ycoordinate


class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y

class Getlen: #define line function
    def __init__(self,x1,x2,y1,y2):
        self.x = x1-x2
        self.y = y1-y2
        self.len= math.sqrt((self.x**2)+(self.y**2))

    def getlen(self): #function for getting length
        return self.len



def chooseCanteen():
    i=0
    distance=[]
    canteenSort=[]
    x1,y1=x_clickPosition,y_clickPosition #get your position coordinate
    #print("test position ",x1,y1)          #get length

    for i in range(0,canteenPositionX.__len__()):
        x2=list(canteenPositionX.values())[i]
        y2=list(canteenPositionY.values())[i]
        length = Getlen(x1,x2,y1,y2)
        distance.append(length.getlen())
        indexCanteen=distance.index()
        #canteenSort.append(canteenPositionX.keys())
        #indexDis=sorted(distance)
        #canteenSort=list(canteenPositionX.keys())[indexCanteen]
        print("testttt",indexCanteen)
            #print(x2,y2)
        i+=1
        #print(canteenSort)
        # print(min(distance))
        # print(distance.index(min(distance)))
    z=distance.index(min(distance))
    finalCanteen=list(canteenPositionX.keys())[z]
    print("The nearest canteen is ",finalCanteen)

clickPosition()




