init python:
    audio_when_minimized = False # set audio state when minimized false means muted when minimized 
    preferences.audio_when_unfocused = False # as above but for unfocused 
    preferences.text_cps = 0 # number of characters to display per second for text boxes 0 is infante

###################################################################
#
# Where default objects and lists are defined
# (persistent`s are defined in the persistent file)
#
###################################################################
default pc = Player(persistent.max_stamina, persistent.current_hand_exp, persistent.hand_level, persistent.current_mouth_exp, persistent.mouth_level, persistent.current_foot_exp, persistent.foot_level, persistent.current_vaginal_exp, persistent.vaginal_level, persistent.current_anal_exp, persistent.anal_level, persistent.current_just_the_tip_exp, persistent.just_the_tip_level, persistent.current_cock_exp, persistent.cock_level, persistent.total_orgasms, persistent.total_sperm_in_uterus, persistent.cycle_number)
default pc_talk = Character("????", image="player", who_color="#dc51e9")
default pc_male_talk = Character("????", image="player", who_color="#dc51e9")

default man = Victim(persistent.face_resistance, persistent.hand_resistance, persistent.chest_resistance, persistent.thigh_resistance, persistent.tip_resistance, persistent.cock_resistance, persistent.ass_resistance, persistent.wakefulness_cap, ((floor(persistent.total_ejaculation_all_cycles / 1000)) + 1), persistent.ejaculation_amount)
default victim_talk = Character("????", image="victim", who_color="#d41b1bac")

default gabrielle = Character("????", image="gabrielle", who_color="#802626")
default grace = Character("????", image="grace", who_color="#64d6df")

default game_time = GameTime()
default upgrades = Upgrades(int(floor(persistent.coins_earned/2)))
default day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default game_started = False# Used to decide if reset button is displayed in preferences screen