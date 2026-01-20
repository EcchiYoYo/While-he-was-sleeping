screen coins_gained_popup_screen(amount_gained):
    python:
        if isinstance(amount_gained, int):
            actual_gained = amount_gained
        else:
            actual_gained = "".join(map(str, amount_gained))
        amount_gained = actual_gained
    if amount_gained == "??":
        text "You gained ?? coins" xpos 0.5 ypos 0.5
    else:
        text "{color=#FFBF00}You gained [amount_gained] coins" xpos 0.5 ypos 0.5
    timer 2.5 action Hide("coins_gained_popup_screen")

screen player_arousal_increase_screen(amount_gained):
    python:
        if isinstance(amount_gained, int):
            actual_gained = amount_gained
        else:
            actual_gained = "".join(map(str, amount_gained))
        amount_gained = actual_gained
    text "{color=#D97CC6}You gained [amount_gained] arousal" xpos 0.4 ypos 0.4
    timer 2.5 action Hide("player_arousal_increase_screen")

screen player_stamina_reduction_screen(amount_lost):
    python:
        if isinstance(amount_lost, int):
            actual_lost = amount_lost
        else:
            actual_lost = "".join(map(str, amount_gained))
        stamina_lost = actual_lost
    text "{color=#007500}You used [stamina_lost] stamina" xpos 0.4 ypos 0.6
    timer 2.5 action Hide("player_stamina_reduction_screen")

screen victim_arousal_increase_screen(amount_gained):
    python:
        # Convert amount_gained to string if needed
        amount_gained = amount_gained if isinstance(amount_gained, int) else "".join(map(str, amount_gained))
        
        # Map relationship types to display names
        relationship_names = {
            "Friend": "Your childhood friend",
            "Brother": "Your big brother",
            "Daddy": "Your daddy",
            "Uncle": "Your uncle",
        }
        single_use = relationship_names.get(man.relationship, "The stranger")
    text "[single_use] gained [amount_gained] arousal" xpos 0.6 ypos 0.6
    timer 2.5 action Hide("victim_arousal_increase_screen")

screen hand_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] hand levels" xpos 0.2 ypos 0.15
    timer 2.5 action Hide("hand_level_up_screen")

screen persistent_hand_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] global hand levels" xpos 0.2 ypos 0.25
    timer 2.5 action Hide("persistent_hand_level_up_screen")

screen mouth_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] mouth levels" xpos 0.2 ypos 0.45
    timer 2.5 action Hide("mouth_level_up_screen")

screen persistent_mouth_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] global mouth levels" xpos 0.2 ypos 0.55
    timer 2.5 action Hide("persistent_mouth_level_up_screen")

screen foot_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] foot levels" xpos 0.2 ypos 0.4
    timer 2.5 action Hide("foot_level_up_screen")

screen persistent_foot_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] global foot levels" xpos 0.2 ypos 0.5
    timer 2.5 action Hide("persistent_foot_level_up_screen")

screen vaginal_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] vaginal levels" xpos 0.2 ypos 0.25
    timer 2.5 action Hide("vaginal_level_up_screen")

screen persistent_vaginal_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] global vaginal levels" xpos 0.2 ypos 0.35
    timer 2.5 action Hide("persistent_vaginal_level_up_screen")

screen anal_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] anal levels" xpos 0.2 ypos 0.30
    timer 2.5 action Hide("anal_level_up_screen")

screen persistent_anal_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}You gained [number_of_levels] global anal levels" xpos 0.2 ypos 0.40
    timer 2.5 action Hide("persistent_anal_level_up_screen")

screen money_earned_popup_screen(how_much):
    style_prefix "popupTextColorStyle"
    python:
        how_much = how_much if isinstance(how_much, int) else "".join(map(str, how_much))
    text "{color=#78A825}You earned £[how_much]" xpos 0.5 ypos 0.5
    timer 2.5 action Hide("money_earned_popup_screen")

screen his_mouth_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}He gained [number_of_levels] mouth resistance levels" xpos 0.8 ypos 0.45
    timer 2.5 action Hide("his_mouth_level_up_screen")

screen persistent_his_mouth_level_up_screen(number_of_levels):
    python:
        # Convert number_of_levels to string if needed
        number_of_levels = number_of_levels if isinstance(number_of_levels, int) else "".join(map(str, number_of_levels))
    text "{color=#D46900}He gained [number_of_levels] global mouth resistance levels" xpos 0.8 ypos 0.45
    timer 2.5 action Hide("his_mouth_level_up_screen")
