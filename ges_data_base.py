#!/usr/bin/env python3
import os
src="Database/"
class ContactDataBase():
    
    def __init__(self, database_name):
        self.database_name = database_name
    
    def create(self):
        os.mknod(src+self.database_name)
            

    def exist(self):
        exist = os.path.isfile(src+self.database_name)
        if exist: return True
        return False

    def modify(self, args= ()):
        if self.exist():
            with open(src+self.database_name,"w") as file:
                for i in args:
                    file.writelines(i+"\n")
        else: 
            self.create()
            self.modify(args)

    def read_links(self):
        if self.exist():
            with open(src+self.database_name,"r") as file:
                return tuple(file.read().split("\n"))[:-1]
        return tuple("")
                



if __name__ == "__main__":
    tu = ("hola","que")
    newdata = ContactDataBase(database_name="git")
    newdata.modify(tu)
    print(newdata.read_links())