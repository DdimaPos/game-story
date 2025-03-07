label scene_21:
    scene abandonedinside with dissolve
    show mc_sprite at right with dissolve
    mc "I’m here!{w} Show yourself!"
    play music "tension.mp3" fadeout 1
    #SOUND music should become more intense(I think you get it Ion. As in scenario)
    show villain_sprite at left with fade
    show hostagealive at slight_left
    mysterious "Drop your weapon. Or he dies."
    "The only option I have in this moment is to obey"

    play sound "sliding_gun_on_the_floor.mp3"
    #SOUND of how he puts something down and how it glides on floor
    mysterious "Good. Now we can talk."
    mc "What is this?"
    mysterious "The address of the next murder. The choice is yours."
    # flasheffect
    play sound "gun_shot.mp3" 
    scene abandonedinside with flash_white
    hide villain_sprite
    show hostagedead at slight_left
    # SOUND Intense music, maybe we can make the previous music faster or louder
    show mc_sprite angry at right
    mc "HOLY F...  "
    menu:
        "Follow the guy":
            jump ending2
        "Hurry to adress":
            jump ending3
