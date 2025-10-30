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
    #################################################################################
    #                                                                               #
    # body part experience gain for persistent`s for player                         #
    #                                                                               #
    #################################################################################
    # check the current mouth exp required for current persistent level
    def persistentMouthExpForLevel():
        exp_value_to_set = currentMouthExpGet()
        return exp_value_to_set
    # increase current persistent mouth exp and increase level if required
    def increasePersistentMouthExp(amount):
        levels_gained = 0
        persistent.current_mouth_exp += amount
        mouth_exp_required = persistentMouthExpForLevel()
        while persistent.current_mouth_exp >= mouth_exp_required and mouth_exp_required > 0:
            increasePersistentMouthLevel(1)
            levels_gained += 1
            mouth_exp_required = persistentMouthExpForLevel()
        return levels_gained
    # increase persistent mouth level
    def increasePersistentMouthLevel(amount):
        persistent.mouth_level += amount
        persistent.mouth_exp_for_level = persistentMouthExpForLevel()
    # check the current total exp required for current persistent hand level
    def persistentHandExpForLevel():
        exp_value_to_be_set = currentHandExpGet()
        return exp_value_to_be_set
    # increase current persistent hand exp and increase level if required
    def increasePersistentHandExp(amount):
        levels_gained = 0
        persistent.current_hand_exp += amount
        hand_exp_required = persistentHandExpForLevel()
        while persistent.current_hand_exp >= hand_exp_required and hand_exp_required > 0:
            increasePersistentHandLevel(1)
            levels_gained += 1
            hand_exp_required = persistentHandExpForLevel()
        return levels_gained
    # increase persistent hand level
    def increasePersistentHandLevel(amount):
        persistent.hand_level += amount
        persistent.hand_exp_for_level = persistentHandExpForLevel()
    
    # check the current foot exp required for current persistent level
    def persistentFootExpForLevel():
        exp_value_to_set = currentMouthExpGet()
        return exp_value_to_set
    # increase current persistent foot exp and increase level if required
    def increasePersistentFootExp(amount):
        levels_gained = 0
        persistent.current_foot_exp += amount
        foot_exp_required = persistentFootExpForLevel()
        while persistent.current_foot_exp >= foot_exp_required and foot_exp_required > 0:
            increasePersistentFootLevel(1)
            levels_gained += 1
            foot_exp_required = persistentFootExpForLevel()
        return levels_gained
    def increasePersistentFootLevel(amount):
        persistent.foot_level += amount
        persistent.foot_exp_for_level = persistentFootExpForLevel()
    # check the current vaginal exp required for current persistent level
    def persistentVaginalExpForLevel():
        exp_value_to_set = currentVaginalExpGet()
        return exp_value_to_set
    # increase current persistent vaginal exp and increase level if required
    def increasePersistentVaginalExp(amount):
        levels_gained = 0
        persistent.current_vaginal_exp += amount
        vaginal_exp_required = persistentVaginalExpForLevel()
        while persistent.current_vaginal_exp >= vaginal_exp_required and vaginal_exp_required > 0:
            increasePersistentVaginalLevel(1)
            levels_gained += 1
            vaginal_exp_required = persistentVaginalExpForLevel()
        return levels_gained
    def increasePersistentVaginalLevel(amount):
        persistent.vaginal_level += amount
        persistent.vaginal_exp_for_level = persistentVaginalExpForLevel()
    # check the current anal exp required for current persistent level
    def persistentAnalExpForLevel():
        exp_value_to_set = currentAnalExpGet()
        return exp_value_to_set
    # increase current persistent anal exp and increase level if required
    def increasePersistentAnalExp(amount):
        levels_gained = 0
        persistent.current_anal_exp += amount
        anal_exp_required = persistentAnalExpForLevel()
        while persistent.current_anal_exp >= anal_exp_required and anal_exp_required > 0:
            increasePersistentAnalLevel(1)
            levels_gained += 1
            anal_exp_required = persistentAnalExpForLevel()
        return levels_gained
    def increasePersistentAnalLevel(amount):
        persistent.anal_level += amount
        persistent.anal_exp_for_level = persistentAnalExpForLevel()
    
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
        tip_exp_required = persistentJustTheTipExpForLevel()
        while persistent.current_just_the_tip_exp >= tip_exp_required and tip_exp_required > 0:
            increasePersistentJustTheTipPlayer(1)
            levels_gained += 1
            tip_exp_required = persistentJustTheTipExpForLevel()
        return levels_gained
    def increasePersistentJustTheTipPlayer(amount):
        persistent.just_the_tip_level += 1
        persistent.just_the_tip_exp_for_level = persistentJustTheTipExpForLevel()
    # check the current cock epx required for current persistent level
    def persistentCockExpForLevel():
        exp_value_to_set = currentCockExpGet()
        return exp_value_to_set
    # increase current persistent cock exp and increase level if required
    def increasePersistentCockExp(amount):
        levels_gained = 0
        persistent.current_cock_exp += amount
        cock_exp_required = persistentCockExpForLevel()
        while persistent.current_cock_exp >= cock_exp_required and cock_exp_required > 0:
            persistent.cock_level += 1
            levels_gained += 1
            cock_exp_required = persistentCockExpForLevel()
        return levels_gained
    def increasePersistentCockLevel(amount):
        persistent.cock_level += amount
        persistent.cock_exp_for_level = persistentCockExpForLevel()
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

    #################################################################################
    #                                                                               #
    # persistent body part experience gain`s for for victim                         #
    #                                                                               #
    #################################################################################
    # face resistance level related functions
    # check the current face resistance exp required for level
    def persistentHisFaceExpForLevel():
        exp_value_to_set = hisCurrentFaceExpGet()
        return exp_value_to_set
    # increase current face resistance exp and increase level if required
    def increasePersistentHisFaceExp(amount):
        levels_gained = 0
        persistent.face_resistance_exp += amount
        face_exp_required = persistentHisFaceExpForLevel()
        while persistent.face_resistance_exp >= face_exp_required and face_exp_required > 0:
            increasePersistentFaceResistanceLevel(1)
            levels_gained += 1
            face_exp_required = persistentHisFaceExpForLevel()
        return levels_gained
    def increasePersistentFaceResistanceLevel(amount):
        persistent.face_resistance_level += amount
        persistent.face_resistance_exp_for_level = persistentHisFaceExpForLevel()
    # hand related
    def persistentHisHandExpForLevel():
        exp_value_to_set = hisCurrentHandExpGet()
        return exp_value_to_set
    
    def increasePersistentHisHandExp(amount):
        levels_gained = 0
        persistent.hand_resistance_exp += amount
        hand_exp_required = persistentHisHandExpForLevel()
        while persistent.hand_resistance_exp >= hand_exp_required and hand_exp_required > 0:
            increasePersistentHandResistanceLevel(1)
            levels_gained += 1
            hand_exp_required = persistentHisHandExpForLevel()
        return levels_gained
    def increasePersistentHandResistanceLevel(amount):
        persistent.hand_resistance_level += amount
        persistent.hand_resistance_exp_for_level = persistentHisHandExpForLevel()
    # chest related
    def persistentHisChestExpForLevel():
        exp_value_to_set = hisCurrentChestExpGet()
        return exp_value_to_set
    def increasePersistentHisChestExp(amount):
        levels_gained = 0
        persistent.chest_resistance_exp += amount
        chest_exp_required = persistentHisChestExpForLevel()
        while persistent.chest_resistance_exp >= chest_exp_required and chest_exp_required > 0:
            increasePersistentChestResistanceLevel(1)
            levels_gained += 1
            chest_exp_required = persistentHisChestExpForLevel()
        return levels_gained
    
    def increasePersistentChestResistanceLevel(amount):
        persistent.chest_resistance_level += amount
        persistent.chest_resistance_exp_for_level = persistentHisChestExpForLevel()
    # thigh related
    def persistentHisThighExpForLevel():
        exp_value_to_set = hisCurrentThighExpGet()
        return exp_value_to_set
    def increasePersistentHisThighExp(amount):
        levels_gained = 0
        persistent.thigh_resistance_exp += amount
        thigh_exp_required = persistentHisThighExpForLevel()
        while persistent.thigh_resistance_exp >= thigh_exp_required and thigh_exp_required > 0:
            increasePersistentThighResistanceLevel(1)
            levels_gained += 1
            thigh_exp_required = persistentHisThighExpForLevel()
        return levels_gained
    def increasePersistentThighResistanceLevel(amount):
        persistent.thigh_resistance_level += amount
        persistent.thigh_resistance_exp_for_level = persistentHisThighExpForLevel()
    # tip related
    def persistentHisTipExpForLevel():
        exp_value_to_set = hisCurrentTipExpGet()
        return exp_value_to_set
    def increasePersistentHisTipExp(amount):
        levels_gained = 0
        persistent.tip_resistance_exp += amount
        tip_exp_required = persistentHisTipExpForLevel()
        while persistent.tip_resistance_exp >= tip_exp_required and tip_exp_required > 0:
            increasePersistentTipResistanceLevel(1)
            levels_gained += 1
            tip_exp_required = persistentHisTipExpForLevel()
        return levels_gained
    def increasePersistentTipResistanceLevel(amount):
        persistent.tip_resistance_level += amount
        persistent.tip_resistance_exp_for_level = persistentHisTipExpForLevel()
    # cock related
    def persistentHisCockExpForLevel():
        exp_value_to_set = hisCurrentChestExpGet()
        return exp_value_to_set
    def increasePersistentHisCockExp(amount):
        levels_gained = 0
        persistent.cock_resistance_exp += amount
        cock_exp_required = persistentHisCockExpForLevel()
        while persistent.cock_resistance_exp >= cock_exp_required and cock_exp_required > 0:
            increasePersistentCockResistanceLevel(1)
            levels_gained += 1
            cock_exp_required = persistentHisCockExpForLevel()
        return levels_gained
    def increasePersistentCockResistanceLevel(amount):
        persistent.cock_resistance_level += amount
        persistent.cock_resistance_exp_for_level = persistentHisCockExpForLevel()
    # ass related
    def persistentHisAssExpForLevel():
        exp_value_to_set = hisCurrentAssExpGet()
        return exp_value_to_set
    def increasePersistentHisAssExp(amount):
        levels_gained = 0
        persistent.ass_resistance_exp += amount
        ass_exp_required = persistentHisAssExpForLevel()
        while persistent.ass_resistance_exp >= ass_exp_required and ass_exp_required > 0:
            increasePersistentAssResistanceLevel(1)
            levels_gained += 1
            ass_exp_required
        return levels_gained
    def increasePersistentAssResistanceLevel(amount):
        persistent.ass_resistance_level += 1
        persistent.ass_resistance_exp_for_level = persistentHisAssExpForLevel()
    
    ##################################################
    # actions using players body                     #
    ##################################################
    #
    # unique
    #
    # Stroke hair (used to reduce wakefulness medium) increases face resistance, raises player arousal small amount


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
