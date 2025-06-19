init python:
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
            return self.game_end

    def noneFunction():
        1 + 1
        # I do nothing, used for blank python blocks yet to be populated

    def globalAdvanceTime(amount):
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
    # victim ejaculation counts
    #
    def persistentIncreaseEjaculationCount(amount):
        persistent.ejaculation_times += 1
    
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

    # player sucks girl cum/victim cum from fingers, raises player arousal girl = tiny victim = small, reduces wakefulness small, removes girl cum from player hands, adds saliva to player hands, neutral stamina

    # player cleans cum from victim, raises arousal small, neutral wakefulness, removes cum from body part adds saliva to body part, raises suspicion if all cum not cleaned at end of night, neutral stamina

    # 
    # Player chest
    #
    # rub right breast, increase player arousal medium, reduce stamina small, reduce wakefulness small

    # rub left breast, increase player arousal medium, reduce stamina small, reduce wakefulness small

    # rub both breasts, increase player arousal large, reduce stamina medium, reduce wakefulness small

    # pinch right nipple, increase player arousal large, reduce stamina medium, reduce wakefulness small

    # pinch left nipple, increase player arousal large, reduce stamina medium, reduce wakefulness small

    # pinch both nipples, increase player arousal very large, reduce stamina large, reduce wakefulness small

    #
    # player pussy
    #
    # rub pubis, increase player arousal tiny, reduce stamina tiny, reduce wakefulness small

    # rub inner thigh, increase player arousal small, reduce stamina small, reduce wakefulness small

    # rub outer pussy lips, increase player arousal medium, reduce stamina medium, reduce wakefulness small

    # rub clit (requires moist fingers), increase player arousal large, reduce stamina medium, reduce wakefulness small

    # finger pussy (requires moist pussy), increase player arousal very large, reduce stamina large, reduce wakefulness small

    #
    # ass
    #
    # rub players ass, increase player arousal small, reduce stamina small, reduce wakefulness small

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