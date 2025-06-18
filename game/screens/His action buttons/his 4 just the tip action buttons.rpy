init:
    transform his_just_the_tip_custom_zoom:
        zoom 0.90

screen his_just_the_tip_screen():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.965
        ypos 0.5
        focus_mask True
        if intro_3_completed == True:
            idle "images/buttons/his just the tip button.png"
            hover "images/buttons/his just the tip button hover.png"
            hovered Show("his_tooltip", input_text = "Perform actions involving the tip of his cock", x_pos = 0.88,  y_pos = 0.43)
            #
            #
            #
            action [Hide("his_tooltip"), Show("his_just_the_tip_actions_select_screen")]
        else:
            idle "images/buttons/his just the tip button locked.png"
            hovered Show("his_tooltip", input_text = "Locked during introduction", x_pos = 0.88, y_pos = 0.43)
            action NullAction()
    
screen his_just_the_tip_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "/images/Backgrounds/blank background.png"
        action [Hide("his_just_the_tip_actions_select_screen"), Hide("his_tooltip")]
    use rub_the_tip_of_his_cock_button()
    use lick_the_tip_of_his_cock_button()
    use suck_the_tip_of_his_cock_button()
    use just_his_tip_vaginal_button()
    use just_his_tip_anal_button()
    
screen rub_the_tip_of_his_cock_button():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.2
        focus_mask True
        idle "images/buttons/rub his tip button.png"
        hover "images/buttons/rub his tip button hover.png"
        hovered Show("his_tooltip", input_text = "Rub the tip of his cock", x_pos = 0.83, y_pos = 0.13)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen lick_the_tip_of_his_cock_button():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.3
        focus_mask True
        idle "images/buttons/lick his tip button.png"
        hover "images/buttons/lick his tip button hover.png"
        hovered Show("his_tooltip", input_text = "Lick the tip of his cock", x_pos = 0.83, y_pos = 0.23)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen suck_the_tip_of_his_cock_button():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.4
        focus_mask True
        idle "images/buttons/suck his tip button.png"
        hover "images/buttons/suck his tip button hover.png"
        hovered Show("his_tooltip", input_text = "Gently suck the tip of his cock", x_pos = 0.83, y_pos = 0.33)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen just_his_tip_vaginal_button():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.5
        focus_mask True
        idle "images/buttons/just his tip vaginal button.png"
        hover "images/buttons/just his tip vaginal button hover.png"
        hovered Show("his_tooltip", input_text = "Impale yourself with just his tip, vaginal", x_pos = 0.83, y_pos = 0.43)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()

screen just_his_tip_anal_button():
    imagebutton:
        at his_just_the_tip_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.905
        ypos 0.6
        focus_mask True
        idle "images/buttons/just his tip anal button.png"
        hover "images/buttons/just his tip anal button hover.png"
        hovered Show("his_tooltip", input_text = "Impale yourself with just his tip, anal", x_pos = 0.83, y_pos = 0.53)
        unhovered Hide("his_tooltip")
        #
        #
        #
        action NullAction()
