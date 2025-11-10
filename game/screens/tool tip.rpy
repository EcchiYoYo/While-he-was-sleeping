screen her_tooltip(input_text, x_pos, y_pos):
    style_prefix "herTooltips"
    frame:
        background Frame("images/tooltip background.png", left = Borders(15,10,15,10))
        xpadding 15 # change this to increase/decrease space between letters and edge of image left and right
        ypadding 10 # change this to increase/decrease space between letters and edge of image top and bottom
        xpos x_pos
        ypos y_pos
        xmaximum 350
        hbox:
            spacing 10
            box_wrap True
            vbox:
                text input_text

screen his_tooltip(input_text, x_pos, y_pos):
    style_prefix "hisTooltips"
    frame:
        background Frame("images/tooltip background.png", left = Borders(15,10,15,10))
        xpadding 15 # change this to increase/decrease space between letters and edge of image left and right
        ypadding 10 # change this to increase/decrease space between letters and edge of image top and bottom
        xpos x_pos
        ypos y_pos
        xmaximum 350
        xanchor 1.0
        hbox:
            spacing 10
            box_wrap True
            vbox:
                text input_text

screen global_tooltip(input_text, x_pos, y_pos):
    style_prefix "globalTooltips"
    frame:
        background Frame("images/tooltip background.png", left = Borders(15,10,15,10))
        xpadding 15
        ypadding 10
        xpos x_pos
        ypos y_pos
        xmaximum 350
        yanchor 1.0
        hbox:
            spacing 10
            box_wrap True
            vbox:
                text input_text
