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
        def __init__(self, max_stamina, hand_exp, hand_level, mouth_exp, mouth_level, foot_exp, foot_level, vaginal_exp, vaginal_level, anal_exp,
            anal_level, just_the_tip_exp, just_the_tip_level, cock_exp, cock_level, total_number_of_orgasms, total_sperm_in_uterus, cycle_number,player_name, victim_name):
            self.name = player_name
            self.male_name = victim_name
            self.stamina = max_stamina
            self.max_stamina = max_stamina
            self.arousal = 0
            self.finger_state = "dry"
            self.player_finger_cum_amount = 0
            self.victim_finger_cum_amount = 0
            self.vaginal_state = "dry"
            self.anal_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.player_type = "default"
            self.money = 0
            self.number_of_orgasms = 0
            self.cock_orgasm_max = 2
            self.total_number_of_orgasms = total_number_of_orgasms
            self.player_sperm_in_uterus_Monday = 0
            self.player_sperm_in_uterus_tuesday = 0
            self.player_sperm_in_uterus_wednesday = 0
            self.player_sperm_in_uterus_thursday = 0
            self.player_sperm_in_uterus_friday = 0
            self.player_sperm_in_uterus_saturday = 0
            self.player_sperm_in_uterus_sunday = 0
            self.victim_sperm_in_uterus_Monday = 0
            self.victim_sperm_in_uterus_tuesday = 0
            self.victim_sperm_in_uterus_wednesday = 0
            self.victim_sperm_in_uterus_thursday = 0
            self.victim_sperm_in_uterus_friday = 0
            self.victim_sperm_in_uterus_saturday = 0
            self.victim_sperm_in_uterus_sunday = 0
            self.total_sperm_in_uterus_this_cycle = 0
            self.total_sperm_in_uterus = total_sperm_in_uterus
            # set hand exp and level
            self.current_hand_exp = hand_exp
            self.hand_level = hand_level
            self.hand_exp_for_level = self.currentHandExpGet()
            # set mouth exp and level
            self.current_mouth_exp = mouth_exp
            self.mouth_level = mouth_level
            self.hand_exp_for_level = self.currentMouthExpGet()
            # set foot exp and level
            self.current_foot_exp = foot_exp
            self.foot_level = foot_level
            self.foot_exp_for_level = self.currentFootExpGet()
            # set vaginal exp and level
            self.current_vaginal_exp = vaginal_exp
            self.vaginal_level = vaginal_level
            self.vaginal_exp_for_level = self.currentVaginalExpGet()
            # set anal exp and level
            self.current_anal_exp = anal_exp
            self.anal_level = anal_level
            self.anal_exp_for_level = self.currentAnalExpGet()
            #######################################################
            # The following are only used for trans/futa/gay packs#
            #######################################################
            # set just the tip level and exp
            self.current_just_the_tip_exp = just_the_tip_exp
            self.just_the_tip_level = just_the_tip_level
            self.just_the_tip_exp_for_level = self.currentJustTheTipExpGet()
            # set cock level and exp
            self.current_cock_exp = cock_exp
            self.cock_level = cock_level
            self.cock_exp_for_level = self.currentCockExpGet()
            # used to check for mismatch after resetting cycle
            self.cycle_number = cycle_number
            # used to show correct failure scene
            self.cycle_end_reason = "none"


        #####################################
        #                                   #
        # mouth related functions           #
        #####################################
        def increaseMouthExp(self, amount):
            level_up = 0
            self.current_mouth_exp += amount
            mouth_exp_for_level = self.mouth_exp_for_level
            while self.current_mouth_exp >= mouth_exp_for_level and mouth_exp_for_level > 0:
                self.increaseMouthLevel(1)
                level_up += 1
                mouth_exp_for_level = currentMouthExpGet()
            return level_up
        
        def increaseMouthLevel(self, amount):
            self.mouth_level += 1
            self.mouth_exp_for_level = currentMouthExpGet()
        
        def kissArousalGain(self):
            default_increase = 5
            mouth_skill_multiplier = self.mouth_level / 1000
            return default_increase, mouth_skill_multiplier
        
        def deepKissArousalGain(self):
            default_increase = 5
            mouth_skill_multiplier = self.mouth_level / 1000
            return default_increase, mouth_skill_multiplier
        
        def suckHerFingersArousalGain(self):
            default_increase = 1
            mouth_skill_multiplier = self.mouth_level / 1000
            return default_increase, mouth_skill_multiplier
        
        def suckCumFingersArousalGain(self):
            default_increase = 4
            mouth_skill_multiplier = self.mouth_level / 1000
            return default_increase, mouth_skill_multiplier
        
        def suckFluidsFromHimArousalGain(self):
            default_increase = 2
            mouth_skill_multiplier = self.mouth_level / 1000
            return default_increase, mouth_skill_multiplier
        
        #####################################
        #                                   #
        # hand related functions            #
        #####################################

        # function to call when player uses their hand for any action to increase experience
        def increaseHandExp(self, amount):
            level_up = 0
            self.current_hand_exp += amount
            hand_exp_for_level = self.hand_exp_for_level
            while self.current_hand_exp >= hand_exp_for_level and hand_exp_for_level > 0: # keep cycling this to increase level
                self.increaseHandLevel(1)
                level_up += 1
                hand_exp_for_level = pc.currentHandExpGet()
            return level_up
        # function to increase hand level, used when hand exp is greater than the amount required for the next level
        def increaseHandLevel(self, amount):
            self.hand_level += 1
            self.hand_exp_for_level = pc.currentHandExpGet()
            return self.hand_exp_for_level

        def rubBreastArousalGain(self):
            default_increase = 7
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier
        
        def rubBothBreastArousalGain(self):
            default_increase = 10
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier
        
        def pinchNippleArousalGain(self):
            default_increase = 7
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier

        def pinchBothNipplesArousalGain(self):
            default_increase = 10
            hand_skill_multiplier = self.hand_level / 1000
            return default_increase, hand_skill_multiplier
        
        #####################################
        #                                   #
        # pussy related functions           #
        #####################################
        # function to call when player uses their pussy for any action (requires penetration) to increase experience
        def increaseVaginalExp(self, amount):
            level_up = 0
            self.current_vaginal_exp += amount
            vaginal_exp_for_level = self.vaginal_exp_for_level
            while self.current_vaginal_exp >= vaginal_exp_for_level and vaginal_exp_for_level > 0: # keep cycling to increase level
                self.increaseVaginalLevel(1)
                level_up += 1
                vaginal_exp_for_level = currentVaginalExpGet()
            return level_up
        
        # function to increase vaginal level, used when vaginal exp is greater than the amount required for the next level
        def increaseVaginalLevel(self, amount):
            self.vaginal_level += amount
            self.vaginal_exp_for_level = currentVaginalExpGet()

        def rubPubisArousalGain(self):
            default_increase = 3
            hand_skill_multiplier = self.hand_level / 1000
            return default_arousal, hand_skill_multiplier
        
        def rubInnerThighArousalGain(self):
            default_increase = 5
            hand_skill_multiplier = self.hand_level / 1000
            return default_arousal, hand_skill_multiplier

        def rubOuterPussyLipsArousalGain(self):
            default_increase = 7
            hand_skill_multiplier = self.hand_level / 1000
            return default_arousal, hand_skill_multiplier       
        
        def massageClitArousalGain(self):
            default_increase = 7
            hand_skill_multiplier = self.hand_level / 1000
            return default_arousal, hand_skill_multiplier
        
        def fingerPussyArousalGain(self):
            default_increase = 10
            hand_skill_multiplier = self.hand_level / 1000
            vaginal_skill_multiplier = self.vaginal_level / 1000
            skill_multiplier = hand_skill_multiplier + vaginal_skill_multiplier
            return default_arousal, skill_multiplier

        #####################################
        #                                   #
        # arse related functions            #
        #####################################
        # function to call when player uses their arse for any action (requires penetration) to increase experience
        def increaseAnalExp(self, amount):
            level_up = 0
            self.current_anal_exp += amount
            anal_exp_for_level = self.anal_exp_for_level
            while self.current_anal_exp >= vaginal_exp_for_level and anal_exp_fro_level > 0: # keep cycling to increase level
                self.increaseAnalLevel(1)
                level_up += 1
                anal_exp_for_level = currentAnalExpGet()
            return level_up
        
        # function to increase anal level, used when anal exp is greater than anal exp required for the next level
        def increaseAnalLevel(self, amount):
            self.anal_level += amount
            self.anal_exp_for_level = currentAnalExpGet()
        
        def rubBumArousalGain(self):
            default_increase = 5
            hand_skill_multiplier = self.hand_level / 1000
            return default_arousal, hand_skill_multiplier
        
        def fingerArseArousalGain(self):
            default_arousal_gain = 7
            hand_skill_multiplier = self.hand_level / 1000
            anal_skill_multiplier = self.anal_level / 1000
            skill_multiplier = hand_skill_multiplier + anal_skill_multiplier
            return default_arousal, skill_multiplier

        def resetMoistState(self):
            self.finger_state = "dry"
            self.vaginal_state = "dry"
            self.anal_state = "dry"
            self.tip_state = "dry"
            self.cock_state = "dry"
            self.player_finger_cum_amount = 0
            self.victim_finger_cum_amount = 0
        
        def increaseArousal(self, amount):
            self.arousal += amount
            if self.arousal >= 150: # check for orgasm
                return True
            else:
                return False
        
        def orgasm(self):
            self.arousal = 0
        
    
        def increaseStamina(self, amount):
            self.stamina += amount
            if self.stamina > pc.max_stamina:
                self.stamina = pc.max_stamina

        def reduceStamina(self, amount):
            self.stamina -= amount
            if self.stamina < 0:
                self.stamina = 0

        # check exp required for player levels
        def currentHandExpGet(self):
            exp_needed = 0
            if self.hand_level <= 999:
                amount = self.hand_level + 1
                with open(renpy.loader.transfn("CSVs/hand table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0
        
        def currentMouthExpGet(self):
            exp_needed = 0
            if self.mouth_level <= 999:
                amount = self.mouth_level + 1
                with open(renpy.loader.transfn("CSVs/mouth table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0

        def currentFootExpGet(self):
            exp_needed = 0
            if self.foot_level <= 999:
                amount = self.foot_level + 1
                with open(renpy.loader.transfn("CSVs/foot table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0
        
        def currentVaginalExpGet(self):
            exp_needed = 0
            if self.vaginal_level <= 999:
                amount = self.vaginal_level + 1
                with open(renpy.loader.transfn("CSVs/vaginal table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0
        
        def currentAnalExpGet(self):
            exp_needed = 0
            if self.anal_level < 999:
                amount = self.anal_level + 1
                with open(renpy.loader.transfn("CSVs/anal table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0
        # only needed for packs with a cock
        def currentJustTheTipExpGet(self):
            exp_needed = 0
            if self.just_the_tip_level <= 999:
                amount = self.just_the_tip_level + 1
                with open(renpy.loader.transfn("CSVs/just the tip table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0

        def currentCockExpGet(self):
            exp_needed = 0
            if self.cock_level < 999:
                amount = self.cock_level + 1
                with open(renpy.loader.transfn("CSVs/cock table.csv"), "r", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for index, row in enumerate(reader):
                        if (index + 1 == amount):
                            exp_needed = int(row["exp needed"])
                            return exp_needed
            else:
                return 0

    class Upgrades:
        def __init__(self, starting_coins):
            # upgrades that Grace believes she is applying to player but is instead applying them to the victim
            self.face_resistance = 0
            self.hand_resistance = 0
            self.chest_resistance = 0
            self.thighs_resistance = 0
            self.cock_resistance = 0 # maybe combine these into genitals or make comment in event about clit and vagina being tip and cock
            self.tip_resistance = 0
            self.ass_resistance = 0
            self.wakefulness_cap = 0
            # buffs, yet to be fleshed out
            self.sleep_buff = 0 # used to set level of buffs from items that increase sleep level, bath salts for example
            self.resistance_buff = 0 # used to set level of buffs from items that increase resistance to actions, oil for example
            self.touch_buff = 0 # used to set level of buffs from items that increase skill gain for MC, porn mags for example
            self.light_level = 0 # used to set light level for scenes, lower numbers means darker
            # multipliers
            self.experience_multiplier = 0.0
            self.coin_multiplier = 0.0
            self.pounds_multiplier = 0.0
            # multipliers for skill level from upgrade shop (added with body part level to determine total multiplier)
            self.mouth_arousal_multiplier = 0
            self.hand_arousal_multiplier = 0
            self.vaginal_arousal_multiplier = 0
            self.anal_arousal_multiplier = 0
            self.just_the_tip_multiplier = 0
            self.cock_arousal_multiplier = 0
            self.foot_arousal_multiplier = 0
            # unlocks for viewing victim stats during night attack
            self.view_victim_arousal_gains = False
            self.view_victim_arousal = False
            self.view_victim_wakefulness_gain = False
            self.view_victim_wakefulness_bar = 0 # 0 means no view, 1 is thirds, 2 is fifths, 3 is tenths, 4 is twenty-fifths, 5 is hundredths and 6 is thousandths
            # ejaculation related stats
            self.victim_ejaculation_amount_increased = 0 # cost one coin per 10 increase
            # starting coins is 50 % of spent coins in previous cycles (cumulative, counts coins spent in all cycles)
            self.upgrade_coins = starting_coins
            # passive unlocks
            self.train_mouth_unlocked = False
            self.train_hands_unlocked = False
            self.train_feet_unlocked = False
            self.train_vaginal_unlocked = False
            self.train_anal_unlocked = False
            self.train_just_the_tip_unlocked = False
            self.train_cock_unlocked = False

        def increaseUpgradeCoins(self, amount):
            base_coins = amount
            points_multiplier = self.coin_multiplier
            coin_gain = floor(amount + (points_multiplier * amount)) # example if multiplier is 0.10 that would be 10 % additional coins
            self.upgrade_coins += coin_gain
            persistentIncreaseUpgradeCoins(coin_gain)
            return coin_gain
        
        
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
