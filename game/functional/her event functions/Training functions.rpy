# Skill increase
# persistent skill increase
# Arousal increase
# ?? coins gained
#
init python:
    # hand training functions
    def handTrainingLocationChoice():
        if pc.stamina >= 7:
            choices = ["Breast", "Pubis", "Bum", "Inner thigh", "Both Breasts"]
        elif pc.stamina >= 5:
            choices = ["Breast", "Pubis", "Bum", "Inner thigh"]
        else:
            choices = ["Pubis"]
        picked = random.choice(choices)
        return picked
    def handTrainingVariableGenerator(location):
        if location == "Breast":
            her_arousal_gain = rubBreastArousalGainGlobal()
            base_coin_gain, not_used = pc.rubBreastArousalGain()
            did_orgasm, not_used = rubBreastArousalIncrease()
            stamina_cost = 5
        elif location == "Pubis":
            her_arousal_gain == rubPubisArousalGainGlobal()
            base_coin_gain, not_used = pc.rubPubisArousalGain()
            did_orgasm, not_used = rubPubisArousalIncrease()
            stamina_cost = 3
        elif location == "Bum":
            her_arousal_gain == rubBumArousalGainGlobal()
            base_coin_gain, not_used = pc.rubBumArousalGain()
            did_orgasm, not_used = rubBumArousalIncrease()
            stamina_cost = 5
        elif location == "Inner thigh":
            her_arousal_gain == rubInnerThighArousalGainGlobal()
            base_coin_gain, not_used = pc.rubInnerThighArousalGain()
            did_orgasm, not_used = rubInnerThighArousalIncrease()
            stamina_cost = 5
        elif location == "Both breasts":
            her_arousal_gain == rubBothBreastArousalGainGlobal()
            base_coin_gain, not_used = pc.rubBothBreastArousalGain()
            did_orgasm, not_used = rubBothBreastArousalIncrease()
            stamina_cost = 7
        else:
            her_arousal_gain = 0
            base_coin_gain = 0
            did_orgasm = False
            stamina_cost = 0
        multiplied_exp_value = int(floor(her_arousal_gain * pc.training_multiplier)) # monitor for balance
        did_level_up = pc.increaseHandExp(multiplied_exp_value)
        did_persistent_level_up = increasePersistentHandExp(multiplied_exp_value)
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return her_arousal_gain, base_coin_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost
    # mouth training functions
    def mouthTrainingLocationChoice():
        choices = ["Fingers"]
        if groceries.dildo == True:
            choices.append("Dildo")
        if groceries.training_dummy == True and pc.stamina >= 4:
            choices.append("Training dummy")
        picked = random.choice(choices)
        return picked
    def mouthTrainingVariableGenerator(location):
        if location == "Fingers":
            her_arousal_gain = suckDryFingersArousalGainGlobal()
            base_coin_gain, not_used = pc.suckHerFingersArousalGain()
            did_orgasm, not_used = suckDryFingersArousalIncrease()
            stamina_cost = 2
            pc.reduceStamina(stamina_cost)
        elif location == "Dildo":
            her_arousal_gain = pc.suckDildoArousalGain()
            base_coin_gain, not_used = pc.suckDildoArousalGain()
            did_orgasm, not_used = suckDildoArousalIncrease()
            stamina_cost = 2
        elif location == "Training dummy":
            her_arousal_gain = suckDummyArousalGainGlobal()
            base_coin_gain, not_used = pc.suckDummyArousalGain()
            did_orgasm, not_used = suckDummyArousalIncrease()
            stamina_cost = 4
        else:
            her_arousal_gain = 0
            base_coin_gain = 0
            did_orgasm = False
            stamina_cost = 0
        multiplied_exp_value = int(floor(her_arousal_gain * pc.training_multiplier))
        did_level_up = pc.increaseMouthExp(multiplied_exp_value)
        did_persistent_level_up = increasePersistentMouthExp(multiplied_exp_value)
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost
    # feet training functions
    def footTrainingLocationChoice():
        choices = ["Fingers"]
        if groceries.dildo == True and pc.stamina >= 5:
            choices.append("Dildo")
        if groceries.training_dummy == True:
            choices.append("Training dummy")
        picked = random.choice(choices)
        return picked
    def footTrainingVariableGenerator(location):
        if location == "Fingers":
            her_arousal_gain = rubChestWithFootArousalGainGlobal()
            base_coin_gain, not_used = pc.rubChestWithFootArousalGain()
            did_orgasm, not_used = rubChestWithFootArousalIncrease()
            stamina_cost = 3
        elif location == "Dildo":
            her_arousal_gain = footjobHerArousalGainGlobal()
            base_coin_gain, not_used = pc.footjobArousalGain()
            did_orgasm, not_used = footjobHerArousalIncrease()
            stamina_cost = 5
        elif location == "Training dummy":
            her_arousal_gain = rubChestWithFootArousalGainGlobal()
            base_coin_gain, not_used = pc.rubChestWithFootArousalGain()
            did_orgasm, not_used = rubChestWithFootArousalIncrease()
            stamina_cost = 3
        else:
            her_arousal_gain = 0
            base_coin_gain = 0
            did_orgasm = False
            stamina_cost = 0
        multiplied_exp_value = int(floor(her_arousal_gain * pc.training_multiplier))
        did_level_up = pc.increaseFootExp(multiplied_exp_value)
        did_persistent_level_up = increasePersistentFootExp(multiplied_exp_value)
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost
    # vaginal training functions
    def vaginalTrainingLocationChoice():
        choices = ["Fingers", "Clit"]
        if groceries.dildo == True and pc.stamina >= 8:
            choices.append("Dildo outer")
        if groceries.training_dummy == True and pc.stamina >= 8:
            choices.append("Training dummy outer")
        if groceries.dildo == True and pc.stamina >= 15 and pc.vaginal_virgin == False:
            choices.append("Dildo inter")
        if groceries.training_dummy == True and pc.stamina >= 15 and pc.vaginal_virgin == False:
            choices.append("Training dummy inter")
        picked = random.choice(choices)
        return picked
    def vaginalTrainingVariableGenerator(location):
        if location == "Fingers":
            her_arousal_gain = fingerPussyArousalGainGlobal()
            base_coin_gain, not_used = pc.fingerPussyArousalGain()
            did_orgasm, not_used = fingerPussyArousalIncrease()
            stamina_cost = 6
        elif location == "Clit":
            her_arousal_gain = massageClitArousalGainGlobal()
            base_coin_gain, not_used = pc.massageClitArousalGain()
            did_orgasm, not_used = massageClitArousalIncrease()
            stamina_cost = 6
        elif location == "Dildo outer" or location == "Training dummy outer":
            her_arousal_gain = vaginalOutercourseArousalGainGlobal()
            base_coin_gain, not_used = pc.vaginalOutercourseArousalGain()
            did_orgasm, not_used = vaginalOutercourseArousalIncrease()
            stamina_cost = 8
        elif location == "Training dummy inter" or location == "Dildo inter":
            her_arousal_gain = vaginalIntercourseArousalGainGlobal()
            base_coin_gain, not_used = pc.vaginalIntercourseArousalGain()
            did_orgasm, not_used = vaginalIntercourseArousalIncrease()
            stamina_cost = 15
        else:
            her_arousal_gain = 0
            base_coin_gain = 0
            did_orgasm = False
            stamina_cost = 0
        multiplied_exp_value = int(floor(her_arousal_gain * pc.training_multiplier))
        did_level_up = pc.increaseVaginalExp(multiplied_exp_value)
        did_persistent_level_up = increasePersistentVaginalExp(multiplied_exp_value)
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost
    # anal training functions
    def analTrainingLocationChoice():
        choices = ["Fingers"]
        if groceries.dildo == True and pc.stamina >= 8:
            choices.append("Dildo outer")
            if pc.stamina >= 15 and pc.anal_virgin == False:
                choices.append("Dildo inter")
        if groceries.training_dummy == True and pc.stamina >= 8:
            choices.append("Training dummy outer")
            if pc.stamina >= 15 and pc.anal_virgin == False:
                choices.append("Training dummy inter")
        picked = random.choice(choices)
        return picked
    def analTrainingVariableGenerator(location):
        if location == "Fingers":
            her_arousal_gain = fingerArseArousalGainGlobal()
            base_coin_gain, not_used = pc.fingerArseArousalGain()
            did_orgasm, not_used = fingerArseArousalIncrease()
            stamina_cost = 6
        elif location == "Dildo outer" or location == "Training dummy outer":
            her_arousal_gain = analOutercourseArousalGainGlobal()
            base_coin_gain, not_used = pc.analOutercourseArousalGain()
            did_orgasm, not_used = analOutercourseArousalIncrease()
            stamina_cost = 8
        elif location == "Dildo inter" or location == "Training dummy inter":
            her_arousal_gain = analIntercourseArousalGainGlobal()
            base_coin_gain, not_used = pc.analIntercourseArousalGain()
            did_orgasm, not_used = analIntercourseArousalIncrease()
            stamina_cost = 15
        else:
            her_arousal_gain = 0
            base_coin_gain = 0
            did_orgasm = False
            stamina_cost = 0
        multiplied_exp_value = int(floor(her_arousal_gain * pc.training_multiplier))
        did_level_up = pc.increaseAnalExp(multiplied_exp_value)
        did_persistent_level_up = increasePersistentAnalExp(multiplied_exp_value)
        coin_gain = upgrades.increaseUpgradeCoins(base_coin_gain)
        return her_arousal_gain, did_orgasm, did_level_up, did_persistent_level_up, coin_gain, stamina_cost