# Define characters
define doctor = Character("Doctor", color="#a8d8ea")
define mc = Character("Detective", color="#c0c0c0")
define pa = Character("PA", color="#808080")
define killer = Character("Killer", color="#ff6666")
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
image asshole_cop1 = "assholecop1.png"
image asshole_cop2 = "assholecop2.png"

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

label start:

label scene_12:

    ####SCREEN 12
    scene jail
    show mc at slight_left
    with slowdissolve
    mc "We need to talk.{w} About the pizza place.{w} What was the name?"

    #barely audible
    show killer2 at slight_right
    with slowdissolve
    killer "(barely audible) I...{w=0.5} I don't remember.{w=0.7} It was something… {w=1} something simple."
    mc "Think.{w} Was it a man or a woman who called?"
    killer "A man.{w=0.3} Just a man."
    killer "And…{w} there was music.{w} I don’t know why,{w=0.5} but it felt… {w=1}familiar"
    mc "What kind of music?"
    killer "I don’t know. I can’t remember. But it’s important. I know it is."
    "Detective exchanges a look with PA, who shrugs helplessly."
    mc "We’ll find it.{w} But you need to help us.{w} Anything else you remember?"
    
    show killer2 at shake_animation
    killer "{size=+7}Please…!!!{/size}{w=0.3} You have to believe me!{w=0.3} It wasn’t me!{w=0.3} I didn’t do this!"
    "MC nods, but before he can respond, the two officers from earlier appear, their mocking laughter echoing down the hallway."


    hide killer2 with dissolve
    show mc at right with move
    show asshole_cop1 at slight_left behind mc with dissolve 
    officer1 "Still chasing pizza leads, huh?{w} Maybe you should stick to traffic duty."
    show asshole_cop2 at Position(xalign=-0.1) behind mc with dissolve 
    officer2 "Yeah, leave the real police work to us."
     
    show mc at center with move 
    show killer2 at right with dissolve
    mc "We’ll figure this out. I promise."


label scene_13:
    scene mc_car_noon with fade
    show mc at left
    show pa at right
    pa "We’ve checked every pizza place in the city"
    pa "Nothing matches the description"
    mc "It doesn’t make sense" 
    mc "There’s no way we missed it"
    pa "Unless it’s not on the map.{w=0.2} Or…{w=0.2} it doesn’t exist."
    mc "Either way, we’re running out of time."
    # SOUND of sirens
    pa "You’ve got to be kidding me"
    mc "Let's go"
  
label scene_14:
    scene crimescene2 with fade
    show mc at left
    show pa at right

    pa "This is bad."
    pa "Two murders in two days?"
    pa "This town hasn’t seen something like this in decades."
    mc "Let’s see what we’re dealing with."
    
    #They need to approach the house
    
    pa "This is… something else."
    mc "Same MO. Brutal cuts, same kind of message. And look—"
    pa "You think it’s connected?"
    mc "I know it is. The killer—where is he?"
    pa "Outside. He’s in custody. But… you’re gonna want to see this."

label scene_15:
    mc "What’s your name?"
    killer "I… I don’t know. I don’t know what happened."
    mc "What do you remember?" 
    killer "I was home. My wife was… she was making dinner. Then the phone rang. It was… it was a burger place. They were advertising something. And then…"
    mc "And then what?"
    killer "I don’t know! I woke up, and she was… she was…"
    pa "This is exactly like the first one. The phone call, the blackout, the murder. What the hell is going on?"
    mc "We’re missing something. Something big."


label scene_16:
    pa "This is a nightmare. Two murders, two killers, both claiming they don’t remember a thing. And that phone call… it’s the only link we’ve got."
    mc "We need to track that call. Find out where it came from."
    pa  "Easier said than done. Without a name or a location, we’re shooting in the dark."
    officer "Detective! It’s for you."


label scene_17:
    #image of how mc is holding a phone
    mc "This is Detective [MC’s Name]."
    misterious_caller "Listen carefully. If you want to stop the next murder, come to [PLACE] at midnight. Tell no one. If you do, you’ll find nothing but an empty room."
    mc "Who is this? What do you want?"
    misterious_caller "Midnight. Don’t be late."
    
    # hang the phone sound 
    pa "Who was that?"
    mc "Just… a friend. Updating me on something. Nothing important."

label scene_18:
    "Some cases pull you in. They wrap themselves around you, digging deeper and deeper until they become a part of you. This one… this one felt like it was just getting started."
    "And that call… it wasn’t just a lead. It was a challenge. A test. And I had no choice but to take it."

label scene_19:
    
    "Midnight. That’s when it would happen. That’s when I’d get my answers. Or die trying."



label scene_20:
    "This was it. The place from the call. The place where everything would change."


label scene_21:
    mc "I’m here!{w} Show yourself!"
    misterious_caller "Drop your weapon. Or he dies."
    misterious_caller "Good. Now we can talk."
    mc "What is this?"
    misterious_caller "The address of the next murder. The choice is yours."

    return
