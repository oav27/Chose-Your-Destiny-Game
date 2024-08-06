import welcome as w
import functions as f
import time as t, os as o
### NOTE: there is a way to win and lose
#Based on location will go to either function

def ready():
  print("\nWell I guess we can wait till you are ready.")
  print("\n\"Ready\" so that we can start the game.")
  ready = input(" -").lower()
  if "ready" in ready:
    print("\nOK! Here we go!\n")
    t.sleep(1)
    o.system("clear")
  else:
    print("\nSorry we know you didn't say ready, but we're going to start. Get ready, quick!")
    f.to_clear()

##########
def start():
  print("\nWant to play the game?")
  play = input(" -").lower()
  if "yes" in play:
    print("\nOK! Here we go!\n")
    f.s_to_clear()
  elif "no" in play:
    ready()
  else:
    print("Sorry, but you need to answer yes or no. Let's try again!")
    f.s_to_clear()
    start()

##########
def first():
  print("Do you want to go to a deserted island, or a swamp?")
  global location
  location = input(" -").lower()
  if "swamp" in location:
    f.swamp()
  elif "deserted island" in location:
    f.d_i()
  else:
    print("You must pick either the deserted island or the swamp.")
    t.sleep(2)
    o.system("clear")
    first()

##########
def beginning():
  if "deserted island" in location:
    print("Do you want to drink the soda?")
    yn_soda = input(" -").lower()
    if "yes" in yn_soda:
      f.di_drink()
    elif "no" in yn_soda:
      f.din_drink()
    else:
      print("You have to say yes or no.")
      t.sleep(2)
      o.system("clear")
      beginning()
  
  #At the swamp, asks about the taco
  elif "swamp" in location:
    print("Do you want to eat the taco?")
    yn_taco = input(" -").lower()
    if "yes" in yn_taco:
      f.s_eat()
    elif "no" in yn_taco:
      f.sn_eat()
    else:
      print("You have to say yes or no.")
      t.sleep(2)
      o.system("clear")
      beginning()

##########
w.welcome()
start()
first()
beginning()

##########
if "deserted island" in location:
  f.by_sunscreen()
  f.fishing_rod()
elif "swamp" in location:
  f.use_sharp_stick()
  f.yn_fish()


if "deserted island" in location:
  if f.lives > 0:
    f.eat_fish()

if "deserted island" in location:
  if f.lives > 0:
    f.di_final_point()

if "deserted island" in location:
  if f.points != 5 and f.lives > 0:
    f.d_last_point()

#######
if "swamp" in location:
  if f.lives > 0:
    f.alligator_tooth()
    
if "swamp" in location:
  if f.lives > 0:
    f.bug_repellent()

if "swamp" in location:
  if f.lives > 0 and f.points != 5:
    f.extend_backpack()

if "swamp" in location:
  if f.lives > 0 and f.points != 5:
    f.last_s_one()
