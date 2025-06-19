label players_room:
    call screen players_room_screen()

screen players_room_screen():
    python:
        day = day_of_week[(game_time.days_passed - 1)]
    if game_time.block == 1:
        text day + ": Morning" xpos 0.02 ypos 0.05
    elif game_time.block == 2:
        text day + ": Afternoon" xpos 0.02 ypos 0.05
    elif game_time.block == 3:
        text day + ": Evening" xpos 0.02 ypos 0.05
    else:
        text day + ": Night" xpos 0.02 ypos 0.05
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
            hovered Show("global_tooltip", input_text = "Head out to work and earn some money", x_pos = 0.30, y_pos = 0.88)
            action [Hide("global_tooltip"), Jump("you_work_a_little")]
        else:
            idle "images/buttons/go to work button locked.png"
            hovered Show("global_tooltip", input_text = "You can only work in the morning and afternoon", x_pos = 0.30, y_pos = 0.88)
            action NullAction()
        unhovered Hide("global_tooltip")

# button used to open the item shop (Grace) from players room
screen item_shop_button():
    python:
        if man.relationship == "Friend":
            first_use = "your friend"
        elif man.relationship == "Brother":
            first_use = "your brother"
        elif man.relationship == "Father":
            first_use = "your dad"
        elif man.relationship == "Uncle":
            first_use = "your uncle"
        else:
            first_use = "the stranger"
        #
        #
        # add in function to calculate cheapest available upgrade
        #
        #
        minimum_money_needed = 1
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.4
        ypos 0.9
        focus_mask True
        if (game_time.block == 2 or game_time.block == 3) and pc.money >= minimum_money_needed: # add check for money
            idle "images/buttons/item shop button.png"
            hover "images/buttons/item shop button hover.png"
            hovered Show("global_tooltip", input_text = "Spend some of your hard earned pennies with [grace.name]", x_pos = 0.40, y_pos = 0.88)
            #
            #
            #
            action NullAction()
        else:
            idle "images/buttons/item shop button locked.png"
            if pc.money < minimum_money_needed:
                hovered Show("global_tooltip", input_text = "You don`t even have enough money to buy any upgrades. While [grace.name] is sleeping it would be a good idea to go to work and earn money", x_pos = 0.40, y_pos = 0.90)
            elif game_time.block == 1:
                hovered Show("global_tooltip", input_text = "The twins are quite lazy and are sleeping right now, come back in the afternoon or evening", x_pos = 0.40, y_pos = 0.88)
            else:
                hovered Show("global_tooltip", input_text = "You should be assaulting [first_use] or practising your technique right now", x_pos = 0.40, y_pos = 0.88)
            action NullAction()
        unhovered Hide("global_tooltip")

# button used to open technique shop (Gabrielle) from players room
screen technique_shop_button():
    python:
        if man.relationship == "Friend":
            first_use = "your friend"
        elif man.relationship == "Brother":
            first_use = "your brother"
        elif man.relationship == "Father":
            first_use = "your dad"
        elif man.relationship == "Uncle":
            first_use = "your uncle"
        else:
            first_use = "the stranger"
        minimum_points_needed = 1
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.5
        ypos 0.9
        focus_mask True
        if (game_time.block == 2 or game_time.block == 3) and upgrades.upgrade_coins >= minimum_points_needed: # add check for unspent points
            idle "images/buttons/technique shop button.png"
            hover "images/buttons/technique shop button hover.png"
            hovered Show("global_tooltip", input_text = "Spend some of your hard earned points with [gabrielle.name]", x_pos = 0.50, y_pos = 0.88)
            #
            #
            #
            action NullAction()
        else:
            idle "images/buttons/technique shop button locked.png"
            if upgrades.upgrade_coins < minimum_points_needed:
                hovered Show("global_tooltip", input_text = "You don't have enough points to buy any upgrades from [gabrielle.name]. Points can be earned from actions during the night time assault phase", x_pos = 0.50, y_pos = 0.90)
            elif game_time.block == 1:
                hovered Show("global_tooltip", input_text = "The twins are quite lazy and are sleeping right now, come back in the afternoon or evening", x_pos = 0.50, y_pos = 0.88)
            else:
                hovered Show("global_tooltip", input_text = "You should be assaulting [first_use] or practising your technique right now", x_pos = 0.50, y_pos = 0.88)
        unhovered Hide("global_tooltip")
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
    python:
        if man.relationship == "Friend":
            first_use = "your friends"
        elif man.relationship == "Brother":
            first_use = "your brothers"
        elif man.relationship == "Father":
            first_use = "your dads"
        elif man.relationship == "Uncle":
            first_use = "your uncles"
        else:
            first_use = "the strangers"
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.7
        ypos 0.9
        focus_mask True
        if game_time.block == 4:
            idle "images/buttons/place holder button.png"
            hover "images/buttons/place holder button hover.png"
            hovered Show("global_tooltip", input_text = "Head to [first_use] room", x_pos = 0.70, y_pos = 0.88)
            action [Jump("his_room")]
        else:
            idle "images/buttons/place holder button locked.png"
            hovered Show("global_tooltip", input_text = "It`s too early to head to [first_use] bedroom, you can only assault him at night", x_pos = 0.70, y_pos = 0.88)
            action NullAction()
        unhovered Hide("global_tooltip")
