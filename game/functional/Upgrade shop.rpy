init python:    
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