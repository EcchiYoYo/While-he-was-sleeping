init python:    
    import math
    import pygame
    import time
    import random
    import heapq
    from math import floor

#################################################################
#                                                               #
# Primary stats and functions for Player                        #
#                                                               #
#################################################################
    class Player:
        def __init__(self, max_stamina, hs, hl, ms, ml, fs, fl, vs, vl, anal_skill, al):
            self.name = "????"
            self.male_name = "????"
            self.stamina = max_stamina
            self.max_stamina = max_stamina
            self.arousal = 0
            self.hand_skill = hs
            self.hand_level = hl
            self.mouth_skill = ms
            self.mouth_level = ml
            self.foot_skill = fs
            self.foot_level = fl
            self.vagina_skill = vs
            self.vagina_level = vl
            self.anal_skill = anal_skill
            self.anal_level = al
            self.finger_state = "dry"
            self.vaginal_state = "dry"
            self.anal_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.player_type = "default"
            self.money = 0

        def resetMoistState(self):
            self.finger_state = "dry"
            self.vaginal_state = "dry"
            self.anal_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
        
        def increaseArousal(self, amount):
            self.arousal += amount
            if self.arousal > 100: # check for orgasm
                self.arousal = 100
                return True
            else:
                return False
        
        def orgasm(self):
            self.arousal = 0
        ###
        # skill level requirements
        # 100 (100 total) level 1
        # 150 (250 total) level 2
        # 225 (475 total) level 3
        # 375 (850 total) level 4
        # 500 (1350 total) level 5
        # 650 (2000 total) level 6
        # 800 (2800 total) level 7
        # 1000 (3800 total) level 8
        # 2000 (5800 total) level 9
        # 4200 (10000 total) level 10 cap

        #
        # add in functions for increasing skill exp and levels
        #
    
        def increaseStamina(self, amount):
            self.stamina += amount
            if self.stamina > pc.max_stamina:
                self.stamina = pc.max_stamina

        def reduceStamina(self, amount):
            self.stamina -= amount
            if self.stamina < 0:
                self.stamina = 0

    class Upgrades:
        def __init__(self, starting_coins):
            self.face_resistance = 0
            self.hand_resistance = 0
            self.chest_resistance = 0
            self.thighs_resistance = 0
            self.cock_resistance = 0
            self.tip_resistance = 0
            self.ass_resistance = 0
            self.wakefulness_cap = 0
            self.sleep_buff = 0 # used to set level of buffs from items that increase sleep level, bath salts for example
            self.resistance_buff = 0 # used to set level of buffs from items that increase resistance to actions, oil for example
            self.touch_buff = 0 # used to set level of buffs from items that increase skill gain for MC, porn mags for example
            self.light_level = 0 # used to set light level for scenes, lower numbers means darker
            self.experience_multiplier = 0.0
            self.points_multiplier = 0.0
            self.upgrade_coins = starting_coins
        
        def increaseUpgradeCoins(self, amount):
            self.upgrade_coins += amount
            persistentIncreaseUpgradeCoins(amount)
        
        def reduceUpgradeCoins(self, amount):
            self.upgrade_coins -= amount

        def increaseFaceResistance(self, amount):
            self.face_resistance += amount
        
        def increaseHandResistance(self, amount):
            self.hand_resistance += amount
        
        def increaseChestResistance(self, amount):
            self.body_resistance += amount
        
        def increaseThighResistance(self, amount):
            self.thighs_resistance += amount
        
        def increaseCockResistance(self, amount):
            self.cock_resistance += amount

        def increaseTipResistance(self, amount):
            self.tip_resistance += amount

        def increaseAssResistance(self, amount):
            self.ass_resistance += amount
        
        def increaseWakefulnessCap(self, amount):
            self.wakefulness_cap += amount
