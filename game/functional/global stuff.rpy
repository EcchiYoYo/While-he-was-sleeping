init python:
    import csv
    import math
    class GameTime:
        def __init__(self):
            self.block = 1
            self.days_passed = 0
            self.game_end = False
        
        def advanceTime(self, amount):
            self.block += 1
            if self.block > 4:
                self.block = 1
                advanceDay(1)
        
        def advanceDay(self, amount):
            self.days_passed += 1
            if self.days_passed > 7:
                self.game_end = True
            else:
                self.game_end = False
            return self.game_end

    def noneFunction():
        1 + 1
        # I do nothing, used for blank python blocks yet to be populated

    def globalAdvanceTime(amount):
        if game_time.block == 4:
            # this will be higher than 0 if player did not hide the evidence the previous night
            # only checked during advance time when moving to next day
            suspicion_gained = suspicionGainFromPreviousNight()
            man.suspicion = suspicion_gained
            # used to update victim cum number of times once threshold reached
            if ((persistent.total_ejaculation_all_cycles / 1000) + 1) != man.self.ejaculation_times:
                man.self.ejaculation_times = ((persistent.total_ejaculation_all_cycles / 1000) + 1)
        # advance time by amount specified in function call block
        game_time.advanceTime(amount)
        pc.resetMoistState()
        man.resetMoistState()
        

        # Check if the cycle has reached its end
        cycle_ended = game_time.advanceDay(1)
        if cycle_ended == True:
            return True
        else:
            return False
    
    # used to calculate money earned from working (will be used to buy buffs in upgrade shop)
    def globalPoundsEarnedWorking():
        base_amount = 25
        amount_with_multipliers = base_amount + (base_amount * upgrades.pounds_multiplier)
        actual = floor(amount_with_multipliers)
        return actual
    
    # used to increase current cycle count
    def increaseCycleCount():
        pc.cycle_number += 1
        persistent.cycle_number += 1
    
    # this adds a wakefulness gain multiplier if the player did not properly clean the victims body at the end of the night phase
    def suspicionGainFromPreviousNight():
        count = 0
        if man.chest_state == "cum" or man.chest_state == "girl cum":
            count += 1
        if man.stomach_state == "cum" or man.stomach_state == "girl cum":
            count += 1
        if man.finger_state == "cum" or man.finger_state == "girl cum":
            count += 1
        if man.thigh_state == "cum" or man.thigh_state == "girl cum":
            count += 1
        if man.face_state == "cum" or man.face_state == "girl cum":
            count += 1
        if man.ass_state == "cum":
            count += 1
        return count

    #
    # resistance increases
    #
    def persistentIncreaseWakefulness(amount):
        persistent.wakefulness_cap += amount
    
    def persistentIncreaseFaceResistance(amount):
        persistent.face_resistance += amount
    
    def persistentIncreaseHandResistance(amount):
        persistent.hand_resistance += amount
    
    def persistentIncreaseChestResistance(amount):
        persistent.chest_resistance += amount
    
    def persistentIncreaseThighsResistance(amount):
        persistent.thigh_resistance += amount
    
    def persistentIncreaseCockResistance(amount):
        persistent.cock_resistance += amount
    
    def persistentIncreaseTipResistance(amount):
        persistent.tip_resistance += amount

    def persistentIncreaseAssResistance(amount):
        persistent.ass_resistance += amount
    #
    # body part experience gain for persistent`s
    #
    # check the current total exp required for current persistent hand level
    def persistentHandExpForLevel():
        exp_value_to_be_set = currentHandExpGet()
        return exp_value_to_be_set
    # increase current persistent hand exp and increase level if required
    def increasePersistentHandExp(amount):
        levels_gained = 0
        persistent.current_hand_exp += amount
        while persistent.current_hand_exp >= persistentHandExpForLevel():
            persistent.hand_level += 1
            levels_gained += 1
        return levels_gained
    # check the current mouth exp required for current persistent level
    def persistentMouthExpForLevel():
        exp_value_to_set = currentMouthExpGet()
        return exp_value_to_set
    # increase current persistent mouth exp and increase level if required
    def increasePersistentMouthExp(amount):
        levels_gained = 0
        persistent.current_mouth_exp += amount
        while persistent.current_mouth_exp >= persistentMouthExpForLevel():
            persistent.mouth_level += 1
            levels_gained += 1
        return levels_gained
    # check the current foot exp required for current persistent level
    def persistentFootExpForLevel():
        exp_value_to_set = currentMouthExpGet()
        return exp_value_to_set
    # increase current persistent foot exp and increase level if required
    def increasePersistentFootExp(amount):
        levels_gained = 0
        persistent.current_foot_exp += amount
        while persistent.current_foot_exp >= persistentFootExpForLevel():
            persistent.foot_level += 1
            levels_gained += 1
        return levels_gained
    # check the current vaginal exp required for current persistent level
    def persistentVaginalExpForLevel():
        exp_value_to_set = currentVaginalExpGet()
        return exp_value_to_set
    # increase current persistent vaginal exp and increase level if required
    def increasePersistentVaginalExp(amount):
        levels_gained = 0
        persistent.current_vaginal_exp += amount
        while persistent.current_vaginal_exp >= persistentVaginalExpForLevel():
            persistent.vaginal_level += 1
            levels_gained += 1
        return levels_gained
    # check the current anal exp required for current persistent level
    def persistentAnalExpForLevel():
        exp_value_to_set = currentAnalExpGet()
        return exp_value_to_set
    # increase current persistent anal exp and increase level if required
    def increasePersistentAnalExp(amount):
        levels_gained = 0
        persistent.current_anal_exp += amount
        while persistent.current_anal_exp >= persistentAnalExpForLevel():
            persistent.anal_level += 1
            levels_gained += 1
        return levels_gained
    ##################################################
    #                                                #
    # for player types with penis                    #
    ##################################################
    # check the current just the tip exp required for current persistent level
    def persistentJustTheTipExpForLevel():
        exp_value_to_set = currentJustTheTipExpGet()
        return exp_value_to_set
    # increase current persistent just the tip exp and increase level if required
    def increasePersistentJustTheTipExp(amount):
        levels_gained = 0
        persistent.current_just_the_tip_exp += amount
        while persistent.current_just_the_tip_exp >= persistentJustTheTipExpForLevel():
            persistent.just_the_tip_level += 1
            levels_gained += 1
        return levels_gained
    # check the current cock epx required for current persistent level
    def persistentCockExpForLevel():
        exp_value_to_set = currentCockExpGet()
        return exp_value_to_set
    # increase current persistent cock exp and increase level if required
    def increasePersistentCockExp(amount):
        levels_gained = 0
        persistent.current_cock_exp += amount
        while persistent.current_cock_exp >= persistentCockExpForLevel():
            persistent.cock_level += 1
            levels_gained += 1
        return levels_gained
    #
    # victim ejaculation amount
    #    
    def persistentIncreaseEjaculationAmount(amount):
        persistent.ejaculation_amount += amount
    #
    # upgrade persistent increases
    #
    def persistentIncreaseUpgradeCoins(amount):
        persistent.coins_earned += amount

    ##################################################
    #                                                #
    # Functions for increasing persistent exp and    #
    # levels for skill                               #
    ##################################################
    def currentHandExpGet():
        exp_needed = 0
        if persistent.hand_level <= 999:
            amount = persistent.hand_level + 1
            with open(renpy.loader.transfn("CSVs/hand table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/hand table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.hand_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed
        
    
    def currentMouthExpGet():
        exp_needed = 0
        if persistent.mouth_level <= 999:
            amount = persistent.mouth_level + 1
            with open(renpy.loader.transfn("CSVs/mouth table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/mouth table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.mouth_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed

    def currentFootExpGet():
        exp_needed = 0
        if persistent.foot_level <= 999:
            amount = persistent.foot_level + 1
            with open(renpy.loader.transfn("CSVs/foot table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/foot table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.foot_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed
    
    def currentVaginalExpGet():
        exp_needed = 0
        if persistent.vaginal_level <= 999:
            amount = persistent.vaginal_level + 1
            with open(renpy.loader.transfn("CSVs/vaginal table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/vaginal table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.vaginal_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed
    
    def currentAnalExpGet():
        exp_needed = 0
        total_exp_needed = 0
        if persistent.anal_level < 999:
            amount = persistent.anal_level + 1
            with open(renpy.loader.transfn("CSVs/anal table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/anal table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.anal_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed
    ##########################################################
    # the following are only needed for futa/gay/trans packs # (need to decide if male presenting female or female presenting male)
    ##########################################################
    def currentJustTheTipExpGet():
        exp_needed = 0
        if persistent.just_the_tip_level <= 999:
            amount = persistent.just_the_tip_level + 1
            with open(renpy.loader.transfn("CSVs/just the tip table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(reny.loader.transfn("CSVs/just the tip.csv"), "r", newline="") as csvfile:
                reader = csv.DicReader(csvfile)
                for idex, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp_needed"])
            additional = persistent.just_the_tip_level - 999
            total_exp_needed = exp_needed + (additional + persistent.additional_exp)
            return total_exp_needed
    
    def currentCockExpGet():
        exp_needed = 0
        total_exp_needed = 0
        if persistent.cock_level < 999:
            amount = persistent.cock_level + 1
            with open(renpy.loader.transfn("CSVs/cock table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            amount = 999
            with open(renpy.loader.transfn("CSVs/cock table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
            additional = persistent.cock_level - 999
            total_exp_needed = exp_needed + (additional * persistent.additional_exp)
            return total_exp_needed

    ##################################################
    #                                                #
    # Functions for night time interactions          #
    #                                                #
    ##################################################
    # actions using players body                     #
    ##################################################
    #
    # unique
    #
    # Stroke hair (used to reduce wakefulness medium) increases face resistance, raises player arousal small amount

    #
    # Player mouth
    #
    # Kiss, raises player arousal small, raises victim arousal tiny, raises wakefulness small, reduce stamina tiny

    # player sucks her fingers, raises player arousal tiny, reduces wakefulness small, moistness players hands, neutral stamina

    # player sucks girl cum/victim cum from fingers, raises player arousal tiny, reduces wakefulness small, removes girl cum from player hands, adds saliva to player hands, neutral stamina

    # player cleans cum from victim, raises player arousal small, neutral wakefulness, removes cum from body part adds saliva to body part, raises suspicion if all cum not cleaned at end of night, neutral stamina

    # 
    # Player chest
    #
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
    #
    # player pussy
    #
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
        pc.reduceStamina(7)
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
        pc.reduceStamina(10)
        return did_orgasm, arousal_gain
    #
    # ass
    #
    # rub players ass, increase player arousal small, reduce stamina small, reduce wakefulness small
    # used to calculate arousal gained from action
    

    # finger ass (requires moist ass/fingers), increase player arousal medium, reduce stamina medium, reduce wakefulness small

    #
    # cock (her(futa, trans, gay))
    #
    # rub players cock, increase player arousal medium, reduce stamina medium, reduce wakefulness small

    # rub players balls, increase player arousal tiny, reduce stamina tiny, reduce wakefulness small

    # masturbate players cock, increase player arousal very large, reduce stamina large, reduce wakefulness small

    # push player cock into victim mouth, increase player arousal large, reduce stamina medium, increase wakefulness large

    #
    # tip of cock (her(futa, trans, gay))
    #
    # rub tip of players cock, increase player arousal medium, reduce stamina medium, reduce wakefulness small

    # put tip of cock in victims mouth, increase player arousal large, reduce stamina medium, reduce wakefulness small

    #
    # players feet
    #
    # caress chest with foot, increase player arousal very tiny, increase victim arousal small, increase wakefulness small, reduce stamina small

    # get victim to suck toe, increase player arousal small, reduce stamina small, increase wakefulness small

    # rub victim balls with foot, increase player arousal very tiny, increase victim arousal tiny, reduce stamina tiny increase wakefulness tiny

    # foot job, increase player arousal tiny, increase victim arousal medium, reduce stamina medium, increase wakefulness medium
    ##################################################
    # actions using victims body                     #
    ##################################################
    #
    # mouth
    #
    # face ride victims mouth, increase player arousal medium, increase victim arousal small, reduce stamina medium, increase wakefulness large

    # make victim suck player/victim fingers, reduce stamina tiny, increase wakefulness tiny, remove girl cum.victim cum from fingers sucked, add finger moist state to player/victim hands

    # make victim suck cum from player/victim fingers, increase player arousal small, if girl cim increase victim arousal tiny, reduce stamina tiny, increase wakefulness small, remove girl cum.victim cum from fingers sucked, add finger moist state to player/victim hands

    #
    # Chest
    #
    def rubChestArousalGainGlobal():
        default_arousal_increase = man.rubChestArousalGain()
        default_multiplier = pc.hand_level / 1000
        upgrades_arousal_multiplier = upgrades.hand_arousal_multiplier
        multiplier_total = default_multiplier + upgrades_arousal_multiplier
        actual_arousal_gain = floor(default_arousal_increase + ((multiplier_total / 1000) * default_arousal_increase))
        return actual_arousal_gain

    def rubChestArousalIncrease():
        arousal_gain = rubChestArousalGainGlobal()
        #
        # need to add her arousal gain from this action
        #
        did_orgasm = man.increaseArousal(arousal_gain)
        pc.reduceStamina(5)
        return did_orgasm, arousal_gain
