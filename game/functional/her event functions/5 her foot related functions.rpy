# caress chest
# he sucks her toes
# rub his balls
# give him a footjob
init python:
    import math

    def rubChestWithFootArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubChestWithFootArousalGain()
        upgrades_arousal_multiplier = (upgrades.foot_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain

    def rubChestWithFootArousalIncrease():
        arousal_gain = rubChestWithFootArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(3)
        return did_orgasm, arousal_gain
    
    def heSucksHerToesArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.heSucksHerToesArousalGain()
        upgrades_arousal_multiplier = (upgrades.foot_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain

    def heSucksHerToesArousalIncrease():
        arousal_gain = heSucksHerToesArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(3)
        return did_orgasm, arousal_gain
    
    def rubHisBallsHerFootArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.rubHisBallsHerFootArousalGain()
        upgrades_arousal_multiplier = (upgrades.foot_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain

    def rubHisBallsHerFootArousalIncrease():
        arousal_gain = rubHisBallsHerFootArousalGainGlobal()
        did_orgasm = pc.increaseArousal(arousal_gain)
        pc.reduceStamina(1)
        return did_orgasm, arousal_gain
    
    def footjobHerArousalGainGlobal():
        default_arousal_increase, default_multiplier = pc.footjobArousalGain()
        upgrades_arousal_multiplier = (upgrades.foot_arousal_multiplier / 1000)
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + (multiplier_total * default_arousal_increase))
        return actual_arousal_gain
    
    def footjobHerArousalIncrease():
        arousal_gain = footjobArousalGainGlobal()
        did_orgasm = pc.footjobArousalGain(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
    #############################################################
    # Functions combining the above plus character specific     #
    # functions to generate variables required for events       #
    #############################################################
    def rubChestWithFootCombinedVariableGenerator():
        her_global_arousal_gain = rubChestWithFootArousalGainGlobal() # calculate her arousal gain
        did_level_up = pc.increaseFootExp(her_global_arousal_gain) # increase her foot exp
        did_persistent_level_up = increasePersistentFootExp(her_global_arousal_gain) # increase her persistent foot exp
        did_orgasm, not_used = rubChestWithFootArousalIncrease() # increase her arousal
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.rubChestWithFootArousalGain() # coins gained from her arousal increase
        his_arousal_increase, his_default_arousal_increase = man.rubChestWithFootArousalGain((pc.foot_level / 1000)) # calculate his arousal gain
        did_he_level_up = man.increaseChestExp(his_arousal_increase) # increase his chest resistance exp
        did_he_persistent_level_up = increasePersistentHisChestExp(his_arousal_increase) # increase his persistent chest resistance exp
        did_he_orgasm = man.increaseArousal(his_arousal_increase) # increase his arousal
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase)) # calculate and increase upgrade shop coins
        return did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase

    def heSucksHerToesCombinedVariableGenerator():
        her_global_arousal_gain = heSucksHerToesArousalGainGlobal()
        did_level_up = pc.increaseFootExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentFootExp(her_global_arousal_gain)
        did_orgasm, not_used = heSucksHerToesArousalIncrease()
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.heSucksHerToesArousalGain()
        # he gets no arousal increase from this action
        # he can`t level up
        # he can`t gain persistent levels
        # he can`t orgasm
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return did_level_up, did_persistent_level_up, did_orgasm, coin_gain, her_global_arousal_gain
    
    def rubHisBallsHerFootCombinedVariableGenerator():
        her_global_arousal_gain = rubHisBallsHerFootArousalGainGlobal()
        did_level_up = pc.increaseFootExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentFootExp(her_global_arousal_gain)
        did_orgasm, not_used = rubHisBallsHerFootArousalIncrease()
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.rubHisBallsHerFootArousalGain()
        his_arousal_increase, his_default_arousal_increase = man.rubHisBallsHerFootArousalGain((pc.foot_level / 1000))
        did_he_level_up = man.increaseCockExp(his_arousal_increase)
        did_he_persistent_level_up = increasePersistentHisCockExp()
        did_he_orgasm = man.increaseArousal(his_arousal_increase)
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase))
        return did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase
    
    def footjobCombinedVariableGenerator():
        her_global_arousal_gain = footjobHerArousalGainGlobal()
        did_level_up = pc.increaseFootExp(her_global_arousal_gain)
        did_persistent_level_up = increasePersistentFootExp(her_global_arousal_gain)
        did_orgasm, not_used = footjobHerArousalIncrease()
        base_coin_gain, used_for_his_arousal_gain_multiplier = pc.footjobArousalGain()
        his_arousal_increase, his_default_arousal_increase = man.footjobHisArousalGain((pc.foot_level / 1000))
        did_he_level_up = man.increaseCockExp(his_arousal_increase)
        did_he_persistent_level_up = increasePersistentHisCockExp()
        did_he_orgasm = man.increaseArousal(his_arousal_increase)
        coin_gain = upgrades.increaseUpgradeCoins((base_coin_gain + his_default_arousal_increase))
        return did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase
