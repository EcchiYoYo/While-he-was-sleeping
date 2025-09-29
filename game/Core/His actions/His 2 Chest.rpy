label rub_chest_introduction_scene:
    "Caress his chest hair"
    #
    #
    #
    #
    python:
        intro_3_completed = True
        did_orgasm, arousal_gain = rubChestArousalIncrease()
        base_coin_gain = man.rubChestArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        activate_buttons = True
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if upgrades.view_victim_arousal_gains == True:
        show screen coins_gained_popup_screen(amount_gained = coin_gain)
        show screen victim_arousal_increase_screen(amount_gained = rubChestArousalGainGlobal())
    else:
        show screen coins_gained_popup_screen(amount_gained = "??")
        show screen victim_arousal_increase_screen(amount_gained = "??")
    jump introduction_to_mechanics_final

label rub_his_chest:
    if intro_3_completed == False:
        jump rub_chest_introduction_scene
    "Caress his chest hair"


    python:
        noneFunction()
        #
        # increase stats here
        #
        #
    jump his_room
