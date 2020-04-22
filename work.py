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


class Database():
    def __init__(self):
        self.workspace = None

    def get_list_workspaces_generator(self):
        return (i for i in os.listdir(src))

    def get_list_workspaces(self):
        return set([i for i in self.get_list_workspaces_generator()])


def prepareWork(database_works):  # lista los archivos que tenemos en Database
    for workspase in database_works:
        print(workspase)
        return
    print("You need to save a workspace first!")


def readInput(database_works, database):
    search_filename = input().split()
    first = search_filename[0]
    if first == "save":
        save(search_filename, database_works, database)
    elif not first in database_works:
        line = "\nThere's no filename named {}\n\nFor more info, write 'work -h'"
        print(line.format(first))
    else:
        database.workspace = ContactDataBase(first)
        openWork(database)



def save(search_filename, database_work, database):
    filename = search_filename[1]
    database.workspace = ContactDataBase(filename)
    if not filename in database_work:
        line = "\nCreating workspace named {}...\n"
        print(line.format(filename))
    urls = copyUrls()
    database.workspace.modify(urls)
    


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


def openWork(database):
    urls = database.workspace.read_links()
    for line in urls:
        webbrowser.open(line, new=0, autoraise=True)
    sleep(5)
    sys.exit()


def main():
    print("Hello! What do you want to work on?")
    database = Database()
    database_works = database.get_list_workspaces()
    prepareWork(database_works)
    readInput(database_works, database)
    


if __name__ == "__main__":

    #parser = argparser.ArgumentParser()
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
