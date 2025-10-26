#############################################################
#                                                           #
# persistent variables                                      #
# carried over between saves                                #
#############################################################
#
# main stats to carry over
#
default persistent.cycle_number = 0 # 1
default persistent.current_points = 0 # 2
default persistent.total_points_earned = 0 # 3
#
# Player stats
#
default persistent.player_name = "????" # 4
default persistent.victim_name = "????" # 5
default persistent.max_stamina = 100 # 6

default persistent.current_hand_exp = 0 # 7
default persistent.hand_exp_for_level = 6.25 # 8
default persistent.hand_level = 0 # 9

default persistent.current_mouth_exp = 0 # 10
default persistent.mouth_exp_for_level = 6.25 # 11
default persistent.mouth_level = 0 # 12

default persistent.current_foot_exp = 0 # 13
default persistent.foot_exp_for_level = 6.25 # 14
default persistent.foot_level = 0 # 15

default persistent.current_vaginal_exp = 0 # 16
default persistent.vaginal_exp_for_level = 6.25 # 17
default persistent.vaginal_level = 0 # 18

default persistent.current_anal_exp = 0 # 19
default persistent.anal_exp_for_level = 6.25 # 20
default persistent.anal_level = 0 # 21

default persistent.total_orgasms = 0 # 22
default persistent.total_sperm_in_uterus = 0 # 23
#######################################################
# The following are only used for trans/futa/gay packs#
#######################################################
default persistent.current_just_the_tip_exp = 0 # 24
default persistent.just_the_tip_exp_for_level = 6.25 # 25
default persistent.just_the_tip_level = 0 # 26

default persistent.current_cock_exp = 0 # 27
default persistent.cock_exp_for_level = 6.25 # 28
default persistent.cock_level = 0 # 29

default persistent.additional_exp = 85 # exp required for all levels above 999
default persistent.coins_earned = 0.1 # 30
default persistent.first_upgrade_visit = False # 31
#
# victim stats
#
default persistent.wakefulness_cap = 100 # 32

default persistent.face_resistance = 0 # 33 (1000th of current level or zero whichever is lower)
default persistent.face_resistance_level = 0 # 34
default persistent.him_cum_sucking = 0 # 35
default persistent.him_girl_cum_sucking = 0 # 36
default persistent.him_face_sit = 0 # 37
default persistent.him_finger_sucking = 0 # 38

default persistent.hand_resistance = 0 # 39
default persistent.hand_resistance_level = 0 # 40
default persistent.him_finger_sucked = 0 # 41
default persistent.him_clit_rubbed = 0 # 42
default persistent.him_finger_cunt = 0 # 43
default persistent.him_rubbed_breast = 0 # 44
default persistent.him_rubbed_cock = 0 # 45

default persistent.chest_resistance = 0 # 46
default persistent.chest_resistance_level = 0 # 47
default persistent.him_chest_rubbed = 0 # 48
default persistent.him_nipple_rubbed_with_hand = 0 # 49
default persistent.him_pussy_ground_on_chest = 0 # 50
default persistent.him_nipple_rubbed_with_foot = 0 # 51

default persistent.thigh_resistance = 0 # 52
default persistent.thigh_resistance_level = 0 # 53
default persistent.him_thighs_rubbed = 0 # 54
default persistent.him_thighs_rubbed_with_foot = 0 # 55
default persistent.him_pussy_ground_on_thigh = 0 # 56

default persistent.tip_resistance = 0 # 57
default persistent.tip_resistance_level = 0 # 58
default persistent.him_tip_rubbed = 0 # 59
default persistent.him_tip_sucked = 0 # 60
default persistent.him_tip_vaginal = 0 # 61
default persistent.him_tip_anal = 0 # 62

default persistent.cock_resistance = 0 # 63
default persistent.cock_resistance_level = 0 # 64
default persistent.him_cock_masturbated = 0 # 65
default persistent.him_cock_fondle_balls = 0 # 66
default persistent.him_deep_throat = 0 # 67
default persistent.him_cock_dry_hump = 0 # 68
default persistent.him_cock_vaginal = 0 # 69
default persistent.him_cock_anal = 0 # 70

default persistent.ass_resistance = 0 # 71
default persistent.ass_resistance_level = 0 # 72
default persistent.him_ass_rubbed = 0 # 73
default persistent.him_ass_fingered = 0 # 74
default persistent.him_anal_just_the_tip = 0 # 75
default persistent.him_anal = 0 # 76

default persistent.ejaculation_amount = 1000 # 77
default persistent.total_ejaculation_all_cycles = 0 # 78

default persistent.face_resistance_exp = 0 # 82
default persistent.face_resistance_exp_for_level = 6.25 # 83
default persistent.hand_resistance_exp = 0 # 84
default persistent.hand_resistance_exp_for_level = 6.25 # 85
default persistent.chest_resistance_exp = 0 # 86
default persistent.chest_resistance_exp_for_level = 6.25 # 87
default persistent.thigh_resistance_exp = 0 # 88
default persistent.thigh_resistance_exp_for_level = 6.25 # 89
default persistent.tip_resistance_exp = 0 # 90
default persistent.tip_resistance_exp_for_level = 6.25 # 91
default persistent.cock_resistance_exp = 0 # 92
default persistent.cock_resistance_exp_for_level = 6.25 # 93
default persistent.ass_resistance_exp = 0 # 94
default persistent.ass_resistance_exp_for_level = 6.25 # 95
#
#
# Values used during introduction to victims room
#
default intro_2_completed = False # 79
default intro_3_completed = False # 80
default activate_buttons = False # 81

init python:
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
            return 0
        
    
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
            return 0

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
            return 0
    
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
            return 0
    
    def currentAnalExpGet():
        exp_needed = 0
        if persistent.anal_level < 999:
            amount = persistent.anal_level + 1
            with open(renpy.loader.transfn("CSVs/anal table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
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
            return 0
    
    def currentCockExpGet():
        exp_needed = 0
        if persistent.cock_level < 999:
            amount = persistent.cock_level + 1
            with open(renpy.loader.transfn("CSVs/cock table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    ##########################################################
    # his persistent exp levels                              #
    ##########################################################
    def hisCurrentFaceExpGet():
        exp_needed = 0
        if persistent.face_resistance_level < 999:
            amount = persistent.face_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentHandExpGet():
        exp_needed = 0
        if persistent.hand_resistance_level < 999:
            amount = persistent.hand_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentChestExpGet():
        exp_needed = 0
        if persistent.chest_resistance_level < 999:
            amount = persistent.chest_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentThighExpGet():
        exp_needed = 0
        if persistent.thigh_resistance_level < 999:
            amount = persistent.thigh_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentTipExpGet():
        exp_needed = 0
        if persistent.tip_resistance_level < 999:
            amount = persistent.tip_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentCockExpGet():
        exp_needed = 0
        if persistent.cock_resistance_level < 999:
            amount = persistent.cock_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    
    def hisCurrentAssExpGet():
        exp_needed = 0
        if persistent.ass_resistance_level < 999:
            amount = persistent.ass_resistance_level + 1
            with open(renpy.loader.transfn("CSVs/resistance table.csv"), "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if (index + 1 == amount):
                        exp_needed = int(row["exp needed"])
                        return exp_needed
        else:
            return 0
    # used to reset all stats to their defaults, used when a player wants to start a clean cycle
    # persistent values are used to create the player and victim objects
    def fullReset():
        persistent.cycle_number = 0 # 1 
        persistent.current_points = 0 # 2
        persistent.total_points_earned = 0 # 3
        #
        # Player stats
        #
        persistent.player_name = "????" # 4
        persistent.victim_name = "????" # 5
        persistent.max_stamina = 100 # 6

        persistent.current_hand_exp = 0 # 7
        persistent.hand_exp_for_level = 100 # 8
        persistent.hand_level = 0 # 9

        persistent.current_mouth_exp = 0 # 10
        persistent.mouth_exp_for_level = 100 # 11
        persistent.mouth_level = 0 # 12

        persistent.current_foot_exp = 0 # 13
        persistent.foot_exp_for_level = 100 # 14
        persistent.foot_level = 0 # 15

        persistent.current_vaginal_exp = 0 # 16
        persistent.vaginal_exp_for_level = 100 # 17
        persistent.vaginal_level = 0 # 18

        persistent.current_anal_exp = 0 # 19
        persistent.anal_exp_for_level = 100 # 20
        persistent.anal_level = 0 # 21

        persistent.total_orgasms = 0 # 22
        persistent.total_sperm_in_uterus = 0 # 23

        persistent.current_just_the_tip_exp = 0 # 24
        persistent.just_the_tip_exp_for_level = 100 # 25
        persistent.just_the_tip_level = 0 # 26

        persistent.current_cock_exp = 0 # 27
        persistent.cock_exp_for_level = 100 # 28
        persistent.cock_level = 0 # 29

        persistent.coins_earned = 0.1 # 30
        persistent.first_upgrade_visit = False # 31
        #
        # victim stats
        #
        persistent.wakefulness_cap = 100 # 32

        persistent.face_resistance = 0 # 33
        persistent.face_resistance_level = 0 # 34
        persistent.him_cum_sucking = 0 # 35
        persistent.him_girl_cum_sucking = 0 # 36
        persistent.him_face_sit = 0 # 37
        persistent.him_finger_sucking = 0 # 38

        persistent.hand_resistance = 0 # 39
        persistent.hand_resistance_level = 0 # 40
        persistent.him_finger_sucked = 0 # 41
        persistent.him_clit_rubbed = 0 # 42
        persistent.him_finger_cunt = 0 # 43
        persistent.him_rubbed_breast = 0 # 44
        persistent.him_rubbed_cock = 0 # 45

        persistent.chest_resistance = 0 # 46
        persistent.chest_resistance_level = 0 # 47
        persistent.him_chest_rubbed = 0 # 48
        persistent.him_nipple_rubbed_with_hand = 0 # 49
        persistent.him_pussy_ground_on_chest = 0 # 50
        persistent.him_nipple_rubbed_with_foot = 0 # 51

        persistent.thigh_resistance = 0 # 52
        persistent.thigh_resistance_level = 0 # 53
        persistent.him_thighs_rubbed = 0 # 54
        persistent.him_thighs_rubbed_with_foot = 0 # 55
        persistent.him_pussy_ground_on_thigh = 0 # 56

        persistent.tip_resistance = 0 # 57
        persistent.tip_resistance_level = 0 # 58
        persistent.him_tip_rubbed = 0 # 59
        persistent.him_tip_sucked = 0 # 60
        persistent.him_tip_vaginal = 0 # 61
        persistent.him_tip_anal = 0 # 62

        persistent.cock_resistance = 0 # 63
        persistent.cock_resistance_level = 0 # 64
        persistent.him_cock_masturbated = 0 # 65
        persistent.him_cock_fondle_balls = 0 # 66
        persistent.him_deep_throat = 0 # 67
        persistent.him_cock_dry_hump = 0 # 68
        persistent.him_cock_vaginal = 0 # 69
        persistent.him_cock_anal = 0 # 70

        persistent.ass_resistance = 0 # 71
        persistent.ass_resistance_level = 0 # 72
        persistent.him_ass_rubbed = 0 # 73
        persistent.him_ass_fingered = 0 # # 74
        persistent.him_anal_just_the_tip = 0 # 75
        persistent.him_anal = 0 # 76

        persistent.ejaculation_amount = 1000 # 77
        persistent.total_ejaculation_all_cycles = 0 # 78
        #
        #
        # Values used during introduction to victims room
        #
        intro_2_completed = False # 79
        intro_3_completed = False # 80
        activate_buttons = False # 81
        # exp and levels for victim resistance
        persistent.face_resistance_exp = 0  # 82
        persistent.face_resistance_exp_for_level = 6.25 # 83
        persistent.hand_resistance_exp = 0 # 84
        persistent.hand_resistance_exp_for_level = 6.25 # 85
        persistent.chest_resistance_exp = 0 # 86
        persistent.chest_resistance_exp_for_level = 6.25 # 87
        persistent.thigh_resistance_exp = 0 # 88
        persistent.thigh_resistance_exp_for_level = 6.25 # 89
        persistent.tip_resistance_exp = 0 # 90
        persistent.tip_resistance_exp_for_level = 6.25 # 91
        persistent.cock_resistance_exp = 0 # 92
        persistent.cock_resistance_exp_for_level = 6.25 # 93
        persistent.ass_resistance_exp = 0 # 94
        persistent.ass_resistance_exp_for_level = 6.25 # 95
