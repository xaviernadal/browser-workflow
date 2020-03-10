#!/usr/bin/env python3

import os
import argparse
import webbrowser
import sys
import pyautogui
from tkinter import Tk
from time import sleep

SLEEP_TIME = 0.1
MAX_DUPLICATE = 2

#TODO: optional, alias ~/.bashrc + add path
path = ""

#TODO: Automate dictionary and workspace names    
work={"xarxes": path + "xarxesLinks.txt","flutter":path +  "flutterLinks.txt", "ml":path +  "mlLinks.txt", "test":path + "testLinks.txt"}

links=[]
def writeLinks(subject):
    pages = work[subject]
    f = open(pages, 'w')
    f.write('\n'.join(links))
    f.close()

def copyUrls():
    pyautogui.hotkey('winleft','7') 
    sleep(SLEEP_TIME)
    pyautogui.hotkey('ctrl','1')
    duplicate_count = 0
    tabs_count = 0
    while duplicate_count < MAX_DUPLICATE:
        pyautogui.click(x=290,y=111, button='left')
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl','a')   #Not necessary
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl','c')
        sleep(SLEEP_TIME)
        link = Tk().clipboard_get()
        if link in links:
            duplicate_count += 1
        else:
            links.append(link)
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl','tab')
        sleep(SLEEP_TIME)
        tabs_count +=1
    for _ in range(tabs_count):
        pyautogui.hotkey('ctrl','w')
        

def openWork(subject):
    pages = work[subject]

    urls = open(pages, 'r')
    for line in urls:
        webbrowser.open(line, new=0, autoraise=True)
    sleep(5)
    sys.exit()

        

def readInput():
    subject = input()
    if subject == "save":
        subject = input()
        if not subject in work.keys():
            line="\nThere's no subject named {}\n\nFor more info, write 'work -h'"
            print(line.format(subject))
        else:
            copyUrls()
            writeLinks(subject)
    elif not subject in work.keys():
        line="\nThere's no subject named {}\n\nFor more info, write 'work -h'"
        print(line.format(subject))    
    else:
        openWork(subject)
            

def main():
    print("Hello! What do you want to work on?")
    readInput()


if __name__ == "__main__":
    
    #parser = argparser.ArgumentParser()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
