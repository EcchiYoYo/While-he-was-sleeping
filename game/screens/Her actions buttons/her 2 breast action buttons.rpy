init:
    transform her_breast_custom_zoom:
        zoom 0.90

screen your_breast():
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.3
        focus_mask True
        if intro_2_completed == False or activate_buttons == True:
            idle "images/buttons/her breast button.png"
            hover "images/buttons/her breast button hover.png"
            action [Hide("her_tooltip"), Show("breast_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving your breasts",x_pos = 0.10, y_pos = 0.23)
        else:
            idle "images/buttons/her breast button locked.png"
            hovered Show("her_tooltip", input_text="You need to select his chest not yours",x_pos = 0.10, y_pos = 0.23)
        unhovered Hide("her_tooltip")

screen breast_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("breast_actions_select_screen"), Hide("her_tooltip")]
    use rub_left_breast_button()
    use rub_right_breast_button()
    use rub_both_breasts_button()
    use pinch_left_nipple_button()
    use pinch_right_nipple_button()
    use pinch_both_nipples_button()

screen rub_left_breast_button():
    python:
        increase_arousal = str(rubBreastArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 5:
                idle "images/buttons/left breast button.png"
                hover "images/buttons/left breast button hover.png"
                hovered Show("her_tooltip", input_text = f"Rub your left breast increasing your arousal level by " + increase_arousal + ".", x_pos = 0.15, y_pos = 0.13)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("rub_left_breast_label")]
            else:
                idle "images/buttons/left breast button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 5 you have [pc.stamina]")
                action NullAction()
        else:
            idle "images/buttons/left breast button.png"
            hover "images/buttons/left breast button hover.png"
            hovered Show("her_tooltip", input_text="Rub your left breast",x_pos = 0.15, y_pos = 0.13)
            action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("rub_left_breast_label")]
        unhovered Hide("her_tooltip")

screen rub_right_breast_button():
    python:
        increase_arousal = str(rubBreastArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 5:
                idle "images/buttons/right breast button.png"
                hover "images/buttons/right breast button hover.png"
                hovered Show("her_tooltip", input_text = f"Rub your right breast increasing your arousal level by " + increase_arousal +" .", x_pos = 0.15, y_pos = 0.23)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("rub_right_breast_label")]
            else:
                idle "images/buttons/left breast button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 5 you have [pc.stamina]", x_pos = 0.15, y_pos = 0.23)
                action NullAction()
        else:
            idle "images/buttons/right breast button locked.png"
            hovered Show("her_tooltip", input_text="Cannot be used in introduction", x_pos = 0.15, y_pos = 0.23)
            action NullAction()
        unhovered Hide("her_tooltip")
        

screen rub_both_breasts_button():
    python:
        increase_arousal = str(rubBothBreastArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 7:
                idle "images/buttons/both breasts button.png"
                hover "images/buttons/both breasts button hover.png"
                hovered Show("her_tooltip", input_text = f"Rub both of your breasts increasing your arousal level by " + increase_arousal +  ".", x_pos = 0.15, y_pos = 0.33)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("rub_both_breasts_label")]
            else:
                idle "images/buttons/both breasts button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 7 you have [pc.stamina]", x_pos = 0.15, y_pos = 0.33)
                action NullAction()
        else:
            idle "images/buttons/both breasts button locked.png"
            hovered Show("her_tooltip", input_text="Cannot be used in introduction", x_pos = 0.15, y_pos = 0.33)
            action NullAction()        
        unhovered Hide("her_tooltip")

screen pinch_left_nipple_button():
    python:
        increase_arousal = str(pinchNippleArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 5:
                idle "images/buttons/left nipple button.png"
                hover "images/buttons/left nipple button hover.png"
                hovered Show("her_tooltip", input_text = f"Pinch your left nipple increasing your arousal level by " + increase_arousal + ".", x_pos = 0.15, y_pos = 0.43)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("pinch_left_nipple_label")]
            else:
                idle "images/buttons/left nipple button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 5 you have [pc.stamina]", x_pos = 0.15, y_pos = 0.43)
                action NullAction()
        else:
            idle "images/buttons/left nipple button locked.png"
            hovered Show("her_tooltip", input_text="Cannot be used in introduction",x_pos = 0.15, y_pos = 0.43)
            action NullAction()
        unhovered Hide("her_tooltip")

screen pinch_right_nipple_button():
    python:
        increase_arousal = str(pinchNippleArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.6
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 5:
                idle "images/buttons/right nipple button.png"
                hover "images/buttons/right nipple button hover.png"
                hovered Show("her_tooltip", input_text = f"Pinch your right nipple increasing your arousal level by " + increase_arousal + ".", x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("pinch_right_nipple_label")]
            else:
                idle "images/buttons/right nipple button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 5 you have [pc.stamina]", x_pos = 0.15, y_pos = 0.53)
                action NullAction()
        else:
            idle "images/buttons/right nipple button locked.png"
            hovered Show("her_tooltip", input_text="Cannot be used in introduction",x_pos = 0.15, y_pos = 0.53)
            action NullAction()
        unhovered Hide("her_tooltip")

screen pinch_both_nipples_button():
    python:
        increase_arousal = str(pinchBothNippleArousalGainGlobal())
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_breast_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.7
        focus_mask True
        if activate_buttons == True:
            if pc.stamina >= 7:
                idle "images/buttons/both nipples button.png"
                hover "images/buttons/both nipples button hover.png"
                hovered Show("her_tooltip", input_text = f"Pinch both of your nipples increasing your arousal level by " + increase_arousal + ".",x_pos = 0.15, y_pos = 0.63)
                action [Hide("her_tooltip"), Hide("breast_actions_select_screen"), Jump("pinch_both_nipple_label")]
            else:
                idle "images/buttons/both nipples button locked.png"
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action, requires 7 you have [pc.stamina]",x_pos = 0.15, y_pos = 0.63)
        else:
            idle "images/buttons/both nipples button locked.png"
            hovered Show("her_tooltip", input_text="Cannot be used in introduction",x_pos = 0.15, y_pos = 0.63)
            action NullAction()
        unhovered Hide("her_tooltip")
