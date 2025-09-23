screen your_actions():
    textbutton "Introduction 2" action SetVariable("intro_2_completed", False), Jump("introduction_2") xalign 0.3 ypos 0.9
    use your_breast()
    use your_mouth()
    use your_pussy()
    use your_arse()
    use your_feet()
    use your_just_the_tip()
    use your_cock()
    if activate_buttons == True:
        use rub_hair_screen()

#############################################
#                                           #
# Unique buttons for her actions            #
#############################################
screen rub_hair_screen():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.14
        ypos 0.2
        focus_mask True
        if pc.stamina >= 3:
            idle "images/buttons/rub his hair button.png"
            hover "images/buttons/rub his hair button hover.png"
            hovered Show("her_tooltip", input_text="Gently rub his hair to help him relax and fall into a deeper sleep",x_pos = 0.15, y_pos = 0.13)
            action [Hide("her_tooltip"), Jump("rub_his_hair_label")]
        else:
            hovered Show("her_tooltip", input_text="Not enough stamina to do that, consider ending the night ({color='#E32636'}Make sure you hide any evidence left on his body)",x_pos = 0.15, y_pos = 0.23)
            action NullLAction()
            idle "images/buttons/rub his hair button locked.png"
        unhovered Hide("her_tooltip")