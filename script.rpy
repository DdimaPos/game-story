# Define characters
define doctor = Character("Doctor", color="#a8d8ea")
define mc = Character("Detective", color="#c0c0c0")
define pa = Character("PA", color="#808080")
define killer = Character("Killer", color="#ff6666")
define killer2 = Character("Killer", color="#ff8666")
define officer1 = Character("Officer 1", color="#999999")
define officer2 = Character("Officer 2", color="#999999")
define operator = Character("Operator", color="#66ccff")
define mysterious = Character("Mysterious Caller", color="#ff0000")
define Street_Name = "2980 Lyndon Street"

# Character images
image side mc = "MC.png"
image side pa = "PA.png"
image side doctor = "dr.png"
image side killer = "killer1.png"
image side killer2 = "killer2.png"
image asshole_cop1 = "assholecop1.png"
image asshole_cop2 = "assholecop2.png"
image villain = "villaingun.png"

# Scene backgrounds
image doctor_office = "doctoroffice.png"
image battlefield = "terrorist.png"
image city_day = "city1.png"
image apartment_night = "MCbedroom.png"
image crimescene1 = "crimescene1.png"
image crimescene2 = "crimescene2.png"
image crimescene3 = "crimescene3.png"
image interrogation = "interrogation.png"
image hallway = "policedepartment.png"
image mc_car_night = "MCcarNight.png"
image mc_car_noon = "MCcarNoon.png"
image mc_house = "MCliving.png"
image jail = "jail.png"
image abandoned = "abandoned.png"
image abandoned_inside = "abandonedinside.png"
image murder_house1 = "housemurder2.png"
image murder_house2 = "housemurder1.png"

# Transitions
define slowdissolve = Dissolve(0.5)
define flash_white = Fade(0.1, 0.0, 0.1, color="#FFFFFF")

transform slight_left:
    xalign 0.25
    yalign 1.00

transform slight_right:
    xalign 0.75
    yalign 1.00

transform left:
    xalign 0.1
    yalign 1.00

transform pos_right:
    xalign 0.9
    yalign 1.00

transform shake_animation:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    repeat

#variables
define liedpa = True


label start:

label scene_12:

    scene jail
    "The killer sits slumped in his cell, staring blankly at the wall"
    show mc at slight_left
    with slowdissolve
    mc "We need to talk.{w} About the pizza place.{w} What was the name?"

    #barely audible
    show killer2 at slight_right
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
    
    show killer2 at shake_animation
    killer2 "{size=+7}Please…!!!{/size}{w=0.3} You have to believe me!{w=0.3} It wasn’t me!{w=0.3} I didn’t do this!"
    "MC nods, but before he can respond, the two officers from earlier appear, their mocking laughter echoing down the hallway."


    hide killer2 with dissolve
    show mc at right with move
    show asshole_cop1 at slight_left behind mc with dissolve 

    #need to add consequence of choice branching here
    officer1 "Still chasing pizza leads, huh?{w} Maybe you should stick to traffic duty."
    show asshole_cop2 at Position(xalign=-0.1) behind mc with dissolve 
    officer2 "Yeah, leave the real police work to us."
     
    show mc at center with move 
    show killer2 at right with dissolve
    mc "We’ll figure this out. I promise."


label scene_13:
    scene mc_car_noon with fade
    show mc at left
    # SPRITE need a sprite how pa holds a map(could be just a paper that looks like a map)RT
    show pa at right
    pa "We’ve checked every pizza place in the city"
    pa "Nothing matches the description"
    mc "It doesn’t make sense" 
    mc "There’s no way we missed it"
    pa "Unless it’s not on the map.{w=0.2} Or…{w=0.2} it doesn’t exist."
    mc "Either way, we’re running out of time."
    # SOUND of sirens
    play music "police_sirens.mp3" fadeout 1
    
    pa "You’ve got to be kidding me"
    mc "Let's go"

    stop music fadeout 1
  
label scene_14:
    # SOUND of closing door of a car
    play sound "car_door_close.mp3"
    scene city1 with fade
    show mc at left
    show pa at right

    pa "This is bad."
    pa "Two murders in two days?"
    pa "This town hasn’t seen something like this in decades."
    mc "Let’s see what we’re dealing with."
    
    #They need to approach the house
    #ART how they are approaching the house(check the scenario scene 14)
    play music "tension.mp3" fadeout 1 
    scene housemurder1 with fade
    pause 2.0
    show mc at left with dissolve
    show pa at right with dissolve

    pa "This is…{w} something else."
    mc "Same MO.{w} Brutal cuts,{w} same kind of message." 
    mc "And look—"
    pa "You think it’s connected?"
    mc "I know it is. The killer—where is he?"
    pa "Outside."
    pa "He’s in custody." 
    pa "But…{w=0.4} you’re gonna want to see this."
label scene_15:
    # BACKGROUND (possibly we have it) outside the house(scene 15)
    scene city1 with fade
    show mc at left with dissolve
    show killer1 at center with dissolve
    show pa at right with dissolve
    mc "What’s your name?"
    killer "I… I don’t know. I don’t know what happened."
    mc "What do you remember?" 
    killer "I was home. My wife was… she was making dinner. Then the phone rang. It was… it was a burger place. They were advertising something. And then…"
    mc "And then what?"
    killer "I don’t know! I woke up, and she was… she was…"
    pa "This is exactly like the first one. The phone call, the blackout, the murder. What the hell is going on?"
    mc "We’re missing something. Something big."
    stop music fadeout 1

label scene_16:
    # SOUND of phone calls, papers and people in rush
    scene hallway with fade
    play music "office_noise.mp3"
    show mc at left with dissolve
    show pa at right with dissolve
    # SPRITE need the PA with a neutral emotion
    pa "This is a nightmare. Two murders, two killers, both claiming they don’t remember a thing. And that phone call… it’s the only link we’ve got."
    mc "We need to track that call. Find out where it came from."
    pa  "Easier said than done. Without a name or a location, we’re shooting in the dark."
    # SOUND ringing phone and picking up the phone
    play sound "phone_ring.mp3"
    pause 4.0
    play sound "phone_hang_up.mp3"
    pause 3.0
    "Officer" "Detective!{w} It’s for you."
    


label scene_17:
    #show show another scene of only the mc holding phone and another generic background
    #ART of how mc is holding a phone
    mc "This is Detective \[MCs Name\]."
    mysterious "Listen carefully. If you want to stop the next murder, come to \[PLACE\] at midnight. Tell no one. If you do, you\’ll find nothing but an empty room."
    mc "Who is this? What do you want?"
    mysterious "Midnight. Don’t be late."
    # SOUND Beeping sound 
    play sound "phone_beeping.mp3"
    pause 4.0
    # SOUND of hanging the phone sound 
    #switch back to normal scene with fade
    play sound "phone_hang_up.mp3"
    pause
    pa "Who was that?"
    menu:
      "Tell him the truth": 
          jump told_truth
      "Lie and solve it on your own": 
          jump told_lie

    label told_truth:
      $ liedpa = False
      # show a screen message that pa remembered our honesty
      mc "It was… a tip. Someone called about the case. They said if I want to stop the next murder, I need to go to \[PLACE\] at midnight. Alone."
      pa "Alone? That sounds like a trap."
      mc "Yeah. But it’s the only lead we’ve got."
      pa "You sure about this? I don’t like the sound of it."
      mc "I don’t either. But if there’s a chance to stop another killing, I have to take it."
      pa "Alright. But if you’re going, I’m going with you. No arguments."
      mc "Fine. But we need to be careful. This guy… he’s playing games with us."
      pa "Yeah, I got that. Let’s move."

      jump scene_18_withpa

    label told_lie:
      $ liedpa = True
      mc "Just… a friend. Updating me on something. Nothing important."
      "pa raised an eyebrow showing distrust"
      jump scene_18_withnopa

label scene_18_withpa: # ending 1
    stop music fadeout 1
    scene abandoned with fade
    "The building stood like a forgotten relic of a time long past."
    "Its windows were shattered, its walls cracked and stained with years of neglect."
    "The air was heavy with the scent of decay,{w} and the only sound was the faint creak of the wind pushing against the broken door."
    "Somewhere inside, the answers waited."
    "Or maybe it was just another trap."
    "Either way, there was no turning back now."
    pa "This place gives me the creeps."
    pa "You sure this is the right spot?"
    mc "It’s the address he gave me." 
    mc "Let’s check it out."

    scene black with fade
    play sound "footsteps.mp3"
    pause 2.0
    show pa at left with dissolve
    show mc at right with dissolve
    pa "This place gives me the creeps. You sure this is the right spot?"
    mc "It’s the address he gave me. Let’s check it out."
    play sound "footsteps.mp3"
    pause 2.0
    #show the scene with chair and the phone
    scene abandonedinside with dissolve
    play sound "phone_ring.mp3" loop
    show pa at left with dissolve
    show mc at right with dissolve
    pa "What the hell..."
    pause 1.0
    play sound "phone_hang_up.mp3"
    mysterious "Alone."
    mysterious "Didn’t I tell you?"
    mysterious "Now go."
    mysterious "There’s another case for you."
    mysterious "Maybe if you hurry, it won’t be too late."

    play sound "phone_beeping.mp3"
    # pause 2.0
    # sound of slamming a phone
    pa "What was that?{w} Who was that?"
    mc "He knew.{p}He knew I'd bring you."
    pa "So this was a waste of time?{p}What now?"
    mc "We follow his lead.{w} There's another case.{p}And we're running out of time."
    jump ending1


label scene_18_withnopa:
    #ART of the car driving in the rain
    play music "calm.mp3" fadeout 1
    "Some cases pull you in."
    "They wrap themselves around you,{w} digging deeper and deeper until they become a part of you."
    "This one…" 
    "This one felt like it was just getting started."
    "And that call… it wasn’t just a lead. It was a challenge. A test. And I had no choice but to take it."

label scene_19:
    # ART of a gun on the table, bullets nearby and bottle on the same table
    "Midnight." 
    "That’s when it would happen." 
    "That’s when I’d get my answers." 
    "Or die trying."
    # ART how the mc puts go outside through the door (how I imagine this. mc is viewed from back and he just walks towards a white rectangle which is the door) 



label scene_20:
    stop music fadeout 1
    scene abandoned with fade
    "This was it. The place from the call. The place where everything would change."
    # ART image of how he is checking the gun. reference: https://img.freepik.com/premium-photo/reloading-gun-closeup-mens-hands-check-bullets-revolver-barrel-person-prepares-shots-fire_72464-1948.jpg
    # SOUND of gun click
    play sound "gun_loading.mp3"

label scene_21:
    scene abandonedinside with dissolve
    show mc at right with dissolve
    mc "I’m here!{w} Show yourself!"
    play music "tension.mp3" fadeout 1
    #SOUND music should become more intense(I think you get it Ion. As in scenario)
    show villain at left with fade
    show hostagealive at slight_left
    mysterious "Drop your weapon. Or he dies."
    "The only option I have in this moment is to obey"

    play sound "sliding_gun_on_the_floor.mp3"
    #SOUND of how he puts something down and how it glides on floor
    mysterious "Good. Now we can talk."
    mc "What is this?"
    mysterious "The address of the next murder. The choice is yours."
    # flasheffect
    play sound "gun_shot.mp3" 
    scene abandonedinside with flash_white
    hide villain
    show hostagedead
    # SOUND Intense music, maybe we can make the previous music faster or louder
    "show text"
    return


label ending1:
    nvl show
    nvl "And so, the detectives stood in the hollow silencce of a forgotten place, their hopes of answers shattered like the broken windows around them." 
    nvl "The caller has vanished, leaving only murder before only a cruel reminder."
    nvl "They were always one step behind."
    nvl hide dissolve
    scene black with fade
    pause 2.0
    play sound "clock_ticking.mp3"
    pause 10.0
    
