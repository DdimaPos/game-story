label scene_21:
    scene abandonedinside with dissolve
    show mc_sprite at right with dissolve
    mc "I’m here!{w} Show yourself!"
    play music "tension.mp3" fadeout 1
    #SOUND music should become more intense(I think you get it Ion. As in scenario)
    show villain_sprite at left with fade
    show hostagealive at slight_left:
        ypos 1300
    mysterious "Drop your weapon. Or he dies."
    "The only option I have in this moment is to obey."

    play sound "sliding_gun_on_the_floor.mp3"
    "I slided the gun to him."
    "Now I waited to hear something from this guy."
    mysterious "Good. Now we can talk."
    "Suddenly this motherfucker got a letter from his pocket."
    scene black with fade
    show envelope with dissolve

    

    "I was feeling with my guts it's not a good thing"
    mc "What is this?"
    scene abandonedinside with dissolve
    show mc_sprite at right with dissolve
    show villain_sprite at left with dissolve
    show hostagealive at slight_left:
        ypos 1300
    mysterious "The address of the next murder. The choice is yours."
    hide mc_sprite with dissolve
    show hostagealive at center with move:
        ypos 1300
        linear 1.0
    pause 0.5
    # flasheffect
    play sound "gun_shot.mp3" 
    scene abandonedinside with flash_white
    hide villain_sprite
    show hostagedead at center:
        ypos 1300
    # SOUND Intense music, maybe we can make the previous music faster or louder
    pause 0.2
    mc "HOLY F...  "
    "I can't let him go now."
    "But what if somebody dies while I try to catch him."
    menu:
        "Follow the guy":
            jump ending2
        "Hurry to adress":
            jump ending3
