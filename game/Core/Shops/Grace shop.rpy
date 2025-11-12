label grace_shop_screen_label():
    # add in Gabrielle shop background (different angle of Players room)
    # fuck renpy
    call screen grace_shop_screen

screen grace_shop_screen():
    add "grace_shop"
    image "screens/gabrielle shop/shop background.png" xalign 0.08 ypos 0.1 yzoom 0.8 xzoom 0.9
    image "screens/gabrielle shop/shop background.png" xalign 0.92 ypos 0.1 yzoom 0.8 xzoom 0.9
    image "screens/gabrielle shop/shop background.png" xalign 0.5 ypos 0.7 yzoom 0.25 xzoom 1.0
    text "Money: [pc.money]":
        xpos 0.625
        ypos 0.705
        xanchor 1.0 # anchoring o the right, makes text move left when amount of coins increases
        yanchor 0.0






    textbutton"Close":
        xalign 0.5
        ypos 0.9
        action [Hide("grace_shop_screen"), Jump("players_room")]
