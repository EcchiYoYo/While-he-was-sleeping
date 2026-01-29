init python:
    import math    
    # rub bu, increase player arousal tiny, reduce stamina small, reduce wakefulness small
    def rubBumArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubBumArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduce stamina
    def rubBumArousalIncrease():
        arousal_gain = rubBumArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    # rub bu, increase player arousal small, reduce stamina small, reduce wakefulness small
    def fingerArseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.fingerArseArousalGain()
        upgrades_arousal_multiplier = ((upgrades.hand_arousal_multiplier + upgrades.anal_arousal_multiplier) / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduce stamina
    def fingerArseArousalIncrease():
        arousal_gain = fingerArseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        # block 4 is night time assault where all other time blocks would be daytime training scenes, training scenes require less stamina
        if game_time.block == 4:
            pc.reduceStamina(5)
        else:
            pc.reduceStamina(6)
        return did_orgasm, arousal_gain
    # intercourse and outercourse are handled by his cock actions rather than player vaginal actions, as such combined generators will call these functions but
    # be located in 5 his cock actions
    # anal outercourse
    def analOutercourseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.analOutercourseArousalGain()
        upgrades_arousal_multiplier = (upgrades.anal_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def analOutercourseArousalIncrease():
        arousal_gain = analOutercourseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(8)
        return did_orgasm, arousal_gain
    # anal intercourse
    def analIntercourseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.analIntercourseArousalGain()
        upgrades_arousal_multiplier = (upgrades.anal_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def analIntercourseArousalIncrease():
        arousal_gain = analIntercourseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(15)
        return did_orgasm, arousal_gain
    #############################################################
    # Functions combining the above plus character specific     #
    # functions to generate variables required for events       #
    #############################################################
    def rubBumCombinedVariableGenerator():
        her_global_arousal_gain = rubBumArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubBumArousalIncrease()
        base_coin_gain, not_used = pc.rubBumArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm

    def fingerArseholeCombinedVariableGenerator():
        her_global_arousal_gain = fingerArseArousalGainGlobal()
        did_hand_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_hand_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_anal_level_up = pc.increaseAnalExp(her_global_arousal_gain)
        did_persistent_anal_level_up = increasePersistentAnalExp(her_global_arousal_gain)
        did_orgasm, not_used = fingerArseArousalIncrease()
        base_coin_gain, not_used = pc.fingerArseArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_hand_level_up, did_persistent_hand_level_up, did_anal_level_up, did_persistent_anal_level_up, coin_gain, her_global_arousal_gain
