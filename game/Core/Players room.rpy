label players_room:
    call screen players_room_screen()

screen players_room_screen():
    use go_to_work_button()
    use item_shop_button()
    use technique_shop_button()
    use practice_technique_button()
    use predator_button()

# Button used to go to work from players room screen
screen go_to_work_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.3
        ypos 0.9
        focus_mask True
        if game_time.block == 1 or game_time.block == 2:
            idle "images/buttons/go to work button.png"
            hover "images/buttons/go to work button hover.png"
        else:
            idle "images/buttons/go to work button locked.png"
        action NullAction()

# button used to open the item shop (Grace) from players room
screen item_shop_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.4
        ypos 0.9
        focus_mask True
        if game_time.block == 2 or game_time.block == 3:
            idle "images/buttons/item shop button.png"
            hover "images/buttons/item shop button hover.png"
        else:
            idle "images/buttons/item shop button locked.png"
        action NullAction()

# button used to open technique shop (Gabrielle) from players room
screen technique_shop_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.5
        ypos 0.9
        focus_mask True
        if game_time.block == 2 or game_time.block == 3:
            idle "images/buttons/technique shop button.png"
            hover "images/buttons/technique shop button hover.png"
        else:
            idle "images/buttons/technique shop button locked.png"
        action NullAction()

# button used to open practice menu from players room
screen practice_technique_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.6
        ypos 0.9
        focus_mask True
        if game_time.block != 1:
            idle "images/buttons/place holder button.png"
            hover "images/buttons/place holder button hover.png"
        else:
            idle "images/buttons/place holder button locked.png"
        action NullAction()

# button used to move to victims room from players room
screen predator_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.7
        ypos 0.9
        focus_mask True
        if game_time.block == 4:
            idle "images/buttons/place holder button.png"
            hover "images/buttons/place holder button hover.png"
        else:
            idle "images/buttons/place holder button locked.png"
        action NullAction()
