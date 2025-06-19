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

            self.chest_state = "dry"
            self.stomach_state = "dry"
            self.finger_state = "dry"
            self.thigh_state = "dry"
            self.face_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.ass_state = "dry"
        
        def resetMoistState(self):
            self.chest_state = "dry"
            self.stomach_state = "dry"
            self.finger_state = "dry"
            self.thigh_state = "dry"
            self.face_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.ass_state = "dry"
        
        def increaseArousal(amount):
            self.arousal += amount
            if self.arousal > 100: # check for orgasm
                self.arousal = 100
                return True
            else:
                return False
        
        def orgasm():
            self.arousal = 0
        
        def increaseWakefulness(amount):
            self.wakefulness += amount
        
        def reduceWakefulness(amount):
            self.wakefulness -= amount
        
        def increaseMaxWakefulness(amount):
            self.wakefulness_cap += amount
            # must also increase persistent value
            persistentIncreaseWakefulness(amount)
        
        def increaseFaceResistance(amount):
            self.face_resistance += amount
            persistentIncreaseFaceResistance(amount)
        
        def increaseHandResistance(amount):
            self.hand_resistance += amount
            persistentIncreaseHandResistance(amount)
        
        def increaseChestResistance(amount):
            self.chest_resistance += amount
            persistentIncreaseChestResistance(amount)
        
        def increaseThighResistance(amount):
            self.thigh_resistance += amount
            persistentIncreaseThighsResistance(amount)

        def increaseCockResistance(amount):
            self.cock_resistance += amount
            persistentIncreaseCockResistance(amount)

        def increaseTipResistance(amount):
            self.tip_resistance += amount
            persistentIncreaseTipResistance(amount)
        
        def increaseAssResistance(amount):
            self.ass_resistance += amount
            persistentIncreaseAssResistance(amount)
        
        def increaseEjaculationCount(amount):
            self.ejaculation_times += amount
            persistentIncreaseEjaculationCount(amount)
        
        def increaseEjaculationAmount(amount):
            self.ejaculation_amount += amount
            persistentEjaculationAmount(amount)
