label scene_16:
    # SOUND of phone calls, papers and people in rush
    scene hallway with fade
    play music "office_noise.mp3"
    show mc_sprite at left with dissolve
    show panormal at right with dissolve:
        ypos 1200
        xzoom -1.0
    # SPRITE need the PA with a neutral emotion
    pa "This is a nightmare. Two murders, two killers, both claiming they don’t remember a thing." 
    pa "And that phone call… it’s the only link we’ve got."
    mc "We need to track that call. Find out where it came from."
    pa "Easier said than done. Without a name or a location, we’re shooting in the dark."
    # SOUND ringing phone and picking up the phone
    play sound "phone_ring.mp3"
    pause 4.0
    play sound "phone_hang_up.mp3"
    pause 3.0
    "Officer" "Detective!{w} It’s for you."
    jump scene_17
    
