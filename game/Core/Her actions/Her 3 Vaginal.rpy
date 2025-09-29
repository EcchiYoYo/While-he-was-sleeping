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
        did_persistent_level_up = increasePersistentHandExp(rubPubisArousalGainGlobal())
        did_level_up = pc.increaseHandExp(rubPubisArousalGainGlobal()) # increase in hand exp is arousal gain with multipliers
        did_orgasm, coins_gained = rubPubisArousalIncrease()
        base_coin_gain, not_used = pc.rubPubisArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubPubisArousalIncrease())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed from rubbing your pubis"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label rub_inner_thigh_label:
    "Your massage the top of your inner thigh"
    #
    #
    #
    python:
        did_persistent_level_up = increasePersistentHandExp(rubInnerThighArousalGainGlobal())
        did_level_up = pc.increaseHandExp(rubInnerThighArousalGainGlobal())
        did_orgasm, coins_gained = rubInnerThighArousalIncrease()
        base_coin_gain, not_used = pc.rubInnerThighArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubInnerThighArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while rubbing your inner thigh"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up == True:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label rub_outer_pussy_lips_label:
    "Your rub your outer pussy lips"
    #
    #
    #
    python:
        did_persistent_level_up = increasePersistentHandExp(rubOuterPussyLipsArousalGainGlobal())
        did_level_up = pc.increaseHandExp(rubOuterPussyLipsArousalGainGlobal())
        did_orgasm, coins_gained = rubOuterPussyLipsArousalIncrease()
        base_coin_gain, not_used = pc.rubOuterPussyLipsArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = rubOuterPussyLipsArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while rubbing your outer pussy lips"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label massage_clit_label:
    "You flick your bean"
    #
    #
    #
    python:
        did_persistent_level_up = increasePersistentHandExp(massageClitArousalGainGlobal())
        did_level_up = pc.increaseHandExp(massageClitArousalGainGlobal())
        did_orgasm, coins_gained = massageClitArousalIncrease()
        base_coin_gain, not_used = pc.massageClitArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = massageClitArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while flicking your bean"
    if did_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_level_up)
    if did_persistent_level_up:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_level_up)
    jump his_room

label finger_pussy_label:
    #
    # check for virginity (if not virgin more fingers, maybe if virgin some reference to not pushing to deep in fear of breaking hymen)
    #
    "You finger yourself"
    python:
        # check code to ensure dual multiplier is being accounted for. as well as dual skill increase
        did_persistent_hand_level_up = increasePersistentHandExp(fingerPussyArousalGainGlobal())
        did_persistent_vaginal_level_up = increasePersistentVaginalExp(fingerPussyArousalGainGlobal())
        did_hand_level_up = pc.increaseHandExp(fingerPussyArousalGainGlobal())
        did_vaginal_level_up = pc.increaseVaginalExp(fingerPussyArousalGainGlobal())
        did_orgasm, coins_gained = fingerPussyArousalIncrease()
        base_coin_gain, not_used = pc.fingerPussyArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
    show screen coins_gained_popup_screen(amount_gained = coin_gain)
    show screen player_arousal_increase_screen(amount_gained = fingerPussyArousalGainGlobal())
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm == True:
        "You orgasmed while fingering yourself"
    if did_hand_level_up == True:
        show screen hand_level_up_screen(number_of_levels = did_hand_level_up)
    if did_persistent_hand_level_up:
        show screen persistent_hand_level_up_screen(number_of_levels = did_persistent_hand_level_up)
    if did_vaginal_level_up == True:
        show screen vaginal_level_up_screen(number_of_levels = did_vaginal_level_up)
    if did_persistent_hand_level_up:
        show screen persistent_vaginal_level_up_screen(number_of_levels = persistent_vaginal_level_up_screen)
    jump his_room