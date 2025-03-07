label scene_14:
    # SOUND of closing door of a car
    play sound "car_door_close.mp3"
    scene crimescene2 with fade
    show mc_sprite at left with dissolve
    show panormal at right with dissolve:
        ypos 1200
        xzoom -1.0

    pa "This is bad."
    pa "Two murders in two days?"
    pa "This town hasn’t seen something like this in decades."
    mc "Let’s see what we’re dealing with."
    #They need to approach the house
    #ART how they are approaching the house(check the scenario scene 14)
    play music "tension.mp3" fadeout 1
    scene housemurder1 with fade
    pause 1.0
    play sound "phone_beeping.mp3" loop 
    pause 2.0
    show mc_sprite at left with dissolve
    show panormal at right with dissolve:
        ypos 1200
        xzoom -1.0

    pa "This is…{w} something else."
    mc "Same MO.{w} Brutal cuts, same kind of message." 
    mc "And look—"
    "I looked at a phone near the window"
    pa "You think it’s connected?"
    mc "I know it is. The killer—where is he?"
    pa "Outside."
    pa "He’s in custody." 
    pa "But…{w=0.4} you’re gonna want to see this."
    stop sound
    jump scene_15

