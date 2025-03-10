label scene_17:
    #show show another scene of only the mc holding phone and another generic background
    #ART of how mc is holding a phone
    hide mc with dissolve 
    show mc_sprite phone at left with dissolve
    mc "This is Detective \[MCs Name\]."
    mysterious "Listen carefully."
    mysterious "If you want to stop the next murder, come to \[PLACE\] at midnight."
    mysterious "Tell no one.{w} If you do, you\’ll find nothing but an empty room."
    mc "Who is this? What do you want?"
    mysterious "Midnight. Don’t be late."
    # SOUND Beeping sound 
    play sound "phone_beeping.mp3"
    pause 4.0
    # SOUND of hanging the phone sound 
    #switch back to normal scene with fade
    hide mc_sprite phone with dissolve
    show mc at left with dissolve
    play sound "phone_hang_up.mp3"
    pause
    pa "Who was that?"
    menu:
        "Tell him the truth": 
            jump told_truth
        "Lie and solve it on your own": 
            jump told_lie

    label told_truth:
        $ liedpa = False
        # show a screen message that pa remembered our honesty
        mc "It was… a tip. Someone called about the case. They said if I want to stop the next murder, I need to go to \[PLACE\] at midnight. Alone."
        pa "Alone? That sounds like a trap."
        mc "Yeah. But it’s the only lead we’ve got."
        pa "You sure about this? I don’t like the sound of it."
        mc "I don’t either. But if there’s a chance to stop another killing, I have to take it."
        pa "Alright. But if you’re going, I’m going with you. No arguments."
        mc "Fine. But we need to be careful. This guy… he’s playing games with us."
        pa "Yeah, I got that. Let’s move."

        jump scene_18_withpa

    label told_lie:
        $ liedpa = True
        mc "Just… a friend. Updating me on something. Nothing important."
        "pa raised an eyebrow showing distrust"
        jump scene_18_withnopa

