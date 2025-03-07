label scene_15:
    # BACKGROUND (possibly we have it) outside the house(scene 15)
    scene crimescene2 with fade
    show mc at left with dissolve
    show killer1 at center with dissolve
    show panormal at right with dissolve:
        ypos 1200
        xzoom -1.0
    mc "What’s your name?"
    killer "I… I don’t know. I don’t know what happened."
    mc "What do you remember?" 
    killer "I was home." 
    killer "My wife was…{w=0.3} she was making dinner."
    killer "Then the phone rang." 
    killer "It was… it was a burger place. They were advertising something." 
    killer "And then…"
    mc "And then what?"
    killer "I don’t know! I woke up, and she was…{w=0.2} she was…"
    pa "This is exactly like the first one. The phone call, the blackout, the murder. What the hell is going on?"
    mc "We’re missing something. Something big."
    stop music fadeout 1
    jump scene_16
