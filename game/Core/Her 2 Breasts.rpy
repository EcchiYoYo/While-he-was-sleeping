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
        did_orgasm, coins_gained = rubBreastArousalIncrease()
    show screen coins_gained_popup_screen(amount_gained = coins_gained)
    show screen player_arousal_increase_screen(amount_gained = rubBreastArousalGainGlobal())
    jump introduction_3



