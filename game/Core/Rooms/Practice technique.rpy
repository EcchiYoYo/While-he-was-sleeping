label practice_technique_screen_label:
    call screen practice_technique_screen()

screen practice_technique_screen():
    use train_mouth_button()
    use train_hands_button()
    use train_feet_button()
    use train_vaginal_button()
    use train_anal_button()
    use train_just_the_tip_button()
    use train_cock_button()
    #
    #
    #
    #
    image "screens/gabrielle shop/shop background.png" xalign 0.5 ypos 0.92 xzoom 0.2 yzoom 0.05
    textbutton "Close":
        style_prefix "practiceScreenTextButton"
        xalign 0.5
        ypos 0.92
        action Jump("players_room")

screen train_mouth_button():
    python:
        minimum_increase_arousal, maximum_increase_arousal = trainMouthMinMaxCheck()
    imagebutton:
        xpos 0.25
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.train_mouth_unlocked == True and pc.stamina >= 2:
            idle "images/buttons/clean cum from him button.png"
            hover "images/buttons/clean cum from him button hover.png"
            hovered Show("global_tooltip", input_text = f"Train your mouth using the techniques taught to you by [gabrielle.name], increasing your arousal by {{color=#FFB0F2}}{minimum_increase_arousal}-{maximum_increase_arousal}", x_pos = 0.25, y_pos = 0.895)
            action [Hide("global_tooltip"), Jump("train_mouth_label")]
        else:
            idle "images/buttons/clean cum from him button locked.png"
            if upgrades.train_mouth_unlocked == False:
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.25, y_pos = 0.895)
            else:
                hovered Show("global_tooltip", input_text = "Not enough stamina for this action requires 2 you have [pc.stamina]", x_pos = 0.25, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_hands_button():
    python:
        minimum_increase_arousal, maximum_increase_arousal = trainHandsMinMaxCheck()
    imagebutton:
        xpos 0.35
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.train_hands_unlocked == True and pc.stamina >= 3:
            idle "images/buttons/her hands action button.png"
            hover "images/buttons/her hands action button hover.png"
            hovered Show("global_tooltip", input_text = f"Train your hands using the techniques taught to you by [gabrielle.name], increasing your arousal by {{color=#FFB0F2}}{minimum_increase_arousal}-{maximum_increase_arousal}", x_pos = 0.35, y_pos = 0.895)
            action [Hide("global_tooltip"), Jump("train_hands_label")]
        else:
            idle "images/buttons/her hands action button locked.png"
            if upgrades.train_hands_unlocked == False:
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.35, y_pos = 0.895)
            else:
                hovered Show("global_tooltip", input_text = "Not enough stamina for this action requires 3 you have [pc.stamina]", x_pos = 0.35, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_feet_button():
    python:
        minimum_increase_arousal, maximum_increase_arousal = trainFeetMinMaxCheck()
    imagebutton:
        xpos 0.45
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        if upgrades.train_feet_unlocked == True and pc.stamina >= 3:
            idle "images/buttons/her feet button.png"
            hover "images/buttons/her feet button hover.png"
            hovered Show("global_tooltip", input_text = f"Train your foot technique using the skills [gabrielle.name] taught you, increasing your arousal by {{color=#FFB0F2}}{minimum_increase_arousal}-{maximum_increase_arousal}", x_pos = 0.45, y_pos = 0.895)
            action [Hide("global_tooltip"), Jump("train_feet_label")]
        else:
            idle "images/buttons/her feet button locked.png"
            if upgrades.train_feet_unlocked == False:
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.45, y_pos = 0.895)
            else:
                hovered Show("global_tooltip", input_text = "Not enough stamina for this action requires 3 you have [pc.stamina]", x_pos = 0.45, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_vaginal_button():
    python:
        minimum_increase_arousal, maximum_increase_arousal = trainVaginalMinMaxCheck()
    imagebutton:
        xpos 0.55
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        if pc.player_type == "default" or pc.player_type == "futa": # maybe add the trans pack here for male presenting female
            if upgrades.train_vaginal_unlocked == True and pc.stamina >= 6:
                idle "images/buttons/her pussy button.png"
                hover "images/buttons/her pussy button hover.png"
                hovered Show("global_tooltip", input_text = f"Train your pussy using the techniques taught to you by [gabrielle.name], increasing your arousal by {{color=#FFB0F2}}{minimum_increase_arousal}-{maximum_increase_arousal}", x_pos = 0.55, y_pos = 0.895)
                action [Hide("global_tooltip"), Jump("train_vaginal_label")]
            else:
                idle "images/buttons/her pussy button locked.png"
                if upgrades.train_vaginal_unlocked == False:
                    hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.55, y_pos = 0.895)
                else:
                    hovered Show("global_tooltip", input_text = "Not enough stamina for this action requires 6 you have [pc.stamina]", x_pos = 0.55, y_pos = 0.895)
                action NullAction()
        else:
            idle "images/buttons/nothing button locked.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part for this technique", x_pos = 0.55, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_anal_button():
    python:
        minimum_increase_arousal, maximum_increase_arousal = trainAnalMinMaxCheck()
    imagebutton:
        xpos 0.65
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        if upgrades.train_anal_unlocked == True and pc.stamina >= 6:
            idle "images/buttons/rub her ass button.png"
            hover "images/buttons/rub her ass button hover.png"
            hovered Show("global_tooltip", input_text = f"Train your ass using the techniques taught to you by [gabrielle.name], increasing your arousal by {{color=#FFB0F2}}{minimum_increase_arousal}-{maximum_increase_arousal}", x_pos = 0.65, y_pos = 0.895)
            action [Hide("global_tooltip"), Jump("train_anal_label")]
        else:
            idle "images/buttons/rub her ass button locked.png"
            if upgrades.train_anal_unlocked == False:
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.65, y_pos = 0.895)
            else:
                hovered Show("global_tooltip", input_text = "You need at least 6 stamina to train using these training techniques", x_pos = 0.65, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_just_the_tip_button():
    #
    # add in functionality for min max
    #
    imagebutton:
        xpos 0.75
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        if pc.player_type == "futa" or pc.player_type == "gay":
            if upgrades.train_just_the_tip_unlocked == True:
                idle "images/buttons/his just the tip button.png"
                hover "images/buttons/his just the tip button hover.png"
                hovered Show("global_tooltip", input_text = "Train the tip of your cock using the techniques taught by [gabrielle.name]", x_pos = 0.75, y_pos = 0.895)
                action [Hide("global_tooltip"), Jump("train_just_the_tip_label")]
            else:
                idle "images/buttons/his just the tip button locked.png"
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.75, y_pos = 0.895)
                action NullAction()
        else:
            idle "images/buttons/nothing button locked.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part for this technique", x_pos = 0.75, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")

screen train_cock_button():
    #
    # add in functionality for min max
    #
    imagebutton:
        xpos 0.85
        ypos 0.9
        xanchor 1.0
        yanchor 1.0
        if pc.player_type == "futa" or pc.player_type == "gay":
            if upgrades.train_cock_unlocked == True:
                idle "images/buttons/his cock button.png"
                hover "images/buttons/his cock button hover.png"
                hovered Show("global_tooltip", input_text = "Train your cock using the techniques taught to you by [gabrielle.name]", x_pos = 0.75, y_pos = 0.895)
                action [Hide("global_tooltip"), Jump("train_cock_label")]
            else:
                idle "images/buttons/his cock button locked.png"
                hovered Show("global_tooltip", input_text = "You must unlock this technique in [gabrielle.name]`s shop", x_pos = 0.75, y_pos = 0.895)
                action NullAction()
        else:
            idle "images/buttons/nothing button locked.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part for this technique", x_pos = 0.75, y_pos = 0.895)
            action NullAction()
        unhovered Hide("global_tooltip")
