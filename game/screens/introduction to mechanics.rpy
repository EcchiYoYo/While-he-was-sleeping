label introduction_1:
    python:
        if man.relationship == "Friend":
            first_use = "your friends"
        elif man.relationship == "Brother":
            first_use = "your brothers"
        elif man.relationship == "Father":
            first_use = "your dads"
        elif man.relationship == "Uncle":
            first_use = "your uncles"
        else:
            first_use = "the strangers"
    "As you enter the room you can`t help but feel a little trepidation along with a whole lot of sexual excitement."
    "You slowly approach his bed while thinking about what you are going to do."
    pc_talk "Do I just jump him and to hell with the consequences, or do I take it slow and see how far I can go without getting caught?"
    "You decide the latter option has more potential, with that in mind you kneel beside the bed while thinking about what to do next."
    #
    #
    # Pseudo event screen as background
    #
    gabrielle "We will now go through several steps of introduction to the main mechanics of this game."
    gabrielle "Each night you will have the option to visit [first_use] room, and try to perform lewd acts with his sleeping form."
    gabrielle "At the start of the game you will have no real way of knowing how deeply he is asleep." 
    gabrielle "When we head back to your room you will be introduced to the shop where you can purchase upgrades one of these will help you determine the state of wakefulness."
    gabrielle "For now we don`t need to worry about this."
    #
    # Show screen for action buttons
    #
    #
    gabrielle "The first step is to select the action you wish to perform, we can do this by selecting the body part you wish to use."
    gabrielle "The left buttons are your body parts, the right side are [man.name]`s."
    gabrielle "Let`s start by selecting your hand."
    # hide screens, and call combined screen with only option to select hand
    # Wait for player to select hand, pressing hand will jump to introduction_2
    #
    jump introduction_2


label introduction_2:
    gabrielle "Once you have selected an action type you will be asked what action you wish to perform, for now you can only select rub chest."
    call screen introduction_rub_chest_screen()


screen introduction_rub_chest_screen():
    use your_actions()
    use his_actions()

label introduction_3:
    python:
        if man.relationship == "Friend":
            first_use = "Your friends"
        elif man.relationship == "Brother":
            first_use = "Your brothers"
        elif man.relationship == "Father":
            first_use = "Your dads"
        elif man.relationship == "Uncle":
            first_use = "Your uncles"
        else:
            first_use = "The strangers"
    gabrielle "As you can see you are now rubbing your breast and are ready to select the next action, your stamina has decreased and arousal has increased." 
    gabrielle "Although we can`t see it [first_use] wakefulness has not changed because the action you performed did not involve him."
    gabrielle "Next we will use an action that does involve him by selecting a part of his body on the right, for now you can only select his chest."
    call screen introduction_rub_his_chest_screen()

screen introduction_rub_his_chest_screen():
    use your_actions()
    use his_actions()
    #
    # show image player rubbing left breast
    # 
    # 

label introduction_to_mechanics_final:
    python:
        if man.relationship == "Friend":
            first_use = "your friends"
        elif man.relationship == "Brother":
            first_use = "your brothers"
        elif man.relationship == "Father":
            first_use = "your dads"
        elif man.relationship == "Uncle":
            first_use = "your uncles"
        else:
            first_use = "the stranger"
    pc_talk "Oh shit looks like he`s waking up."
    #
    # wakefulness bar full
    #
    gabrielle "You were too rough with him and now he`s waking up, normally this would lead to a game over but as a one time only favour I will save you."
    #
    # wakefulness empty
    #
    gabrielle "You`ve taken enough chances, time to get out of here."
    "Not wanting to get caught you dash out the door and head back to your own room."
    #
    # transition to players room
    #
    "Safely in your own room you decide to turn in for the night, but vow that you will return again and use [first_use] sleeping form for your own pleasure."
    jump talk_to_player_scene

label talk_to_player_scene:
    gabrielle "Right, now that she`s sleeping let`s teach you how to use the shop."
    #
    # gabrielle turning and shouting to left
    #
    gabrielle "Hey wake up we need to check out the shop."
    #
    # twins together grace annoyed
    #
    grace "What the fuck Gabrielle I was sleeping why so loud."
    python:
        gabrielle.name = "Gabrielle"
    gabrielle "Come on Grace we need to show the player how to use our shops."
    python:
        grace.name = "Grace"
    grace "Oh a new player it`s been a while since I made some coin, I really need some cake but it`s expensive....."
    #
    # grace daydreaming about cake
    #
    gabrielle "Oh snap out of it will you, they can`t give you money for cakes if you don`t hurry up."
    #
    # back to full attention
    #
    grace "Right you are Sis, right you are."
    grace "Now we have two shops, my shop sells things that help you relax and unwind from a busy day ensuring you get a good and long sleep ready to face tomorrow."
    gabrielle "And my shop will teach you techniques to make you an expert in pleasure."
    gabrielle "With even the lightest of touches you can bring untold pleasure to yourself or others."
    grace "That`s disgusting Gabrielle, I doubt this player will be visiting your shop much."
    grace "Anyway I`m going back to sleep, once the perv sleeping over there wakes up make sure you get her out working to earn money for my shop."
    #
    # grace walking away
    #
    grace "I. Need. Cake!!"
    #
    # just gabrielle
    #
    gabrielle "As you may have gathered from that little display, I can make you better at increasing pleasure while not increasing wakefulness too much."
    gabrielle "And my sister, although she won`t admit it, will sell you items to make sure the object of your desires has a nice deep sleep."
    gabrielle "Between you and me I`m sure she`s a closet perv, she`s just too prude to openly admit it."
    grace "I heard that you whore, just because you enjoyed the fall of Babylon doesn`t mean I did."
    gabrielle "Who are you kidding you fucked more people than{i} I {/i}did."
    grace "Ah whatever I just did what I had too to afford my cakes, it`s not my fault you corrupted them all into lust filled degenerates."
    gabrielle "Anyway come see us after the perv finishes work or training in the morning, and you can see what we offer in our shops" 
    gabrielle "Make sure you come see us before you head out for your night time activities."
    jump players_room
