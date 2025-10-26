label her_mouth_kiss_label():
    #
    # Add check for waking him
    #
    "You kiss him"
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_arousal_gain, his_arousal_gain = kissCombinedVariableGenerator()
    if did_level_up == True:
        "Stuff for her mouth level up"
    if did_persistent_level_up == True:
        "Stuff for her persistent mouth level up"
    if did_he_level_up == True:
        "Stuff for his face level up"
    if did_he_persistent_level_up == True:
        "Stuff for his face persistent level up"
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen victim_arousal_increase_screen(amount_gained = [his_arousal_gain])
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    
    if did_orgasm == True and did_he_orgasm == True:
        #
        # reset arousal here while checking for multiple orgasms (not likely but could happen)
        #
        "You both orgasmed while gently kissing him"
    elif did_he_orgasm == True:
        #
        # reset his arousal, and check for multiple orgasms
        #
        "He orgasmed from your gently kiss"
    elif did_orgasm == True:
        #
        # reset her arousal and check for multiple orgasms
        #
        "You orgasmed while gently kissing him"
    else:
        pass
    jump his_room

label her_mouth_deep_kiss_label():
    #
    # add check for him waking
    #
    "You passionately kiss him in his sleep."
    #
    #
    #
    python:
        
        did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_arousal_gain, his_arousal_gain = deepKissCombinedVariableGenerator()
        #
        # add stat change functions
    if did_level_up == True:
        "Stuff for her level up"
    
    if did_persistent_level_up == True:
        "Stuff for her persistent level up"
    
    if did_he_level_up == True:
        "Stuff for his level up"
    
    if did_he_persistent_level_up == True:
        "Stuff for his persistent level up"
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen victim_arousal_increase_screen(amount_gained = [his_arousal_gain])
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    if did_orgasm == True and did_he_orgasm == True:
        "You both orgasmed from your passionate kiss"
        #
        # reset arousal for both
        #
    elif did_orgasm == True:
        "You orgasmed while deeply kissing him"
        #
        # reset his arousal        #
    
    elif did_he_orgasm == True:
        "He orgasmed while you deeply kissed him"
        #
        # reset her arousal
        #
    else:
        pass
    
    jump his_room

label her_mouth_suck_your_fingers_label():
    "You suck your fingers coating them with saliva."
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckDryFingersCombinedVariableGenerator()
        # cannot raise arousal above 40 from sucking fingers
        pc.finger_state = "saliva"
        #
        # Add function for stat changes
    if did_level_up == True:
        "Stuff for her level up"
    if did_persistent_level_up == True:
        "Stuff for her persistent level up"
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    jump his_room

label her_mouth_suck_juices_from_fingers_label():
    if pc.finger_state == "girl cum":
        "You suck your girl cum from your fingers, they are now coated with your saliva."
    else:
        "You slurp his cum from your fingers, they are now coated with your saliva."
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckCumFingersCombinedVariableGenerator()
        # cannot raise arousal above 40 from sucking fingers
        pc.finger_state = "saliva"
        #
        # Add function for stat changes
    if did_level_up == True:
        "Stuff for her level up"
    if did_persistent_level_up == True:
        "Stuff for her persistent level up"
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    jump his_room

label her_mouth_clean_girl_cum_from_face_label():
    "You slurp the girl cum from his face hiding the evidence that you leaked all over his face."
    python:
        man.face_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        #
    # did level up
    if did_level_up == True:
        "You levelled your mouth skill"
    # did persistent level up
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_from_face_label():
    if man.player_face_cum_amount > 0:
        if man.victim_face_cum_amount > 0:
            "You slurp the mixture of your cum mixed with his cum from his face, hiding the evidence it was ever there."
        else:
            "You slurp your cum from his face."
    elif man.victim_face_cum_amount > 0:
        "You slurp his cum from his face, hiding the evidence you wiped it there."
    else:
        "Something went wrong and the game does not know who`s cum is on his face please report this."
    python:
        man.face_state = "saliva"
        man.player_face_cum_amount = 0
        man.victim_face_cum_amount = 0
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add function for stat changes
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_girl_cum_from_chest_label():
    "You lap up the girl cum coating his chest, hiding the evidence you ever ground your pussy along his chest."
    python:
        man.chest_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add function for stat changes
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_from_chest_label():
    if man.player_chest_cum_amount > 0:
        if man.victim_chest_cum_amount > 0:
            "You suck the slimy mix of his and your cum from his chest, hiding it was ever there."
        else:
            "You suck your slimy load from his chest, hiding the evidence that you ever came here."
    elif man.victim_chest_cum_amount > 0:
        "You suck his slimy load from his chest, hiding the evidence his jizz was ever there."
    else:
        "Something went wrong and the game does not know who`s cum is on his chest please report this."
    python:
        man.chest_state = "saliva"
        man.player_chest_cum_amount = 0
        man.victim_chest_cum_amount = 0
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add stat change function here
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_girl_cum_stomach_label():
    "You lick the girl cum from his stomach, hiding the evidence your juices were ever there."
    python:
        man.stomach_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add stat change function
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_stomach_label():
    if man.player_stomach_cum_amount > 0:
        if man.victim_stomach_cum_amount > 0:
            "You suck the combined load splattered across his stomach from both of you, savouring the flavour if the slimy mess, hiding the evidence it was ever there."
        else:
            "You suck the load you splattered across his stomach, savouring flavour as it slides down your throat, hiding the evidence it was ever there."
    elif man.victim_stomach_cum_amount > 0:
        "You suck his cum from his chest, hiding the evidence his load was ever there."
    else:
        "Something went wrong and the game does not know who`s cum is on his stomach please report this."
    python:
        man.stomach_state = "saliva"
        man.victim_stomach_cum_amount = 0
        man.player_stomach_cum_amount = 0
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add stat changes here
        #
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_girl_cum_fingers_label():
    "You suck his fingers cleaning away your girl cum, like you were never here."
    python:
        man.finger_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add stat change functions
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_fingers_label():
    if man.player_finger_cum_amount > 0:
        if man.victim_finger_cum_amount > 0:
            "You suck his fingers clean, hiding the mix of cum coating his fingers like you were never there."
        else:
            "You suck his fingers clean hiding the evidence your load was ever there."
    elif man.victim_finger_cum_amount > 0:
        "You suck his fingers clean hiding that his cum was ver there."
    else:
        "Something went wrong and the game does not know who`s cum is on his fingers please report this."
    python:
        man.finger_state = "saliva"
        man.victim_finger_cum_amount = 0
        man.player.finger_cum_amount = 0
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        #
        # add stat change functions
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_girl_cum_thighs_label():
    "You lap the girl cum coating his thighs, hiding the evidence it was ever there."
    python:
        man.thigh_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # 
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_thighs_label():
    if man.player_thigh_cum_amount > 0:
        if man.victim_thigh_cum_amount > 0:
            "You lap up the mixture of his cum and yours that coats his thighs, hiding the evidence it was ever there."
        else:
            "You lap up your slimy load from his thighs, hiding the evidence it was ever there."
    elif man.victim_thigh_cum_amount > 0:
        "You lap up his slimy load from his thighs, hiding the evidence it was ver there."
    else:
        "Something went wrong and the game does not know who`s cum is on his thighs please report this."
    python:
        man.thigh_state = "saliva"
        man.player_thigh_cum_amount = 0
        man.victim_thigh_cum_amount = 0
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        #
        # add stat change functions
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room

label her_mouth_clean_cum_ass_label():
    "You give him a rimjob ensuring the suck every last drop of your cum from his arse, hiding the evidence you ever came here."
    python:
        man.ass_state = "saliva"
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = suckFluidsFromHim()
        #
        # add stat change functions
    if did_level_up == True:
        "You levelled your mouth skill"
    if did_persistent_level_up == True:
        "You levelled your persistent mouth skill"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    jump his_room
