label train_hands_label:
    python:
        location_choice = "None" # used to ensure variable is created and populated "Breast", "Pubis", "Bum", "Inner thigh", "Both Breasts"
        location_choice = handTrainingLocationChoice() # choose random location to massage with hand
        resetEventRelatedVariables()
    if location_choice == "Breast":
        "This scene will be where to train your hands using [gabrielle.name]`s techniques on your breasts."
    elif location_choice == "Pubis":
        "This scene will be where to train your hands using [gabrielle.name]`s techniques on your pubis."
    elif location_choice == "Bum":
        "This scene will be where to train your hands using [gabrielle.name]`s techniques on your bum."
    elif location_choice == "Inner thigh":
        "This scene will be where to train your hands using [gabrielle.name]`s techniques on your inner thigh."
    elif location_choice == "Both Breasts":
        "This scene will be where to train your hands using [gabrielle.name]`s techniques on both of your breasts."
    else:
        "{color=#E32636}Something went wrong with your randomly selected training plan, report this to the dev"
    python:
        her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost = handTrainingVariableGenerator(location_choice)
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while training your hands"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    
    jump players_room

label train_mouth_label:
    python:
        location_choice = "None"
        location_choice = mouthTrainingLocationChoice()
        resetEventRelatedVariables()
    if location_choice == "Fingers":
        "This scene will be where you train your mouth using the techniques taught by [gabrielle.name] on your fingers."
    elif location_choice == "Dildo":
        "This scene will be where you train your mouth using the techniques taught by [gabrielle.name] using your dildo."
    elif location_choice == "Training dummy":
        "This scene will be where you train your mouth using the techniques taught by [gabrielle.name] training dummy."
    else:
        "{color=#E32636}Something went wrong with your randomly selected training plan, report this to the dev"
    python:
        her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost = mouthTrainingVariableGenerator(location_choice)
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while training your mouth"
    if did_level_up == True:
        show screen mouth_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_mouth_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump players_room

label train_feet_label:
    python:
        location_choice = "None"
        location_choice = footTrainingLocationChoice()
        resetEventRelatedVariables()
    if location_choice == "Fingers":
        "This scene will be training your feet using your hands"
    elif location_choice == "Dildo":
        "This scene will be training your feet using a dildo"
    elif location_choice == "Training dummy":
        "This scene will be training your feet using a training dummy"
    else:
        "{color=#E32636}Something went wrong with your randomly selected training plan, report this to the dev"
    python:
        her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost = footTrainingVariableGenerator(location_choice)
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    $ renpy.block_rollback() # This must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You somehow orgasmed from the thought or using your feet"
    if did_level == True:
        show screen foot_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_foot_level_up_screen(number_of_levels = [did_level_up])
    jump players_room

label train_vaginal_label:
    python:
        location_choice = "None"
        location_choice = vaginalTrainingChoice()
        resetEventRelatedVariables()
    if location_choice == "Fingers":
        "Vaginal training using fingers"
    elif location_choice == "Clit":
        "Vaginal training massaging clit"
    elif location_choice == "Dildo outer":
        "Vaginal training outercourse with dildo"
    elif location_choice == "Dildo inter":
        "Vaginal training intercourse with dildo"
    elif location_choice == "Training dummy outer":
        "Vaginal training outercourse with training dummy"
    elif location_choice == "Training dummy inter":
        "Vaginal training intercourse with training dummy"
    else:
        "{color=#E32636}Something went wrong with your randomly selected training plan, report this to the dev"
    python:
        her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost = vaginalTrainingVariableGenerator(location_choice)
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    $ renpy.block_rollback() # This must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "Your orgasmed while training your pussy"
    if did_level == True:
        show screen vaginal_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_vaginal_level_up_screen(number_of_levels = [did_level_up])
    jump players_room

label train_anal_label:
    python:
        location_choice = "None"
        location_choice = analTrainingChoice()
        resetEventRelatedVariables()
    if location_choice == "Fingers":
        "You train your arse with your fingers"
    elif location_choice == "Dildo outer":
        "You train your arse by using your dildo outside"
    elif location_choice == "Dildo inter":
        "You train your arse by fucking it with your dildo"
    elif location_choice == "Training dummy outer":
        "You train your arse by using your training dummy outside"
    elif location_choice == "Training dummy inter":
        "You train your arse by fucking your training dummy"
    else:
        "{color=#E32636}Something went wrong with your randomly selected training plan, report this to the dev"
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    #
    # some function to increase anal level
    #
    jump players_room

#######################################################
# The following are only used for trans/futa/gay packs#
#######################################################

label train_just_the_tip_label:
    python:
        noneFunction()
        resetEventRelatedVariables()
        #
        # some function to check current just the tip level
        # current_just_the_tip_exp
        # just_the_tip_level
        # just_the_tip_exp_for_level
        #
    "Train your just the tip skill using the techniques taught by [gabrielle.name]."
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    #
    # some function to increase just the tip experience
    #
    jump players_room

label train_cock_label:
    python:
        noneFunction()
        resetEventRelatedVariables()
        #
        # some function to check current cock experience
        # current_cock_exp
        # cock_level
        # cock_exp_for_level
        #
    "Use the skills taught by [gabrielle.name] to train your cock skill."
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    show screen player_stamina_reduction_screen(amount_lost = stamina_cost)
    #
    # some function to increase cock experience
    #
    jump players_room
