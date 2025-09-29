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
        def __init__(self, face_resistance, hand_resistance, chest_resistance, thigh_resistance, tip_resistance, cock_resistance, ass_resistance, wakefulness_cap, ejaculation_times, ejaculation_amount):
            self.name = "????"
            self.relationship = "Friend"

            self.wakefulness = 0
            self.wakefulness_cap = wakefulness_cap
            self.arousal = 0

            self.face_resistance = face_resistance
            self.hand_resistance = hand_resistance
            self.chest_resistance = chest_resistance
            self.thigh_resistance = thigh_resistance
            self.tip_resistance = tip_resistance
            self.cock_resistance = cock_resistance
            self.ass_resistance = ass_resistance

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
            if self.arousal > 150: # check for orgasm
                self.arousal = 150
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
        
        def rubChestArousalGain(self):
            default_increase = 5
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier

        def rubChestArousalGain(self):
            default_increase = 7
            return default_increase

        def increaseWakefulness(amount):
            self.wakefulness += amount
        
        def reduceWakefulness(amount):
            self.wakefulness -= amount
        
        def increaseMaxWakefulness(amount):
            # increase by 10 percent of wakefulness gained capped at something
            self.wakefulness_cap += amount
            # must also increase persistent value
            persistentIncreaseWakefulness(amount)
        
        def increaseFaceResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.face_resistance += amount
            persistentIncreaseFaceResistance(amount)
        
        def increaseHandResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.hand_resistance += amount
            persistentIncreaseHandResistance(amount)
        
        def increaseChestResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.chest_resistance += amount
            persistentIncreaseChestResistance(amount)
        
        def increaseThighResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.thigh_resistance += amount
            persistentIncreaseThighsResistance(amount)

        def increaseCockResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.cock_resistance += amount
            persistentIncreaseCockResistance(amount)

        def increaseTipResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.tip_resistance += amount
            persistentIncreaseTipResistance(amount)
        
        def increaseAssResistance(amount):
            # increase by 10 percent of arousal gained capped at 666
            self.ass_resistance += amount
            persistentIncreaseAssResistance(amount)
        
        # no longer used, instead count is + 1 for every thousand in total amount
        def increaseEjaculationCount(amount):
            # outside of upgrades this is increased every 100 ejaculations through all cycles
            self.ejaculation_times += amount
            persistentIncreaseEjaculationCount(amount)
        
        def increaseEjaculationAmount(amount):
            # increase + 10 for every 1000 ejaculated
            self.ejaculation_amount += amount
            persistentEjaculationAmount(amount)
