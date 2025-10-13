# rub breast intro
# rub left breast
# rub right breast
# rub both breasts
# pinch left nipple
# pinch right nipple
# pinch both nipples
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
        did_level_up = pc.increaseHandExp(rubBreastArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(rubBreastArousalGainGlobal())
        did_orgasm, coins_gained = rubBreastArousalIncrease() # do not use coins gained here for popup, use base coin gain
        base_coin_gain, not_used = pc.rubBreastArousalGain() # this is needed to get base arousal gain so that coin gain is not multiplied twice
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubBreastArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
        #
        # need to set arousal back to zero plus whatever is over 150
        # need to increase player orgasm counters
        #
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
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
        did_level_up = pc.increaseHandExp(rubBreastArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(rubBreastArousalGainGlobal())
        did_orgasm, coins_gained = rubBreastArousalIncrease()
        base_coin_gain, not_used = pc.rubBreastArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubBreastArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label rub_right_breast_label:
    "Caress your right breast."
    #
    #
    #
    #
    python:
        did_level_up = pc.increaseHandExp(rubBreastArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(rubBreastArousalGainGlobal())
        did_orgasm, coins_gained = rubBreastArousalIncrease()
        base_coin_gain, not_used = pc.rubBreastArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubBreastArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label rub_both_breasts_label:
    "Caress both your breasts."
    #
    #
    #
    #
    python:
        did_level_up = pc.increaseHandExp(rubBothBreastArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(rubBothBreastArousalGainGlobal())
        did_orgasm, coins_gained = rubBothBreastArousalIncrease()
        base_coin_gain, not_used = pc.rubBothBreastArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubBothBreastArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from your breast massage"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label pinch_left_nipple_label:
    "You pinch and roll your left nipple"
    #
    #
    #
    #
    python:
        did_level_up = pc.increaseHandExp(pinchNippleArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(pinchNippleArousalGainGlobal())
        did_orgasm, coins_gained = pinchNippleArousalIncrease()
        base_coin_gain, not_used = pc.pinchNippleArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = pinchNippleArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipple"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label pinch_right_nipple_label:
    "You pinch and roll your right nipple"
    #
    #
    #
    #
    python:
        did_level_up = pc.increaseHandExp(pinchNippleArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(pinchNippleArousalGainGlobal())
        did_orgasm, coins_gained = pinchNippleArousalIncrease()
        base_coin_gain, not_used = pc.pinchNippleArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = pinchNippleArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipple"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label pinch_both_nipple_label:
    "You pinch and roll both of your nipples"
    #
    #
    #
    #
    python:
        did_level_up = pc.increaseHandExp(pinchBothNippleArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentHandExp(pinchBothNippleArousalGainGlobal())
        did_orgasm, coins_gained = pinchBothNippleArousalIncrease()
        base_coin_gain, not_used = pc.pinchNippleArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = pinchBothNippleArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from pinching and rolling your nipples"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room
