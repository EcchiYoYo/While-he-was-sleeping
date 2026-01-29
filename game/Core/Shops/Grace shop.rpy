label grace_shop_screen_label():
    # add in Gabrielle shop background (different angle of Players room)
    call screen grace_shop_screen

screen grace_shop_screen():
    add "grace_shop"
    add "grace_shop_eyes"
    image "screens/gabrielle shop/shop background.png" xalign 0.08 ypos 0.1 yzoom 1.5 xzoom 1.8
    image "screens/gabrielle shop/shop background.png" xalign 0.92 ypos 0.1 yzoom 1.5 xzoom 1.8
    image "screens/gabrielle shop/shop background.png" xalign 0.5 ypos 0.7 yzoom 0.50 xzoom 2.0
    text "Money: [pc.money]":
        xpos 0.625
        ypos 0.705
        xanchor 1.0 # anchoring to the right, makes text move left when amount of coins increases
        yanchor 0.0






    textbutton "Close":
        xalign 0.5
        ypos 0.9
        action [Hide("grace_shop_screen"), Jump("players_room")]
