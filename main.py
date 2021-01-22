# Game starts here
name = input("Please enter your name to begin the adventure!\n ")

# Main story blocks are in this dictionary. All story texts are pulled from here.
storychoices = {
"B1":"You stand up and dust off your clothes. Your head still feels dizzy as you try to look around,\n"
     "you find yourself at the edge of a forest. Ahead of you in the clearing is a large town of stone and spires.\n"
     "Just then, you notice some rustling in the bushes near you.\nWhat do you choose?\n\n",
"B1b":"As you slowly near the bush, a tiny, furry little creature darts out and away,\ncausing you to fall back in "
      "surprise.  Feeling foolish for being jumpy,\nyou pick yourself up, and that's when you see it. Something else, "
      "in the bushes.\nYou reach in and grab a red gem stone. It looks to be worth something so you pocket it quickly.\n"
      "You decide to quickly head for town.\n\n",
"B2":"As you make it to the "
     "large open gates of the town, you try to catch your breath.\nYour eyes widen as it hits you: the smell of spices, "
     "the wash of colours and the hustle and bustle of the traders on the street.\nAs you walk around, a sign catches "
     "your eye.\nWhat do you choose?\n\n",
"B2a":"You follow some winding stone steps up along a tower to the top then pass\nthrough some hanging beads into a "
      "rather small room full of cushions and\nincense candles. In the middle is a balding dwarf, with his hands over "
      "a crystal ball\nin front of him. He looks up at you.\n“Nice view from up here, eh? But I don’t think you’re "
      "here for the view,”" " " + name + " " "“.\nHow do I know your name?” He chuckles.\n“I know all.” He very mysteriously "
                                     "hovers his hands over his ball as he says this.\n“Now, what do you want?”\n\n",
"B2aa":"“Now listen here you little shit. You wanna get smart with me?\nWell, hows this for a fortune reading?”\nThe "
       "Dwarf throws one of his crystal balls. With a thud,\nit connects squarely on your forehead, sending you "
       "hurtling\nout and off the edge of the stairs sending you to your untimtely demise.\nGame over.\n\n",
"B2ab":"“Slow down. First I wanna see some coin.  What's that? You're dirt poor?\nThen I can't help ya, now scram, "
       "before I start flingin' my balls around.”\nThe Dwarf gets impatient with your exit and decided to help but "
       "rolling\ninto a ball and slamming into you,sending you hurtling out and off the edge of the tower.  "
       "You die.\nGame over.\n\n",
"B2c":"“Psst, hey, you! Over here”\nA hooded figure standing under a nearby archway beckons you over.\n“You look "
      "lost.  Well I can help you if you help me,\nunderstand?  I can tell you aren’t from around here.\n "
      "I can get you home, no problem.  All you have to do is\nmake sure this gets delivered to an annoying old man "
      "outside of town.”  He tries to\nhand you a parcel.  What do you do?\n\n",
"B3":"You decide to head for the Inn.  While a short walk away, it was a little tricky\nto find as it was nestled in "
     "a dark pocket of town, snuggly between other shops.\nThe tavern’s wooden sign creeks back and forth as you "
     "enter.  The place is packed, with singing and laughing,\nbut you cannot help but catch the glare of others; one "
     "in particular, sitting in the\nback-left corner with a cowl covering most of their face and the hilt of a dagger "
     "playing between their fingers.\nAs you get to the bar, a small woman springs up, cleaning the fog from her "
     "spectacles with her apron.\n“Deary me, it gets so hot in here you could roast a boar!  What can I do you with, "
     "my love?” she says to you.\n\n",
"B3b":"You want to order a drink but realise you have no money. There is a mug filled to the brim "
                  "which looks untouched.\nYou decide to take a chance. You grab it and chug it down.\nIt probably "
                  "wasn't the best idea to drink the contents of something you don't know of.\nYou feel a splitting "
                  "headache and the world goes dark around you.\nThus ends your journey, thrown out and left for dead "
                  "in a dark alley.\nGame over.\n\n",
"B4":"“You don’t know where you are? Oh goodness me. Looks like we got another one.\nYou’re not the first to come "
     "in here asking that lately, and I fear you may not be the last.”\nShe sighs out of concern for you.\n“This "
     "here is the town of Ultime, second only to the grand city of\nKorith in all the lands of Alteria.  But I "
     "suppose you haven’t\na clue what I’m on about, just like the others.”\nRubbing her chin, she gets lost in "
     "thought for a moment.\n“I guess there’s nothin’ for it. He’ll hate me but I’ll deal with that old wart later.\n"
     "What did you say your name was?"" " + name + "? What a lovely name, dear. There is a hermit who lives just\n"
                                                   "outside of town.  He don’t like bein' bothered but he’ll know "
                                                   "how to help.  Just tell him Nettle sent you.\nAnd before you go, "
                                                   "take this map, I have his location marked out for you. Don't get "
                                                   "lost!”\n\n",
"B4b":"“Psst, hey, you! Over here”\nThe hooded figure you saw staring at you from the Inn was standing under a nearby "
      "archway.\n“Couldn’t help over-hearing you need help.  Well I can help you if you help me, understand?\nI know "
      "you’re lost, you aren’t from around here.\nI can get you home, no problem.  All you have to do is make sure "
      "this gets delivered to an annoying old man outside of town.”\nHe tries to hand you a parcel.  What do you do?\n\n",
"B4c":"“You refuse? Not very smart. See, we have an issue now. I can't let anyone know about this package,\nso I'm "
      "afraid I can't let you leave here alive.”\nThe man opens his palm towards you and blows strange dust in "
      "your face. "
      "Before you can react, you feel your feet\nget heavy and your eyes close.  You are left for dead in a cold, "
      "dark alley.\nGame over.\n\n",
"B5":"You find yourself back outside of town, walking across a lush green hill,\nheading for the X marked on your map "
     "by Nettle.  You see smoke drifting lazily\ninto the blue sky and as you get nearer, a half-domed house appears.  "
     "You knock on the door,\nbut there is no answer. What do you choose?\n\n",
"B5a":"You decide to do as the shady man says.  Before you know it, you are knocking on the\ndoor to the hermit’s "
      "house just outside of town.\nAn old man opens the door and screams in delight.\n“My pie has arrived! Out of "
      "my way!”\nHe snatches the parcel from you and unwraps it wildly.  Inside is a pie which he eats in one gulp.  "
      "His face turns green and he goes cross-eyed.\n“P-poison…” he mutters as he falls dead in front of you.\nYou "
      "hear screams as a few onlookers have witnessed what just happened.\nYou panic, quickly stumble out of the way, "
      "and scrap your knees as you pick yourself up and run.\nYou do not have time to think of where you are heading, "
      "but you run as hard as you can, not stopping for a second.\nYour eyes get heavy, then everything goes "
      "dark.\nWhen your eyes open, you don’t know how much time\nhas passed or where you are.  You are no longer in "
      "the green fields outside Ultime, quite the opposite in fact.\nYou find yourself amid structures of stone from "
      "a civilisation of past.\nThere are decaying archways and bridges over swamps.  Houses without walls, and "
      "the constant, faintly echoing cries of the lost souls bound to this\naccursed place.  A rush of wind sends "
      "a chill down your spine.\nAppearing over you in a green mist, a ghost of rotting flesh and bone screams. "
      "“HeLp Me. HELP ME!”  What do you do?\n\n",
"B5b":"You bang on the door again.  This time, the door opens slowly.\nYou see an old man dead on the floor, pie "
      "coming out of his mouth.\n “Murderer!” comes a shout from behind you.  It’s the shady hooded figure from "
      "the Inn.\n“I seen it with my own eyes!”\nAn angry mob begins to descend upon you. You panic, quickly stumble "
      "out of the way, and scrap your\nknees as you pick yourself up and run.  You do not have time to think of where "
      "you are heading, but you run as hard as you can, not stopping for a second.\nYour eyes get heavy, then "
      "everything goes dark.\nWhen your eyes open, you don’t know how much time has passed or where you are.  "
      "You are no longer in the green fields outside Ultime, quite the opposite in fact.\nYou find yourself amid "
      "structures of stone from a civilisation of past.\nThere are decaying archways and bridges over swamps.  "
      "Houses without walls, and the constant,\nfaintly echoing cries of the lost souls bound to this accursed place.  "
      "A rush of wind sends a chill down your spine.\nAppearing over you in a green mist, a ghost of rotting flesh "
      "and bone screams. “HeLp Me. HELP ME!”\nWhat do you do?\n\n",
"B6":"You peer in through the window.  It is hard to make anything out as the room is dimly lit.\nYou spot "
     "something on the floor.  To your horror, you see an old man lying\nstill in a pool of his own blood.  You "
     "jerk away from the window.\n“What’s this?” comes a voice from behind you.\nThe mysterious hooded figure from "
     "the Inn is standing there, with a mischievous grin.\nA few passers-by slow down and look in "
     "your direction.\n“It seems this outsider has killed the poor hermit!” he shouts to the onlookers. "
     "“Justice must be done.” \n"
     "He flings his dagger, which plants itself firmly into the wall, inches from your face.\nHe lunges for you.  "
     "You panic, quickly stumble out of the way, and scrap your knees as you pick yourself up\nand run.  You do not "
     "have time to think of where you are heading,\nbut you run as hard as you can, not stopping for a second.  Your "
     "eyes get heavy, then everything goes dark.\n " "\nWhen your eyes open, you don’t know how much time has passed or "
     "where you are.\nYou are no longer in the green fields outside Ultime, quite the opposite in fact.  You find "
     "yourself amid structures of stone from a civilisation of past.\nThere are decaying archways and bridges over "
     "swamps.  Houses without walls, and the constant,\nfaintly echoing cries of the lost souls bound to this "
     "accursed place.  A rush of wind sends a chill down your spine.\nAppearing over you in a green mist, a ghost "
     "of rotting flesh and bone screams.\n“HeLp Me. HELP MEEE!” What do you do?\n\n",
"B6a":"You scramble around for something to fight off the ghost with.\nYou grab a large stone by your foot "
      "and through it as hard as you can.\nThe ghost looks at you in disbelief as the rock completely passes "
      "through it.\n“Really? Of all the things, you thought that would be a good idea? I may be dead but you’re "
      "the one with dirt for brains.\nThis is why I bloody hate the living; you ask for help but all they know "
      "how to do is resort to violence.”\nThe ghost disappears into the mist, leaving you lost and alone.  "
      "You walk on for hours but it is no good, you are just going around in circles.\nYou give up, falling "
      "to the floor exhausted, waiting for the inevitable end.\nGame over.\n\n",
"B6b":"“Heart… I have lost… my heart… red… shiny.”\nYou show that you are in no possession of such a thing, "
      "much to the dismay of the ghost.\n“Well fiddlesticks. I don’t know where I lost it, but my search "
      "continues.\nWhat’s that? You, like my heart, are lost too? You shouldn’t be\nwondering these woods, "
      "get too deep and you’ll never make it back out.\nListen, just head straight for that large rock in "
      "the distance,\nthen make a right and you’ll come across an old, marooned ship.\nHead in through the hull "
      "and you’ll be out of here.”\n\nListening to the ghost’s directions, you find yourself outside the very ship "
      "he mentioned.  Lucky for you he was telling the truth!\nYou run inside through a gaping hole in the hull. "
      "You stand amazed as the interior looks\nnothing like a decrepit ship. Rows of food-stuffed tables are laid "
      "out, separated by royal red carpets.\nCandles are placed everywhere, even on top of other candles,\nall "
      "melting as one. And ghosts.  A lot more ghosts.\nBut these were not human.  They were sharks, all "
      "dressed smartly in old-fashioned suits.\n“You there!” shouts the largest of them, who happened to be "
      "sitting on a golden throne in the back.\n\n“You finally made it" " " + name + " "",wonderful! You’re probably "
                                                                               "wondering just what in Davy "
                                                                               "Jones’ Locker is going on here.\n"
                                                                               "Just bear in mind, I’m only the "
                                                                               "messenger, but I have direct contact "
                                                                               "with the… shall we say, author, of "
                                                                               "all this.\nYou see, you’re in a game. "
                                                                               "An insultingly simplistic game that "
                                                                               "needs to come to an\nend now before "
                                                                               "those nested if statements become "
                                                                               "too burdensome.\nI don’t know what "
                                                                               "that means either, I’m just telling "
                                                                               "you what I’ve been told.\nLuckily I "
                                                                               "can summon a portal home for you "
                                                                               "because magic.\nStep into the portal "
                                                                               "and you’ve won the game!“\n\n",
"B6c":"“Heart… I have lost… my heart… red… shiny.”\nYou show the glowing red gem you found earlier.\n“MY HEART! Where "
      "did you find it? Please, return it me!”\nYou hand over the heart. The ghost flies up and down in joy before "
      "composing himself.\n“Thank you so much! I always thought the living were insufferable jerks, but you’re "
      "alright.\nWhat’s that? You need to find the way out? \nJust head straight for that large rock in "
      "the distance,\nthen make a right and you’ll come across an old, marooned ship.  Head in through the hull "
      "and you’ll be out of here.”\n\nListening to the ghost’s directions, you find yourself outside the very ship\n "
      "he mentioned.  Lucky for you he was telling the truth!\nYou run inside through a gaping hole in the hull. "
      "You stand amazed as the\ninterior looks nothing like a decrepit ship.\nRows of food-stuffed tables are laid "
      "out, separated by royal red carpets.\nCandles are placed everywhere, even on top of other candles, all\n"
      "melting as one. And ghosts.  A lot more ghosts. But these were not human.\nThey were sharks, all "
      "dressed smartly in old-fashioned suits.\n“You there!” shouts the largest of them, who happened to be\n "
      "sitting on a golden throne in the back.\n\n“You finally made it"" " + name + " "",wonderful! You’re probably "
                                                                               "wondering just what in Davy "
                                                                               "Jones’ Locker is going on here.\n"
                                                                               "Just bear in mind, I’m only the "
                                                                               "messenger, but I have direct contact "
                                                                               "with the… shall we say, author, of "
                                                                               "all this.\nYou see, you’re in a game. "
                                                                               "An insultingly simplistic game that "
                                                                               "needs to come to an\nend now before "
                                                                               "those nested if statements become "
                                                                               "too burdensome.\nI don’t know what "
                                                                               "that means either, I’m just telling "
                                                                               "you what I’ve been told.\nLuckily I "
                                                                               "can summon a portal home for you "
                                                                               "because magic.\nStep into the portal "
                                                                               "and you’ve won the game!“\n\n",
}
# All ending outcomes are within this function
def ending():
    if gem != 0 and map != 0:
        print(
            "Well done! You got the best ending!\nThe lady from Crows Inn and the ghost with his heart are both\nstanding next to the Shark King, waving you good-bye.")
        quit = input("\nPress any key to quit")
    elif gem != 0 and map == 0:
        print(
            "Well done! You didn't get the best ending, but that's fine!\nThe ghost with his heart is standing next to the Shark King, waving you good-bye.")
        quit = input("\nPress any key to quit")
    elif gem == 0 and map != 0:
        print(
            "Well done! You didn't get the best ending, but that's fine!\nThe lady from Crows Inn is standing next to the Shark King, waving you good-bye.")
        quit = input("\nPress any key to quit")
    else:
        print("Well, you got to the end,\nbut I don't know if I'd call that winning, really. Try again for a better outcome?")
        quit = input("\nPress any key to quit")

# Items
gem = 0
map = 0

print(storychoices["B1"])

choice = input("1) Run toward town\n2) Inspect the bush\n\n")

if choice == "1":
    print(storychoices["B2"])
    choice = input("1) Fortune Tellers straight ahead\n2) Town exit to the left\n3) Dark Crow Inn to the right\n\n")
    if choice == "1":
        print(storychoices["B2a"])
        choice = input("1) I thought you knew all?\n2) I want to go home\n")
        if choice == "1":
            print(storychoices["B2aa"])
            quit = input("\nPress any key to quit")
        elif choice == "2":
            print(storychoices["B2ab"])
            quit = input("\nPress any key to quit")
        else:
            pass
    elif choice == "2":
        print(storychoices["B2c"])
        choice = input("1) Take parcel\n2) Refuse offer\n\n")
        if choice == "1":
            print(storychoices["B5a"])
            choice = input("1) Attack ghost\n2) Help ghost\n\n")
            if choice == "1":
                print(storychoices["B6a"])
            elif choice == "2":
                print(storychoices["B6b"])
                ending()
        elif choice == "2":
            print(storychoices["B4c"])
            quit = input("\nPress any key to quit")
        else:
            pass
    else:
        print(storychoices["B3"])
        choice = input("1)	Where am I?\n2)	Order a drink\n\n")
        if choice == "1":
            print(storychoices["B4"])
            map += 1
            choice = input("1) Visit the hermit\n2) Ignore Nettles advice and head back to the main market\n\n")
            if choice == "1":
                print(storychoices["B5"])
                choice = input("1) Knock again, but harder\n2) Peep through the window\n\n")
                if choice == "1":
                    print(storychoices["B5b"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()
                elif choice == "2":
                    print(storychoices["B6"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()
                else:
                    pass
            elif choice == "2":
                print(storychoices["B4b"])
                choice = input("1) Take parcel\n2) Refuse offer\n\n")
                if choice == "1":
                    print(storychoices["B5a"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()

                elif choice == "2":
                    print(storychoices["B4c"])
                    quit = input("\nPress any key to quit")
                else:
                    pass
            else:
                pass
        elif choice == "2":
            print(storychoices["B3b"])
            quit = input("\nPress any key to quit")
        else:
            pass
elif choice == "2":
    print(storychoices["B1b"])
    gem += 1
    print(storychoices["B2"])
    choice = input("1) Fortune Tellers straight ahead\n2) Town exit to the left\n3) Dark Crow Inn to the right\n\n")
    if choice == "1":
        print(storychoices["B2a"])
        choice = input("1) I thought you knew all?\n2) I want to go home\n\n")
        if choice == "1":
            print(storychoices["B2aa"])
            quit = input("\nPress any key to quit")
        elif choice == "2":
            print(storychoices["B2ab"])
            quit = input("\nPress any key to quit")
        else:
            pass
    elif choice == "2":
        print(storychoices["B2c"])
        choice = input("1) Take parcel\n2) Refuse offer\n\n")
        if choice == "1":
            print(storychoices["B5a"])
            choice = input("1) Attack ghost\n2) Help ghost\n\n")
            if choice == "1":
                print(storychoices["B6a"])
                quit = input("\nPress any key to quit")
            elif choice == "2" and gem == 1:
                print(storychoices["B6c"])
                ending()
            elif choice == "2":
                print(storychoices["B6b"])
                ending()
        elif choice == "2":
            print(storychoices["B4c"])
            quit = input("\nPress any key to quit")
        else:
            pass
    else:
        print(storychoices["B3"])
        choice = input("1)	Where am I?\n2)	Order a drink\n\n")
        if choice == "2":
            print(storychoices["B3b"])
            quit = input("\nPress any key to quit")
        elif choice == "1":
            print(storychoices["B4"])
            map += 1
            choice = input("1) Visit the hermit\n2) Ignore Nettles advice and head back to the main market\n\n")
            if choice == "1":
                print(storychoices["B5"])
                choice = input("1) Knock again, but harder\n2) Peep through the window\n\n")
                if choice == "1":
                    print(storychoices["B5b"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2" and gem == 1:
                        print(storychoices["B6c"])
                        ending()
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()
                elif choice == "2":
                    print(storychoices["B6"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2" and gem == 1:
                        print(storychoices["B6c"])
                        ending()
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()
                else:
                    pass
            elif choice == "2":
                print(storychoices["B4b"])
                choice = input("1) Take parcel\n2) Refuse offer\n\n")
                if choice == "1":
                    print(storychoices["B5a"])
                    choice = input("1) Attack ghost\n2) Help ghost\n\n")
                    if choice == "1":
                        print(storychoices["B6a"])
                        quit = input("\nPress any key to quit")
                    elif choice == "2" and gem == 1:
                        print(storychoices["B6c"])
                        ending()
                    elif choice == "2":
                        print(storychoices["B6b"])
                        ending()

                elif choice == "2":
                    print(storychoices["B4c"])
                    quit = input("\nPress any key to quit")
                else:
                    pass
            else:
                pass
else:
    pass
