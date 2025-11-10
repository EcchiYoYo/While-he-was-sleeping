label his_room:
    scene his room
    call screen his_room_screen()

screen his_room_screen():
    use your_actions()
    use his_actions()
    #
    #
    #
    #
    textbutton "Return to your room" xpos 0.0 ypos 0.9:
        style_prefix "practiceScreenTextButton"
        action [Function(game_time.advanceTime, 1), Jump("players_room")]