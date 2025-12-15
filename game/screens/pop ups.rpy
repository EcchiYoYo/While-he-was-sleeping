screen coins_gained_popup_screen(amount_gained):
    python:
        actual_gained = "".join(map(str, amount_gained))
        amount_gained = actual_gained
    if amount_gained == "??":
        text "You gained ?? coins" xpos 0.5 ypos 0.5
    else:
        text "{color=#FFBF00}You gained [amount_gained] coins" xpos 0.5 ypos 0.5
    timer 2.5 action Hide("coins_gained_popup_screen")

screen player_arousal_increase_screen(amount_gained):
    python:
        actual_gained = "".join(map(str, amount_gained))
        amount_gained = actual_gained
    text "{color=#D97CC6}You gained [amount_gained] arousal" xpos 0.4 ypos 0.4
    timer 2.5 action Hide("player_arousal_increase_screen")

screen player_stamina_reduction_screen(amount_lost):
    python:
        actual_lost = "".join(map(str, amount_lost))
        amount_lost = actual_lost
    text "{color=#007500}You used [amount_lost] stamina" xpos 0.4 ypos 0.6
    timer 2.5 action Hide("player_stamina_reduction_screen")

screen victim_arousal_increase_screen(amount_gained):
    python:
        actual_gained = "".join(map(str, amount_gained))
        amount_gained = actual_gained
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
        text "[single_use] gained ?? arousal" xpos 0.6 ypos 0.6
    else:
        text "[single_use] gained [amount_gained] arousal" xpos 0.6 ypos 0.6
    timer 2.5 action Hide("victim_arousal_increase_screen")

screen hand_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] hand levels" xpos 0.2 ypos 0.15
    timer 2.5 action Hide("hand_level_up_screen")

screen persistent_hand_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] global hand levels" xpos 0.2 ypos 0.25
    timer 2.5 action Hide("persistent_hand_level_up_screen")

screen mouth_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] mouth levels" xpos 0.2 ypos 0.45
    timer 2.5 action Hide("mouth_level_up_screen")

screen persistent_mouth_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] global mouth levels" xpos 0.2 ypos 0.55
    timer 2.5 action Hide("persistent_mouth_level_up_screen")

screen foot_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] foot levels" xpos 0.2 ypos 0.4
    timer 2.5 action Hide("foot_level_up_screen")

screen persistent_foot_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] global foot levels" xpos 0.2 ypos 0.5
    timer 2.5 action Hide("persistent_foot_level_up_screen")

screen vaginal_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] vaginal levels" xpos 0.2 ypos 0.25
    timer 2.5 action Hide("vaginal_level_up_screen")

screen persistent_vaginal_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] global vaginal levels" xpos 0.2 ypos 0.35

screen anal_level_up_screen(number_of_levels):
    python:
        actual_gained = "".join(map(str, number_of_levels))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] anal levels" xpos 0.2 ypos 0.30

screen persistent_anal_level_up_screen(number_of_levels_gained):
    python:
        actual_gained = "".join(map(str, number_of_levels_gained))
        amount_gained = actual_gained
    text "{color=#D46900}You gained [amount_gained] global anal levels" xpos 0.2 ypos 0.40

screen money_earned_popup_screen(how_much):
    style_prefix "popupTextColorStyle"
    python:
        actual_gained = "".join(map(str, how_much))
        amount_gained = actual_gained
    text "{color=#78A825}You earned £[amount_gained]" xpos 0.5 ypos 0.5
    timer 2.5 action Hide("money_earned_popup_screen")
