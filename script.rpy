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
image interrogation = "interrogation.png"
image hallway = "policedepartment.png"
image mc_car_night = "MCcarNight.png"
image mc_house = "MCliving.png"
image jail = "jail.png"
image abandoned = "abandoned.png"
image abandoned_inside = "abandonedinside.png"
image murder_house = "housemurder2.png"

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
    linear 0.1 xoffset -5
    linear 0.1 xoffset 5
    repeat

label start:

    scene bg room

    ####SCREEN 12
    scene jail
    show mc at slight_left
    with slowdissolve
    mc "We need to talk. About the pizza place. What was the name?"
    

    #barely audible
    show killer2 at slight_right
    with slowdissolve
    killer "(barely audible) I...{w=0.5} I don't remember.{w=0.7} It was something… {w=1} something simple."
    mc "Think. Was it a man or a woman who called?"
    killer "A man. Just a man. And… there was music. I don’t know why, but it felt… {w=1}familiar"
    mc "What kind of music?"
    killer "I don’t know. I can’t remember. But it’s important. I know it is."
    "Detective exchanges a look with PA, who shrugs helplessly."
    mc "We’ll find it. But you need to help us. Anything else you remember?"
    
    show killer2 at shake_animation
    killer "Please… you have to believe me. It wasn’t me. I didn’t do this."
    "MC nods, but before he can respond, the two officers from earlier appear, their mocking laughter echoing down the hallway."


    hide killer2 with dissolve
    show mc at right with move
    show asshole_cop1 at slight_left behind mc with dissolve 
    officer1 "Still chasing pizza leads, huh? Maybe you should stick to traffic duty."
    show asshole_cop2 at Position(xalign=-0.1) behind mc with dissolve 
    officer2 "Yeah, leave the real police work to us."
     
    show mc at center with move 
    show killer2 at right with dissolve
    mc "We’ll figure this out. I promise."

    hide asshole_cop1 with dissolve
    hide asshole_cop2 with dissolve
    "some text"


    return
