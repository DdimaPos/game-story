
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
image  mc = "MC.png"
image  mc_angry = "MCAngry.png"
image  mc_depressed = "MCDepressed.png"
image  mc_intrigued = "MCIntrigued.png"
image  mc_phone = "MCPhone.png"
image  mc_scared = "MCScared.png"
image  pa = "PANormal.png"
image  pa_angry = "PAAngry.png"
image  pa_depressed = "PADepressed.png"
image  pa_scared = "PAScared.png"
image  pa_intrigued = "PAIntrigued.png" 
image doctor = "dr.png"
image killer = "killer1.png"
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
image hallway = "PoliceDepartment.png"
image hallway2 = "PoliceDepartment1.png"
image mc_car_night = "MCcarNight.png"
image mc_house = "MCliving.png"
image jail = "jail.png"
image abandoned = "abandoned.png"
image abandoned_inside = "abandonedinside.png"
image murder_house = "housemurder2.png"
image mc_smoke = "mcsmoke.png"
image mc_tel = "mctel.png"
image battlefield2 = "battlefield.png"
image pills = "pillshere.png"

# Transitions
define slowdissolve = Dissolve(0.5)
 

transform shake_animation:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    repeat

#Variables 
python:
    rude = False

# Start of the game
label start:
    jump scene_1
