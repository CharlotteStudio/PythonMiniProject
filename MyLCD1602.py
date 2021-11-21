#!/usr/bin/python

from rpi_lcd import LCD

lcd = LCD()



# LCD Display string
def  DisplayLCD(string_1, string_2):
    global lcd
    try:
        if string_1 is not None:
            lcd.text(string_1, 1)
            
        if string_2 is not None:
            lcd.text(string_2, 2)
        
    except:
        print("LCD have some Error")



# LCD Display Temp & Humi
def  DisplayLCD_DHT11(humidity, temperature):
    global lcd
    try:
        if temperature is not None:
            lcd.text("Now Temp: %d C" % temperature, 1)
            
        if humidity is not None:
            lcd.text("Now Humi: %d %%" % humidity, 2)
        
    except:
        print("LCD have some Error")



def CloseLCD():
    global lcd
    lcd.clear()