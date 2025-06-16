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
    use suck_your_juices_button()
    use clean_cum_from_him_button()

screen kiss_button():
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        idle "images/buttons/kiss button.png"
        hover "images/buttons/kiss button hover.png"
        hovered Show("her_tooltip", input_text="Lightly kiss him",x_pos = 0.15, y_pos = 0.13)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen deep_kiss_button():
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        idle "images/buttons/kiss button.png"
        hover "images/buttons/kiss button hover.png"
        hovered Show("her_tooltip", input_text="Kiss him using plenty of tongue action",x_pos = 0.15, y_pos = 0.23)
        unhovered Hide("her_tooltip")
        #
        #
        #
        #
        action NullAction()

screen suck_your_fingers_button():
    #
    # some calculations for amount of experience and arousal gained
    #
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if pc.finger_state != "dry": # add stamina check for action here with an and check
            idle "images/buttons/suck her fingers button.png"
            hover "images/buttons/suck her fingers button hover.png"
            hovered Show("her_tooltip", input_text="Suck your fingers to get them moist",x_pos = 0.15, y_pos = 0.33)
            #
            #
            #
            action NullAction()
        else:
            if pc.finger_state == "dry:":
                hovered Show("her_tooltip", input_text="Not enough stamina to do that",x_pos = 0.15, y_pos = 0.33)
            else:
                if pc.finger_state == "saliva":
                    hovered Show("her_tooltip", input_text="Your fingers are already coated in saliva",x_pos = 0.15, y_pos = 0.33)
                elif pc.finger_state == "girl cum":
                    hovered Show("her_tooltip", input_text="Your fingers are slick with girl cum",x_pos = 0.15, y_pos = 0.33)
                else:
                    hovered Show("her_tooltip", input_text="Your fingers are slimy with cum",x_pos = 0.15, y_pos = 0.33)
            idle "images/buttons/suck her fingers button locked.png"
            unhovered Hide("her_tooltip")
            action NullAction()
        unhovered Hide("her_tooltip")
        

screen suck_your_juices_button():
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
            #
            #
            #
            action NullAction()
            if pc.finger_state == "girl cum":
                hovered Show("her_tooltip", input_text="Suck the girl cum from your fingers",x_pos = 0.15, y_pos = 0.43)
            else:
                hovered Show("her_tooltip", input_text="Consume the slimy cum coating your fingers",x_pos = 0.15, y_pos = 0.43)
        unhovered Hide("her_tooltip")

screen clean_cum_from_him_button():
    imagebutton:
        at her_mouth_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.6
        focus_mask True
        if man.face_state == "girl cum" or man.face_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.face_state == "girl cum":
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Slurp your girl cum from his face, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
            else:
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Slurp up the cum covering his face, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
        elif man.chest_state == "girl cum" or man.chest_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.chest_state == "girl cum":
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lap up your girl cum from his chest, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
            else:
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lap up the cum coating his chest, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
        elif man.stomach_state == "girl cum" or man.stomach_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images.buttons/clean cum from him button hover.png"
            if man.stomach_state == "girl cum":
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lick the girl cum from his stomach, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
            else:
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lick the cum from his stomach, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
        elif man.finger_state == "girl cum" or man.finger_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.finger_state == "girl cum":
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Suck the girl cum from his fingers, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
            else:
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Suck away the cum coating his fingers, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
        elif man.thigh_state == "girl cum" or man.thigh_state == "cum":
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            if man.thigh_state == "girl cum":
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lick his thighs clean of your girl cum, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
            else:
                #
                # some calculations for gains
                #
                #
                hovered Show("her_tooltip", input_text="Lick his thighs clean of the cum coating them, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
                #
                #
                #
                action NullAction()
        elif man.ass_state == "cum":
            #
            # some calculations for gains
            #
            #
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            hovered Show("her_tooltip", input_text="Give him a rimjob making sure to suck out all your cum, hiding the evidence you were ever here",x_pos = 0.15, y_pos = 0.53)
            #
            #
            #
            action NullAction()
        else:
            #
            # some calculations for gains
            #
            #
            idle "images/buttons/clean cum from him button locked.png"
            hovered Show("her_tooltip", input_text="The only fluids (if any) left on him is saliva, it`s like you were never here",x_pos = 0.15, y_pos = 0.53)
            action NullAction()
        unhovered Hide("her_tooltip")
