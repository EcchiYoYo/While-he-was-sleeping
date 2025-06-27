label her_mouth_kiss_label():
    "You kiss him"
    #
    #
    #
    python:
        noneFunction()
        #
        # Add function for stat changes
    jump his_room

label her_mouth_deep_kiss_label():
    "You passionately kiss him in his sleep."
    #
    #
    #
    python:
        noneFunction()
        #
        # add stat change functions
    jump his_room

label her_mouth_suck_your_fingers_label():
    "You suck your fingers coating them with saliva."
    python:
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
    if man.who_cum_on_face == "player":
        "You slurp your cum from his face, hiding the evidence that you jizzed there."
    elif man.who_cum_on_face == "victim":
        "You slurp his cum from his face, hiding the evidence you wiped it there."
    else:
        "Something went wrong and the game does not know who`s cum is on his face please report this."
    python:
        man.face_state = "saliva"
        man.who_cum_on_face = "none"
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
    if man.who_cum_on_chest == "player":
        "You suck your slimy load from his chest, hiding the evidence that you ever came here."
    elif man.who_cum_on_chest == "victim":
        "You suck his slimy load from his chest, hiding the evidence his jizz was ever there."
    else:
        "Something went wrong and the game does not know who`s cum is on his chest please report this."
    python:
        man.chest_state = "saliva"
        man.who_cum_on_chest = "none"
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
    if man.who_cum_on_stomach == "player":
        "You suck your cum from his chest, hiding the evidence your load was ever there."
    elif who_cum_on_stomach == "victim":
        "You suck his cum from his chest, hiding the evidence his load was ever there."
    else:
        "Something went wrong and the game does not know who`s cum is on his stomach please report this."
    python:
        man.stomach_state = "saliva"
        man.who_cum_on_stomach = "none"
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
    if man.who_cum_on_finger == "player":
        "You suck his fingers clean hiding that your cum was ever there."
    elif man.who_cum_on_finger == "victim":
        "You suck his fingers clean hiding that his cum was ver there."
    else:
        "Something went wrong and the game does not know who`s cum is on his fingers please report this."
    python:
        man.finger_state = "saliva"
        man.who_cum_on_finger = "none"
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
    if man.who_cum_on_thigh == "player":
        "You lap up your slimy load from his thighs, hiding the evidence it was ever there."
    elif man.who_wum_on_thigh == "victim":
        "You lap up his slimy load from his thighs, hiding the evidence it was ver there."
    else:
        "Something went wrong and the game does not know who`s cum is on his thighs please report this."
    python:
        man.thigh_state = "saliva"
        man.who_wum_on_thigh = "none"
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