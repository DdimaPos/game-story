label ending3:
    scene black with fade
    play sound "city-traffic-in-the-rain.mp3"
    scene driving_in_rain with fade
    "The address burned in my mind, a beacon in the storm." 
    "I raced through the night, each second ticking closer to disaster." 
    "Somewhere ahead, another life hung in the balance, and the clock was running out."
    "But as the city lights flickered past, one question lingered—what would I find at the end of the road?" 
    "A chance to stop the killer?" 
    "Or another cruel twist in a game I still didn't fully understand?"


    stop sound fadeout 1.0
    scene house with fade
    play sound "car_door_close.mp3"

    "The house stood silent, its windows glowing faintly in the night." 
    "The air was thick with tension, as if the walls themselves were holding their breath."
    "Somewhere inside, the truth waited—or perhaps, another trap."

    "The room felt smaller now, the air heavier." 
    "My desperation was palpable, every move fueled by a mix of fear and determination." 
    "But in my haste, I failed to notice the cracks in the facade—the signs that something was terribly wrong."

    scene black with fade
    pause 0.2
    play sound "door_slamming.mp3"
    "I rushed to the house and broke the door. I was afraid that I would be too late"
    #show scene people's house
    show man at center 
    show woman at left 
    #show the characters
    "Man" "Who the hell are you?!"
    "Woman" "What do you want?!"
    "Man" "Look, whatever's going on, we don't know anything, okay? Just leave us alone!"

    show mc_sprite angry at right with dissolve
    mc "Police! Where's your phone?!"
    "Man" "What? Our phone? It's—it's right there. What's going on?"
    "The room felt smaller now, the air heavier." 
    "My desperation was palpable, every move fueled by a mix of fear and determination." 
    "But in my haste, I failed to notice the cracks in the facade—the signs that something was terribly wrong."
    play sound "phone_ring.mp3"
    pause 1.0
    play sound "phone_hang_up.mp3"
    show mc_sprite phone
    pause 0.5
    mc "Who is this?"
    mysterious "How many times will you fall for this, detective?" 
    mysterious "You're smarter than this…{w} or are you?"
    mysterious "The clock's ticking."
    mysterious "How many lives will you lose before you figure it out?"
    "Damn it!"
    play sound "phone_beeping.mp3"
    pause 1.0
    show mc_sprite angry with dissolve
    play sound "phone_hang_up.mp3"
    "Man" "What is going on? What are you doing?"
    "It's not here.{p} It's not here..."
    hide man with dissolve
    "How I could make this."
    hide woman with dissolve
    if taken_pills:
        scene black with fade
        "It is my mistake that I left him go." 
        "I lost..."
        return
    else:
        #bright scene to showcase that he is inside his own mind
        stop music 
        play sound "bell.mp3"
        scene mind with flash_white 
        "Those pills..."
        "I haven't taken them since I visited the doctor..."
        "I feel now so strange."
        "Like Dr. Strange in Avengers.{w} Million of thoughts goind in my head.{w} Million of scenarios."
        "And I am sure this is the loosing one."

        
        jump scene_21_chosing 