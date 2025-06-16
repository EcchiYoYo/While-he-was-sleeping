init:
    transform her_just_the_tip_custom_zoom:
        zoom 0.90

screen your_just_the_tip():
    imagebutton:
        at her_feet_custom_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.08
        ypos 0.6
        focus_mask True
        if activate_buttons == True and (pc.player_type == "trans_male" or pc.player_type == "futa" or pc.player_type == "gay"):
            idle "images/buttons/her feet button.png"
            hover "images/buttons/her feet button hover.png"
            action [Hide("her_tooltip"), Show("your_just_the_tip_actions_select_screen")]
            hovered Show("her_tooltip", input_text="Perform an action involving the tip of your cock",x_pos = 0.10, y_pos = 0.53)
        else:
            idle "images/buttons/nothing button locked.png"
            if activate_buttons == False and (pc.player_type == "trans_male" or pc.player_type == "futa" or pc.player_type == "gay"):
                hovered Show("her_tooltip", input_text="Locked during introduction",x_pos = 0.10, y_pos = 0.53)
            else:
                hovered Show("her_tooltip", input_text = "Not available while playing [pc.player_type] pack",x_pos = 0.10, y_pos = 0.53)
            action NullAction()
        unhovered Hide("her_tooltip")

screen your_just_the_tip_actions_select_screen():
    imagebutton:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
        idle "images/Backgrounds/blank background.png"
        action [Hide("your_just_the_tip_actions_select_screen"), Hide("her_tooltip")]
