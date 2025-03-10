label scene_11:
    scene black with Dissolve(0.4)
    scene mc_house with fade
    play music "calm.mp3" fadein 1.0  # Calm morning music
    show pa_intrigued at left:
        xalign 0.3 yalign 1.0
        ypos 1200
    show mc at right:
        xalign 0.7 yalign 1.0

    play sound "car_door_close.mp3"  # PA arrives
    "*Next morning, PA bursts into the detective's house*"
    mc "What are you doing here?"
    pa "(impatient) We're detectives, remember? I know where you live. Can we get moving?"
    mc "(sighing) Fine. Let's go."

    # Transition to police department
    scene black with fade
    play sound "office_noise.mp3" fadein 1.0  # Background office noise
    jump scene_11_1
