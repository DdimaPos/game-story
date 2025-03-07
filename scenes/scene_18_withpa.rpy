label scene_18_withpa: # ending 1
    stop music fadeout 1
    scene abandoned with fade
    "The building stood like a forgotten relic of a time long past."
    "Its windows were shattered, its walls cracked and stained with years of neglect."
    "The air was heavy with the scent of decay,{w} and the only sound was the faint creak of the wind pushing against the broken door."
    "Somewhere inside, the answers waited."
    "Or maybe it was just another trap."
    "Either way, there was no turning back now."
    pa "This place gives me the creeps."
    pa "You sure this is the right spot?"
    mc "It’s the address he gave me." 
    mc "Let’s check it out."

    scene black with fade
    play sound "footsteps.mp3"
    pause 2.0
    pa "This place gives me the creeps. You sure this is the right spot?"
    mc "It’s the address he gave me. Let’s check it out."
    play sound "footsteps.mp3"
    pause 2.0
    #show the scene with chair and the phone
    scene abandonedinside with dissolve
    play sound "phone_ring.mp3" loop
    show panormal at left with dissolve:
        ypos 1200
    show mc_sprite at slight_right with dissolve
    pa "What the hell..."
    pause 1.0
    play sound "phone_hang_up.mp3"
    hide mc_sprite with dissolve
    show mc_sprite phone at slight_right with dissolve

    mysterious "Alone."
    mysterious "Didn’t I tell you?"
    mysterious "Now go."
    mysterious "There’s another case for you."
    mysterious "Maybe if you hurry, it won’t be too late."

    play sound "phone_beeping.mp3"
    # pause 2.0
    
    hide mc_sprite phone with dissolve
    show mc_sprite angry at slight_right with dissolve

    # sound of slamming a phone
    pa "What was that?{w} Who was that?"
    mc "He knew.{p}He knew I'd bring you."
    pa "So this was a waste of time?{p}What now?"
    mc "We follow his lead.{w} There's another case.{p}And we're running out of time."
    jump ending1


