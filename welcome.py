#This is the start screen!
import time as t, os as o

def welcome():
  for i in range(3):
    t.sleep(.25)
    print("__  __  __  ____   __     ___   _____   __     __   ____    _ ")
    print("\ \/  \/ / |   _] |  |   |  _| |  _  | |  \   /  | |   _]  | |")
    print(" \  /\  /  |   _] |  |_  | |_  | |_| | |   \ /   | |   _]  |_|")
    print("  \/  \/   |____] | ___| |___| |_____| |__|\ /|__| |____]   o ")
    t.sleep(.5)
    if i < 2:
      o.system("clear")
