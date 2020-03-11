#!/usr/bin/env python3

import argparse  # per llegir arguments
import os
import sys
import webbrowser
from time import sleep
from tkinter import Tk  # clipboard

import pyautogui  # automatitzar hotkeys

from ges_data_base import ContactDataBase

SLEEP_TIME = 0.1
MAX_DUPLICATE = 2

src = "Database/"


class Database(object):

    def get_list_workspaces_generator(self):
        return (i for i in os.listdir(src))

    def get_list_workspaces(self):
        return set([i for i in self.get_list_workspaces_generator()])


def prepareWork():  # lista los archivos que tenemos en Database
    database = Database()
    database_work = database.get_list_workspaces_generator()
    for workspase in database_work:
        print(workspase)
        return
    print("You need to save a workspace first!")


def copyUrls():
    pyautogui.hotkey('winleft', '1')
    sleep(SLEEP_TIME)
    pyautogui.hotkey('ctrl', '1')
    duplicate_count = 0
    tabs_count = 0
    links = set()
    while duplicate_count < MAX_DUPLICATE:
        pyautogui.hotkey('alt', 'd')
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'c')
        sleep(SLEEP_TIME)
        link = Tk().clipboard_get()
        if link in links:
            duplicate_count += 1
        else:
            links.update(link)
        sleep(SLEEP_TIME)
        pyautogui.hotkey('ctrl', 'tab')
        sleep(SLEEP_TIME)
        tabs_count += 1
    for _ in range(tabs_count):
        pyautogui.hotkey('ctrl', 'w')
    return links


def openWork(filename):
    data = ContactDataBase(filename)
    urls = data.read_links()
    for line in urls:
        webbrowser.open(line, new=0, autoraise=True)
    sleep(5)
    sys.exit()


def readInput():
    search_filename = input().split()
    first = search_filename[0]
    database = Database()
    database_work = database.get_list_workspaces()
    if first == "save":
        filename = search_filename[1]
        if not filename in database_work:
            line = "\nCreating workspace named {}...\n"
            print(line.format(filename))
            data = ContactDataBase(filename)
        urls = copyUrls()
        data.modify(urls)
    elif not first in database_work:
        line = "\nThere's no filename named {}\n\nFor more info, write 'work -h'"
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
