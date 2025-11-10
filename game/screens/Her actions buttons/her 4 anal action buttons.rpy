init:
    transform her_ass_custom_zoom:
        zoom 0.90

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
    use finger_her_arse_his_fingers_button()    

screen rub_arse_her_button():
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        idle "images/buttons/rub her ass button.png"
        hover "images/buttons/rub her ass button hover.png"
        hovered Show("her_tooltip", input_text = "Gently massage your buttocks", x_pos = 0.15, y_pos = 0.23)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen finger_her_arse_her_fingers_button():
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        if pc.finger_state != "dry":
            idle "images/buttons/finger her ass button.png"
            hover "images/buttons/finger her ass button hover.png"
            hovered Show("her_tooltip", input_text = "Finger your backdoor", x_pos = 0.15, y_pos = 0.33)
        else:
            idle "images/buttons/finger her ass button locked.png"
            hovered Show("her_tooltip", input_text = "Your fingers must be moist to perform this action, coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.33)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen finger_her_arse_his_fingers_button():
    imagebutton:
        at her_ass_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        if man.finger_state != "dry":
            idle "images/buttons/finger her ass his fingers button.png"
            hover "images/buttons/finger her ass his fingers button hover.png"
            hovered Show("her_tooltip", input_text = "Finger your backdoor using his fingers", x_pos = 0.15, y_pos = 0.43)
        else:
            idle "images/buttons/finger her ass his fingers button locked.png"
            hovered Show("her_tooltip", input_text = "His fingers must be moist to perform this action, coat his fingers in some fluid", x_pos = 0.15, y_pos = 0.43)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()
    