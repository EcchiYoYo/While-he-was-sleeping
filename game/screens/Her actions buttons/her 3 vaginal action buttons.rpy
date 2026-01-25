screen your_pussy():
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.4
        focus_mask True
        if activate_buttons == True:
            idle "images/buttons/her pussy button.png"
            hover "images/buttons/her pussy button hover.png"
            action [Hide("her_tooltip"), Show("pussy_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving your pussy",x_pos = 0.10, y_pos = 0.33)
        else:
            idle "images/buttons/her pussy button locked.png"
            hovered Show("her_tooltip", input_text="Locked during introduction",x_pos = 0.10, y_pos = 0.33)
            action NullAction()
        unhovered Hide("her_tooltip")

screen pussy_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("pussy_actions_select_screen"), Hide("her_tooltip")]
    use rub_pubis_button()
    use rub_inner_thigh_button()
    use rub_outer_pussy_lips_button()
    use massage_clit_button()
    use finger_pussy_button()
    
screen rub_pubis_button():
    python:
        increase_arousal = str(rubPubisArousalGainGlobal())
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        if pc.stamina >= 3:
            idle "images/buttons/pubis button.png"
            hover "images/buttons/pubis button hover.png"
            hovered Show("her_tooltip", input_text = f"Rub your pubis, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.13)
            action [Hide("her_tooltip"), Hide("pussy_actions_select_screen"), Jump("rub_pubis_label")]
        else:
            idle "images/buttons/pubis button locked.png"
            hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 3 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.13)
            action NullAction()
        unhovered Hide("her_tooltip")

screen rub_inner_thigh_button():
    python:
        increase_arousal = str(rubInnerThighArousalGainGlobal())
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        if pc.stamina >= 5:
            idle "images/buttons/inner thigh button.png"
            hover "images/buttons/inner thigh button hover.png"
            hovered Show("her_tooltip", input_text = f"Rub your inner thigh, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.23)
            action [Hide("her_tooltip"), Hide("pussy_actions_select_screen"), Jump("rub_inner_thigh_label")]
        else:
            idle "images/buttons/inner thigh button locked.png"
            hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 5 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.23)
            action NullAction()
        unhovered Hide("her_tooltip")

screen rub_outer_pussy_lips_button():
    python:
        increase_arousal = str(rubOuterPussyLipsArousalGainGlobal())
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if pc.stamina >= 5:
            idle "images/buttons/outer lips button.png"
            hover "images/buttons/outer lips button hover.png"
            hovered Show("her_tooltip", input_text = f"Rub your outer pussy lips, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.33)
            action [Hide("her_tooltip"), Hide("pussy_actions_select_screen"), Jump("rub_outer_pussy_lips_label")]
        else:
            idle "images/buttons/outer lips button locked.png"
            hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 5 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.33)
            action NullAction()
        unhovered Hide("her_tooltip")

screen massage_clit_button():
    python:
        increase_arousal = str(massageClitArousalGainGlobal())
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        focus_mask True
        if pc.finger_state != "dry" and pc.stamina >= 7:
            idle "images/buttons/clit button.png"
            hover "images/buttons/clit button hover.png"
            hovered Show("her_tooltip", input_text = f"Massage your clit, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.43)
            action [Hide("her_tooltip"), Hide("pussy_actions_select_screen"), Jump("massage_clit_label")]
        else:
            idle "images/buttons/clit button locked.png"
            # fingers must have some fluid on to massage clit
            if pc.finger_state == "dry":
                hovered Show("her_tooltip", input_text = "Your fingers must be moist to perform this action, coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.43)
            else:
                hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 7 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.43)
            action NullAction()
        unhovered Hide("her_tooltip")

screen finger_pussy_button():
    python:
        increase_arousal = str(fingerPussyArousalGainGlobal())
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.6
        focus_mask True
        if pc.stamina < 10:
            idle "images/buttons/finger button locked.png"
            hovered Show("her_tooltip", input_text = "Not enough stamina for this action requires 10 you have [pc.stamina], consider ending the night ({color=#E32636}Make sure you hide any evidence left on his body)", x_pos = 0.15, y_pos = 0.53)
            action NullAction()
        # fingers or pussy must be moist to finger self
        elif pc.finger_state == "dry" and pc.vaginal_state == "dry":
            idle "images/buttons/finger button locked.png"
            hovered Show("her_tooltip", input_text = "Your fingers or pussy must be moist to perform this action, raise arousal to increase pussy moistness or coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.53)
            action NullAction()
        else:
            idle "images/buttons/finger button.png"
            hover "images/buttons/finger button hover.png"
            hovered Show("her_tooltip", input_text = f"Vigorously finger yourself, increasing your arousal by {{color=#FFB0F2}}{increase_arousal}", x_pos = 0.15, y_pos = 0.53)
            action [Hide("her_tooltip"), Hide("pussy_actions_select_screen"), Jump("finger_pussy_label")]
        unhovered Hide("her_tooltip")
