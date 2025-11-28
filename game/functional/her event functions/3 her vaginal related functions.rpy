init python:
    import math
    # rub pubis, increase player arousal tiny, reduce stamina tiny, reduce wakefulness small
    # used to calculate arousal gained from action
    def rubPubisArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubPubisArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total* default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def rubPubisArousalIncrease():
        arousal_gain = rubPubisArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(3)
        return did_orgasm, arousal_gain
    # rub inner thigh, increase player arousal small, reduce stamina small, reduce wakefulness small
    # used to calculate arousal gained from action
    def rubInnerThighArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubInnerThighArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def rubInnerThighArousalIncrease():
        arousal_gain = rubInnerThighArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    # rub outer pussy lips, increase player arousal medium, reduce stamina medium, reduce wakefulness small
    # used to calculate arousal gained from action
    def rubOuterPussyLipsArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubOuterPussyLipsArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def rubOuterPussyLipsArousalIncrease():
        arousal_gain = rubOuterPussyLipsArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    # rub clit (requires moist fingers), increase player arousal large, reduce stamina medium, reduce wakefulness small
    # used to calculate arousal gained from action
    def massageClitArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.massageClitArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def massageClitArousalIncrease():
        arousal_gain = massageClitArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        if game_time.block == 4:
            pc.reduceStamina(7)
        else:
            pc.reduceStamina(6)
        return did_orgasm, arousal_gain
    # finger pussy (requires moist pussy), increase player arousal very large, reduce stamina large, reduce wakefulness small
    # used to calculate arousal gained from action
    def fingerPussyArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.fingerPussyArousalGain()
        upgrades_arousal_multiplier = ((upgrades.hand_arousal_multiplier + upgrades.vaginal_arousal_multiplier) / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def fingerPussyArousalIncrease():
        arousal_gain = fingerPussyArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        if game_time.block == 4:
            pc.reduceStamina(10)
        else:
            pc.reduceStamina(6)
        return did_orgasm, arousal_gain
    # vaginal outercourse
    def vaginalOutercourseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.vaginalOutercourseArousalGain()
        upgrades_arousal_multiplier = (upgrades.vaginal_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def vaginalOutercourseArousalIncrease():
        arousal_gain = vaginalOutercourseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(8)
        return did_orgasm, arousal_gain
    # vaginal intercourse
    def vaginalIntercourseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.vaginalIntercourseArousalGain()
        upgrades_arousal_multiplier = (upgrades.vaginal_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal and reduces stamina
    def vaginalIntercourseArousalIncrease():
        arousal_gain = vaginalIntercourseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(15)
        return did_orgasm, arousal_gain

    #############################################################
    # Functions combining the above plus character specific     #
    # functions to generate variables required for events       #
    #############################################################
    def rubPubisCombinedVariableGenerator():
        her_global_arousal_gain = rubPubisArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubPubisArousalIncrease()
        base_coin_gain, not_used = pc.rubPubisArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain
    
    def rubInnerThighCombinedVariableGenerator():
        her_global_arousal_gain = rubInnerThighArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubInnerThighArousalIncrease()
        base_coin_gain, not_used = pc.rubInnerThighArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain

    def rubOuterPussyLipsCombinedVariableGenerator():
        her_global_arousal_gain = rubOuterPussyLipsArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubOuterPussyLipsArousalIncrease()
        base_coin_gain, not_used = pc.rubOuterPussyLipsArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain

    def massageClitCombinedVariableGenerator():
        her_global_arousal_gain = massageClitArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = massageClitArousalIncrease()
        base_coin_gain, not_used = pc.massageClitArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain
    
    def fingerPussyCombinedVariableGenerator():
        her_global_arousal_gain = fingerPussyArousalGainGlobal()
        did_hand_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_hand_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_vaginal_level_up = pc.increaseVaginalExp(her_global_arousal_gain)
        did_persistent_vaginal_level_up = increasePersistentVaginalExp(her_global_arousal_gain)
        did_orgasm, not_used = fingerPussyArousalIncrease()
        base_coin_gain, not_used = pc.fingerPussyArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_hand_level_up, did_persistent_hand_level_up, did_vaginal_level_up, did_persistent_vaginal_level_up, coin_gain, her_global_arousal_gain
