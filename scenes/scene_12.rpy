label scene_12:

    scene jail
    "The killer sits slumped in his cell, staring blankly at the wall"
    show mc_sprite at slight_left
    with slowdissolve
    mc "We need to talk.{w} About the pizza place.{w} What was the name?"

    #barely audible
    show killer2_sprite at slight_right
    with slowdissolve
    killer2 "(barely audible) I...{w} I don't remember.{w} It was something… {w} something simple."
    mc "Think.{w} Was it a man or a woman who called?"
    killer2 "A man.{w} Just a man."
    killer2 "And…{w} there was music.{w} I don’t know why,{w} but it felt… {w=1}familiar"
    mc "What kind of music?"
    killer2 "I don’t know." 
    killer2 "I can’t remember." 
    killer2 "But it’s important."
    killer2 "I know it is."
    "Detective exchanges a look with PA, who shrugs helplessly."
    mc "We’ll find it.{w} But you need to help us.{w} Anything else you remember?"
    
    show killer2_sprite at shake_animation
    killer2 "{size=+7}Please…!!!{/size}{w=0.3} You have to believe me!{w=0.3} It wasn’t me!{w=0.3} I didn’t do this!"
    "MC nods, but before he can respond, the two officers from earlier appear, their mocking laughter echoing down the hallway."


    hide killer2_sprite with dissolve
    show mc_sprite at right with move
    show asshole_cop1_sprite at slight_left behind mc with dissolve 

    #need to add consequence of choice branching here
    if True:
        officer1 "Still chasing pizza leads, huh?{w} Maybe you should stick to traffic duty."
        show asshole_cop2_sprite at Position(xalign=-0.1) behind mc with dissolve 
        officer2 "Yeah, leave the real police work to us."
    else:
        officer1 "Still wasting time, huh? Maybe you should stick to traffic duty."
        show asshole_cop2_sprite at Position(xalign=-0.1) behind mc with dissolve 
        officer2 "Yeah, leave the real police work to those who can handle it."

    show mc_sprite at center with move 
    show killer2_sprite at right with dissolve
    mc "We’ll figure this out. I promise."
    jump scene_13