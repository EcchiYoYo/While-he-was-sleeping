init:
    transform her_feet_custom_zoom:
        zoom 0.90

screen your_feet():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.6
        focus_mask True
        if activate_buttons == True:
            idle "images/buttons/her feet button.png"
            hover "images/buttons/her feet button hover.png"
            action [Hide("her_tooltip"), Show("your_feet_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving your bum",x_pos = 0.10, y_pos = 0.53)
        else:
            idle "images/buttons/her feet button locked.png"
            hovered Show("her_tooltip", input_text="Locked during introduction",x_pos = 0.10, y_pos = 0.53)
            action NullAction()
        unhovered Hide("her_tooltip")


screen your_feet_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "images/Backgrounds/blank background.png"
        action [Hide("your_feet_actions_select_screen"), Hide("her_tooltip")]
    use feet_rub_chest_button()
    use feet_suck_toes_button()
    use rub_his_balls_with_your_feet_button()
    use footjob_button()

screen feet_rub_chest_button():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.3
        focus_mask True
        idle "images/buttons/rub chest with feet button.png"
        hover "images/buttons/rub chest with feet button hover.png"
        hovered Show("her_tooltip", input_text ="Caress his chest with your foot", x_pos = 0.15, y_pos = 0.23)
        unhovered Hide("her_tooltip")
        #
        # 
        #
        action NullAction()

screen feet_suck_toes_button():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.4
        focus_mask True
        idle "images/buttons/suck toes button.png"
        hover "images/buttons/suck toes button hover.png"
        hovered Show("her_tooltip", input_text = "Have him suck your toes", x_pos = 0.15, y_pos = 0.33)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen rub_his_balls_with_your_feet_button():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.5
        focus_mask True
        idle "images/buttons/rub balls with feet button.png"
        hover "images/buttons/rub balls with feet button hover.png"
        hovered Show("her_tooltip", input_text = "Gently caress his balls with your foot", x_pos = 0.15, y_pos = 0.43)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()

screen footjob_button():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.6
        focus_mask True
        idle "images/buttons/footjob button.png"
        hover "images/buttons/footjob button hover.png"
        hovered Show("her_tooltip", input_text = "Masturbate him with your foot", x_pos = 0.15, y_pos = 0.53)
        unhovered Hide("her_tooltip")
        #
        #
        #
        action NullAction()
