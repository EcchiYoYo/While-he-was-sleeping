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


    textbutton "Return to your room":
        action Jump("players_room")