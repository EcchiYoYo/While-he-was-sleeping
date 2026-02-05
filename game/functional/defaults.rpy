init python:
    preferences.audio_when_unfocused = False # as above but for unfocused 
    preferences.text_cps = 0 # number of characters to display per second for text boxes 0 is infinite

###################################################################
#
# Where default objects and lists are defined
# (persistent`s are defined in the persistent file)
#
###################################################################
#
# persistent levels are the level the player starts at and does not need to be used in arousal increase calculations
#
# order if player parameters
# Maximum stamina
# persistent hand experience earned through all playthroughs
# current hand level set at game start by reading persistent hand level levelled through all playthroughs
# persistent mouth experience earned through all playthroughs
# current mouth level set at game start by reading persistent mouth level, levelled through all playthroughs
# foot experience set as above
# foot level set as above
# vaginal experience set as above
# vaginal level set as above
# anal exp set as above
# anal level set as above
# tip exp set as above
# tip level set as above
# cock exp set as above
# cock level set as above
# total player orgasms through all playthroughs
# total sperm that has entered players uterus throughout all playthroughs
# total cycles played, increased at the start of each playthrough
# players name, set at game start
# victims name, set at game start
#
default pc = Player(persistent.max_stamina, persistent.current_hand_exp, persistent.hand_level, persistent.current_mouth_exp, persistent.mouth_level, persistent.current_foot_exp, persistent.foot_level, persistent.current_vaginal_exp, persistent.vaginal_level,
    persistent.current_anal_exp, persistent.anal_level, persistent.current_just_the_tip_exp, persistent.just_the_tip_level, persistent.current_cock_exp, persistent.cock_level, persistent.total_orgasms, persistent.total_sperm_in_uterus, persistent.cycle_number,
    persistent.player_name, persistent.victim_name)
default pc_talk = Character("????", image="player", who_color="#dc51e9")
default pc_male_talk = Character("????", image="player_male", who_color="#dc51e9")
# order of victim parameters
# face resistance experience earned through all playthroughs
# hand resistance exp set as above
# chest resistance exp set as above
# thigh resistance exp set as above
# tip resistance exp set as above
# cock resistance exp set as above
# ass resistance exp set as above
# current victim wakefulness cap
# total number of ejaculations victim is allowed (default 1, increases by 1 for every thousand sperm ejaculated)
# total ejaculation amount for victim
# face resistance level cumulative through all playthroughs
# hand level as above
# chest level as above
# thigh level as above
# tip level as above
# cock level as above
# ass level as above
#
default man = Victim(persistent.face_resistance_exp, persistent.hand_resistance_exp, persistent.chest_resistance_exp, persistent.thigh_resistance_exp, persistent.tip_resistance_exp, persistent.cock_resistance_exp, persistent.ass_resistance_exp, persistent.wakefulness_cap,
    ((floor(persistent.total_ejaculation_all_cycles / 1000)) + 1), persistent.ejaculation_amount, persistent.face_resistance_level, persistent.hand_resistance_level, persistent.chest_resistance_level, persistent.thigh_resistance_level,
        persistent.tip_resistance_level, persistent.cock_resistance_level, persistent.ass_resistance_level)
default victim_talk = Character("????", image="victim", who_color="#d41b1b")

default gabrielle = Character("????", image="gabrielle", who_color="#802626")
default grace = Character("????", image="grace", who_color="#64d6df")

default game_time = GameTime()
default sperm_location_amounts = spermLocationAmounts()
default groceries = Groceries()
# persistent.coins_earned is set during pre-launch phase and is set as a global variable
default upgrades = Upgrades(int(floor(persistent.coins_earned/2)))
default day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default random_girl_names_list = ["Bonnie", "Gemma", "Genevieve", "Amelia", "Freya", "Annalise", "Aurora", "Calista", "Calliope", "Dakota", "Eliza", "Harper", "Ivy", "Jolie", "Josephine", "Julia", "Leah", "Lorelei", "Nicole"]
default random_guy_names_list = ["David", "John", "Ethan", "Noah", "Samuel", "Jacob", "Nicholas", "Liam", "Oliver", "Henry", "Ryan", "Daniel", "Anthony", "Charles", "William", "Logan", "Romeo"]
