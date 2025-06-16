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

        def resetMoistState():
            self.finger_state = "dry"
            self.vaginal_state = "dry"
            self.anal_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
        
        def increaseArousal(amount):
            self.arousal += amount
            if self.arousal > 100: # check for orgasm
                self.arousal = 100
                return True
            else:
                return False
        
        def orgasm():
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

    def increaseHandSkill(amount):
        pc.hand_skill += amount
        persistent.hand_skill += amount
        if pc.hand_level < 10:
            if pc.hand_skill >= 10000:
                pc.hand_level = 10
                persistent.hand_level = 10
            elif pc.hand_skill >= 5800:
                pc.hand_level = 9
                persistent.hand_level = 9
            elif pc.hand_skill >= 3800:
                pc.hand_level = 8
                persistent.hand_level = 8
            elif pc.hand_skill >= 2800:
                pc.hand_level = 7
                persistent.hand_level = 7
            elif pc.hand_skill >= 2000:
                pc.hand_level = 6
                persistent.hand_level = 6
            elif pc.hand_skill >= 1350:
                pc.hand_level = 5
                persistent.hand_level = 5
            elif pc.hand_skill >= 850:
                pc.hand_level = 4
                persistent.hand_level = 4
            elif pc.hand_skill >= 475:
                pc.hand_level = 3
                persistent.hand_level = 3
            elif pc.hand_skill >= 250:
                pc.hand_level = 2
                persistent.hand_level = 2
            elif pc.hand_skill >= 100:
                pc.hand_level = 1
                persistent.hand_level = 1
            else:
                pc.hand_level = 0
                persistent.hand_level = 0

    def increaseMouthSkill(amount):
        pc.mouth_skill += amount
        persistent.mouth_skill += amount
        if pc.mouth_level < 10:
            if pc.mouth_skill >= 10000:
                pc.mouth_level = 10
                persistent.mouth_level = 10
            elif pc.mouth_skill >= 5800:
                pc.mouth_level = 9
                persistent.mouth_level = 9
            elif pc.mouth_skill >= 3800:
                pc.mouth_level = 8
                persistent.mouth_level = 8
            elif pc.mouth_skill >= 2800:
                pc.mouth_level = 7
                persistent.mouth_level = 7
            elif pc.mouth_skill >= 2000:
                pc.mouth_level = 6
                persistent.mouth_level = 6
            elif pc.mouth_skill >= 1350:
                pc.mouth_level = 5
                persistent.mouth_level = 5
            elif pc.mouth_skill >= 850:
                pc.mouth_level = 4
                persistent.mouth_level = 4
            elif pc.mouth_skill >= 475:
                pc.mouth_level = 3
                persistent.mouth_level = 3
            elif pc.mouth_skill >= 250:
                pc.mouth_level = 2
                persistent.mouth_level = 2
            elif pc.mouth_skill >= 100:
                pc.mouth_level = 1
                persistent.mouth_level = 1
            else:
                pc.mouth_level = 0
                persistent.mouth_level = 0

    def increaseFootSkill(amount):
        pc.foot_skill += amount
        persistent.foot_skill += amount
        if pc.foot_level < 10:
            if pc.foot_skill >= 10000:
                pc.foot_level = 10
                persistent.foot_level = 10
            elif pc.foot_skill >= 5800:
                pc.foot_level = 9
                persistent.foot_level = 9
            elif pc.foot_skill >= 3800:
                pc.foot_level = 8
                persistent.foot_level = 8
            elif pc.foot_skill >= 2800:
                pc.foot_level = 7
                persistent.foot_level = 7
            elif pc.foot_skill >= 2000:
                pc.foot_level = 6
                persistent.foot_level = 6
            elif pc.foot_skill >= 1350:
                pc.foot_level = 5
                persistent.foot_level = 5
            elif pc.foot_skill >= 850:
                pc.foot_level = 4
                persistent.foot_level = 4
            elif pc.foot_skill >= 475:
                pc.foot_level = 3
                persistent.foot_level = 3
            elif pc.foot_skill >= 250:
                pc.foot_level = 2
                persistent.foot_level = 2
            elif pc.foot_skill >= 100:
                pc.foot_level = 1
                persistent.foot_level = 1
            else:
                pc.foot_level = 0
                persistent.foot_level = 0

    def increaseVaginaSkill(amount):
        pc.vagina_skill += amount
        persistent.vagina_skill += amount
        if pc.vagina_level < 10:
            if pc.vagina_skill >= 10000:
                pc.vagina_level = 10
                persistent.vagina_level = 10
            elif pc.vagina_skill >= 5800:
                pc.vagina_level = 9
                persistent.vagina_level = 9
            elif pc.vagina_skill >= 3800:
                pc.vagina_level = 8
                persistent.vagina_level = 8
            elif pc.vagina_skill >= 2800:
                pc.vagina_level = 7
                persistent.vagina_level = 7
            elif pc.vagina_skill >= 2000:
                pc.vagina_level = 6
                persistent.vagina_level = 6
            elif pc.vagina_skill >= 1350:
                pc.vagina_level = 5
                persistent.vagina_level = 5
            elif pc.vagina_skill >= 850:
                pc.vagina_level = 4
                persistent.vagina_level = 4
            elif pc.vagina_skill >= 475:
                pc.vagina_level = 3
                persistent.vagina_level = 3
            elif pc.vagina_skill >= 250:
                pc.vagina_level = 2
                persistent.vagina_level = 2
            elif pc.vagina_skill >= 100:
                pc.vagina_level = 1
                persistent.vagina_level = 1
            else:
                pc.vagina_level = 0
                persistent.vagina_level = 0

    def increaseAnalSkill(amount):
        pc.anal_skill += amount
        persistent.anal_skill += amount
        if pc.anal_level < 10:
            if pc.anal_skill >= 10000:
                pc.anal_level = 10
                persistent.anal_level = 10
            elif pc.anal_skill >= 5800:
                pc.anal_level = 9
                persistent.anal_level = 9
            elif pc.anal_skill >= 3800:
                pc.anal_level = 8
                persistent.anal_level = 8
            elif pc.anal_skill >= 2800:
                pc.anal_level = 7
                persistent.anal_level = 7
            elif pc.anal_skill >= 2000:
                pc.anal_level = 6
                persistent.anal_level = 6
            elif pc.anal_skill >= 1350:
                pc.anal_level = 5
                persistent.anal_level = 5
            elif pc.anal_skill >= 850:
                pc.anal_level = 4
                persistent.anal_level = 4
            elif pc.anal_skill >= 475:
                pc.anal_level = 3
                persistent.anal_level = 3
            elif pc.anal_skill >= 250:
                pc.anal_level = 2
                persistent.anal_level = 2
            elif pc.anal_skill >= 100:
                pc.anal_level = 1
                persistent.anal_level = 1
            else:
                pc.anal_level = 0
                persistent.anal_level = 0

    def increaseStamina(amount):
        pc.stamina += amount
        if pc.stamina > pc.max_stamina:
            pc.stamina = pc.max_stamina

    def reduceStamina(amount):
        pc.stamina -= amount
        if pc.stamina < 0:
            pc.stamina = 0

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
            self.sleep_buff = 0 # used to set level of buffs from items that increase sleep level, bath slats for example
            self.resistance_buff = 0 # used to set level of buffs from items that increase resistance to actions, oil for example
            self.touch_buff = 0 # used to set level of buffs from items that increase skill gain for MC, porn mags for example
            self.light_level = 0 # used to set light level for scenes, lower numbers means darker
            self.experience_multiplier = 0.0
            self.points_multiplier = 0.0
            self.upgrade_coins = starting_coins
        
        def increaseUpgradeCoins(amount):
            self.upgrade_coins += amount
            persistentIncreaseUpgradeCoins(amount)
        
        def reduceUpgradeCoins(amount):
            self.upgrade_coins -= amount

        def increaseFaceResistance(amount):
            self.face_resistance += amount
        
        def increaseHandResistance(amount):
            self.hand_resistance += amount
        
        def increaseChestResistance(amount):
            self.body_resistance += amount
        
        def increaseThighResistance(amount):
            self.thighs_resistance += amount
        
        def increaseCockResistance(amount):
            self.cock_resistance += amount

        def increaseTipResistance(amount):
            self.tip_resistance += amount

        def increaseAssResistance(amount):
            self.ass_resistance += amount
        
        def increaseWakefulnessCap(amount):
            self.wakefulness_cap += amount