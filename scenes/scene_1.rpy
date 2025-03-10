label scene_1:
    scene doctor_office with fade
    play music "basic_soundtrack.mp3" fadein 2.0  # Soft background music
    show dr at left
    show mc at right

    doctor "Let's start simple. What do you remember about yourself?"
    mc "Not much. My name, my training... fragments of something else."
    doctor "And the last thing you recall before 'it' happened?"
    jump scene_2