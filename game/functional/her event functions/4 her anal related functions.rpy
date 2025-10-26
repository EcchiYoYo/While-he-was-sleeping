init python:
    import math    
    
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
    
    def fingerArseArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.fingerArseArousalGain()
        upgrades_arousal_multiplier = ((upgrades.hand_arousal_multiplier + upgrades.anal_arousal_multiplier) / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain

    def fingerArseArousalIncrease():
        arousal_gain = fingerArseArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain


    # combined functions for variable generation in events
    def rubBumCombinedVariableGenerator():
        her_global_arousal_gain = rubBumArousalGainGlobal()
        did_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_orgasm, not_used = rubBumArousalIncrease()
        base_coin_gain, not_used = pc.rubBumArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain

    def fingerArseholeCombinedVariableGenerator():
        her_global_arousal_gain = fingerArseArousalGainGLobal()
        did_hand_level_up = pc.increaseHandExp(her_global_arousal_gain)
        did_persistent_hand_level_up = increasePersistentHandExp(her_global_arousal_gain)
        did_anal_level_up = pc.increaseAnalExp(her_global_arousal_gain)
        did_persistent_anal_level_up = increasePersistentAnalExp(her_global_arousal_gain)
        did_orgasm, not_used = fingerArseArousalIncrease()
        base_coin_gain, not_used = pc.fingerArseArousalGain()
        coin_gain = upgrades.increaseUpgradesCoins(base_coin_gain)
        return did_hand_level_up, did_persistent_hand_level_up, did_anal_level_up, did_persistent_anal_level_up, coin_gain, her_global_arousal_gain
