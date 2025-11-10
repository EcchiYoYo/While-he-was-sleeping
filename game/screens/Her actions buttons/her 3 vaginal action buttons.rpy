init:
    transform pussy_custom_zoom:
        zoom 0.90

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
    #
    # Add some calculations here
    #
    #
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        idle "images/buttons/pubis button.png"
        hover "images/buttons/pubis button hover.png"
        hovered Show("her_tooltip", input_text="Gently massage your pubis",x_pos = 0.15, y_pos = 0.13)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen rub_inner_thigh_button():
    #
    #
    # Add some calculations here
    #
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        idle "images/buttons/inner thigh button.png"
        hover "images/buttons/inner thigh button hover.png"
        hovered Show("her_tooltip", input_text="Gently rub your inner thigh", x_pos = 0.15, y_pos = 0.23)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen rub_outer_pussy_lips_button():
    #
    # Add some calculations here
    #
    #
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        idle "images/buttons/outer lips button.png"
        hover "images/buttons/outer lips button hover.png"
        hovered Show("her_tooltip", input_text="Rub your outer pussy lips", x_pos = 0.15, y_pos= 0.33)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen massage_clit_button():
    #
    # Add some calculations here
    #
    #
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        focus_mask True
        if pc.finger_state != "dry":
            idle "images/buttons/clit button.png"
            hover "images/buttons/clit button hover.png"
            hovered Show("her_tooltip", input_text="Massage your clit", x_pos = 0.15, ypos = 0.43)
        else:
            idle "images/buttons/clit button locked.png"
            hovered Show("her_tooltip", input_text="Your fingers must be moist to perform this action, coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.43)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen finger_pussy_button():
    #
    # add some calculations here
    #
    #
    imagebutton:
        at pussy_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        if pc.finger_state == "dry" and pc.vaginal_state == "dry":
            idle "images/buttons/finger button locked.png"
            hovered Show("her_tooltip", input_text = "Your fingers or pussy must be moist to perform this action, raise arousal to increase pussy moistness or coat your fingers in some fluid", x_pos = 0.15, y_pos = 0.33)
        else:
            idle "images/buttons/finger button.png"
            hover "images/buttons/finger button hover.png"
            hovered Show("her_tooltip", input_text = "Vigorously finger yourself", x_pos = 0.15, y_pos = 0.53)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()
