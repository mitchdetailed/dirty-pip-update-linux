#!usr/env/python3

# To Use this program, put this file in some directory, and navigate to that directory in the terminal.

# to navigate to the folder, type: ~$ cd <FOLDER_LOCATION>
# modify folder location with actual location. eg.: /home/user/Documents/python3

# From there, type the following into the Shell terminal:
#  ~$ pip list --outdated | python3 pip_update_all.py


import os
import sys

print("Gathering outdated package information. This may take a minute...\n")
data = sys.stdin.readlines()

#path = "/home/mitch/Python/pip_outdatedlist.txt"
#with open(path,'r') as fp:
a = 0
for line in data:
    #print(line)
    a += 1
    if a > 2 : 
        b,*c = line.split()
        print("\nAttempting to update %s\n" % (b))
        os.system('pip install --user --upgrade %s' % (b))