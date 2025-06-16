init:
    transform chest_custom_zoom:
        zoom 0.90

screen his_chest():
    imagebutton:
        at chest_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.3
        focus_mask True
        if intro_3_completed == False:
            if intro_2_completed == False:
                idle "images/buttons/his chest button locked.png"
                hovered Show("his_tooltip", input_text="You need to select your chest not his",x_pos = 0.70, y_pos = 0.23)
                action NullAction()
            else:
                idle "images/buttons/his chest button.png"
                hover "images/buttons/his chest button hover.png"
                action [Hide("his_tooltip"), Show("chest_actions_select_screen")]
                hovered Show("his_tooltip", input_text="Perform an action involving his chest",x_pos = 0.70, y_pos = 0.23)
        else:
            idle "images/buttons/his chest button locked.png"
            hovered Show("his_tooltip", input_text="You need to select his chest not yours",x_pos = 0.70, y_pos = 0.23)
            action NullAction()
        unhovered Hide("his_tooltip")


screen chest_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("chest_actions_select_screen"), Hide("his_tooltip")]
    use rub_his_chest_button()
    use rub_his_nipples_button()
    use rub_his_nipples_with_your_foot_button()
    use rub_your_pussy_along_his_chest_button()

screen rub_his_chest_button():
    #
    # some calculation for amount of experience and arousal gained
    #
    imagebutton:
        at chest_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.2
        focus_mask True
        idle "images/buttons/rub his chest button.png"
        hover "images/buttons/rub his chest button hover.png"
        hovered Show("his_tooltip", input_text="Run your fingers through his chest hair",x_pos = 0.65, y_pos = 0.13)
        unhovered Hide("his_tooltip")
        if activate_buttons == True:
            action NullAction()
        else:
            action [Hide("his_tooltip"), Hide("chest_actions_select_screen"), Jump("rub_chest_introduction_scene")]

screen rub_his_nipples_button():
    text "stuff and things"

screen rub_his_nipples_with_your_foot_button():
    text "stuff and things"

screen rub_your_pussy_along_his_chest_button():
    text "stuff and things"
    