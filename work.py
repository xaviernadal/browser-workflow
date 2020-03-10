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

path = ""

work = {}


def prepareWork():
    subjectList = open('workspaces.txt', 'r')
    print("List:")
    for key in subjectList:
        subjectFile = key + "Links.txt"

        work.update({key: subjectFile})
        print("- " + key)
    if bool(work) == False:
        print("You need to save a workspace first!")


def writeNewWorkspace(subject):
    subjectFile = subject + "Links.txt"
    spaces = open('workspaces.txt', 'w')
    spaces.write(subject)
    work.update({subject: subjectFile})


links = []


def writeLinks(subject):
    pages = work[subject]
    f = open(pages, 'w')
    f.write('\n'.join(links))
    f.close()


def copyUrls():
    pyautogui.hotkey('winleft', '7')
    sleep(SLEEP_TIME)
    pyautogui.hotkey('ctrl', '1')
    duplicate_count = 0
    tabs_count = 0
    while duplicate_count < MAX_DUPLICATE:
        pyautogui.hotkey('alt', 'd')
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'c')
        sleep(SLEEP_TIME)
        link = Tk().clipboard_get()
        if link in links:
            duplicate_count += 1
        else:
            links.append(link)
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'tab')
        sleep(SLEEP_TIME)
        tabs_count += 1
    for _ in range(tabs_count):
        pyautogui.hotkey('ctrl', 'w')


def openWork(subject):
    pages = work[subject]

    urls = open(pages, 'r')
    for line in urls:
        webbrowser.open(line, new=0, autoraise=True)
    sleep(5)
    sys.exit()


def readInput():
    subject = input().split()
    first = subject[0]
    if first == "save":
        subject = subject[1]
        if not subject in work.keys():
            line = "\nCreating workspace named {}...\n"
            print(line.format(subject))
            writeNewWorkspace(subject)

        copyUrls()
        writeLinks(subject)

    elif not first in work.keys():
        line = "\nThere's no subject named {}\n\nFor more info, write 'work -h'"
        print(line.format(first))
    else:
        openWork(first)


def main():
    print("Hello! What do you want to work on?")
    prepareWork()
    readInput()


if __name__ == "__main__":

    #parser = argparser.ArgumentParser()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
