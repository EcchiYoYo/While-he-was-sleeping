screen coins_gained_popup_screen(amount_gained):
    python:
        amount_gained = str(amount_gained)
    if amount_gained == "??":
        text "You gained ?? coins" xpos 0.5 ypos 0.5
    else:
        text f"You gained " + amount_gained + " coins" xpos 0.5 ypos 0.5
    timer 1.5 action Hide("coins_gained_popup_screen")

screen player_arousal_increase_screen(amount_gained):
    python:
        amount_gained = str(amount_gained)
    text f"You gained " + amount_gained + " arousal" xpos 0.4 ypos 0.4
    timer 1.5 action Hide("player_arousal_increase_screen")

screen victim_arousal_increase_screen(amount_gained):
    python:
        amount_gained = str(amount_gained)
        if man.relationship == "Friend":
            single_use = "Your childhood friend"
        elif man.relationship == "Brother":
            single_use = "Your big brother"
        elif man.relationship == "Daddy":
            single_use = "Your daddy"
        elif man.relationship == "Uncle":
            single_use = "Your uncle"
        else:
            single_use = "The stranger"
    if amount_gained == "??":
        text f"" + single_use + " gained ?? arousal" xpos 0.6 ypos 0.6
    else:
        text f"" + single_use + " gained " + amount_gained + " arousal" xpos 0.6 ypos 0.6
    timer 1.5 action Hide("victim_arousal_increase_screen")

screen hand_level_up_screen(number_of_levels):
    python:
        amount_gained = str(number_of_levels)
    text f"You gained " + amount_gained + " hand levels" xpos 0.2 ypos 0.15
    timer 1.5 action Hide("hand_level_up_screen")

screen persistent_hand_level_up_screen(number_of_levels):
    python:
        amount_gained = str(number_of_levels)
    text f"You gained " + amount_gained + " global hand levels" xpos 0.4 ypos 0.15
    timer 1.5 action Hide("persistent_hand_level_up_screen")

screen vaginal_level_up_screen(number_of_levels):
    python:
        amount_gained = str(number_of_levels)
    text f"You gained " + amount_gained + " hand vaginal levels" xpos 0.2 ypos 0.25
    timer 1.5 action Hide("vaginal_level_up_screen")

screen vaginal_level_up_screen(number_of_levels):
    python:
        amount_gained = str(number_of_levels)
    text f"You gained " + amount_gained + " global vaginal levels" xpos 0.4 ypos 0.25
    timer 1.5 action Hide("vaginal_level_up_screen")

screen money_earned_popup_screen(how_much):
    python:
        amount_gained = str(how_much)
    text f"You earned £" + amount_gained xpos 0.5 ypos 0.5
    timer 1.5 action Hide("money_earned_popup_screen")
   