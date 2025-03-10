label scene_5:
    scene apartment_night with fade
    pause 1.4
    play sound "phone_ring.mp3"  # Phone rings
    show mc_tel at center
    pause 1.4  # Let the sound play for exactly 1.4 seconds
    stop sound fadeout 0.7  # Smooth fadeout
    scene apartment_night with fade
    show mc_phone at right
    mc "(Groggily) Yeah?"
    play music "suspense_soundtrack.mp3"
    operator "(Urgent tone) Detective. We need you!!. Now!!."
    mc "(Sleepy) What happened?"
    operator "Murder. First in years. Address is on [Street_Name]  everyone's already there."
    jump scene_6