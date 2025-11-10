# rub breast intro
# rub left breast
# rub right breast
# rub both breasts
# pinch left nipple
# pinch right nipple
# pinch both nipples
label rub_breast_introduction_scene:
    python:
        resetEventRelatedVariables()
    "You rub your left breast"
    #
    #
    #
    #
    #
    #
    python:
        intro_2_completed = True
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = rubBreastCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
        #
        # need to set arousal back to zero plus whatever is over 150
        # need to increase player orgasm counters
        #
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump introduction_3

label rub_left_breast_label:
    python:
        resetEventRelatedVariables()
    if intro_2_completed == False:
        jump rub_breast_introduction_scene
    "Caress your left breast."
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = rubBreastCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label rub_right_breast_label:
    python:
        resetEventRelatedVariables()
    "Caress your right breast."
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = rubBreastCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label rub_both_breasts_label:
    python:
        resetEventRelatedVariables()
    "Caress both your breasts."
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = rubBothBreastCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label pinch_left_nipple_label:
    python:
        resetEventRelatedVariables()
    "You pinch and roll your left nipple"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = pinchNippleCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipple"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label pinch_right_nipple_label:
    python:
        resetEventRelatedVariables()
    "You pinch and roll your right nipple"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = pinchNippleCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipple"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label pinch_both_nipple_label:
    python:
        resetEventRelatedVariables()
    "You pinch and roll both of your nipples"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, coin_gain, her_arousal_gain = pinchBothNippleCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipples"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room
