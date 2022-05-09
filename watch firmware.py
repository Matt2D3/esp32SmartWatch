from time import sleep
import xglcd_font
from ssd1351 import Display, color565
from machine import Pin, SPI
from machine import deepsleep
from time import sleep

import ds1302

#esp   scr
#3v    vcc
#gnd   gnd
#p18   scl
#p23   sda
#p16   res
#p17   dc
#p5    cs

#esp   ds1302
#gnd   gnd
#3v    vcc
#p12    clk
#p13    dat
#p14    rst

#esp   5way
#3v    com
#p22   u
#p21   d
#p19   l
#p35   r
#p34   mid
#p33   b1
#p32   b2
#b2 reserved for sleep 

#esp   hap
#p2   red
#gnd   blk

ssid_ = ""
wp2_pass = ""
up = Pin(22,Pin.IN,Pin.PULL_UP)
down = Pin(21,Pin.IN,Pin.PULL_UP)
left = Pin(19,Pin.IN,Pin.PULL_UP)
right = Pin(4,Pin.IN,Pin.PULL_UP)

b1 = Pin(33,Pin.IN,Pin.PULL_UP)
b2 = Pin(32,Pin.IN,Pin.PULL_UP)
haptic = Pin(2,Pin.OUT)
ds = ds1302.DS1302(Pin(12),Pin(13),Pin(14))

xfont = xglcd_font.XglcdFont('terminal8x12.c', 8, 12)
oledSpi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
display = Display(oledSpi, dc=Pin(17), cs=Pin(5), rst=Pin(16))
print("init")
display.draw_text(50,30,"welcome to", xfont, color565(255,0,0),0,True)
display.draw_text(60,30,"esp watch", xfont, color565(255,0,0),0,True)

display.draw_polygon(24, 64, 64, 51, color565(0, 0, 100))
display.draw_polygon(24, 64, 64, 50, color565(0, 0, 100))
display.draw_polygon(24, 64, 64, 49, color565(0, 0, 100))
display.draw_polygon(24, 64, 64, 48, color565(0, 0, 100))
display.draw_polygon(24, 64, 64, 47, color565(0, 0, 100))
display.draw_polygon(24, 64, 64, 46, color565(0, 0, 100))

display.draw_polygon(24, 64, 64, 51, color565(0, 100, 50))
display.draw_polygon(24, 64, 64, 50, color565(0, 100, 50))
display.draw_polygon(24, 64, 64, 49, color565(0, 100, 50))
display.draw_polygon(24, 64, 64, 48, color565(0, 100, 50))
display.draw_polygon(24, 64, 64, 47, color565(0, 100, 50))
display.draw_polygon(24, 64, 64, 46, color565(0, 100, 50))

display.draw_polygon(24, 64, 64, 51, color565(100, 0, 0))
display.draw_polygon(24, 64, 64, 50, color565(100, 0, 0))
display.draw_polygon(24, 64, 64, 49, color565(100, 0, 0))
display.draw_polygon(24, 64, 64, 48, color565(100, 0, 0))
display.draw_polygon(24, 64, 64, 47, color565(100, 0, 0))
display.draw_polygon(24, 64, 64, 46, color565(100, 0, 0))

sleep(0.75)
red = 0
green = 0
blue = 255

baseB = red
baseR = blue
baseG = green

print(ds.hour())
print(ds.minute())
curScreen = "time"
GUIUPDATE = True
spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))

global notifyList
notifyList = [""]

#put code here to run in the background
def backgroundTask():
 
    imposter = "sus"
def split(word): 
     return list(word)
updateTime = 5
angle = -1
triAngle = 0
hour = ds.hour()
minute = ds.minute()
month = ds.month()
day = ds.day()
year = ds.year()
xfont = xglcd_font.XglcdFont('terminal8x12.c', 8, 12)
bigfont = xglcd_font.XglcdFont('terminal11x16.c', 11, 16)
display.clear()
while True:
    #get ready to change screens
    if GUIUPDATE == True:
        spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
        display.clear()
        #run this when displaying time screen
        if curScreen == "time":
            GUIUPDATE = False
            print("entered watch face")
            display.draw_polygon(24, 64, 64, 51, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            display.draw_polygon(24, 64, 64, 50, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            display.draw_polygon(24, 64, 64, 49, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            display.draw_polygon(24, 64, 64, 48, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            display.draw_polygon(24, 64, 64, 47, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            display.draw_polygon(24, 64, 64, 46, color565(int(baseR/2),int(baseG/2),int(baseB/2)))
            print(GUIUPDATE)
            while GUIUPDATE == False:
                if(updateTime==5):

                    prevMin = minute
                    hour = ds.hour()
                    minute = ds.minute()
                    month = ds.month()
                    day = ds.day()
                    year = ds.year()
                    if angle>359:
                        angle = 0
                    if hour >12:
                        hour = hour-12
                    if hour == 0:
                        hour = 12
                    if hour > 9:
                        timeOfset = 45
                    if hour < 9:
                        timeOfset = 50
                    if minute < 10:
                        minute = "0"+str(minute)
                    dateString = str(month)+"-"+str(day)+"-"+str(year)
                    dateX = int(64-((len(dateString)*8)/2))
                    timeString = str(hour)+":"+str(minute)
                    timeX = int(64-((len(timeString)*8)/2))
                    if prevMin != minute:
                        display.draw_polygon(6, 64, 64, 62, color565(0, 0, 0),angle)
                        display.draw_polygon(6, 64, 64, 63, color565(0, 0, 0),angle)
                        display.draw_polygon(6, 64, 64, 64, color565(0, 0, 0),angle)
                        angle+=1
                    display.draw_text(35,50,"time", xfont, color565(baseR,baseG,baseB),0,True)
                    
                    display.draw_text(50,timeX,(str(hour) + ":" +str(minute)), bigfont, color565(baseR,baseG,baseB),0,True)
                    display.draw_text(70,dateX,dateString, xfont, color565(baseR,baseG,baseB),0,True)
                    
                    display.draw_polygon(6, 64, 64, 62, color565(baseR,baseG,baseB),angle)
                    display.draw_polygon(6, 64, 64, 63, color565(baseR,baseG,baseB),angle)
                    print(hour)
                    print(minute)
                    updateTime = 0
                backgroundTask()
                updateTime += 1
                triAngle +=1
                display.draw_polygon(6, 64, 64, 43, color565(int(baseR),int(baseG),int(baseB)),triAngle)
                if triAngle > 359:
                    triAngle = 0
                    
                display.draw_polygon(6, 64, 64, 43, color565(0,0,0),triAngle)
                display.draw_text(35,50,"time", xfont, color565(baseR,baseG,baseB),0,True)
                display.draw_text(50,timeX,(str(hour) + ":" +str(minute)), bigfont, color565(baseR,baseG,baseB),0,True)
                display.draw_text(70,dateX,(str(month)+"-"+str(day)+"-"+str(year)), xfont, color565(baseR,baseG,baseB),0,True)
                print(updateTime)
                if left.value() == 0:
                    curScreen = "notifications"
                    GUIUPDATE = True
                if right.value() == 0:
                    curScreen = "time"
                    GUIUPDATE = True
        #run this when displaying notifications screen
        if curScreen == "notifications":
            currentNotification = 0
            curNotification = ""
            curScreen = 0
            curSelect = 0
            curCharecter = 0
            GUIUPDATE = False
            display.clear()
            while(left.value()==0 or right.value()==0):
                print("screen select held")
            
            while not GUIUPDATE:
                backgroundTask()
                display.draw_text(0,0,"notifications", xfont, color565(baseR,baseG,baseB),0,True)
                while(currentNotification<7):
                    if (len(notifyList)>currentNotification):
                        print("notification to be printed next")
                        print((currentNotification+(curScreen*8)))
                        curNotification = notifyList[(currentNotification+(curScreen*8))]
                        if int(len(curNotification)) > 15:
                            curCharecter = 0
                            fullNotification = split(notifyList[(currentNotification+(curScreen*8))])
                            curNotification = ""
                            while curCharecter < 15:
                                curNotification = curNotification + str(fullNotification[curCharecter])
                                curCharecter += 1
                        print(curNotification)
                        print(type(curNotification))
                        
                        print(len(curNotification))
                        display.draw_text((currentNotification*14)+14,0,curNotification, xfont, color565(baseR,baseG,baseB),0,True)
                    currentNotification += 1
                #changes screen
                if left.value() == 0:
                    curScreen = "notes"
                    GUIUPDATE = True
                if right.value() == 0:
                    curScreen = "time"
                    GUIUPDATE = True
                
                #scrolls notification screen
                if up.value() == 0:
                    display.draw_polygon(6,(curSelect*15)+2,120,6, color565(0,0,0))
                    curSelect += -1
                    if curSelect < 1:
                        curSelect = 7
                    display.draw_polygon(6,(curSelect*15)+2,120,6, color565(baseR,baseG,baseB)) 
                if down.value() == 0:
                    display.draw_polygon(6,(curSelect*15)+2,120,6, color565(0,0,0))
                    curSelect += 1
                    if curSelect >7:
                        curSelect = 1
                    display.draw_polygon(6,(curSelect*15)+2,120,6, color565(baseR,baseG,baseB))
                #selects a notification to display     
                if b1.value() == 0:
                    display.clear()
                    backNotPress = True
                    while backNotPress: 
                        if b1.value==0:
                            backNotPress = False
                            curNotificationTextSelect = ((notifyScreen - 1) *6)+curSelected
                            display.draw_text(0,128, notifyLIst[curNotificationTextSelect],color565(0,0,128))
        if curScreen == "notes":
            GUIUPDATE = False
            display.clear()
            selected = 1
            maxItems = 7
            while(not GUIUPDATE):
                
                while(left.value()==0 or right.value()==0):
                    print("screen select held")
                if left.value() == 0:
                    curScreen = "notifications"
                    GUIUPDATE = True
                if right.value() == 0:
                    curScreen = "alexa"
                    GUIUPDATE = True
                display.draw_polygon(6,(selected*16)+2,120,6, color565(baseR,baseG,baseB))
                display.draw_text(0,0,"notes", xfont, color565(baseR,baseG,baseB),0,True)
                display.draw_text(14,0,"bell schedual", xfont, color565(baseR,baseG,baseB),0,True)
                display.draw_text(28,0,"spanish", xfont, color565(baseR,baseG,baseB),0,True)

                while not (left.value()==0 or right.value()==0 or up.value()==0 or down.value()==0 or b2.value()==0):
                    imposter = "sus"
                    backgroundTask()
                display.draw_polygon(6,(selected*16)+2,120,6, color565(0,0,0))
                print("button pressed")
                if up.value() == 0:
                    selected += -1
                    if selected <1:
                        selected = 1
                if down.value() == 0:
                    selected += 1
                    if selected >maxItems:
                        selected = maxItems
                if right.value() == 0:
                    curScreen = "notifications"
                    GUIUPDATE = True
                if left.value() == 0:
                    curScreen = "alexa"
                    GUIUPDATE = True
                if b2.value() == 0:
                    print("b2 pressed")
                    print(selected)
                    
        #changes to alexa screen          
        if curScreen == "alexa":
            display.clear()
            
            GUIUPDATE = False
            while not GUIUPDATE:
                backgroundTask()
                display.draw_text(0,0,"alexa" , xfont, color565(baseR,baseG,baseB),0,True)
                groupControll = ["","",""]
                if right.value() == 0:
                    curScreen = "notes"
                    GUIUPDATE = True
            

