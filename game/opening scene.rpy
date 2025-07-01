label opening_scene:
    # This block checks for installed packs and if present activates them
    python:
        try:
            if l_pack_installed == True:
                l_pack = True
        except:
            l_pack = False
        try:
            if t_pack_installed == True:
                t_pack = True
        except:
            t_pack = False
        try:
            if g_pack_installed == True:
                g_pack = True
        except:
            g_pack = False
        try:
            if f_pack_installed == True:
                f_pack = True
        except:
            f_pack = False
        increaseCycleCount()
    if l_pack == True or t_pack == True or g_pack == True or f_pack == True:
        "Would you like to select from an installed pack or play using the default girl?"
        menu:
            "Play default":
                jump default_opening
            "Select from an installed pack":
                jump select_from_installed_packs
    else:
        jump default_opening


label select_from_installed_packs:
    python:
        if pc.name == "????":
            pc_name = "Nicole"
        else:
            pc_name = pc.name
        if pc.male_name == "????":
            pc_male_name = "Nick"
        else:
            pc_male_name = pc.male_name
    "Please select the pack you wish to play."
    menu:
        "Play the young {pc_name} pack?":
            jump l_pack_opening
        "Play the trans {pc_name} pack?":
            jump t_pack_opening
        "Play the {pc_male_name} pack?":
            jump g_pack_opening
        "Play the hermaphrodite {pc_name} pack?":
            jump f_pack_opening    
    
label default_opening:
    #
    # MC in bed
    #
    #
    pc_talk "Gah, so damn horny, I`ve already cum three times but I still need more."
    pc_talk "I think I should get a drink before going again."
    "At least once a month you have a period where you are super horny, no matter how much you masturbate it never seems to be enough."
    "This happens to be one of those periods, you`ve already cum three times, you`ve been masturbating for hours but still can`t seem to scratch that itch."
    #
    # opening scene, Nicole masturbates while watching victim sleep
    #
    #
    "As you walk down the hall you spot an open doorway and decide to peek inside."
    "Lying in bed is the figure of a man, a body you know quite well having just masturbated while thinking about it for the last few hours."
    "He is asleep, the sound of his slow rhythmic breathing reaching your ears."
    pc_talk "Hmmm, maybe once more before I get that drink."
    "Saying this you slip your hand into your panties while thinking about what you`d like to do with this man."
    "In no time at all you reach your peak and have to bite your lips to prevent you letting out a loud moan."
    pc_talk "Wow, didn`t think I`d get there that fast."
    "You reached your peak significantly faster than you had expected, and head back out to go get that drink while thinking about why you came so fast."
    #
    # MC back in her room leaning against wall
    #
    "While heading back to your room you had the thought that maybe you came so much faster because you were so close to him, the object of your obsession."
    "You decide to test your theory and head back towards his room."
    #
    # Standing at door
    #
    #
    pc_talk "What if I get closer, he seems to be sleeping soundly..."
    #
    # Lust filled eyes
    #
    pc_talk "...I might even be able to touch him."
    "I guess we should introduce this lust filled pervert, this is you the player."
    jump mc_naming

label mc_naming:
    #
    # Show player naked
    #
    python:
        pc.name = renpy.input("Enter your name or leave it blank for the default of Nicole.").capitalize()
        if not pc.name:
            pc.name = "Nicole"
        pc.name = pc.name.strip()
        pc.name = pc.name.split(" ")
        pc.name = pc.name[0]
    menu:
        "Your name is [pc.name], is that correct?"

        "Yes":
            python:
                pc_talk.name = pc.name
            jump victim_relation_setting
        "No":
            jump mc_naming

label victim_relation_setting:
    #
    # Standing image victim clothing level dependant upon some yet undecided metric
    #
    #
    menu:
        "And here we have the target of your lust..."
        
        "Your Friend":
            python:
                man.relationship = "Friend"
            "This is your childhood friend, he is staying for a week during the holidays, but whenever he stays you can`t help but lust after him."
            "He shows no interest in you sexually which frustrates you even more, he has no idea about your night time fantasies involving him."
        "Your Brother":
            python:
                man.relationship = "Brother"
            "Although he is your brother you share a close relationship and unknown to him, he is frequently the target of your night time fantasies."
            "He of course shows no sexual interest in his sister, but he does however love you quite dearly."
        "Your Father":
            python:
                man.relationship = "Daddy"
            "Many of your nightly fantasies involve your daddy, you just can`t help how much you find him sexually arousing."
            "As any father does, he loves his little girl without exception, and as with any normal father he does not have any sexual attraction to you, his daughter, his sweet little princess."
        "Your Uncle":
            python:
                man.relationship = "Uncle"
            "You can`t help but lust after your uncle, a man you share a close familial bond with but don`t see all that often, how could you not lust after him." 
            "He loves his niece and would do anything to make her smile."
            "During your night time fantasies you dream of him making you smile in a much more perverse way than he would ever consider."
        "A Stranger":
            python:
                man.relationship = "Stranger"
            "This man is unknown to you, he is a friend of your fathers and is staying for a while, he is gone when you wake in the morning and asleep before you get home at night, so you have no idea who he is."
            "Since he came to stay you can`t help but fantasise about this unknown man performing lewd acts with you, the added arousal from him being a complete stranger is almost too much to bear."
    python:
        if man.relationship == "Friend":
            single_use = "your childhood friend"
        elif man.relationship == "Brother":
            single_use = "your big brother"
        elif man.relationship == "Daddy":
            single_use = "your daddy"
        elif man.relationship == "Uncle":
            single_use = "your uncle"
        else:
            single_use = "a complete stranger"
    menu:
        "The target of your lust is [single_use], is that correct?"
        "Yes":
            pass
        "No":
            jump victim_relation_setting 

    "Although he doesn`t know about your perverse fantasies involving him, you can`t help but wonder what you could do to get a taste of that forbidden fruit for yourself."
    jump victim_naming

label victim_naming:    
    #
    # Standing image victim
    #
    #            
    python:
        man.name = renpy.input("And the name for the target of your lust filled fantasies is? Default is Romeo.").capitalize()
        if not man.name:
            man.name = "Romeo"
        man.name = man.name.strip()
        man.name = man.name.split(" ")
        man.name = man.name[0]
        victim_talk.name = man.name
    menu:
        "Your targets name is [man.name], is this correct?"

        "Yes":
            python:
                victim_talk.name = man.name
            if persistent.cycle_number > 0:
                menu:
                    "Would you like to view the introduction again? If not the points you would have gained will be added."
                    "Yes":
                        jump introduction_1
                    "No":
                        #
                        # add in points that would be gained from breast rub
                        # add in points that would be gained from chest caress
                        #
                        jump players_room
            else:
                jump introduction_1
            jump players_room
        "No":
            jump victim_naming
