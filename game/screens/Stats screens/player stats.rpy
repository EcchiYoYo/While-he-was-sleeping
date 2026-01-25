screen player_stats_screen_button():
    imagebutton:
        at global_button_size_zoom
        xanchor 1.0
        yanchor 1.0
        xpos 0.8
        ypos 0.15
        focus_mask True
        idle "images/buttons/player button.png"
        hover "images/buttons/player button hover.png"
        hovered Show("her_tooltip", input_text = "Show your stats", x_pos = 0.85, y_pos = 0.18)
        unhovered Hide("her_tooltip")
        action [Hide("her_tooltip"), Jump("player_stats_screen_label")]

label player_stats_screen_label():
    call screen player_stats_screen

screen player_stats_screen():
    image "images/Stats page/player stats.png"
    add "images/Stats page/player standard.png"
    add "images/stats page/player top open.png"
    add "player_stats_page_eyes"
    text "{color=#000000}Stamina: [pc.stamina]/[pc.max_stamina]" xpos 0.02 ypos 0.11
    text "{color=#000000}Arousal: [pc.arousal]/150" xpos 0.02 ypos 0.17
    text "{color=#000000}Coins: [upgrades.upgrade_coins]" xpos 0.02 ypos 0.23
    use hand_stats_button()
    use mouth_stats_button()
    #use breast_stats_button()
    use pussy_stats_button()
    use arse_stats_button()
    use foot_stats_button()



    textbutton "Close":
        xalign 0.5
        ypos 0.9
        action [Hide("player_stats_screen"), Jump("players_room")]

screen mouth_stats_button:
    python:
        mouth_exp_for_level = pc.mouth_exp_for_level - pc.current_mouth_exp
    imagebutton:
        xpos 0.485
        ypos 0.149
        idle "images/stats page/mouth label.png"
        #hover "images/stats page/mouth label.png"
        hovered Show("her_tooltip", input_text = f"Current mouth level: {pc.mouth_level}\nExperience needed for next level: {mouth_exp_for_level}", x_pos = 0.61, y_pos = 0.24)
        unhovered Hide("her_tooltip")
        action NullAction()

screen hand_stats_button:
    python:
        hand_exp_for_level = pc.hand_exp_for_level - pc.current_hand_exp
    imagebutton:
        xpos 0.2
        ypos 0.53
        #focus_mask True
        idle "images/Stats page/hand label.png"
        #hover "images/stats page/hand label.png"
        hovered Show("her_tooltip", input_text = f"Current hand level: {pc.hand_level}\nExperience needed for next level: {hand_exp_for_level}", x_pos = 0.2, y_pos = 0.42)
        unhovered Hide("her_tooltip")
        action NullAction()

screen pussy_stats_button:
    python:
        vaginal_exp_for_level = pc.vaginal_exp_for_level - pc.current_vaginal_exp
    imagebutton:
        xpos 0.18
        ypos 0.75
        idle "images/stats page/pussy label.png"
        if pc.vaginal_virgin:
            hovered [Show("her_tooltip", input_text = f"Virginity status: {{color=#84DE02}}Virgin{{/color}}\nCurrent vaginal level: {pc.vaginal_level}\nExperience needed for next level: {vaginal_exp_for_level}", x_pos = 0.22, y_pos = 0.72), Show("player_panties_shifted_stats_screen")]
        else:
            hovered [Show("her_tooltip", input_text = f"Virginity status: {{color=#E32636}}Non-virgin{{/color}}\nCurrent vaginal level: {pc.vaginal_level}\nExperience needed for next level: {vaginal_exp_for_level}", x_pos = 0.22, y_pos = 0.72), Show("player_panties_shifted_stats_screen")]
        unhovered [Hide("her_tooltip"), Hide("player_panties_shifted_stats_screen")]
        action NullAction()

screen arse_stats_button:
    python:
        anal_exp_for_level = pc.anal_exp_for_level - pc.current_anal_exp
    imagebutton:
        xpos 0.56
        ypos 0.52
        idle "images/stats page/arse label.png"
        if pc.anal_virgin:
            hovered [Show("her_tooltip", input_text = f"Anal virginity status: {{color=#84DE02}}Virgin{{/color}}\nCurrent anal level: {pc.anal_level}\nExperience needed for next level: {anal_exp_for_level}", x_pos = 0.65, y_pos = 0.4), Show("player_panties_shifted_stats_screen")]
        else:
            hovered [Show("her_tooltip", input_text = f"Anal virginity status: {{color=#E32636}}Non-virgin{{/color}}\nCurrent anal level: {pc.anal_level}\nExperience needed for next level: {anal_exp_for_level}", x_pos = 0.65, y_pos = 0.4), Show("player_panties_shifted_stats_screen")]
        unhovered [Hide("her_tooltip"), Hide("player_panties_shifted_stats_screen")]
        action NullAction()

screen foot_stats_button:
    python:
        foot_exp_for_level = pc.foot_exp_for_level - pc.current_foot_exp
    imagebutton:
        xpos 0.56
        ypos 0.8
        idle "images/stats page/foot label.png"
        hovered Show("her_tooltip", input_text = f"Current feet level: {pc.foot_level}\nExperience needed for next level: {foot_exp_for_level}", x_pos = 0.635, y_pos = 0.72)
        unhovered Hide("her_tooltip")
        action NullAction()

screen player_top_open_stats_screen:
    image "images/stats page/player top open.png"

screen player_panties_shifted_stats_screen:
    image "images/stats page/player panties open.png"