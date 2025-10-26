# rub pubis
# rub inner thigh
# rub outer pussy lips
# massage clit
# finger pussy (only option to also increase vaginal exp)
label rub_pubis_label:
    "Your rub your pubis"
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = rubPubisCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from rubbing your pubis"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label rub_inner_thigh_label:
    "Your massage the top of your inner thigh"
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = rubInnerThighCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while rubbing your inner thigh"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label rub_outer_pussy_lips_label:
    "Your rub your outer pussy lips"
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = rubOuterPussyLipsCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while rubbing your outer pussy lips"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label massage_clit_label:
    "You flick your bean"
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain = massageClitCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while flicking your bean"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label finger_pussy_label:
    #
    # check for virginity (if not virgin more fingers, maybe if virgin some reference to not pushing to deep in fear of breaking hymen)
    #
    "You finger yourself"
    python:
        # check code to ensure dual multiplier is being accounted for. as well as dual skill increase
        did_hand_level_up, did_persistent_hand_level_up, did_vaginal_level_up, did_persistent_vaginal_level_up, coin_gain, her_global_arousal_gain = fingerPussyCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while fingering yourself"
    if did_hand_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_hand_level_up])
    if did_persistent_hand_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_hand_level_up])
    if did_vaginal_level_up == True:
        show screen vaginal_level_up_screen(number_of_levels = [did_vaginal_level_up])
    if did_persistent_vaginal_level_up == True:
        show screen persistent_vaginal_level_up_screen(number_of_levels = [did_persistent_vaginal_level_up])
    jump his_room
