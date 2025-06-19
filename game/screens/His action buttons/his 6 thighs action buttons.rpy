init:
    transform his_thighs_custom_zoom:
        zoom 0.90

screen his_thigh_screen():
    imagebutton:
        at his_thighs_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.7
        focus_mask True
        if intro_3_completed == True:
            idle "images/buttons/his thighs button.png"
            hover "images/buttons/his thighs button hover.png"
            hovered Show("his_tooltip", input_text = "Perform actions involving the tip of his cock", x_pos = 0.88,  y_pos = 0.63)
            #
            #
            #
            action [Hide("his_tooltip"), Show("his_thighs_actions_select_screen")]
        else:
            idle "images/buttons/his thighs button locked.png"
            hovered Show("his_tooltip", input_text = "Locked during introduction", x_pos = 0.88, y_pos = 0.63)
            #
            #
            #
            action NullAction()
        unhovered Hide("his_tooltip")

screen his_thighs_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("his_thighs_actions_select_screen"), Hide("his_tooltip")]
    use caress_his_thighs_button()
    use rub_his_thigh_with_foot_button()
    use grind_pussy_against_thigh_button()
    use rub_cock_against_his_thigh()
    

screen caress_his_thighs_button():
    imagebutton:
        at his_thighs_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.2
        focus_mask True
        idle "images/buttons/rub his balls button.png"
        hover "images/buttons/rub his balls button hover.png"
        hovered Show("his_tooltip", input_text = "Gently caress his thighs", x_pos = 0.83, y_pos = 0.13)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen rub_his_thigh_with_foot_button():
    imagebutton:
        at his_thighs_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.3
        focus_mask True
        idle "images/buttons/rub thigh with foot button.png"
        hover "images/buttons/rub thigh with foot button hover.png"
        hovered Show("his_tooltip", input_text = "Rub his thigh with your foot", x_pos = 0.83, y_pos = 0.23)
        #
        #
        #
        action NullAction()

screen grind_pussy_against_thigh_button():
    imagebutton:
        at his_thighs_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.4
        focus_mask True
        if pc.vaginal_state == "dry": # add stamina check here also
            idle "images/buttons/pussy grind on thigh button locked.png"
            hovered Show("his_tooltip", input_text = "Your pussy must be moist to perform this action, raise arousal to increase pussy moistness or coat coat your pussy in some fluids", x_pos = 0.83, y_pos = 0.33)
            #
            #
            #
            action NullAction()
        else:
            idle "images/buttons/pussy grind on thigh button.png"
            hover "images/buttons/pussy grind on thigh button hover.png"
            hovered Show("his_tooltip", input_text = "Grind your pussy along his thigh", x_pos = 0.83, y_pos = 0.33)
            #
            #
            #
            #
            action NullAction()
        unhovered Hide("his_tooltip")

screen rub_cock_against_his_thigh():
    imagebutton:
        at his_thighs_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.5
        focus_mask True
        if (pc.player_type == "trans_male" or pc.player_type == "futa" or pc.player_type == "gay"): # add stamina check here also
            if pc.stamina > 50: # adjust to correct stamina
                idle "images/buttons/cock rub on thigh button.png"
                hover "images/buttons/cock rub on thigh button hover.png"
                hovered Show("his_tooltip", input_text = "Rub your cock against his thigh", x_pos = 0.83, y_pos = 0.43)
                #
                #
                #
                action NullAction()
            else:
                idle "images/buttons/cock rub on thigh button locked.png"
                hovered Show("his_tooltip", input_text = "You do not have enough stamina to perform this action")
                #
                #
                #
                action NullAction()
        else:
            idle "images/buttons/nothing button locked.png"
            hovered Show("his_tooltip", input_text = "Not available while playing [pc.player_type] pack", x_pos = 0.83, y_pos = 0.43)
            #
            #
            #
            action NullAction()
        unhovered Hide("his_tooltip")
