#############################################################
#                                                           #
# persistent variables                                      #
# carried over between saves                                #
#############################################################
#
# main stats to carry over
#
default persistent.cycle_number = 0
default persistent.current_points = 0
default persistent.total_points_earned = 0
#
# Player stats
#
default persistent.max_stamina = 100

default persistent.current_hand_exp = 0
default persistent.hand_exp_for_level = 100
default persistent.hand_level = 0

default persistent.current_mouth_exp = 0
default persistent.mouth_exp_for_level = 100
default persistent.mouth_level = 0

default persistent.current_foot_exp = 0
default persistent.foot_exp_for_level = 100
default persistent.foot_level = 0

default persistent.current_vaginal_exp = 0
default persistent.vaginal_exp_for_level = 100
default persistent.vaginal_level = 0

default persistent.current_anal_exp = 0
default persistent.anal_exp_for_level = 100
default persistent.anal_level = 0

default persistent.total_orgasms = 0
default persistent.total_sperm_in_uterus = 0
#######################################################
# The following are only used for trans/futa/gay packs#
#######################################################
default persistent.current_just_the_tip_exp = 0
default persistent.just_the_tip_exp_for_level = 100
default persistent.just_the_tip_level = 0

default persistent.current_cock_exp = 0
default persistent.cock_exp_for_level = 100
default persistent.cock_level = 0

default persistent.additional_exp = 85 # exp required for all levels above 999
default persistent.coins_earned = 0.1
default persistent.first_upgrade_visit = False
#
# victim stats
#
default persistent.wakefulness_cap = 100

default persistent.face_resistance = 0
default persistent.him_cum_sucking = 0
default persistent.him_girl_cum_sucking = 0
default persistent.him_face_sit = 0
default persistent.him_finger_sucking = 0

default persistent.hand_resistance = 0
default persistent.him_finger_sucked = 0
default persistent.him_clit_rubbed = 0
default persistent.him_finger_cunt = 0
default persistent.him_rubbed_breast = 0
default persistent.him_rubbed_cock = 0

default persistent.chest_resistance = 0
default persistent.him_chest_rubbed = 0
default persistent.him_nipple_rubbed_with_hand = 0
default persistent.him_pussy_ground_on_chest = 0
default persistent.him_nipple_rubbed_with_foot = 0

default persistent.thigh_resistance = 0
default persistent.him_thighs_rubbed = 0
default persistent.him_thighs_rubbed_with_foot = 0
default persistent.him_pussy_ground_on_thigh = 0

default persistent.tip_resistance = 0
default persistent.him_tip_rubbed = 0
default persistent.him_tip_sucked = 0
default persistent.him_tip_vaginal = 0
default persistent.him_tip_anal = 0

default persistent.cock_resistance = 0
default persistent.him_cock_masturbated = 0
default persistent.him_cock_fondle_balls = 0
default persistent.him_deep_throat = 0
default persistent.him_cock_dry_hump = 0
default persistent.him_cock_vaginal = 0
default persistent.him_cock_anal = 0

default persistent.ass_resistance = 0
default persistent.him_ass_rubbed = 0
default persistent.him_ass_fingered = 0
default persistent.him_anal_just_the_tip = 0
default persistent.him_anal = 0

default persistent.ejaculation_amount = 1000
default persistent.total_ejaculation_all_cycles = 0

#
#
# Values used during introduction to victims room
#
default intro_2_completed = False
default intro_3_completed = False
default activate_buttons = False

init python:
    # used to reset all stats to their defaults, used when a player wants to start a clean cycle
    # persistent values are used to create the player and victim objects
    def fullReset():
        persistent.cycle_number = 0
        persistent.current_points = 0
        persistent.total_points_earned = 0
        #
        # Player stats
        #
        persistent.max_stamina = 100

        persistent.current_hand_exp = 0
        persistent.hand_exp_for_level = 100
        persistent.hand_level = 0

        persistent.current_mouth_exp = 0
        persistent.mouth_exp_for_level = 100
        persistent.mouth_level = 0

        persistent.current_foot_exp = 0
        persistent.foot_exp_for_level = 100
        persistent.foot_level = 0

        persistent.current_vaginal_exp = 0
        persistent.vaginal_exp_for_level = 100
        persistent.vaginal_level = 0

        persistent.current_anal_exp = 0
        persistent.anal_exp_for_level = 100
        persistent.anal_level = 0

        persistent.total_orgasms = 0
        persistent.total_sperm_in_uterus = 0

        persistent.current_just_the_tip_exp = 0
        persistent.just_the_tip_exp_for_level = 100
        persistent.just_the_tip_level = 0

        persistent.current_cock_exp = 0
        persistent.cock_exp_for_level = 100
        persistent.cock_level = 0

        persistent.additional_exp = 85
        persistent.coins_earned = 0.1
        persistent.first_upgrade_visit = False
        #
        # victim stats
        #
        persistent.wakefulness_cap = 100

        persistent.face_resistance = 0
        persistent.him_cum_sucking = 0
        persistent.him_girl_cum_sucking = 0
        persistent.him_face_sit = 0
        persistent.him_finger_sucking = 0

        persistent.hand_resistance = 0
        persistent.him_finger_sucked = 0
        persistent.him_clit_rubbed = 0
        persistent.him_finger_cunt = 0
        persistent.him_rubbed_breast = 0
        persistent.him_rubbed_cock = 0

        persistent.chest_resistance = 0
        persistent.him_chest_rubbed = 0
        persistent.him_nipple_rubbed_with_hand = 0
        persistent.him_pussy_ground_on_chest = 0
        persistent.him_nipple_rubbed_with_foot = 0

        persistent.thigh_resistance = 0
        persistent.him_thighs_rubbed = 0
        persistent.him_thighs_rubbed_with_foot = 0
        persistent.him_pussy_ground_on_thigh = 0

        persistent.tip_resistance = 0
        persistent.him_tip_rubbed = 0
        persistent.him_tip_sucked = 0
        persistent.him_tip_vaginal = 0
        persistent.him_tip_anal = 0

        persistent.cock_resistance = 0
        persistent.him_cock_masturbated = 0
        persistent.him_cock_fondle_balls = 0
        persistent.him_deep_throat = 0
        persistent.him_cock_dry_hump = 0
        persistent.him_cock_vaginal = 0
        persistent.him_cock_anal = 0

        persistent.ass_resistance = 0
        persistent.him_ass_rubbed = 0
        persistent.him_ass_fingered = 0
        persistent.him_anal_just_the_tip = 0
        persistent.him_anal = 0

        persistent.ejaculation_amount = 1000
        persistent.total_ejaculation_all_cycles = 0
        #
        #
        # Values used during introduction to victims room
        #
        intro_2_completed = False
        intro_3_completed = False
        activate_buttons = False
