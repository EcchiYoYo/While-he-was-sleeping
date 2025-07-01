label you_work_a_little:
    if persistent.first_upgrade_visit == False: # used to check if the scene tricking Grace has been seen before
        python:
            persistent.first_upgrade_visit = True
            if man.relationship == "Friend":
                first_use = "your friend"
            elif man.relationship == "Brother":
                first_use = "your brother"
            elif man.relationship == "Father":
                first_use = "your dad"
            elif man.relationship == "Uncle":
                first_use = "your uncle"
            else:
                first_use = "the stranger"
            persistent.first_upgrade_visit = True
        gabrielle "One moment before you head off to work [pc.name]."
        pc_talk "As long as it`s quick, [gabrielle.name] was it?"
        gabrielle "Correct and my sister is [grace.name], but while she sleeps we need to get a few things done."
        pc_talk "Like what?"
        gabrielle "Well like I told you I can teach you techniques to bring pleasure with the lightest of touches and my sister can sell you sleeping aids, bath oils incense sticks and the like."
        pc_talk "I remember this from last night, why are you telling me again?"
        gabrielle "Well the thing is my sister can manipulate the body to make it more resistant to things that would normally wake you."
        pc_talk "So?"
        gabrielle "Well if we trick her into thinking she`s performing these upgrades on you but instead she performs them on [first_use] he won`t wake si easily and you can have more time using him for pleasure."
        pc_talk "That sounds interesting, but she said her shop cost money and I don`t get paid that much from my work."
        gabrielle "Well that`s where some of the techniques I can teach you come in, not only can I teach you to bring untold pleasure I can make you more adept in your work, meaning you can earn more money."
        pc_talk "That does sound handy, so what do I need to do?"
        gabrielle "Well you just need to get an item that has the essence of [first_use] on it."
        pc_talk "Essence? What`s that like his cum?"
        gabrielle "Well cum is easiest but even sweat will do, so any item of clothing he has work should be enough."
        #
        #
        # PLayer retrieves the item
        #
        pc_talk "Okay, I`ll go grab something from the washing basket and then we can get this done; I really need to get to work soon."
        #
        # player hands item to Gabrielle
        #
        pc_talk "Will this do?"
        #
        # Gabrielle takes a long sniff
        #
        "[gabrielle.name] takes a long deep sniff of the clothing you brought her."
        gabrielle "Mmmmm... This should work."
        #
        # dodgy magic performed
        #
        gabrielle "Okay now give me something that belongs to you, make sure it`s clean, we will transfer his essence from his jumper to that."
        gabrielle "That way when we start the ritual to lock in the target of [grace.name]`s magic."
        pc_talk "Ritual? Magic?"
        gabrielle "Don`t worry about that, just think about how much more fun you can have if [first_use] is less likely to wake up when you`re having your night time fun."
        pc_talk "I guess you`re right, as long as it works I don`t care how it works."
        gabrielle "Okay I will get this done while you`re at work, once you get back come and see me and we`ll get started with [grace.name]`s ritual, you also earned a few coins last night soo make sure you buy an upgrade or two."
        pc_talk "Yeah you`re right I don`t wanna be late, catch you later [gabrielle.name]."
        "With that you head off to work."
    python:
        globalAdvanceTime(1)
        cash_earned = globalPoundsEarnedWorking()
        pc.money += cash_earned
    show screen money_earned_popup_screen(how_much = cash_earned)
    "You put in a shift at work and earned £[cash_earned]."
    
    #
    #
    #
    #
    jump players_room
