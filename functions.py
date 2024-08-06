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
        points_n_lives()
        i.d_i_backpack()
        to_clear()
    else:
      print("\nNow you're walking and find a lighter. Do you want to keep it for later?")
      yn_lighter = input(" -").lower()
      if "yes" in yn_lighter:
        print("\nGood idea! Now you have a nice lighter!")
        points += 1
        points_n_lives()
        i.di_backpack.append("lighter")
        i.d_i_backpack()
        to_clear()
      elif "no" in yn_lighter:
        print("\nEs no bueno, that could've been used to make a fire!")
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
        eat_fish()

##########
#Ask if they want to make a fire
def di_final_point():
  global lives, points
  if "lighter" in i.di_backpack:
    print("\nIt's dark, do you want to make a fire?")
    yn_fire = input(" -").lower()
    if "yes" in yn_fire:
      print("\nYay! You made a fire!")
      points += 1
      if points == 5:
        made_it()
      else:
        points_n_lives()
        i.d_i_backpack()
        to_clear()
    elif "no" in yn_fire:
      print("\nWow, that was not smart. Now you're cold")
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
      di_final_point()
  else:
    print("\nIt's dark, and you're getting tired. Do you want to sleep?")
    yn_sleep = input(" -").lower()
    if "yes" in yn_sleep:
      print("\nMmmm, you fell asleep and a shark came and ate you. You \nlost all " + str(lives) + " of your lives!")
      lives = 0
      if lives < 1 and points == 4:
        if_lives_less_than_1()
      elif "no" in yn_sleep:
        print("\nGood thing you didn't fall asleep cause a shark could've eaten you...")
        points += 1
        points_n_lives()
        i.d_i_backpack()
      elif points == 5:
        made_it()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      di_final_point()

##########
#Asks if they want mirror
def d_last_point():
  global points, lives
  s_to_clear()
  print("You are walking and found a mirror, do you pick it up?")
  yn_mirror = input(" -").lower()
  if "yes" in yn_mirror:
    print("\nGood idea! You were able to shine the light at a helicopter, and now you're saved! You get all 5 points!\n")
    points = 5
    points_n_lives()
    i.di_backpack.append("mirror")
    i.d_i_backpack()
    made_it()
  elif "no" in yn_mirror:
    print("You should've pick it up!")
    lives -= 1
    points_n_lives()
    if lives < 1:
      if_lives_less_than_1()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    d_last_point()

##########
#They eat taco, and gets removed, and get 1 point
def s_eat():
  global points, lives
  i.s_backpack.remove("taco")
  print("\nYou ate the taco, and feel energized! Yay!")
  points += 1
  points_n_lives()
  i.swamp_backpack()
  to_clear_swamp()
  
##########
#Doesn't eat taco, lives - 1
def sn_eat():
  global points, lives
  print("\nYou should've eaten the taco! Come on! It's all old and soggy, nowy you can't eat it.")
  lives -= 1
  points_n_lives()
  i.s_backpack.remove("taco")
  i.swamp_backpack()
  to_clear_swamp()

##########
#Asks if they want to use sharp stick and can get fish
def use_sharp_stick():
  global lives, points
  print("\nYou're getting bored and a little hungry, so \ndo you want to use your stick and get a fish from the swamp?")
  yn_use_sharp_stick = input(" -").lower()
  if "yes" in yn_use_sharp_stick:
    print("\nExcellent! That was a good decision because you needed the exercise and you got a fish!")
    points += 1
    points_n_lives()
    i.s_backpack.append("fish")
    i.swamp_backpack()
    to_clear_swamp()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    use_sharp_stick()
    
##########
def yn_fish():
  global lives, points
  if "fish" in i.s_backpack:
    print("\nSo now that you have your fish, do you want to eat it?")
    yn_eat_fish = input(" -").lower()
    if "yes" in yn_eat_fish:
      print("\nYou ate the fish, but it had salmonella!")
      lives -= 1
      points_n_lives()
      i.s_backpack.remove("fish")
      i.swamp_backpack()
      to_clear_swamp()
    elif "no" in yn_eat_fish:
      print("\nGood idea! I think the fish had salmonella. You dump the fish.")
      points += 1
      points_n_lives()
      i.s_backpack.remove("fish")
      i.swamp_backpack()
      to_clear_swamp()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      yn_fish()
  else:
    print("\nYou find an alligator tooth, do you want to keep it?")
    yn_alligator = input(" -").lower()
    if "yes" in yn_alligator:
      print("\nGood idea! You might need that for later...")
      points += 1
      points_n_lives()
      i.s_backpack.append("alligator tooth")
      i.swamp_backpack()
      to_clear_swamp()
    elif "no" in yn_alligator:
      print("\nHmmm you should've gotten that cause it could come in handy.")
      lives -= 1
      if lives < 1:
        if_lives_less_than_1()
      else:
        points_n_lives()
        i.swamp_backpack()
        to_clear_swamp()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      yn_fish()

##########
def alligator_tooth():
  global lives, points
  if "alligator tooth" in i.s_backpack:
    print("\nSo you have the tooth, do you want to use it to make a \nnecklace.")
    yn_necklace = input(" -").lower()
    if "yes" in yn_necklace:
      print("\nGood idea! The necklace will show others your awesomeness!")
      points += 1
      points_n_lives()
      i.s_backpack.remove("alligator tooth")
      i.swamp_backpack()
      to_clear_swamp()
    elif "no" in yn_necklace:
      print("\nThat was a bad idea! You could've showed off. Sorry, but you lost a point!")
      lives -= 1
      if lives < 1:
        if_lives_less_than_1()
      else:
        points_n_lives()
        i.s_backpack.remove("alligator tooth")
        i.swamp_backpack()
        to_clear_swamp()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      alligator_tooth()
  else:
    print("\nNow you found a blanket! Do you want the blanket?")
    yn_alligator_weapon = input(" -").lower()
    if "no" in yn_alligator_weapon:
      print("\nIt's dark, cold, and you have no blanket. Bad decision.")
      lives -= 1
      if lives < 1:
        if_lives_less_than_1()
      else:
        points_n_lives()
        i.swamp_backpack()
        to_clear_swamp()
    elif "yes" in yn_alligator_weapon:
      print("It's dark, cold, and you have a nice warm blanket.")
      points += 1
      points_n_lives()
      i.s_backpack.append("blanket")
      i.swamp_backpack()
      to_clear_swamp()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      alligator_tooth()

##########
def bug_repellent():
  global lives, points
  print("\nIt's getting dark and there are a ton of mosquitos.")
  print("Do you want to put on bug repellent?")
  yn_bug_repellent = input(" -").lower()
  if "yes" in yn_bug_repellent:
    print("\nYay! Now you're protected from the dang bugs.")
    points += 1
    if points == 5:
      made_it()
    else:
      points_n_lives()
      i.s_backpack.remove("bug repellent")
      i.swamp_backpack()
      to_clear_swamp()
  elif "no" in yn_bug_repellent:
    print("Well, a mosquito bit you. Guess what. The bug had a fatal virus. YOU DIED! You lost all " + str(lives) +
          " of your lives!")
    lives = 0
    t.sleep(2)
    if lives < 1 and points == 4:
      if_lives_less_than_1()
      print("SO CLOSE!")
    else:
      if_lives_less_than_1()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    bug_repellent()

##########
new_backpack = ["hammer", "soda", "nails", "tarp"]

def extend_backpack():
  global lives, points
  print("\nNow you're walking when you find an entirely different backpack!")
  print("In this backpack there is: ")
  print(new_backpack)
  print("\nDo you want to add these supplies to your own backpack?")
  yn_add_backpack = input(" -").lower()
  if "yes" in yn_add_backpack:
    points += 1
    if points == 5:
      print("\nThat was an amazing choice because...")
      made_it()
    else:
      print("\nSounds good!")
      i.s_backpack.extend(new_backpack)
      points_n_lives()
      i.swamp_backpack()
      to.clear_swamp()
  elif "no" in yn_add_backpack:
    print("\nOK, so you didn't get a point because you said no.")
    lives -= 1
    if lives < 1:
      if_lives_less_than_1()
    else:
      points_n_lives()
      i.swamp_backpack()
      to_clear_swamp()
  else:
    print("You have to say yes or no.")
    s_to_clear()
    extend_backpack()

##########
def last_s_one():
  global lives, points
  print("\nOK! This is the last question. With these new materials you can build something.")
  print("\nYou can either build a tent or a soda bar, \nso which is it?")
  which_one = input(" -").lower()
  if "tent" in which_one:
    print("\nI can see why you picked that you now, but also this is \n the end of the game.")
    print("\nYou deserve a little relaxation. So a tent is incorrect.")
    lives -= 1
    t.sleep(5)
    if lives < 1:
      if_lives_less_than_1()
      print("SOO CLOSE!\n")
      print("\nsorry :(")
    elif "bar" or "soda" in last_s_one:
      print("\nI am please to tell you that you made the right decision! You deserve relaxation!")
      points += 1
      t.sleep(4)
      made_it()
    else:
      print("You have to say yes or no.")
      s_to_clear()
      last_s_one()

##########
#Backpack for the swamp
s_backpack = ["taco", "sharp stick", "bug repellent"]

#Will always tell the user what's in the backpack
def swamp_backpack():
  global s_backpack
  print("In your backpack you have:")
  print(s_backpack)

#Backpack for the beach
di_backpack = ["expired soda", "fishing rod", "sunscreen"]

#Will always tell the user what's in the backpack
def d_i_backpack():
  global di_backpack
  print("In your backpack you have:")
  print(di_backpack)


#notes for readme. Writing better functions when needed. Naming varibales better. Commenting code. Just really breaking this down better.
