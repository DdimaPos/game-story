label scene_2:
    scene black with fade
    play sound "static.mp3" fadein 0.5  # Glitch effect
    show battlefield2:
        alpha 0.5 blur 50
        linear 0.3 alpha 1.0 blur 0
    with vpunch

    mc "(voice broken) I was...{w=0.5} a soldier.{w} Special Corps.{w=0.3} But the details..." 

    # Memory glitch effect
    play sound "glitch.mp3"  # Additional glitch sound
    show battlefield2:
        xalign 0.5 yalign 0.5
        linear 0.1 xalign 0.51 yalign 0.51
        linear 0.1 xalign 0.49 yalign 0.49
        repeat 3
    with hpunch

    show terrorist at center:
        alpha 0.0
        linear 0.2 alpha 1.0
        linear 0.2 alpha 0.5
        repeat

    play sound "heartbeat.mp3" loop  # Tension building
    mc "(strained) ...are...{w=0.7} blurred."

    # Rapid flash sequence
    scene black with Dissolve(0.1)
    show terrorist at center with pixellate
    hide terrorist with dissolve
    show battlefield2 with vpunch
    hide battlefield2 with dissolve
    show terrorist at left with hpunch
    hide terrorist with dissolve

    play sound "heartbeat.mp3"
    show battlefield2:
        matrixcolor TintMatrix("#ff0000")  # Red tint
        alpha 0.7
    with vpunch

    mc " Had to...{w} capture...{w} someone alive... {w} someone important"
    show terrorist at center with hpunch
    mc "(whisper) ...I succeeded."
    

    play sound "explosion.mp3"  # Climactic explosion
    scene black with vpunch
    stop sound fadeout 1.0
    jump scene_3