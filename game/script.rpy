# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label splashscreen:
    scene black
    with Pause(1)

    show text "All characters involved in sexual activities within this game are at least 18 years of age." with dissolve
    with Pause(2)

    show text "{size=+15}{color=#BB33FF}EcchiYoYoProductions{/color} presents.{/size}"
    with Pause(2)

    show text "{size=+75}While he was sleeping.{/size}"
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
