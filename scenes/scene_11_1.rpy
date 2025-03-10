label scene_11_1:
    scene hallway2 with fade
    play music "tension.mp3" fadein 1.0  # Tense background music
    show pa at left:
        xalign 0.3 yalign 1.0
        ypos 1200
    show mc at right:
        xalign 0.7 yalign 1.0

    "*They return to the station for updates*"
    hide pa
    show pa_depressed at left:
        xalign 0.3 yalign 1.0
        ypos 1200
    pa "(serious) Bad news. The killer's completely unresponsive now."
    hide mc 
    show mc_depressed at right:
        xalign 0.7 yalign 1.0
    mc "(leaning on desk) So, no chance of getting anything else out of him?"
    hide mc_depressed
    show mc at right:
        xalign 0.7 yalign 1.0
    pa "(shaking head) Not unless he snaps out of it. And even then..."
    mc "(straightening up) Then we'll have to work with what we've got. That pizza place - what's the plan?"
    hide pa_depressed
    show pa_intrigued at left:
        xalign 0.3 yalign 1.0
        ypos 1200
    pa "(pulling out list) I've got a list of every pizza joint in the city. We'll start with the ones closest to the crime scene and work our way out."
    mc "(heading to door) Let's move."


    # Transition to next scene
    scene black with fade
    stop music fadeout 1.0
    stop sound fadeout 1.0
    jump scene_12