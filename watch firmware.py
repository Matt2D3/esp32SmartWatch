from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI
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
#p27   u
#p26   d
#p25   l
#p35   r
#p34   mid
#p33   b1
#p32   b2
ssid_ = ""
wp2_pass = ""
up = Pin(27,Pin.IN,Pin.PULL_UP)
down = Pin(26,Pin.IN,Pin.PULL_UP)
left = Pin(25,Pin.IN,Pin.PULL_UP)
right = Pin(35,Pin.IN,Pin.PULL_UP)
mid = Pin(34,Pin.IN,Pin.PULL_UP)
b1 = Pin(33,Pin.IN,Pin.PULL_UP)
b2 = Pin(32,Pin.IN,Pin.PULL_UP)
haptic = Pin(22,Pin.OUT)
ds = ds1302.DS1302(Pin(12),Pin(13),Pin(14))


spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(17), cs=Pin(5), rst=Pin(16))
display.fill_polygon(7, 63, 63, 50, color565(0, 255, 0))

sleep(5)
display.cleanup()

ds.date_time([2022, 2, 8, 3, 14, 23, 1,0])
print(ds.hour())
print(ds.minute())
curScreen = "time"
GUIUPDATE = True

global notifyList
notifyList = []

#put code here to run in the background
def backgroundTask():
    penis = False


while True:
    if GUIUPDATE == True:
        display.cleanup()
        if curScreen == "time":
            GUIUPDATE = False
            while not GUIUPDATE:
                hour = ds.hour()
                minute = ds.minute()
                display.draw_text(56,64,str(hour) + ":" +str(minute), color565(0,0,128))
                if left.value() == HIGH:
                    curScreen = "notifications"
                    GUIUPDATE = True
                if right.value() == HIGH:
                    curScreen = "time"
                    GUIUPDATE = True
        if curScreen == "notifications":
            while not GUIUPDATE:
                curSelected = 0
                curNotif = 0
                drawNotif = 8
                curNotifY = 112
                notifyScreen = 0
                notifyScreenLimit = round((len(notifyList) / 7))
                display.draw_text(0,128,"notifications" , color565(0,0,128))
                while drawnNotif < curNotif:
                    notifySelect = notifyScreen * 7
                    display.draw_text(0,curNotifY,notifyList[curNotif + notifySelect],color565(0,0,128))
                    curNotifY += -16
                display.draw_rectangle(0,(curNotify),128,(curNotifY+16),color565(0,0,64))
                if left.value() == HIGH:
                    curScreen = "alexa"
                    GUIUPDATE = True
                if right.value() == HIGH:
                    curScreen = "time"
                    GUIUPDATE = True
                if up.value() == HIGH:
                    curSelected += -1
                    if curSelected < 0:
                        curSelected = 6
                        notifyScreen += -1
                        curNotify = 0
                        if notifyScreen < notifyScreenLimit:
                            notifyScreen += 1
                        
                if down.value == High:
                    curSelected += 1
                    if curSelected > 6:
                        notifyScreen += 1
                        curSelected = 0
                        curNotify = 0
                        if notifyScreen > notifyScreenLimit:
                            notifyScreen +=-1
                            
                if mid.value() == HIGH:
                    display.cleanup()
                    backNotPress = True
                    while backNotPress:
                        if b1.value==High:
                            backNotPress = False
                            curNotificationTextSelect = ((notifyScreen - 1) *6)+curSelected
                            display.draw_text(0,128, notifyLIst[curNotificationTextSelect],color565(0,0,128))
                        
        if curScreen == "alexa":
            while not GUIUPDATE:
                display.draw_text(0,128,"alexa" , color565(0,0,128))
                groupControll = ["","",""]
                
                    
                