label scene_8:
    scene interrogation with Dissolve(1)
    play music "tension.mp3" fadein 1.0  # Tense background music
    show killer1 at left
    show mc at right
    show pa behind mc at right:
        xalign 0.7
        ypos 1200
    show killer1 at shake_animation
    mc "Let's start from the beginning. What do you remember?"
    killer "I… I don't know. I swear, I don't remember doing this. I woke up, and he was… he was already…"
    mc "You called the police. Why?"
    killer "I… I thought I was helping. I didn't know what else to do."
    mc "What about the phone call? The one before this happened. Do you remember it?"
    killer "Yeah… yeah, I do. It was… some pizza place. They were advertising a deal or something."
    mc "What did they say? Anything specific?"
    killer "It was a man's voice. No background noise, just… some music. I don't know why, but it felt familiar. Like I'd heard it before."
    mc "And then?"
    killer "Then… nothing. Everything went blank. Next thing I knew, I was standing over him, and… and…"
    "*He breaks down sobbing, bloodstained hands clutching his head*"

    label interrogation_loop:
        menu:
            "Ask about the music he heard during the call" if not persistent.loop_count:
                $ choice_made = "music"
                jump progress_scene

            "Ask about his relationship with the victim":
                mc "What was your relationship with the victim? Were you close?"
                killer "He was my friend! My best friend! I would never… I could never…"
                "*The killer becomes hysterical"
                pa "Detective, maybe try a different approach..."
                $ persistent.loop_count = True
                jump interrogation_loop

            "Ask about the pizza place name again":
                mc "The pizza place. Do you remember the name?"
                killer "I… I don't know. It was something simple. I can't remember."
                "*The killer stares blankly, offering nothing new*"
                $ persistent.loop_count = True
                jump interrogation_loop

            "You mentioned music. What did it sound like?" if persistent.loop_count:
                $ choice_made = "music"
                jump progress_scene

    label progress_scene:
        killer "It was… I don't know. Something old. Like from a radio. I can't remember the tune, but it felt… familiar."
        mc "(Music from a radio? That's specific. Maybe it's a clue.)"
        "*PA nods subtly, making a note in his pad*"

        scene interrogation with fade
        show asshole_cop1 at left
        show asshole_cop2 at right
        
        officer1 "That's enough. We'll take it from here."
        officer2 "Guys like him don't deserve your time. He's just playing dumb."
        
        menu:
            "Say nothing and leave":
                $ officer_attitude = "silent"
            
                "*You exchange a look with PA and exit silently*"
                "The officers will remember your silence."
                python:
                    rude = False

            "Respond rudely":
                $ officer_attitude = "rude"
                mc  "Maybe if you did your jobs, I wouldn't have to clean up your mess."
                officer2 "Watch your mouth, new guy."
                "*PA pulls you away before things escalate*"
                "The officers will remember your attitude."
                python:
                    rude = True

        jump scene_9