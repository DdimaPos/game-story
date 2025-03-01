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


# Start of the game
label start:
    scene doctor_office with fade
    show dr at left
    show mc at right

    doctor "Let's start simple. What do you remember about yourself?"
    mc "Not much. My name, my training... fragments of something else."
    doctor "And the last thing you recall before 'it' happened?"
    
    scene battlefield with dissolve
    show terrorist at center
    mc "I was a soldier. Special Corps. But the details are... blurred."
    
# here we need some battlefield images
    
    mc "I had a mission. Capture someone alive. Someone important. I... I succeeded."
    
    play sound "explosion.wav"
    scene black with vpunch
    stop sound fadeout 1.0
    
    scene doctor_office with fade
    show dr at left
    show mc at right
    doctor "And then?"
    mc "Nothing. Just... waking up in a hospital. Six months in a coma."
    
    doctor "Your records say you were awarded medals for your service."
    
    # Medal flashback
    menu:
        "Show medal flashback?":
#Need photo for medals
            pause 2.0
            scene doctor_office with fade
            show dr at left
            show mc at right
    
    mc "Yeah... Guess I did something right. Not that it matters now."
    doctor "Why do you say that?"
    mc "Because I can't go back. The trauma, the amnesia... I'm no longer fit for special ops. So they sent me here."
    doctor "Here?"
    mc "A quiet town. A detective job. Small cases. Small crimes. Trying to put myself back together."
    doctor "(Doctor nods, hands a small bottle of pills) That’s enough for today. Here—take these. One pill a day. Don’t forget."

    scene city1 with fade
    play music "calm.mp3" fadein 1.0
    mc "(Narrating) It was one of those rare peaceful days. The kind where the city breathes in slow motion, and you can almost pretend nothing bad ever happens."
    mc "(Narrating) No calls, no reports, no paperwork. Just a free day to do absolutely nothing."
    mc "(Narrating) I went home. Laid on the bed. And let the silence take over."
    
    scene apartment_night with fade
    play sound "phone_ring.wav"
    pause 1.5
    mc "(Groggily) Yeah?"
    operator "(Urgent tone) Detective. We need you!!. Now!!."
    mc "(Sleepy) What happened?"
    operator "Murder. First in years. Address is on [Street_Name]  everyone's already there."
    
    scene crimescene1 with fade
    play music "tension.mp3" fadein 1.0
    "*MC approaches PA at the crime scene*"
    scene crimescene2 with fade
    show mc at right
    show pa at left
    mc "Give me the rundown."
    pa "(Shaking his head) You picked a hell of a first case."
    mc "That bad?"
    pa "Worse. The guy's hands covered in blood. Says he didn't do it."
    mc "And the victim?"
    pa "(Lowering voice) You'll want to see for yourself."
    
    scene murder_house with fade
    pause 1.0
    "*They enter the house, the metallic smell of blood hitting them immediately*"
    show mc at right
    show pa at left
    mc "(staring at wall) What the hell happened here?"
    pa "(pointing) That's what we're trying to figure out. The victim was mauled. Cuts everywhere."
    mc "(kneeling by body) And the suspect?"
    pa "(leaning in) Sitting outside. Barely talking. Just keeps repeating that it wasn't him."
    "*MC scans the room, eyes landing on an old rotary phone hanging off the hook.*"
    mc "The call. The suspect is the one who called this in?"
    pa "Yeah. He called 911 himself."
    "*MC picks up the phone, the line still faintly humming. He clicks it off, deep in thought.*"
    mc "Something about this doesn’t sit right. We need to check this call."
    "*PA nods. The investigation begins.*"


    scene interrogation with fade
    show killer1 at left
    show mc at right
    "*MC sits across from the trembling suspect*"
    mc "Let's start from the beginning. What do you remember?"
    killer "(sobbing) I... I don't know. I swear, I don't remember doing this. I woke up, and he was... he was already..."
    mc "(leaning forward) You called the police. Why?"
    killer "(shaking) I... I thought I was helping. I didn't know what else to do."
    mc "What about the phone call? The one before this happened. Do you remember it?"
    killer "(frowning): Yeah… yeah, I do. It was… some pizza place. They were advertising a deal or something."
    mc "What did they say? Anything specific?"
    killer "(struggling to recall) It was a man’s voice. No background noise, just… some music. I don’t know why, but it felt familiar. Like I’d heard it before."
    mc "And then?"
    killer "Then… nothing. Everything went blank. Next thing I knew, I was standing over him, and… and…"
    "*He breaks down, sobbing.*"

    hide mc
    hide killer1
    show assholecop1 at left
    show assholecop2 at right
    "*Two officers burst into the room*"
    officer1 "(sneering) That's enough. We'll take it from here."
    officer2 "(mocking) Guys like him don't deserve your time. He's just playing dumb."
    "*(MC exchange a look with them and reluctantly leave the room.)*"


    scene policedepartment with fade
    show pa at left
    show mc at right
    "*MC and PA regroup in the hallway*"
    pa "(crossing arms) So, what do you think? You buying his story?"
    mc "(pacing) I don't know. But something's off. The phone call, the music, the way he's reacting... it doesn't add up."
    pa "(sighing) You think he's telling the truth? That he didn't do it?"
    mc "(stopping) I think there's more to this than we're seeing. And I'm not ready to write him off just yet."
    pa "(smirking) You're gonna make this harder than it needs to be, aren't you?"
    mc "(half-smile) Wouldn't be the first time."
    pa "(nodding) Alright, fine. Where do we start?"
    mc "(determined) That pizza place. We need to find out who called him."
    pa "You really think a pizza ad is connected to this?"
    mc "I don’t know. But it’s the only lead we’ve got."
    "*They head out, the weight of the case hanging heavy in the air.*"

    scene mc_car_night with fade
    #Here we need an image of him smoking
    "*MC lights a cigarette, the glow reflecting in his tired eyes*"
    "Some cases stick with you.{w} Not because of the blood, or the bodies, or the mess.{w} But because of the questions they leave behind."
    "This one...{w} this one felt different.{w} Like it wasn't just about the killer or the victim.{w} Like it was about something bigger."

    scene mc_house with fade
    show pa at left
    show mc at right
    "*Next morning, PA bursts into MC's house*"
    mc "What are you doing here?"
    pa "(impatient) We're detectives, remember? I know where you live. And I took the bus. Now, can we get moving?"
    mc "(sighting) Fine. Let's go."

label scene_11_1:
    scene policedepartment with fade
    show pa at left
    show mc at right
    "*They return to the station for updates*"
    pa "(serious) Bad news. The killer's completely unresponsive now."
    mc "(leaning on desk) So, no chance of getting anything else out of him?"
    pa "(shaking head) Not unless he snaps out of it. And even then..."
    mc "(straightening up) Then we'll have to work with what we've got. That pizza place - what's the plan?"
    pa "(pulling out list) I've got a list of every pizza joint in the city. We'll start with the ones closest to the crime scene and work our way out."
    mc "(heading to door) Let's move."