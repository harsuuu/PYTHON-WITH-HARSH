import pyautogui as p
import time            #It is use to pause program for few second.
time.sleep(4)
for i in range(10):    #Means 10 times
    p.typewrite("Bhai tu chutiya hai")  #This typewrite method is of pyautogui pacage(module) which is used to type the message.
    p.press("enter")   #This press method is of pyautogui module which is used press any keyword key.




