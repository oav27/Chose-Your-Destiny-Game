import time as t, os as o
import inventory as i

points = 0
lives = 3

def to_clear():
  t.sleep(6)
  o.system("clear")

##########
def to_clear_swamp():
  t.sleep(6)
  o.system("clear")

##########
def s_to_clear():
  t.sleep(2)
  o.system("clear")

##########
def points_n_lives():
  print("--Lives: " + str(lives))
  print("--Points: " + str(points))

##########
def if_lives_less_than_1():
  global points
  count = 0
  t.sleep(4)
  o.system("clear")
  print("--Lives: " + str(lives))
  print("--Points: " + str(points))
  if points != 5:
    while points != 5:
      points += 1
      count += 1
  if count != 1:
    print("\n All you needed were " + str(count) + " more points!!")
  else:
    print("\nAll you needed was " + str(count) + " more point!!")
  print("GAME OVER!")

##########
def made_it():
  t.sleep(4)
  o.system("clear")
  points_n_lives()
  print("You won the game! You woke up from your dream...")

##########
#They get to the deserted island
def d_i():
  global points, lives
  print("You are at a deserted island")
  points_n_lives()
  print("\nYou find a backpack")
  i.swamp_backpack()

##########
#They drink the soda and lose life, drink removed from backpack
def di_drink():
  global lives, points
  i.di_backpack.remove("expired soda")
  print("\nYou drank your soda and now you're sick,\n that's tough!")
  lives -= 1
  points_n_lives()
  i.d_i_backpack()
  to_clear()

##########
#Will not drink the soda, +1 point
def din_drink():
  global points, lives
  i.di_backpack.remove("soda")
  print("\nGood choice, you would've gotten sick. You dump the soda.")
  points += 1
  points_n_lives()
  i.d_i_backpack()
  to_clear()

##########
#If they use the sunscreen
def by_sunscreen():
  global points, lives
  print("\nThe sun's coming out and it's getting hot, do you want to \nput on sunscreen?")
  yn_sunscreen = input(" -").lower()
  if "yes" in yn_sunscreen:
    print("\nGood job, you applied the sunscreen and now you're safe \nfrom the rays!")
    points += 1
    points_n_lives()
    u.di_backpack.remove("sunscreen")
    i.d_i_backpack()
    to_clear()
  elif "no" in yn_sunscreen:
    print("\nOOF that sucks, you should've put some on, now you're red \as a tomato. And you the sunscreen, nice going!")
    lives -= 1
    points_n_lives()
    i.di_backpack.remove("sunscreen")
    i.d_i_backpack()
    to_clear()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    by_sunscreen()

##########
#Ask if player wants to use fishing rod
def fishing_rod():
  global lives, points
  print("\nYou're getting hungry and want to eat.\nDo you want to use your fishing rod?")
  yn_use_fishingrod = input(" -").lower()
  if "yes" in yn_use_fishingrod:
    print("\nNice! You caught a fish!")
    points += 1
    points_n_lives()
    i.di_backpack.append("fish")
    i.d_i_backpack()
    to_clear()
  elif "no" in yn_use_fishingrod:
    print("\nWell... you didn't use the rod and now you're super hungry, nice going!")
    lives -= 1
    if lives < 1:
      if_lives_less_than_1()
    else:
      points_n_lives()
      i.d_i_backpack()
      to_clear()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    fishing_rod()

##########
#Ask if they want to eat fish, at deserted island
def eat_fish():
  global lives, points
  if "fish" in i.di_backpack:
    print("\nNow that you have the fish do you want to eat it?")
    ys_fish = input(" -").lower()
    if "yes" in ys_fish:
      print("\nGood idea! Now you're not hungry!")
      points += 1
      points_n_lives()
      i.di_backpack.remove("fish")
      i.d_i_backpack()
      to_clear()
    elif "no" in ys_fish:
      print("\nBad move! The fish ended getting super dirty and \was no good. You're still hungry.")
      i.di_backpack.remove("fish")
      lives -= 1
      if lives < 1:
        if_lives_less_than_1()
      else:
        points_n_lives
