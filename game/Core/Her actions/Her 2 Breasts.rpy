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

