label you_work_a_little:
    if persistent.first_upgrade_visit == False: # used to check if the scene tricking Grace has been seen before
        python:
            persistent.first_upgrade_visit = True
        "Do some stuff and things to introduce coin shop"
    "The current time block is [game_time.block]"
    "Not much here yet, you work and earn a few pounds"
    python:
        globalAdvanceTime(1)
    "The current time block is now [game_time.block]"
    #
    #
    #
    #
    jump players_room
