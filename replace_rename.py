#!/usr/bin/env python
#
# Author: Stephen Sanchagrin
# Title: renRep.py
# Date: 9/21/2016
# Description :Replace Rename is a simple utility designed to replace characters
#              or rename files in the current directory.
#

import os,sys

def yesChk(usrInp): #Checks to see if user wants to run script in working directory
    
    usrInp = usrInp.lower()
    if usrInp in ('y', 'yes'):
        return True
    elif usrInp in ('n', 'no'):
        return False
    else:
        print "Invalid entry. Use y/n"
        yesChk()
    
def repRen():
    inpChr = raw_input("Replace Character: ")
    repWth = raw_input("Replace With: ")
    repChk = raw_input( "Replace all occurances of " + inpChr + " with " + repWth + "? (y/n):")
    if yesChk(repChk):  
        filenames = os.listdir(os.curdir)
        for filename in filenames:
            newFilename = filename.replace(inpChr,repWth)
            print ("Renaming ", filename, " to ", newFilename, "...")
            os.rename(filename, newFilename)
    else:
        print("Exiting...")

dirChk = raw_input("Replace/rename files in current directory?(y/n)")
if yesChk(dirChk):
    print ("Time to replace and rename!")
    repRen()
else:
    print("Exiting...")
