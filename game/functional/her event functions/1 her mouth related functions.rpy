init python:
    import math    
    # Kiss, raises player arousal small, raises victim arousal tiny, raises wakefulness small, reduce stamina tiny
    # used to calculate arousal gained from action
    def kissArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.kissArousalGain()
        upgrades_arousal_multiplier = (upgrades.mouth_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def kissArousalIncrease():
        arousal_gain = kissArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(3)
        return did_orgasm, arousal_gain
    # deep kiss
    def deepKissArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.deepKissArousalGain()
        upgrades_arousal_multiplier = (upgrades.mouth_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades-multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increases players arousal and reduces stamina
    def deepKissArousalIncrease():
        arousal_gain = deepKissArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(3)
        return did_orgasm, arousal_gain
    # player sucks her fingers, raises player arousal tiny, reduces wakefulness small, moistness players hands, neutral stamina
    def suckDryFingersArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.suckHerFingersArousalGain()
        upgrades_arousal_multiplier = (upgrades.mouth_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal no stamina reduction
    def suckDryFingersArousalIncrease():
        arousal_gain = suckDryFingersArousalGainGlobal()
        # sucking fingers cannot increase arousal above 40
        if arousal_gain + pc.arousal > 40:
            if pc.arousal < 40:
                arousal_gain = 40 - pc.arousal
            else:
                arousal_gain = 0
        did_orgasm = pc.increaseArousal(arousal_gain)
        return did_orgasm, arousal_gain
    # player sucks girl cum/victim cum from fingers, raises player arousal tiny, reduces wakefulness small, removes girl cum from player hands, adds saliva to player hands, neutral stamina
    def suckCumFingersArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.suckCumFingersArousalGain()
        upgrades_arousal_multiplier = (upgrades.mouth_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal no stamina reduction
    def suckCumFingersArousalIncrease():
        arousal_gain = suckCumFingersArousalGainGlobal()
        # sucking fingers cannot increase arousal above 40
        if arousal_gain + pc.arousal > 40:
            if pc.arousal < 40:
                arousal_gain = 40 - pc.arousal
            else:
                arousal_gain = 0
        did_orgasm = pc.increaseArousal(arousal_gain)
        return did_orgasm, arousal_gain
    # player cleans cum from victim, raises player arousal small, neutral wakefulness, removes cum from body part adds saliva to body part, raises suspicion if all cum not cleaned at end of night, neutral stamina
    def suckFluidsFromHimArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.suckFluidsFromHimArousalGain()
        upgrades_arousal_multiplier = (upgrades.mouth_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    # increase players arousal no stamina reduction
    def suckFluidsFromHimArousalIncrease():
        arousal_gain = suckFluidsFromHimArousalGainGlobal()
        # sucking cum cannot increase arousal above 75
        if arousal_gain + pc.arousal > 75:
            if pc.arousal < 75:
                arousal_gain = 75 - pc.arousal
            else:
                arousal_gain = 0
        did_orgasm = pc.increaseArousal(arousal_gain)
        return did_orgasm, arousal_gain
    #############################################################
    # Functions combining the above plus character specific     #
    # functions to generate variables required for events       #
    #############################################################
    def kissCombinedVariableGenerator():
        her_global_arousal_gain = kissArousalGainGlobal()
        did_level_up = pc.increaseMouthExp(her_global_arousal_gain) # increase in hand exp is arousal gain with multipliers
        did_persistent_level_up = increasePersistentMouthExp(her_global_arousal_gain) # increase in persistent exp as above
        did_orgasm, not_used = kissArousalIncrease() # do not use coins gained here for popup, use base coin gain
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.kissArousalGain() # this is needed to get base arousal gain so that coin gain is not multiplied twice
        his_arousal_increase, his_default_arousal_increase = man.kissArousalGain((pc.mouth_level / 1000)) # need to send the divided value of her mouth skill to calculate his arousal gains
        did_he_level_up = man.increaseFaceExp(his_arousal_increase) # need to send his actual arousal increase for face exp value
        did_he_persistent_level_up = increasePersistentHisFaceExp(his_arousal_increase) # increase in persistent face exp
        did_he_orgasm = man.increaseArousal(his_arousal_increase) # increase victims arousal and check for orgasm
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase)) # need to send base values for arousal gain for both parties
        return did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase

    def deepKissCombinedVariableGenerator():
        her_global_arousal_gain = deepKissArousalGainGlobal()
        did_level_up = pc.increaseMouthExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentMouthExp(her_global_arousal_gain)
        did_orgasm, not_used = kissArousalIncrease()
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.deepKissArousalGain()
        his_arousal_increase, his_default_arousal_increase = man.deepKissArousalGain((pc.mouth_level / 1000))
        did_he_level_up = man.increaseFaceExp(his_arousal_increase)
        did_he_persistent_level_up = increasePersistentHisFaceExp(his_arousal_increase)
        did_he_orgasm = man.increaseArousal(his_arousal_increase)
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase))
        return did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase
    
    def suckDryFingersCombinedVariableGenerator():
        her_global_arousal_gain = suckDryFingersArousalGainGlobal()
        did_level_up = pc.increaseMouthExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentMouthExp(her_global_arousal_gain)
        did_orgasm, not_used = suckDryFingersArousalIncrease()
        base_coin_gain, not_used = pc.suckHerFingersArousalGain()
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        # finger sucking cannot increase arousal above 40 (this must be last within the function to make sure coin gain is still calculated from potential arousal increase)
        if her_global_arousal_gain + pc.arousal > 40:
            if pc.arousal < 40:
                her_global_arousal_gain = 40 - pc.arousal
            else:
                her_global_arousal_gain = 0
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain
    
    def suckCumFingersCombinedVariableGenerator():
        her_global_arousal_gain = suckCumFingersArousalGainGlobal()
        did_level_up = pc.increaseMouthExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentMouthExp(her_global_arousal_gain)
        did_orgasm, not_used = suckCumFingersArousalIncrease()
        base_coin_gain, not_used = pc.suckCumFingersArousalGain()
        coin_gain = upgrades.increaseUpgradesCoins(base_coin_gain)
        # finger sucking cannot increase arousal above 40 (this must be last within the function to make sure coin gain is still calculated from potential arousal increase)
        if her_global_arousal_gain + pc.arousal > 40:
            if pc.arousal < 40:
                her_global_arousal_gain = 40 - pc.arousal
            else:
                her_global_arousal_gain = 0
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain
    
    def suckFluidsFromHim():
        her_global_arousal_gain = suckFluidsFromHimArousalGainGlobal()
        did_level_up = pc.increaseMouthExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentMouthExp(her_global_arousal_gain)
        did_orgasm, not_used = suckFluidsFromHimArousalIncrease()
        base_coin_gain, not_used = pc.suckFluidsFromHimArousalGain()
        coin_gain = upgrades.increaseUpgradesCoins(base_coin_gain)
        # sucking fluids form him cannot increase arousal above 75 (this must be last within the function to make sure coin gain is still calculated from potential arousal increase)
        if her_global_arousal_gain + pc.arousal > 75:
            if pc.arousal < 75:
                her_global_arousal_gain = 75 - pc.arousal
            else:
                her_global_arousal_gain = 0
        return did_level_up, did_persistent_level_up, coin_gain, her_global_arousal_gain
