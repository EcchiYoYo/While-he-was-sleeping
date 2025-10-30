# rub ass
# finger ass
label rub_bum_label:
    "You gently rub your bum cheeks"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = rubBumCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from rubbing your bum cheeks"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label finger_arse_label:
    "You finger your own arsehole"
    #
    #
    #
    #
    python:
        did_hand_level_up, did_persistent_hand_level_up, did_anal_level_up, did_persistent_anal_level_up, coin_gain, her_global_arousal_gain = fingerArseholeCombinedVariableGenerator()
    
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while fingering yourself"
    if did_hand_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_hand_level_up])
    if did_persistent_hand_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_hand_level_up])
    if did_anal_level_up == True:
        show screen anal_level_up_screen(number_of_levels = [did_anal_level_up])
    if did_persistent_anal_level_up == True:
        show screen persistent_anal_level_up_screen(number_of_levels = [did_persistent_anal_level_up])
