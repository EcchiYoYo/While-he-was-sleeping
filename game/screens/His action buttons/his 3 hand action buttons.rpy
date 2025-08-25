init:
    transform his_hand_custom_zoom:
        zoom 0.90

screen his_hand():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.4
        focus_mask True
        if intro_3_completed == True:
            idle "images/buttons/his hands action button.png"
            hover "images/buttons/his hands action button hover.png"
            hovered Show("his_tooltip", input_text = "Perform actions involving his hands", x_pos = 0.88,  y_pos = 0.33)
            #
            #
            #
            action [Hide("his_tooltip"), Show("his_hand_actions_select_screen")]
        else:
            idle "images/buttons/his hands action button locked.png"
            hovered Show("his_tooltip", input_text = "Locked during introduction", x_pos = 0.88, y_pos = 0.33)
            action NullAction()
        unhovered Hide("his_tooltip")

screen his_hand_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("his_hand_actions_select_screen"), Hide("his_tooltip")]
    use he_rubs_her_breast_button()
    use he_rubs_her_clit_button()
    use he_fingers_her_button()
    use he_fingers_her_ass_button()
    use he_rubs_her_cock_button()


screen he_rubs_her_breast_button():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.2
        focus_mask True
        idle "images/buttons/he rubs her breast button.png"
        hover "images/buttons/he rubs her breast button hover.png"
        hovered Show("his_tooltip", input_text = "Massage your breast with his hand", x_pos = 0.83, y_pos = 0.13)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen he_rubs_her_clit_button():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.3
        focus_mask True
        idle "images/buttons/he rubs her clit button.png"
        hover "images/buttons/he rubs her clit button hover.png"
        hovered Show("his_tooltip", input_text = "Use his fingers to flick your bean", x_pos = 0.83, y_pos = 0.23)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen he_fingers_her_button():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.4
        focus_mask True
        idle "images/buttons/he fingers her button.png"
        hover "images/buttons/he fingers her button hover.png"
        hovered Show("his_tooltip", input_text = "Finger yourself using his fingers", x_pos = 0.83, y_pos = 0.33)
        unhovered Hide("his_tooltip")
        #
        #
        #
        #
        action NullAction()

screen he_fingers_her_ass_button():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.5
        focus_mask True
        if man.finger_state != "dry": # ass stamina check here also
            idle "images/buttons/he fingers her ass button.png"
            hover "images/buttons/he fingers her ass button hover.png"
            hovered Show("his_tooltip", input_text = "Finger your arse hole with his fingers", x_pos = 0.83, y_pos = 0.43)
        else:
            idle "images/buttons/he fingers her ass button locked.png"
            if man.finger_state != "dry":
                hovered Show("his_tooltip", input_text = "No enough stamina to perform this action", x_pos = 0.83, y_pos = 0.43)
            else:
                hovered Show("his_tooltip", input_text = "His fingers must be moist to perform this action, coat his fingers in some fluid", x_pos = 0.83, y_pos = 0.43)
            #
            #
            #
            action NullAction()
        unhovered Hide("his_tooltip")

screen he_rubs_her_cock_button():
    imagebutton:
        at his_hand_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.6
        focus_mask True
        if (pc.player_type == "trans_male" or pc.player_type == "futa" or pc.player_type == "gay"): #add stamina check
            idle "images/buttons/he rubs her cock button.png"
            hover "images/buttons/he rubs her cock button hover.png"
            hovered Show("his_tooltip", input_text = "Use his hand to masturbate your cock", x_pos = 0.83, y_pos = 0.53)
            action NullAction()
        else:
            if pc.player_type == "trans_male" or pc.player_type == "futa" or pc.player_type == "gay":
                idle "images/buttons/he rubs her cock button locked.png"
                hovered Show("his_tooltip", input_text = "No enough stamina to perform this action", x_pos = 0.83, y_pos = 0.53)
            else:
                idle "images/buttons/nothing button locked.png"
                hovered Show("his_tooltip", input_text = "Not available while playing [pc.player_type] pack", x_pos = 0.83, y_pos = 0.53)
            action NullAction()
        unhovered Hide("his_tooltip")
                