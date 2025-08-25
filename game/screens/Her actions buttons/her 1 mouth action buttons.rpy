init:
    transform her_mouth_custom_zoom:
        zoom 0.90

screen your_mouth():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.2
        focus_mask True
        if activate_buttons == True:
            idle "images/buttons/her mouth button.png"
            hover "images/buttons/her mouth button hover.png"
            action [Hide("her_tooltip"), Show("mouth_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving your mouth",x_pos = 0.10, y_pos = 0.13)
        else:
            idle "images/buttons/her mouth button locked.png"
            hovered Show("her_tooltip", input_text="Locked during introduction",x_pos = 0.10, y_pos = 0.13)
            action NullAction()
        unhovered Hide("her_tooltip")

screen mouth_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("mouth_actions_select_screen"), Hide("her_tooltip")]
    use kiss_button()
    use deep_kiss_button()
    use suck_your_fingers_button()
    use suck_juices_button()
    use clean_cum_from_him_button()

screen kiss_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        if pc.stamina >= 3:
            idle "images/buttons/kiss button.png"
            hover "images/buttons/kiss button hover.png"
            hovered Show("her_tooltip", input_text="Lightly kiss him",x_pos = 0.15, y_pos = 0.13)
            action [Hide("her_tooltip"), Jump("her_mouth_kiss_label")]
        else:
            hovered Show("her_tooltip", input_text="Not enough stamina to do that, consider ending the night ({color='#E32636'}Make sure you hide any evidence left on his body)",x_pos = 0.15, y_pos = 0.23)
            action NullLAction()
            idle "images/buttons/kiss button locked.png"
        unhovered Hide("her_tooltip")

screen deep_kiss_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        if pc.stamina >= 3:
            idle "images/buttons/deep kiss button.png"
            hover "images/buttons/deep kiss button hover.png"
            hovered Show("her_tooltip", input_text="Kiss him using plenty of tongue action",x_pos = 0.15, y_pos = 0.23)
            action [Hide("her_tooltip"), Jump("her_mouth_deep_kiss_label")]
        else:                
            hovered Show("her_tooltip", input_text="Not enough stamina to do that, consider ending the night ({color='#E3263'}Make sure you hide any evidence left on his body)",x_pos = 0.15, y_pos = 0.23)
            action NullAction()
            idle "images/buttons/deep kiss button locked.png"
        unhovered Hide("her_tooltip")

screen suck_your_fingers_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if pc.finger_state == "dry":
            idle "images/buttons/suck her fingers button.png"
            hover "images/buttons/suck her fingers button hover.png"
            hovered Show("her_tooltip", input_text="Suck your fingers to get them moist",x_pos = 0.15, y_pos = 0.33)
            action [Hide("her_tooltip"), Jump("her_mouth_suck_your_fingers_label")]
        else:
            if pc.finger_state == "saliva":
                hovered Show("her_tooltip", input_text="Your fingers are already coated in saliva",x_pos = 0.15, y_pos = 0.33)
            elif pc.finger_state == "girl cum":
                hovered Show("her_tooltip", input_text="Your fingers are slick with girl cum",x_pos = 0.15, y_pos = 0.33)
            else:
                hovered Show("her_tooltip", input_text="Your fingers are slimy with cum",x_pos = 0.15, y_pos = 0.33)
            idle "images/buttons/suck her fingers button locked.png"
            action NullAction() # These have no action required here this button is to moisten dry fingers only
        unhovered Hide("her_tooltip")
        
screen suck_juices_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        focus_mask True
        if pc.finger_state == "dry" or pc.finger_state == "saliva":
            action NullAction()
            idle "images/buttons/suck her juices button locked.png"
            if pc.finger_state == "dry":
                hovered Show("her_tooltip", input_text="Your fingers are dry as a bone, play with some fluids to moisten them up",x_pos = 0.15, y_pos = 0.43)
            else:
                hovered Show("her_tooltip", input_text="Your fingers are coated with saliva, no need to make them moist",x_pos = 0.15, y_pos = 0.43)
        else:
            idle "images/buttons/suck her juices button.png"
            hover "images/buttons/suck her juices hover.png"
            if pc.finger_state == "girl cum":
                hovered Show("her_tooltip", input_text="Suck the girl cum from your fingers",x_pos = 0.15, y_pos = 0.43)
            else:
                hovered Show("her_tooltip", input_text="Consume the slimy cum coating your fingers",x_pos = 0.15, y_pos = 0.43)
            action [Hide("her_tooltip", Jump("her_mouth_suck_juices_from_fingers_label"))]
        unhovered Hide("her_tooltip")

screen clean_cum_from_him_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.6
        focus_mask True
        # no stamina requirement for these actions, maybe add an upgrade that cleans all cum and girl cum from his body (with a toggle in the options screen)
        if man.face_state == "girl cum" or man.face_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.face_state == "girl cum":
                hovered Show("her_tooltip", input_text="Slurp your girl cum from his face, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_girl_cum_from_face_label")]
            else:
                hovered Show("her_tooltip", input_text="Slurp up the cum covering his face, hiding the evidence it was ever there",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_cum_from_face_label")]
        elif man.chest_state == "girl cum" or man.chest_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.chest_state == "girl cum":
                hovered Show("her_tooltip", input_text="Lap up your girl cum from his chest, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_girl_cum_from_chest_label")]
            else:
                hovered Show("her_tooltip", input_text="Lap up the cum coating his chest, hiding the evidence it was ever there",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_cum_from_chest_label")]
        elif man.stomach_state == "girl cum" or man.stomach_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images.buttons/clean cum from him button hover.png"
            if man.stomach_state == "girl cum":
                hovered Show("her_tooltip", input_text="Lick the girl cum from his stomach, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip", Jump("her_mouth_clean_girl_cum_stomach_label"))]
            else:
                hovered Show("her_tooltip", input_text="Lick the cum from his stomach, hiding the evidence it was ever there",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip", Jump("her_mouth_clean_cum_stomach_label"))]
        elif man.finger_state == "girl cum" or man.finger_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.finger_state == "girl cum":
                hovered Show("her_tooltip", input_text="Suck the girl cum from his fingers, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_girl_cum_fingers_label")]
            else:
                hovered Show("her_tooltip", input_text="Suck away the cum coating his fingers, hiding the evidence it was ever there",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_cum_fingers_label")]
        elif man.thigh_state == "girl cum" or man.thigh_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.thigh_state == "girl cum":
                hovered Show("her_tooltip", input_text="Lick his thighs clean of your girl cum, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_girl_cum_thighs_label")]
            else:
                hovered Show("her_tooltip", input_text="Lick his thighs clean of the cum coating them, hiding the evidence it was ever there",x_pos = 0.15, y_pos = 0.53)
                action [Hide("her_tooltip"), Jump("her_mouth_clean_cum_thighs_label")]
        elif man.ass_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            hovered Show("her_tooltip", input_text="Give him a rimjob making sure to suck out all your cum, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
            action [Hide("her_tooltip"), Jump("her_mouth_cum_ass_label")]
        else:
            idle "images/buttons/clean cum from him button locked.png"
            hovered Show("her_tooltip", input_text="The only fluids (if any) left on him is saliva, it`s like you were never here",x_pos = 0.15, y_pos = 0.53)
            action NullAction()
        unhovered Hide("her_tooltip")
