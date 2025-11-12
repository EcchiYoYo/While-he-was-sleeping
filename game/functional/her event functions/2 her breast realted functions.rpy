init python:
    import math
    # rub breast, increase player arousal medium, reduce stamina small, reduce wakefulness small
    # used to calculate arousal gained from action
    def rubBreastArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubBreastArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def rubBreastArousalIncrease():
        arousal_gain = rubBreastArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    # rub both breasts, increase player arousal large, reduce stamina medium, reduce wakefulness small
    # used to calculate arousal gained from action
    def rubBothBreastArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubBothBreastArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def rubBothBreastArousalIncrease():
        arousal_gain = rubBothBreastArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(7)
        return did_orgasm, arousal_gain
    # pinch nipple, increase player arousal large, reduce stamina medium, reduce wakefulness small
    # used to calculate arousal gained from action
    def pinchNippleArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.pinchNippleArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total* default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def pinchNippleArousalIncrease():
        arousal_gain = pinchNippleArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    # pinch both nipples, increase player arousal very large, reduce stamina large, reduce wakefulness small
    # used to calculate arousal gained from action
    def pinchBothNippleArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.pinchBothNipplesArousalGain()
        upgrades_arousal_multiplier = (upgrades.hand_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def pinchBothNippleArousalIncrease():
        arousal_gain = pinchBothNippleArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(7)
        return did_orgasm, arousal_gain
    #############################################################
    # Functions combining the above plus character specific     #
    # functions to generate variables required for events       #
    #############################################################
    def introRubBreastCombinedVariableGenerator():
        her_global_arousal_gain = 5
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubBreastArousalIncrease()
        base_coin_gain = her_global_arousal_gain
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm

    def rubBreastCombinedVariableGenerator():
        her_global_arousal_gain = rubBreastArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubBreastArousalIncrease()
        base_coin_gain, not_used = pc.rubBreastArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm
    
    def rubBothBreastCombinedVariableGenerator():
        her_global_arousal_gain = rubBothBreastArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubBothBreastArousalIncrease()
        base_coin_gain, not_used = pc.rubBothBreastArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm
        
    def pinchNippleCombinedVariableGenerator():
        her_global_arousal_gain = pinchNippleArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = pinchNippleArousalIncrease()
        base_coin_gain, not_used = pc.pinchNippleArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm
    
    def pinchBothNippleCombinedVariableGenerator():
        her_global_arousal_gain = pinchBothNippleArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = pinchBothNippleArousalIncrease()
        base_coin_gain, not_sued = pc.pinchBothNippleArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain, did_orgasm
