
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
image mc_smoke = "mcsmoke.png"
image mc_tel = "mctel.png"
image battlefield2 = "battlefield.png"



# Start of the game
label start:
    jump scene_1
label scene_1:
    scene doctor_office with fade
    show dr at left
    show mc at right

    doctor "Let's start simple. What do you remember about yourself?"
    mc "Not much. My name, my training... fragments of something else."
    doctor "And the last thing you recall before 'it' happened?"

label scene_2:
    scene black with fade
    play sound "static.mp3"  # Add glitch sound effect
    show battlefield2:
        alpha 0.5 blur 50
        linear 0.3 alpha 1.0 blur 0
    with vpunch

    mc "(voice broken) I was...{w=0.5} a soldier.{w} Special Corps.{w=0.3} But the details..." 

    # Memory glitch effect
    show battlefield2:
        xalign 0.5 yalign 0.5
        linear 0.1 xalign 0.51 yalign 0.51
        linear 0.1 xalign 0.49 yalign 0.49
        repeat 3
    with hpunch

    show terrorist at center:
        alpha 0.0
        linear 0.2 alpha 1.0
        linear 0.2 alpha 0.5
        repeat

    play sound "glitch.mp3"

    mc "(strained) ...are...{w=0.7} blurred."

    # Rapid flash sequence
    scene black with Dissolve(0.1)
    show terrorist at center with pixellate
    hide terrorist with dissolve
    show battlefield2 with vpunch
    hide battlefield2 with dissolve
    show terrorist at left with hpunch
    hide terrorist with dissolve

    play sound "heartbeat.mp3"
    show battlefield2:
        matrixcolor TintMatrix("#ff0000")  # Red tint
        alpha 0.7
    with vpunch

    mc " Had to...{w} capture...{w} someone alive... {w} someone important"
    show terrorist at center with hpunch
    mc "(whisper) ...I succeeded."
    
    play sound "explosion.mp3"
    scene black with vpunch
    stop sound fadeout 1.0

label scene_3:
    scene doctor_office with fade
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
    doctor "That's enough for today." 
    "*Doctor hands you a small bottle of pills.*"
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
label scene_4:
    scene city1 with fade
    play music "calm.mp3" fadein 1.0
    mc "(Narrating) It was one of those rare peaceful days. The kind where the city breathes in slow motion, and you can almost pretend nothing bad ever happens."
    mc "(Narrating) No calls, no reports, no paperwork. Just a free day to do absolutely nothing."
    mc "(Narrating) I went home. Laid on the bed. And let the silence take over."

label scene_5:
    scene apartment_night with fade
    pause 1
    play sound "phone_ring.mp3"
    pause 1.4  # Let the sound play for exactly 1 second
    stop sound fadeout 0.7  # Very quick fadeout to avoid abrupt cutoff
    show mc_tel at center
    mc "(Groggily) Yeah?"
    operator "(Urgent tone) Detective. We need you!!. Now!!."
    mc "(Sleepy) What happened?"
    operator "Murder. First in years. Address is on [Street_Name]  everyone's already there."

label scene_6:
    scene crimescene1 with fade
    play music "tension.mp3" 
    "*The detective approaches PA at the crime scene*"
    scene crimescene2 with fade
    show mc at right
    show pa at left
    mc "Give me the rundown."
    pa "(Shaking his head) You picked a hell of a first case."
    mc "That bad?"
    pa "Worse. The guy's hands covered in blood. Says he didn't do it."
    mc "And the victim?"
    pa "(Lowering voice) You'll want to see for yourself."
    
label scene_7:
    scene murder_house with fade
    play music "suspense_soundtrack.mp3" 
    "*They enter the house, the metallic smell of blood hitting them immediately*"
    show mc at right
    show pa at left
    
    pa "Gruesome scene. Victim's in bad shape. What do you want to check first?"
    
    menu:
        "Focus on the bloodied message":
            show mc at center with move
            "You approach the bloodied scrawl on the wall: {b}\"IT WASN’T ME\"{/b}"
            mc "(This message… it’s too deliberate. Almost like he’s trying to convince someone. But who?)"
            pa "Creepy, huh? Like he’s trying to shift the blame."
            mc "Or maybe he’s telling the truth. Either way, we need to check everything."
            jump examine_body
            
        "Examine the victim’s body":
            show mc at center with move
            "You kneel by the covered body, lifting the sheet slightly."
            mc "(The cuts… they’re too precise. This wasn’t a crime of passion. Someone knew what they were doing.)"
            pa "Brutal, isn’t it? Whoever did this… they weren’t messing around."
            mc "Yeah. But why? And why leave a message like that?"
            jump examine_message
            
        "Inspect the hanging phone":
            show mc at center with move
            "You move to the old rotary phone hanging off the hook."
            mc "(Why is it hanging like that? Almost like someone dropped it in a hurry.)"
            pa "You think the call has something to do with this?"
            mc "Maybe. The killer called 911 himself. We need to check this."
            jump examine_body_second

    label examine_body:
        "You kneel by the covered body, lifting the sheet slightly."
        mc "(Defensive wounds on the arms. Throat cut clean. Professional work.)"
        pa "ME says time of death was around midnight. Same time as the 911 call."
        jump examine_phone

    label examine_message:
        "You approach the bloodied scrawl on the wall: {b}\"IT WASN’T ME\"{/b}"
        mc "(Smear patterns suggest the message was written after the blood dried.)"
        pa "You think the killer came back to leave this?"
        mc "Or someone else wanted us to find it."
        jump examine_phone

    label examine_body_second:
        "You return to the body, carefully examining the wounds."
        mc "(No signs of struggle. Victim knew the attacker.)"
        pa "Wallet's still here. Not a robbery."
        jump examine_message_second

    label examine_phone:
        "You pick up the humming receiver, checking the dial numbers."
        mc "(Last dialed number matches the 911 call timestamp.)"
        pa "So the killer really did call it in himself. Why?"
        mc "Guilt? Or setting up a scene..."
        jump final_investigation

    label examine_message_second:
        mc "(Letters are shaky but deliberate. Someone was panicking when they wrote this.)"
        pa "You think it's genuine?"
        mc "Either way, they wanted us to see it."
        jump final_investigation

    label final_investigation:
        pa "What's your take, detective?"
        mc "This was personal. Calculated. That message is either a confession..."
        mc "...or someone's desperate attempt to frame another."
        "*The ambient police radio chatter grows louder outside*"
        jump scene_8

label scene_8:
    scene interrogation with fade
    play music "tension.mp3" fadein 1.0
    show killer1 at left
    show mc at right
    show pa behind mc at right:
        xalign 0.7

    
    mc  "Let's start from the beginning. What do you remember?"
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

            "Respond rudely":
                $ officer_attitude = "rude"
                mc  "Maybe if you did your jobs, I wouldn't have to clean up your mess."
                officer2 "Watch your mouth, new guy."
                "*PA pulls you away before things escalate*"
                "The officers will remember your attitude."

        scene black with fade
        if officer_attitude == "rude":
            play sound "audio/door_slam.ogg"
        else:
            play sound "audio/door_close.ogg"

        jump scene_9

label scene_9:
    scene policedepartment with fade
    show pa at left
    show mc at right
    "*The detective and PA regroup in the hallway*"
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

label scene_10:
    scene mc_car_night with fade
    "*The detective lights a cigarette, the glow reflecting in his tired eyes*"
    show mc_smoke at right
    "Some cases stick with you.{w} Not because of the blood, or the bodies, or the mess.{w} But because of the questions they leave behind."
    "This one...{w=0.3} this one felt different.{w} Like it wasn't just about the killer or the victim.{w} Like it was about something bigger."

label scene_11:
    scene mc_house with fade
    show pa at left
    show mc at right
    "*Next morning, PA bursts into the detective's house*"
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