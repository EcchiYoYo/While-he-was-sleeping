# rub his chest
# he sucks her toes
# rub his balls
# footjob
label rub_chest_with_foot_label:
    python:
        resetEventRelatedVariables()
    "You gently rub his chest with your foot"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase = rubChestWithFootCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    show screen victim_arousal_increase_screen(amount_gained = [his_arousal_increase])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm:
        python:
            pc.increaseOrgasm()
        "You orgasmed from rubbing his chest with your foot"
    if did_he_orgasm:
        python:
            man.increaseOrgasm()
        "He orgasmed while you rubbed his chest with your foot"
    if did_level_up:
        show screen foot_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up:
        show screen persistent_foot_level_up_screen(number_of_levels = [did_persistent_level_up])
    if did_he_level_up:
        show screen his_chest_level_up_screen(number_of_levels = [did_he_level_up])
    if did_he_persistent_level_up:
        show screen persistent_his_chest_level_up_screen(number_of_levels = [did_he_persistent_level_up])
    jump his_room

label he_sucks_her_toes_label:
    python:
        resetEventRelatedVariables()
    "You place your toe in his mouth, he gently sucks it"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, did_orgasm, coin_gain, her_global_arousal_gain = heSucksHerToesCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm:
        python:
            pc.increaseOrgasm()
        "You orgasmed while he sucked your toes"
    if did_level_up:
        show screen foot_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up:
        show screen persistent_foot_level_up_screen(number_of_levels = [did_persistent_level_up])
    jump his_room

label rub_his_balls_with_foot_label:
    python:
        resetEventRelatedVariables()
    "You gently rub his balls with your foot"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase = rubHisBallsHerFootCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    show screen victim_arousal_increase_screen(amount_gained = [his_arousal_increase])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm:
        python:
            pc.increaseOrgasm()
        "You orgasmed while massaging his balls with your foot"
    if did_he_orgasm:
        python:
            man.increaseOrgasm()
        "He orgasmed while you massaged his balls with your foot"
    if did_level_up:
        show screen foot_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up:
        show screen persistent_foot_level_up_screen(number_of_levels = [did_persistent_level_up])
    if did_he_level_up:
        show screen his_cock_level_up_screen(number_of_levels = [did_he_level_up])
    if did_he_persistent_level_up:
        show screen persistent_his_cock_level_up_screen(number_of_levels = [did_he_persistent_level_up])
    jump his_room

label footjob_label:
    python:
        resetEventRelatedVariables()
    "You stroke his cock using your foot"
    #
    #
    #
    #
    python:
        did_level_up, did_persistent_level_up, did_orgasm, did_he_level_up, did_he_orgasm, did_he_persistent_level_up, coin_gain, her_global_arousal_gain, his_arousal_increase = footjobCombinedVariableGenerator()
    show screen coins_gained_popup_screen(amount_gained = [coin_gain])
    show screen player_arousal_increase_screen(amount_gained = [her_global_arousal_gain])
    show screen victim_arousal_increase_screen(amount_gained = [his_arousal_increase])
    $ renpy.block_rollback() # this must be here to prevent rolling back and gaining additional persistent exp
    if did_orgasm:
        python:
            pc.increaseOrgasm()
        "You orgasmed while giving him a footjob"
    if did_he_orgasm:
        python:
            man.increaseOrgasm()
        "He orgasmed from your footjob"
    if did_level_up:
        show screen foot_level_up_screen(number_of_levels = [did_level_up])
    if did_persistent_level_up:
        show screen persistent_foot_level_up_screen(number_of_levels = [did_persistent_level_up])
    if did_he_level_up:
        show screen his_cock_level_up_screen(number_of_levels = [did_he_level_up])
    if did_he_persistent_level_up:
        show screen persistent_his_cock_level_up_screen(number_of_levels = [did_he_persistent_level_up])
    jump his_room
