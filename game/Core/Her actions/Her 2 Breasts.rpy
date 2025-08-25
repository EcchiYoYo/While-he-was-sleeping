label rub_breast_introduction_scene:
    "You rub your left breast"
    #
    #
    #
    #
    #
    #
    python:
        intro_2_completed = True
        did_orgasm, coins_gained = rubBreastArousalIncrease() # do not use coins gained here for popup, use base coin gain
        base_coin_gain, not_used = pc.rubBreastArousalGain() # this is needed to get base arousal gain so that coin gain is not multiplied twice
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubBreastArousalGainGlobal())
    jump introduction_3

label rub_left_breast_label:
    if intro_2_completed == False:
        jump rub_breast_introduction_scene
    "Caress your left breast."
    #
    #
    #
    #
    python:
        noneFunction()
    jump his_room

label rub_right_breast_label:
    "Caress your right breast."
    #
    #
    #
    #
    python:
        noneFunction()
    jump his_room

label rub_both_breasts_label:
    "Caress both your breasts."
    #
    #
    #
    #
    python:
        noneFunction()
    jump his_room