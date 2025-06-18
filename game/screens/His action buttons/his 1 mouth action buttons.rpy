init:
    transform him_face_custom_zoom:
        zoom 0.90

screen him_face():
    imagebutton:
        at him_face_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.2
        focus_mask True
        if activate_buttons == True:
            idle "images/buttons/his face button.png"
            hover "images/buttons/his face button hover.png"
            action [Hide("his_tooltip"), Show("his_mouth_actions_select_screen")]
            hovered Show("his_tooltip", input_text="Perform an action involving your bum",x_pos = 0.88, y_pos = 0.13)
        else:
            idle "images/buttons/his face button locked.png"
            hovered Show("his_tooltip", input_text="Locked during introduction",x_pos = 0.88, y_pos = 0.13)
            action NullAction()
        unhovered Hide("his_tooltip")

screen his_mouth_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("his_mouth_actions_select_screen"), Hide("his_tooltip")]
    use suck_his_fingers_button()
    use he_sucks_her_fingers_button()
    use ride_his_face_button()

screen suck_his_fingers_button():
    imagebutton:
        at him_face_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.3
        focus_mask True
        if man.finger_state != "dry": # add stamina check for action here
            idle "images/buttons/suck his fingers button.png"
            hover "images/buttons/suck his finger button hover.png"
            hovered Show("his_tooltip", input_text = "Suck his fingers to get them moist", x_pos = 0.83, y_pos = 0.23)
            #
            #
            #
            action NullAction()
        else:
            if man.finger_state == "dry":
                hovered Show("his_tooltip", input_text = "Not enough stamina to do that", x_pos = 0.83, y_pos = 0.23)
            else:
                if man.finger_state == "saliva":
                    hovered Show("his_tooltip", input_text = "His fingers are already coated in saliva", x_pos = 0.83, y_pos = 0.23)
                elif man.finger_state == "girl cum":
                    hovered Show("his_tooltip", input_text = "His fingers are slick with girl cum", x_pos = 0.83, y_pos = 0.23)
                else:
                    hovered Show("his_tooltip", input_text = "His fingers are slimy with cum", x_pos = 0.83, y_pos = 0.23)
            idle "images/buttons/suck his fingers button locked.png"
            action NullAction()
        unhovered Hide("his_tooltip")

screen he_sucks_her_fingers_button():
    imagebutton:
        at him_face_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.4
        focus_mask True
        if pc.finger_state == "dry" or pc.finger_state == "saliva": # add or stamina below x check, put first two arguments in brackets
            idle "images/buttons/he sucks her fingers button locked.png"
            hovered Show("his_tooltip", input_text = "Requires cum or girl cum on your fingers to perform this action")
            #
            #
            #
            action NullAction()
        else:
            idle "images/buttons/he sucks her fingers button.png"
            hover "images/buttons/he sucks her fingers button hover.png"
            if pc.finger_state == "girl cum":
                hovered Show("his_tooltip", input_text = "Make him suck your juices from his fingers", x_pos = 0.83, y_pos = 0.33)
                #
                #
                #
                action NullAction()
            else:
                hovered Show("his_tooltip", input_text = "Make him suck his own slimy cum from his fingers", x_pos = 0.83, y_pos = 0.33)
                #
                #
                #
                action NullAction()
        unhovered Hide("his_tooltip")

screen ride_his_face_button():
    imagebutton:
        at him_face_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.5
        focus_mask True
        idle "images/buttons/ride his face button.png"
        hover "images/buttons/ride his face button hover.png"
        hovered Show("his_tooltip", input_text = "Ride his face grinding your pussy against his mouth", x_pos = 0.83, y_pos = 0.43)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()
