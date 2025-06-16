init python:
    audio_when_minimized = False # set audio state when minimized false means muted when minimized 
    preferences.audio_when_unfocused = False # as above but for unfocused 
    preferences.text_cps = 0 # number of characters to display per second for text boxes 0 is infante

###################################################################
#
# Place to store persistent variables and defaults, as this game
# is designed to repeat the same week persistent variables are a
# must
#
###################################################################
default pc = Player(persistent.stamina, persistent.hand_skill, persistent.hand_level, persistent.mouth_skill, persistent.mouth_level, persistent.foot_skill, persistent.foot_level, persistent.vagina_skill, persistent.vagina_level, persistent.anal_skill, persistent.anal_level)
default pc_talk = Character("????", image="player", who_color="#dc51e9")
default pc_male_talk = Character("????", image="player", who_color="#dc51e9")

default man = Victim(persistent.face_resistance, persistent.hand_resistance, persistent.chest_resistance, persistent.thigh_resistance, persistent.tip_resistance, persistent.cock_resistance, persistent.ass_resistance, persistent.wakefulness_cap, persistent.ejaculation_times, persistent.ejaculation_amount)
default victim_talk = Character("????", image="victim", who_color="#d41b1bac")

default gabrielle = Character("????", image="gabrielle", who_color="#802626")
default grace = Character("????", image="grace", who_color="#64d6df")

default game_time = GameTime()
default upgrades = Upgrades(floor(persistent.coins_earned/2))
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
default persistent.stamina = 100
default persistent.hand_skill = 0
default persistent.hand_level = 0

default persistent.mouth_skill = 0
default persistent.mouth_level = 0

default persistent.foot_skill = 0
default persistent.foot_level = 0

default persistent.vagina_skill = 0
default persistent.vagina_level = 0

default persistent.anal_skill = 0
default persistent.anal_level = 0

default persistent.coins_earned = 0.1
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

default persistent.ejaculation_times = 1
default persistent.ejaculation_amount = 1000

#
#
# Values used during introduction to victims room
#
default intro_2_completed = False
default intro_3_completed = False
default activate_buttons = False


init python:
    # used to reset all stats to their defaults, used when a player wants to start a clean cycle
    def fullReset():
        persistent.cycle_number = 0
        persistent.current_points = 0
        persistent.total_points_earned = 0
        #
        # Player stats
        #
        persistent.stamina = 100
        persistent.hand_skill = 0 # skill = number total number of experience for body part
        persistent.hand_level = 0 # level = current level for body part
        persistent.mouth_skill = 0
        persistent.mouth_level = 0
        persistent.foot_skill = 0
        persistent.foot_level = 0
        persistent.vagina_skill = 0
        persistent.vagina_level = 0
        persistent.anal_skill = 0
        persistent.anal_level = 0
        persistent.coins_earned = 0.1
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

