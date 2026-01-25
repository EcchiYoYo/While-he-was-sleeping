screen your_arse():
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.5
        focus_mask True
        if activate_buttons == True:
            idle "images/buttons/her ass button.png"
            hover "images/buttons/her ass button hover.png"
            action [Hide("her_tooltip"), Show("your_arse_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving your bum",x_pos = 0.10, y_pos = 0.43)
        else:
            idle "images/buttons/her ass button locked.png"
            hovered Show("her_tooltip", input_text="Locked during introduction",x_pos = 0.10, y_pos = 0.43)
            action NullAction()
        unhovered Hide("her_tooltip")

screen your_arse_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("your_arse_actions_select_screen"), Hide("her_tooltip")]
    use rub_arse_her_button()
    use finger_her_arse_her_fingers_button()  

screen rub_arse_her_button():
    python:
        increase_arousal = str(rubBumArousalGainGlobal())
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        if pc.stamina >= 5:
            idle "images/buttons/rub her ass button.png"
            hover "images/buttons/rub her ass button hover.png"
            hovered Show("her_tooltip", input_text = f"You gently massage your buttocks, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.23)
            action [Hide("her_tooltip"), Hide("your_arse_actions_select_screen"), Jump("rub_bum_label")]
        else:
            idle "images/buttons/rub her ass button locked.png"
            hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 5 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.23)
            action NullAction()
        unhovered Hide("her_tooltip")

screen finger_her_arse_her_fingers_button():
    python:
        increase_arousal = str(fingerArseArousalGainGlobal())
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if pc.finger_state != "dry" and pc.stamina >= 5:
            idle "images/buttons/finger her ass button.png"
            hover "images/buttons/finger her ass button hover.png"
            hovered Show("her_tooltip", input_text = f"Finger your backdoor, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.33)
            action [Hide("her_tooltip"), Hide("your_arse_actions_select_screen"), Jump("finger_arse_label")]
        else:
            idle "images/buttons/finger her ass button locked.png"
            if pc.finger_state == "dry":
                hovered Show("her_tooltip", input_text = "Your fingers must be moist to perform this action, coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.33)
            else:
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 5 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.33)
            action NullAction()
        unhovered Hide("her_tooltip")
