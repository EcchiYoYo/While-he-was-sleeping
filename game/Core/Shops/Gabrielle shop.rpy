label gabrielle_shop_screen_label():
    # add in Gabrielle shop background (different angle of Players room)
    # fuck renpy
    call screen gabrielle_shop_screen

screen gabrielle_shop_screen():
    add "gabrielle_shop"
    image "screens/gabrielle shop/shop background.png" xalign 0.08 ypos 0.1 yzoom 0.8 xzoom 0.9 # left panel
    image "screens/gabrielle shop/shop background.png" xalign 0.92 ypos 0.1 yzoom 0.8 xzoom 0.9 #  right panel
    image "screens/gabrielle shop/shop background.png" xalign 0.5 ypos 0.7 yzoom 0.25 xzoom 1.0 # central panel
    text "Coins: [upgrades.upgrade_coins]":
        xpos 0.625
        ypos 0.705
        xanchor 1.0 # anchoring o the right, makes text move left when amount of coins increases
        yanchor 0.0
    # blinking Gabrielle image

    # shop items background

    # small box labeling current coins, coins spent this cycle and amount of coins available on next cycle start

    ###################################################################################################################
    # training unlocks                                                                                                #
    #                                                                                                                 #
    # (these can only be bought for player, and unlock the ability to train with named body part                      #
    # for example unlocking hand training means the player can rub breasts/nipples abd clit while unlocking vaginal   #
    # allows for inserting fingers or items into vagina for training)                                                 #
    #                                                                                                                 #
    ###################################################################################################################
    text "{size=+5}Unlock [gabrielle.name]`s \ntechniques" xalign 0.088 ypos 0.13
    # train mouth

    # train feet

    # train vaginal

    # train anal

    # train just the tip

    # train cock

    #####################################################################################################################
    #                                                                                                                   #
    # passives (first visit forces player to buy wakefulness bar tier 1)                                                #
    #                                                                                                                   #
    #####################################################################################################################
    text "{size=+5}Unlock passive skills" xalign 0.088 ypos 0.53
    # wakefulness (0 means no view, 1 is thirds, 2 is fifths, 3 is tenths, 4 is twenty-fifths, 5 is hundredths and 6 is thousandths)

    # view victim arousal

    # increase victim orgasm counter

    # victim cum amount

    # increase max stamina

    # increase max wakefulness

    #####################################################################################################################
    #                                                                                                                   #
    # multipliers                                                                                                       #
    #                                                                                                                   #
    #####################################################################################################################
    text "{size=+5}Unlock multipliers" xalign 0.846 ypos 0.13
    # points

    # money

    # experience

    # mouth

    # hand

    # vaginal

    # anal

    # foot

    # just the tip

    # cock

    textbutton"Close":
        xalign 0.5
        ypos 0.9
        action [Hide("gabrielle_shop_screen"), Jump("players_room")]