label scene_19:
    scene mctable with fade
    window hide
    pause 2.0
    window show
    "Midnight." 
    "That’s when it would happen." 
    "That’s when I’d get my answers." 
    "Or die trying."
    scene mctable with fade
    "I looked at pills on my table."
    "Doctor said that I should take them without any questions."
    "But I feel like in cage.{p}Like a rat..."
    "Doing something that others tell me without even questioning it."
    "What if they are hiding the truth from me."
    "Or what if I willl go insane."
    "I am holding now the black pill and don't know what to do."
    menu:
        "Take pills":
            "I think this is for my own safety"
            "I will discover the truth on my own without risking my life"
            $ taken_pills = True
        "Don't take the pills":
            "Screw all of this.{p}I want to know what happened to me."
            "And they won't stop me from doing this"
            $ taken_pills = False
    # ART how the mc puts go outside through the door (how I imagine this. mc is viewed from back and he just walks towards a white rectangle which is the door) 
    jump scene_20
