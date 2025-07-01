screen reset_persistent_button():
    imagebutton:
        xanchor 1.0
        yanchor 1.0
        xpos 0.9
        ypos 0.9
        # focus_mask True
        idle "images/buttons/reset 1.png"
        hover Animation("animated_recycle_1", 0.1, "animated_recycle_2", 0.1, "animated_recycle_3", 0.1, "animated_recycle_4", 0.1, "animated_recycle_5", 0.1, "animated_recycle_6", 0.1, "animated_recycle_7", 0.1, "animated_recycle_8", 0.1, "animated_recycle_9", 0.1, "animated_recycle_10", 0.1)
        hovered Show("global_tooltip", input_text = "Reset all progress from previous cycles", x_pos = 0.9, y_pos = 0.9)
        action [Hide("global_tooltip"), Jump("confirm_reset_label")]
        unhovered Hide("global_tooltip")

label confirm_reset_label():
    hide main_menu
    menu:
        "Are you sure you want to reset all data from previous cycles? This cannot be undone, and will also {color=#c52828}delete all saves{/color} to prevent mismatches between save data and persistent data."
        "Yes":
            python:
                fullReset()
                delete_all_saves()
                renpy.full_restart()  
        "No":
            call screen main_menu

label confirm_reset_label_preferences():
    hide preferences
    menu:
        "Are you sure you want to reset all data from previous cycles? This cannot be undone, and will also delete all saves to prevent mismatches between save data and persistent data."
        "Yes":
            menu:
                "This will return you to the main menu and reset all player data and delete saves, are you certain you wish to reset?"
                "Yes":
                    python:
                        fullReset()
                        delete_all_saves()
                                              
                "No":
                    return
        "No":
            return

init python:
    def delete_all_saves():
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
      