label scene_3:
    scene doctor_office with fade
    play music "basic_soundtrack.mp3" fadein 2.0  # Soft background music
    show dr at left
    show mc at right
    doctor "And then?"
    mc "Nothing. Just... waking up in a hospital. Six months in a coma."
    doctor "Your records say you were awarded medals for your service."
    mc "Yeah... Guess I did something right. Not that it matters now."
    doctor "Why do you say that?"
    mc "Because I can't go back. The trauma, the amnesia... I'm no longer fit for special ops. So they sent me here."
    doctor "Here?"
    mc "A quiet town. A detective job. Small cases. Small crimes. Trying to put myself back together."
    doctor "Ok, that's enough for today." 
    play sound "sliding_gun_on_floor.mp3"
    scene pills with fade
    "*Doctor hands you a small bottle of pills.*"
    scene doctor_office with fade
    show dr at left
    show mc at right
    doctor "One pill a day. Don't forget."

    menu:
        "Ask about what those pills are":
            mc "Doc, what exactly are these pills for? You never really explained."
            doctor "They're to help with the trauma. The amnesia. They'll keep your mind... stable. Trust me, you need them."
            mc "Stable how? What aren't you telling me?"
            doctor "You've been through a lot, Detective. More than most people could handle. Those pills are there to help you cope."
            mc "And if I stop taking them?"
            doctor "Don't. Just... don't. Take one a day. No more, no less. That's all you need to know."
            
            "*You study the doctor's face but find no answers. You pocket the pills.*"
            
        "Say nothing":
            "You take the pills without comment."

    scene black with fade
    jump scene_4