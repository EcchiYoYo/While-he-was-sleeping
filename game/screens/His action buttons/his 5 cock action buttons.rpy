init:
    transform his_cock_custom_zoom:
        zoom 0.90

screen his_cock_screen():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.6
        focus_mask True
        if intro_3_completed == True:
            idle "images/buttons/his cock button.png"
            hover "images/buttons/his cock button hover.png"
            hovered Show("his_tooltip", input_text = "Perform actions involving the tip of his cock", x_pos = 0.88,  y_pos = 0.53)
            #
            #
            #
            action [Hide("his_tooltip"), Show("his_cock_actions_select_screen")]
        else:
            idle "images/buttons/his cock button locked.png"
            hovered Show("his_tooltip", input_text = "Locked during introduction", x_pos = 0.88, y_pos = 0.53)
            #
            #
            #
            action NullAction()
        unhovered Hide("his_tooltip")

screen his_cock_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("his_cock_actions_select_screen"), Hide("his_tooltip")]
    use fondle_his_balls_button()
    use masturbate_his_cock_button()
    use blowjob_his_cock_button()
    use vaginal_sex_button()
    use anal_sex_his_cock_button()

screen fondle_his_balls_button():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.2
        focus_mask True
        idle "images/buttons/rub his balls button.png"
        hover "images/buttons/rub his balls button hover.png"
        hovered Show("his_tooltip", input_text = "Play with his balls", x_pos = 0.83, y_pos = 0.13)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen masturbate_his_cock_button():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.3
        focus_mask True
        idle "images/buttons/masturbate his cock button.png"
        hover "images/buttons/masturbate his cock button hover.png"
        hovered Show("his_tooltip", input_text = "Give him a handjob", x_pos = 0.83, y_pos = 0.23)
        unhovered Hide("his_tooltip")
        #
        #
        #
        #
        action NullAction()

screen blowjob_his_cock_button():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.4
        focus_mask True
        idle "images/buttons/blowjob his cock button.png"
        hover "images/buttons/blowjob his cock button hover.png"
        hovered Show("his_tooltip", input_text = "Suck his cock", x_pos = 0.83, y_pos = 0.33)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen vaginal_sex_button():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.5
        focus_mask True
        idle "images/buttons/vaginal sex button.png"
        hover "images/buttons/vaginal sex button hover.png"
        hovered Show("his_tooltip", input_text = "Ride him balls deep, vaginal", x_pos = 0.83, y_pos = 0.43)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()
    
screen anal_sex_his_cock_button():
    imagebutton:
        at his_cock_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.6
        focus_mask True
        idle "images/buttons/anal sex his cock button.png"
        hover "images/buttons/anal sex his cock button hover.png"
        hovered Show("his_tooltip", input_text = "Ride him balls deep, anal", x_pos = 0.83, y_pos = 0.53)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()
