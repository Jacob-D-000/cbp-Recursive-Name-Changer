"""
Program: cbp recursive script
Author: Jacob Dimoff
Starting Date: 28-1-23
filename: cbpRecursive.py
Purpose: To change code blocks project files so I don't have to constantly change them manually 
"""
import os
import xml
import shutil
import glob

# Find the proper file location


def cdpwd():
    # define a var with current work folder
    curdir = os.path.dirname(__file__)
    # define the control variable for the try expect
    convar = 0
    # try to get he user to insert a path if it exists
    while convar == 0:
        try:
            print(f"The current working directory is {curdir}. What is the relative path of the file you want to change(it must stat with a '\\')?")
            # ask for input
            relpath = input()
            # cat the pwd and relative path to form new working path
            truepath = curdir + relpath
            # change working path
            os.chdir(truepath)
            # convar acts as escape.
            convar = 1
        except:
            print("This path doesn't exist please try again.")
            convar = 0
    return truepath

def globwc(pattern):
    files = glob.glob(pattern)
    return files

def deleter(truepath):
    binpath = truepath + "\\bin"
    objpath = truepath + "\\obj"

    try:
        shutil.rmtree(binpath)
    except:
        print("bin does not exist")
    try:
        shutil.rmtree(objpath)
    except:
        print("obj does not exist")
    try:
        layout = globwc("*.layout")
        i = 0
        for i in layout:
            layoutstr = "\\"
            layoutstr += i
            layoutpath = truepath + layoutstr
            os.remove(layoutpath)
    except:
        print(".layout file does not exist")
    try:
        depend = globwc("*.layout")
        i = 0
        for i in depend:
            dependstr = "\\"
            dependstr += i
            dependpath = truepath + dependstr
            os.remove(dependpath)
    except:
        print(".depend does not exist")

def main():
    truepath = cdpwd()
    deleter(truepath)

    




main()