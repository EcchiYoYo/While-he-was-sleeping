screen coins_gained_popup_screen(amount_gained):
    python:
        amount_gained = str(amount_gained)
    text f"You gained " + amount_gained + " coins" xpos 0.5 ypos 0.5
    timer 1.5 action Hide("coins_gained_popup_screen")

screen player_arousal_increase_screen(amount_gained):
    python:
        amount_gained = str(amount_gained)
    text f"You gained " + amount_gained + " arousal" xpos 0.4 ypos 0.4
    timer 1.5 action Hide("player_arousal_increase_screen")
