label splashscreen:
    scene black
    with Pause(1)

    show text "All characters involved in sexual activities within this game are at least 18 years of age." with dissolve
    with Pause(2)

    show text "{size=+15}{color=#BB33FF}EcchiYoYoProductions{/color} presents.{/size}"
    with Pause(2)

    show text "{size=+75}While he was sleeping.{/size}"
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label after_load:
    #
    #
    #
    return

# The game starts here.

label start:
    if persistent.cycle_number == 0:
        "This game runs in cycles, what does this mean?"
        "You play for up to one week, at the end of this week you get your ending."
        "However, many stats are carried over between playthroughs, this means you will not be able to get all possible endings on the first play through."
        "It is possible to get a game over screen before the week is finished, but again many stats will still be carried over."
        jump opening_scene
    else:
        "Do you want to reset your stats from previous play through`s?"
        menu:
            "You are currently on cycle [persistent.cycle_number], you will only get this opportunity once per playthrough."
            "Yes":
                python:
                    fullReset()
                jump opening_scene
            "No":
                jump opening_scene

    return
