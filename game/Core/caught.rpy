label caught_label:
    "Here will be the scenes related to being caught."
    if pc.cycle_end_reason == "the thing":
        jump the_thing_label

label the_thing_label:
    python:
        coins_for_new_cycle = int(floor(persistent.coins_earned/2))
    "You were caught and so must start a new cycle."
    "The new cycle will take into account any coins gained from previous cycles and award you half of those coins, [coins_for_new_cycle], at the start of the new cycle."
    "You will retain any global levels gained for both resistance and player experience, meaning the game wil progress faster."
    if persistent.cycle_number == 1:
        "Every cycle should result in more levels and coins being earned, leading to a faster ramp up time for each cycle played."
    "You have currently played [persistent.cycle_number ] cycles."
    jump main_menu
    