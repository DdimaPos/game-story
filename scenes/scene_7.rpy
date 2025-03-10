label scene_7:
    scene murder_house with fade
    "*They enter the house, the metallic smell of blood hitting them immediately*"
    show  mc_intrigued at right
    show  pa_depressed at left:
        ypos 1200
    pa "Gruesome scene. Victim's in bad shape. What do you want to check first?"
    hide pa_depressed
    show  pa at left:
        ypos 1200
    
    menu:

        "Focus on the bloodied message":
            show mc_intrigued at center with move
            "You approach the bloodied scrawl on the wall: {b}\"IT WASN’T ME\"{/b}"
            mc "(This message… it’s too deliberate. Almost like he’s trying to convince someone. But who?)"
            hide pa 
            show pa_intrigued at left:
                ypos 1200
            pa "Creepy, huh? Like he’s trying to shift the blame."
            mc "Or maybe he’s telling the truth. Either way, we need to check everything."
            jump examine_body
            
        "Examine the victim’s body":
            show mc_intrigued at right with move
            "You kneel by the covered body, lifting the sheet slightly."
            mc "(The cuts… they’re too precise. This wasn’t a crime of passion. Someone knew what they were doing.)"
            pa "Brutal, isn’t it? Whoever did this… they weren’t messing around."
            mc "Yeah. But why? And why leave a message like that?"
            jump examine_message
            
        "Inspect the hanging phone":
            show mc_intrigued at right with move
            "You move to the old rotary phone hanging off the hook."
            mc "(Why is it hanging like that? Almost like someone dropped it in a hurry.)"
            pa "You think the call has something to do with this?"
            mc "Maybe. The killer called 911 himself. We need to check this."
            jump examine_body_second

    label examine_body:
        show mc_intrigued at right with move
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
        scene black with fade
        jump scene_8