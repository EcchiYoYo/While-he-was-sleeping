init python:
    import math
    import pygame
    import time
    import random
    import heapq
    from math import floor

#################################################################
#                                                               #
# Primary stats and functions for Victim                        #
#                                                               #
#################################################################

    class Victim:
        def __init__(self, face_resistance, hand_resistance, chest_resistance, thigh_resistance, tip_resistance, cock_resistance, ass_resistance, wakefulness_cap, ejaculation_times, ejaculation_amount,
            face_resistance_level, hand_resistance_level, chest_resistance_level, thigh_resistance_level, tip_resistance_level, cock_resistance_level, ass_resistance_level):
            self.name = "????"
            self.relationship = "Friend"

            self.wakefulness = 0 # default cap of 100, can be increased
            self.wakefulness_cap = wakefulness_cap
            self.arousal = 0 # orgasm at 150

            self.face_resistance_exp = face_resistance
            self.face_resistance_exp_for_level = hisCurrentFaceExpGet()
            self.face_resistance_level = face_resistance_level
            self.hand_resistance = hand_resistance
            self.hand_resistance_exp_for_level = hisCurrentHandExpGet()
            self.hand_resistance_level = hand_resistance_level
            self.chest_resistance = chest_resistance
            self.chest_resistance_exp_for_level = hisCurrentChestExpGet()
            self.chest_resistance_level = chest_resistance_level
            self.thigh_resistance = thigh_resistance
            self.thigh_resistance_exp_for_level = hisCurrentThighExpGet()
            self.thigh_resistance_level = thigh_resistance_level
            self.tip_resistance = tip_resistance
            self.tip_resistance_exp_for_level = hisCurrentTipExpGet()
            self.tip_resistance_level = tip_resistance_level
            self.cock_resistance = cock_resistance
            self.cock_resistance_exp_for_level = hisCurrentCockExpGet()
            self.cock_resistance_level = cock_resistance_level
            self.ass_resistance = ass_resistance
            self.ass_resistance_exp_for_level = hisCurrentAssExpGet()
            self.ass_resistance_level = ass_resistance_level

            self.ejaculation_amount = ejaculation_amount # how much cum
            self.ejaculation_times = ejaculation_times # how many times can he cum a night
            self.ejaculations_this_night = 0 # used to count orgasms this night, used for max victim times in single night

            self.chest_state = "dry"
            self.player_chest_cum_amount = 0
            self.victim_chest_cum_amount = 0
            self.stomach_state = "dry"
            self.player_stomach_cum_amount = 0
            self.victim_stomach_cum_amount = 0
            self.finger_state = "dry"
            self.player_finger_cum_amount = 0
            self.victim_finger_cum_amount = 0
            self.thigh_state = "dry"
            self.player_thigh_cum_amount = 0
            self.victim_thigh_cum_amount = 0
            self.face_state = "dry"
            self.player_face_cum_amount = 0
            self.victim_face_cum_amount = 0
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.ass_state = "dry"
        
        def resetMoistState(self):
            self.chest_state = "dry"
            self.player_chest_cum_amount = 0
            self.victim_chest_cum_amount = 0
            self.stomach_state = "dry"
            self.player_stomach_cum_amount = 0
            self.victim_stomach_cum_amount = 0
            self.finger_state = "dry"
            self.player_finger_cum_amount = 0
            self.victim_finger_cum_amount = 0
            self.thigh_state = "dry"
            self.player_thigh_cum_amount = 0
            self.victim_thigh_cum_amount = 0
            self.face_state = "dry"
            self.player_face_cum_amount = 0
            self.victim_face_cum_amount = 0
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.ass_state = "dry"
        
        def increaseArousal(self, amount):
            self.arousal += amount
            if self.arousal >= 150: # check for orgasm
                return True
            else:
                return False
        
        def orgasm(self):
            self.arousal = 0
            self.ejaculations_this_night += 1
            ejaculation_amount = self.ejaculation_amount / self.ejaculation_times
            persistent.total_ejaculation_all_cycles += ejaculation_amount
            if self.ejaculations_this_night >= self.ejaculation_times:
                return True, ejaculation_amount # reached ejaculation limit + ejaculation amount (used to keep track of sperm count t on/in body parts)
            else:
                return False, ejaculation_amount # not reached ejaculation limit + ejaculation amount (used to keep track of sperm count t on/in body parts)
        
        #####################################
        #                                   #
        # resistance related functions      #
        #####################################
        # Face
        def increaseFaceExp(self, amount):
            level_up = 0
            if self.face_resistance_level < 999:
                self.face_resistance_exp += amount
                while self.face_resistance_exp >= self.face_resistance_exp_for_level:
                    self.increaseFaceLevel(1)
                    level_up += 1
                    if self.face_resistance_level >= 999:
                        break
            return level_up
        
        def increaseFaceLevel(self, amount):
            self.face_resistance_level += amount # increase resistance level by 1
            self.face_resistance_exp_for_level = hisCurrentFaceExpGet() # read resistance csv file and apply new experience amount required for next level (will be 0 if level is capped)
        # Hand
        def increaseHandExp(self, amount):
            level_up = 0
            if self.hand_resistance_level < 999:
                self.hand_resistance_exp += amount
                while self.hand_resistance_exp >= self.hand_resistance_exp_for_level:
                    self.increaseHandLevel(1)
                    level_up += 1
                    if self.face_resistance_level >= 999:
                        break
        
        def increaseHandLevel(self, amount):
            self.hand_resistance_level += amount
            self.resistance_exp_for_level = hisCurrentHandExpGet()
        # Chest
        def increaseChestExp(self, amount):
            level_up = 0
            if self.chest_resistance_level < 999:
                self.chest_resistance_exp += amount
                while self.chest_resistance_exp >= self.chest_resistance_exp_for_level:
                    self.increaseChestLevel(1)
                    level_up += 1
                    if self.chest_resistance_level >= 999:
                        break
            return level_up
        
        def increaseChestLevel(self, amount):
            self.chest_resistance_level += amount
            self.chest_resistance_exp_for_level = hisCurrentChestExpGet()
        # Thigh
        def increaseThighExp(self, amount):
            level_up = 0
            if self.thigh_resistance_level < 999:
                self.thigh_resistance_exp += amount
                while self.thigh_resistance_exp >= self.thigh_resistance_exp_for_level:
                    self.increaseThighLevel(1)
                    level_up += 1
                    if self.thigh_resistance_level >= 999:
                        break
            return level_up
        
        def increaseThighLevel(self, amount):
            self.thigh_resistance_level += amount
            self.thigh_resistance_exp_for_level = hisCurrentThighExpGet()
        # Tip
        def increaseTipExp(self, amount):
            level_up = 0
            if self.tip_resistance_level < 999:
                self.tip_resistance_exp += amount
                while self.tip_resistance_exp >= self.tip_resistance_exp_for_level:
                    self.increaseTipLevel(1)
                    level_up += 1
                    if self.tip_resistance_level >= 999:
                        break
            return level_up
        
        def increaseTipLevel(self, amount):
            self.tip_resistance_level += amount
            self.tip_resistance_exp_for_level = hisCurrentTipExpGet()
        # cock
        def increaseCockExp(self, amount):
            level_up = 0
            if self.cock_resistance_level < 999:
                self.cock_resistance_exp += amount
                while self.cock_resistance_exp >= self.cock_resistance_exp_for_level:
                    self.increaseCockLevel(1)
                    level_up += 1
                    if self.cock_resistance_level >= 999:
                        break
            return level_up
        
        def increaseCockLevel(self, amount):
            self.cock_resistance_level += amount
            self.cock_resistance_exp_for_level = hisCurrentAssExpGet()
        # ass
        def increaseAssLevel(self, amount):
            level_up = 0
            if self.ass_resistance_level < 999:
                self.ass_resistance_exp += amount
                while self.ass_resistance_exp >= self.ass_resistance_exp_for_level:
                    self.increaseAssLevel(1)
                    level_up += 1
                    if self.ass_resistance_level >= 999:
                        break
            return level_up
        
        def increaseAssLevel(self, amount):
            self.ass_resistance_level += amount

        
        #####################################
        #                                   #
        # mouth related functions           #
        #####################################
        # kiss him
        # calculate his arousal values both default and multiplied for coins and actual arousal gain
        def kissArousalGain(amount):
            default_arousal = 3
            multiplier_from_her_mouth_skill = amount
            multiplier_from_upgrades = (upgrades.mouth_arousal_multiplier / 1000)
            his_actual_arousal_gain = floor(default_arousal + (default_arousal * (multiplier_from_her_mouth_skill + multiplier_from_upgrades)))
            return his_actual_arousal_gain, default_arousal
        # calculate his arousal values for deep kiss
        def deepKissArousalGain(amount):
            default_arousal = 5
            multiplier_from_her_mouth_skill = amount
            multiplier_from_upgrades = (upgrades.mouth_arousal_multiplier / 1000)
            his_actual_arousal_gain = floor(default_arousal + (default_arousal * (multiplier+from_her_mouth_skill + multiplier_from_upgrades)))
            return his_actual_arousal_gain, default_arousal
        
        #####################################
        #                                   #
        # chest related functions           #
        #####################################
        
        def rubChestArousalGain(self):
            default_increase = 5
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier

        def rubChestArousalGain(self):
            default_increase = 7
            return default_increase
        
        def rubChestWithFootArousalGain(amount):
            default_arousal = 3
            multiplier_from_her_foot_skill = amount
            multiplier_from_upgrades = (upgrades.foot_arousal_multiplier / 1000)
            his_actual_actual_arousal_gain = floor(default_arousal + (default_arousal * (multiplier_from_her_foot_skill + multiplier_from_upgrades)))
            return his_actual_arousal_gain, default_arousal
        #####################################
        #                                   #
        # cock and balls related functions  #
        #####################################
        def rubHisBallsHerFootArousalGain(amount):
            default_arousal = 3
            multiplier_from_her_foot_skill = amount
            multiplier_from_upgrades = (upgrades.foot_arousal_multiplier / 1000)
            his_actual_arousal_gain = floor(default_arousal + (default_arousal * (multiplier_from_her_foot_skill + multiplier_from_upgrades)))
            return his_actual_arousal_gain, default_arousal
        
        def footjobHisArousalGain(amount):
            default_arousal = 5
            multiplier_from_her_foot_skill = amount
            multiplier_from_upgrades = (upgrades.foot_arousal_multiplier / 1000)
            his_actual_arousal_gain = floor(default_arousal + (default_arousal * (multiplier_from_her_foot_skill + multiplier_from_upgrades)))
            return his_actual_arousal_gain, default_arousal

        def increaseWakefulness(self, amount):
            self.wakefulness += amount
            if wakefulness >= self.wakefulness_cap:
                if self.wakefulness > self.wakefulness_cap:
                    self.wakefulness = self.wakefulness_cap
                return True
            else:
                return False
        
        def reduceWakefulness(self, amount):
            self.wakefulness -= amount
            if self.wakefulness < 0:
                self.wakefulness = 0 
        
        def increaseMaxWakefulness(self, amount):
            # increase by 10 percent of wakefulness gained capped at something
            self.wakefulness_cap += amount
            # must also increase persistent value
            persistentIncreaseWakefulness(amount)
        
        def increaseFaceResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.face_resistance += amount
            persistentIncreaseFaceResistance(amount)
        
        def increaseHandResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.hand_resistance += amount
            persistentIncreaseHandResistance(amount)
        
        def increaseChestResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.chest_resistance += amount
            persistentIncreaseChestResistance(amount)
        
        def increaseThighResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.thigh_resistance += amount
            persistentIncreaseThighsResistance(amount)

        def increaseCockResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.cock_resistance += amount
            persistentIncreaseCockResistance(amount)

        def increaseTipResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.tip_resistance += amount
            persistentIncreaseTipResistance(amount)
        
        def increaseAssResistance(self, amount):
            # increase by 10 percent of arousal gained capped at 666
            self.ass_resistance += amount
            persistentIncreaseAssResistance(amount)
        
        # no longer used, instead count is + 1 for every thousand in total amount
        # def increaseEjaculationCount(amount):
        #     # outside of upgrades this is increased every 100 ejaculations through all cycles
        #     self.ejaculation_times += amount
        #     persistentIncreaseEjaculationCount(amount)
        
        def increaseEjaculationAmount(self, amount):
            # increase + 10 for every 1000 ejaculated
            self.ejaculation_amount += amount
            persistentEjaculationAmount(amount)
