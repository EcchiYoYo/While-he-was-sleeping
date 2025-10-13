label her_mouth_kiss_label():
    "You kiss him"
    #
    #
    #
    python:
        did_level_up = pc.increaseMouthExp(kissArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(kissArousalGainGlobal())
        did_orgasm, coins_gained = kissArousalIncrease() # do not use coins gained here for popup, use base coin gain
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.kissArousalGain() # this is needed to get base arousal gain so that coin gain is not multiplied twice
        his_arousal_increase, his_default_arousal_increase = man.kissArousalGain((pc.self.mouth_level / 1000)) # need to send the divided value of her mouth skill to calculate his arousal gains
        did_he_level_up = man.increaseFaceExp(his_arousal_increase) # need to send his actual arousal increase for face exp value
        did_he_orgasm = man.kissArousalIncrease(his_arousal_increase) # increase victims arousal and check for orgasm
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase)) # need to send base values for arousal gain for both parties
    # popup for mouth exp

    # popup for global mouth exp

    # popup for face exp

    # popup for global face exp

    # popup for player arousal increase

    # popup for victim arousal increase
    if did_orgasm == True:
        "You orgasmed while gently kissing him"
    if did_he_orgasm == True:
        "He orgasmed from your gently kiss"
    jump his_room

label her_mouth_deep_kiss_label():
    "You passionately kiss him in his sleep."
    #
    #
    #
    python:
        # used standard kiss for her stats, she gains the same 5 arousal he gains 5 instead of 3
        noneFunction()
        #
        # add stat change functions
    jump his_room

label her_mouth_suck_your_fingers_label():
    "You suck your fingers coating them with saliva."
    python:
        # cannot raise arousal above 40 from sucking fingers
        pc.finger_state = "saliva"
        #
        # Add function for stat changes
    jump his_room

label her_mouth_suck_juices_from_fingers_label():
    if pc.finger_state == "girl cum":
        "You suck your girl cum from your fingers, they are now coated with your saliva."
    else:
        "You slurp his cum from your fingers, they are now coated with your saliva."
    python:
        pc.finger_state = "saliva"
        #
        # Add function for stat changes
    jump his_room

label her_mouth_clean_girl_cum_from_face_label():
    "You slurp the girl cum from his face hiding the evidence that you leaked all over his face."
    python:
        man.face_state = "saliva"
        #
        # Add function for stat changes
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
        #
        # add function for stat changes
    jump his_room

label her_mouth_clean_girl_cum_from_chest_label():
    "You lap up the girl cum coating his chest, hiding the evidence you ever ground your pussy along his chest."
    python:
        man.chest_state = "saliva"
        #
        # add function for stat changes
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
        #
        # add stat change function here
    jump his_room

label her_mouth_clean_girl_cum_stomach_label():
    "You lick the girl cum from his stomach, hiding the evidence your juices were ever there."
    python:
        man.stomach_state = "saliva"
        #
        # add stat change function
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
        #
        # add stat changes here
        #
    jump his_room

label her_mouth_clean_girl_cum_fingers_label():
    "You suck his fingers cleaning away your girl cum, like you were never here."
    python:
        man.finger_state = "saliva"
        #
        # add stat change functions
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
        #
        #
        # add stat change functions
    jump his_room

label her_mouth_clean_girl_cum_thighs_label():
    "You lap the girl cum coating his thighs, hiding the evidence it was ever there."
    python:
        man.thigh_state = "saliva"
        #
        # add stat change functions
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
        #
        #
        # add stat change functions
    jump his_room

label her_mouth_clean_cum_ass_label():
    "You give him a rimjob ensuring the suck every last drop of your cum from his arse, hiding the evidence you ever came here."
    python:
        man.ass_state = "saliva"
        #
        # add stat change functions
    jump his_room