label rub_chest_introduction_scene:
    "Caress his chest hair"
    #
    #
    #
    #
    python:
        intro_3_completed
        did_orgasm, arousal_gain = rubChestArousalIncrease()
    if upgrades.view_victim_arousal_gains == True:
        show screen coins_gained_popup_screen(amount_gained = coins_gained)
        show screen player_arousal_increase_screen(amount_gained = rubChestArousalGainGlobal())
    jump introduction_to_mechanics_final

label rub_his_chest:
    "Caress his chest hair"


    python:
        noneFunction()
        #
        # increase stats here
        #
        #
    jump players_room