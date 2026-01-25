label gabrielle_shop_screen_label():
    # add in Gabrielle shop background (different angle of Players room)
    # fuck renpy
    python:
        # Map relationship types to display names
        relationship_names = {
            "Friend": "Your childhood friend",
            "Brother": "Your big brother",
            "Daddy": "Your daddy",
            "Uncle": "Your uncle",
        }
        single_use = relationship_names.get(man.relationship, "the stranger")
    if not upgrades.first_shop_visit:
        gabrielle "I see this is your first visit to my shop, as such I`ll give you some free coins use them to purchase the wakefulness bar upgrade."
        python:
            actual_coins_gained = upgrades.increaseUpgradeCoins(5)
            upgrades.first_shop_visit = True
        show screen coins_gained_popup_screen(amount_gained = actual_coins_gained)
        pc_talk "Wakefulness bar?"
        gabrielle "It is what it is, it will allow you to know how close to waking up [single_use] is."
        gabrielle "Although until you`ve bought a few more upgrades and I teach you how to better read their body language it will only give you a very rough idea of how close they are to waking."
        gabrielle "With that in mind make sure you take things slow until you`ve learnt a little more."
    call screen gabrielle_shop_screen

screen gabrielle_shop_screen():
    add "gabrielle_shop"
    add "gabrielle_shop_eyes"
    image "screens/gabrielle shop/shop background.png" xalign 0.08 ypos 0.1 yzoom 1.5 xzoom 1.8 # left panel
    image "screens/gabrielle shop/shop background.png" xalign 0.92 ypos 0.1 yzoom 1.5 xzoom 1.8 #  right panel
    image "screens/gabrielle shop/shop background.png" xalign 0.5 ypos 0.7 yzoom 0.50 xzoom 2.0 # central panel
    text "Coins: [upgrades.upgrade_coins]":
        xpos 0.625
        ypos 0.705
        xanchor 1.0 # anchoring to the right, makes text move left when amount of coins increases
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
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.125
        ypos 0.325
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.upgrade_coins >= upgrades.train_mouth_cost and upgrades.train_mouth_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/mouth techniques button.png"
            hover "images/buttons/mouth techniques button hover.png"
            hovered Show("global_tooltip", input_text = "Pay [gabrielle.name] to teach you some techniques to increase your mouth skill", x_pos = 0.13, y_pos = 0.3)
            action [Hide("global_tooltip"), Jump("unlock_train_mouth_label")]
        else:
            idle "images/buttons/mouth techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock the wakefulness bar first", x_pos = 0.13, y_pos = 0.3)
            elif upgrades.train_mouth_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.13, y_pos = 0.3)
            else:
                hovered Show("global_tooltip", input_text = "You don't have enough coins to unlock this, required [upgrades.train_mouth_cost] you have [upgrades.upgrade_coins]", x_pos = 0.13, y_pos = 0.3)
            action NullAction()
        unhovered Hide("global_tooltip")
    # train hands (cheapest) 5 coins
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.185
        ypos 0.325
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.upgrade_coins >= upgrades.train_hands_cost and upgrades.train_hands_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/hand techniques button.png"
            hover "images/buttons/hand techniques button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase the techniques related to training your hands", x_pos = 0.19, y_pos = 0.3)
            action [Hide("global_tooltip"), Jump("unlock_train_hands_label")]
        else:
            idle "images/buttons/hand techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock the wakefulness bar first", x_pos = 0.19, y_pos = 0.3)
            elif upgrades.train_hands_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.19, y_pos = 0.3)
            else:
                hovered Show("global_tooltip", input_text = "You don't have enough coins to unlock this, required [upgrades.train_hands_cost] you have [upgrades.upgrade_coins]", x_pos = 0.19, y_pos = 0.3)
            action NullAction()
        unhovered Hide("global_tooltip")
    # train feet
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.245
        ypos 0.325
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.upgrade_coins >= upgrades.train_feet_cost and upgrades.train_feet_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/foot techniques button.png"
            hover "images/buttons/foot techniques button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase the techniques related to training your feet", x_pos = 0.25, y_pos = 0.3)
            action [Hide("global_tooltip"), Jump("unlock_train_feet_label")]
        else:
            idle "images/buttons/foot techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock wakefulness bar first", x_pos = 0.19, y_pos = 0.3)
            elif upgrades.train_feet_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.25, y_pos = 0.3)
            else:
                hovered Show("global_tooltip", input_text = "You don't have enough coins to unlock this, required [upgrades.train_feet_cost] you have [upgrades.upgrade_coins]", x_pos = 0.25, y_pos = 0.3)
            action NullAction()
        unhovered Hide("global_tooltip")
    # train vaginal
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.305
        ypos 0.325
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if pc.playerHasVaginaCheck() == False:
            idle "images/buttons/vaginal techniques button no vagina.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part", x_pos = 0.31, y_pos = 0.3)
            action NullAction()
        elif upgrades.upgrade_coins >= upgrades.train_vaginal_cost and upgrades.train_vaginal_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/vaginal technique button.png"
            hover "images/buttons/vaginal technique button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase techniques related to training your vagina", x_pos = 0.31, y_pos = 0.3)
            action [Hide("global_tooltip"), Jump("unlock_train_vaginal_label")]
        else:
            idle "images/buttons/vaginal techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock wakefulness bar first", x_pos = 0.31, y_pos = 0.3)
            elif upgrades.train_vaginal_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.31, y_pos = 0.3)
            else:
                hovered Show("global_tooltip", input_text = "You don`t have enough coins to unlock this, required [upgrades.train_vaginal_cost] you have [upgrades.upgrade_coins]", x_pos = 0.31, y_pos = 0.3)
            action NullAction()
        unhovered Hide("global_tooltip")
    # train anal
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.155
        ypos 0.425
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.upgrade_coins >= upgrades.train_anal_cost and upgrades.train_anal_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/anal technique button.png"
            hover "images/buttons/anal technique button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase techniques related to training your arse", x_pos = 0.16, y_pos = 0.40)
            action [Hide("global_tooltip"), Jump("unlock_train_anal_label")]
        else:
            idle "images/buttons/anal techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock wakefulness bar first", x_pos = 0.16, y_pos = 0.40)
            elif upgrades.train_anal_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these technique`s", x_pos = 0.16, y_pos = 0.40)
            else:
                hovered Show("global_tooltip", input_text = "You don`t have enough coins to unlock this, required [upgrades.train_anal_cost] you have [upgrades.upgrade_coins]", x_pos = 0.16, y_pos = 0.40)
            action NullAction()
        unhovered Hide("global_tooltip")        
    # train just the tip
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.215
        ypos 0.425
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if pc.playerHasCockCheck() == False:
            idle "images/buttons/just the tip techniques button no cock.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part", x_pos = 0.22, y_pos = 0.40)
            action NullAction()
        elif upgrades.upgrade_coins >= upgrades.train_just_the_tip_cost and upgrades.train_just_the_tip_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/just the tip technique button.png"
            hover "images/buttons/just the tip technique button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase techniques related to training just the tip", x_pos = 0.22, y_pos = 0.40)
            action [Hide("global_tooltip"), Jump("unlock_train_just_the_tip_label")]
        else:
            idle "images/buttons/just the tip technique button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock wakefulness bar first", x_pos = 0.22, y_pos = 0.40)
            elif upgrades.train_just_the_tip_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.22, y_pos = 0.40)
            else:
                hovered Show("global_tooltip", input_text = "You don`t have enough coins to unlock this, required [upgrades.train_just_the_tip_cost] you have [upgrades.upgrade_coins]", x_pos = 0.22, y_pos = 0.40)
            action NullAction()
        unhovered Hide("global_tooltip")
    # train cock
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.275
        ypos 0.425
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if pc.playerHasCockCheck() == False:
            idle "images/buttons/cock techniques button no cock.png"
            hovered Show("global_tooltip", input_text = "You don`t have the required body part", x_pos = 0.28, y_pos = 0.40)
            action NullAction()
        elif upgrades.upgrade_coins >= upgrades.train_cock_cost and upgrades.train_cock_unlocked == False and upgrades.view_victim_wakefulness_bar != 0:
            idle "images/buttons/cock techniques button.png"
            hover "images/buttons/cock techniques button hover.png"
            hovered Show("global_tooltip", input_text = "Purchase techniques related to training your cock", x_pos = 0.28, y_pos = 0.40)
            action [Hide("global_tooltip"), Jump("unlock_train_cock_label")]
        else:
            idle "images/buttons/cock techniques button locked.png"
            if upgrades.view_victim_wakefulness_bar == 0:
                hovered Show("global_tooltip", input_text = "You must unlock wakefulness bar first", x_pos = 0.28, y_pos = 0.40)
            elif upgrades.train_cock_unlocked == True:
                hovered Show("global_tooltip", input_text = "You`ve already purchased these techniques", x_pos = 0.28, y_pos = 0.40)
            else:
                hovered Show("global_tooltip", input_text = "You don`t have enough coins to unlock this, required [upgrades.train_cock_cost] you have [upgrades.upgrade_coins]", x_pos = 0.28, y_pos = 0.40)
            action NullAction()
        unhovered Hide("global_tooltip")
    #####################################################################################################################
    #                                                                                                                   #
    # passives (first visit forces player to buy wakefulness bar tier 1)                                                #
    #                                                                                                                   #
    #####################################################################################################################
    text "{size=+5}Unlock passive skills" xalign 0.088 ypos 0.43
    # wakefulness (0 means no view, 1 is thirds, 2 is fifths, 3 is tenths, 4 is twenty-fifths, 5 is hundredths and 6 is thousandths)
    # unlock tier 0
    imagebutton:
        at technique_purchase_button_custom_zoom
        xpos 0.125
        ypos 0.575
        xanchor 1.0
        yanchor 1.0
        focus_mask True
        if upgrades.view_victim_wakefulness_bar == 0:
            idle "images/buttons/wakefulness button.png"
            hover "images/buttons/wakefulness button hover.png"
            hovered Show("global_tooltip", input_text = "Unlock the first tier of the wakefulness bar", x_pos = 0.13, y_pos = 0.52)
            action [Hide("global_tooltip"), Jump("unlock_tier_0_wakefulness_bar_label")]
        else:
            idle "images/buttons/wakefulness button locked.png"
            hovered Show("global_tooltip", input_text = "You`ve already purchased this upgrade", x_pos = 0.13, y_pos = 0.52)
            action NullAction()
        unhovered Hide("global_tooltip")

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

    textbutton "Close":
        xalign 0.5
        ypos 0.9
        action [Hide("gabrielle_shop_screen"), Jump("players_room")]

label unlock_train_hands_label:
    python:
        upgrades.reduceUpgradeCoins(5)
        upgrades.train_hands_unlocked = True
    "[gabrielle.name] teaches you techniques to train your hand skills"
    jump players_room

label unlock_train_mouth_label:
    python:
        upgrades.reduceUpgradeCoins(15)
        upgrades.train_mouth_unlocked = True
    "[gabrielle.name] teaches you techniques to train your mouth skills"
    jump players_room

label unlock_train_feet_label:
    python:
        upgrades.reduceUpgradeCoins(25)
        upgrades.train_feet_unlocked = True
    "[gabrielle.name] teaches you techniques to train your foot skills"
    jump players_room

label unlock_train_vaginal_label:
    python:
        upgrades.reduceUpgradeCoins(50)
        upgrades.train_vaginal_unlocked = True
    "[gabrielle.name] teaches you techniques to train your pussy skills"
    jump players_room

label unlock_train_anal_label:
    python:
        upgrades.reduceUpgradeCoins(50)
        upgrades.train_anal_unlocked = True
    "[gabrielle.name] teaches you techniques to train your arse skills"
    jump players_room

#########################################
#                                       #
# Labels for characters with a penis    #
#                                       #
#########################################
label unlock_train_just_the_tip_label:
    python:
        upgrades.reduceUpgradeCoins(50)
        upgrades.train_just_the_tip_unlocked = True
    "[gabrielle.name] teaches you techniques to train you to better use just the tip skills"
    jump players_room

label unlock_train_cock_label:
    python:
        upgrades.reduceUpgradeCoins(50)
        upgrades.train_cock_unlocked = True
    "[gabrielle.name] teaches you techniques to train your cock skills"
    jump players_room


label unlock_tier_0_wakefulness_bar_label:
    "stuff and things to unlock tier 0 wakefulness bar"
    python:
        upgrades.view_victim_wakefulness_bar = 1
        upgrades.reduceUpgradeCoins(5)
    jump players_room