#!/usr/bin/env python3

import sass
from input_w_stats import input_s

###FIX FIX FIX when integrating
user_intelligence=3

def beer_encounter(user):
    response_list=["You take a drink of sumptious sorghum whiskey, the finest you've ever tasted.", "You drink some more, it's been quite a day after all.", "You feel at one with all of humanity, but you're also losing fine motor control.", "You're getting a little woozy. Are you sure this is a good idea?", "Your vision is starting to blur and it's hard to see the cask anymore.", "You can't stand."]
    user_intelligence=3
    drink_query="yes"
    extra_drinks=0
    while drink_query=="yes":
        print(response_list[extra_drinks], '\n')
        user.attack-=1
        print("Your attack ability has been reduced to "+ str(user.attack)+".")
        if extra_drinks%2==1:
            user_intelligence-=1
            print("Your intelligence has been reduced to " + str(user_intelligence)+".")
        if extra_drinks>1:
            user.hp-=1
            print("Your health points have been reduced to " + str(user.hp) + ".") 
        if extra_drinks>=5:
            print("You go into a catatonic stupor. You aren't conscious for your death, but rest assured it was embarassing.")
            user.hp=0
            break
        drink_query=input_s("\nDo you want to keep drinking?\n", user)
        extra_drinks+=1