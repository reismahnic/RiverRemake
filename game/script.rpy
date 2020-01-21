# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define joseph = Character("Joseph")
define diane = Character("Diane")
define cheryl = Character("Cheryl")
define father = Character("Father")
define blank = Character("")


#Setting up images:
#Portraits:
#Scene 1:
image joseph Scene1 = "js1neutralport"
image joseph Scene1Sad = "js1sadport"
image joseph Scene1Happy = "js1happyport"
image diane Scene1 = "ds1neutralport"
image diane Scene1Sad = "ds1sadport"
image diane Scene1Happy = "ds1happyport"

#Scene 2:
image joseph Scene2 = "js2neutralport"
image joseph Scene2Angry = "js2angryport"
image diane Scene2Angry = "ds2angryport"
image diane Scene2 = "ds2neutralport"

#Scene 3:
image joseph Scene3 = "js3neutralport"
image joseph Scene3Happy = "js3happyport"
image cheryl Scene3 = "cs3neutralport"
image cheryl Scene3Happy = "cs3happyport"

#Cutaways:
#Scene 1:
image holdingHands = "handsholdingport"
image dianeOnPhone = "dianeonphoneport"

#Scene 2:
image teaKettle = "teakettleport"

#Scene 3:
image josephWalking = "josephwalkingport"
image josephWalkingReversed = "josephwalkingreversedport"
image guitarPlaying = "guitarplayingport"
image coinsIntoCase = "coinsintocaseport"
image onBench = "onbenchport"

#Defining Audio
#Music
define audio.scene1Music = "audio/music/scene1Edited.ogg"
define audio.scene2angryMusic = "audio/music/scene2angryEdited.ogg"
define audio.scene2happyMusic = "audio/music/scene2happyEdited.ogg"
define audio.scene3Music = "audio/music/scene3Edited.ogg"
define audio.scene3Guitar = "audio/music/superhappyEdited.ogg"
define audio.distortedMusic = "audio/music/distortedMusic.ogg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene blackbackground
    pause 1
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    $_dismiss_pause = False
    stop music fadeout 1.0
    play music distortedMusic
    blank "I was born on a farm in Alberta, along the Rockies."
    blank "My mother passed when I was still too young to work, and my father cared for my sister and I."
    blank "When I was eight years old, I experienced something very odd."
    blank "I was walking through the high grass near the river, when a bright orb appeared in the sky."
    blank "It slowly descended, until it hovered in place just before me."
    blank "I experienced something that I do not understand."
    scene 2015background with dissolve
    stop music fadeout 1.0
    pause 3
    scene blackbackground with dissolve
    pause 1
    scene sceneonebackground with dissolve
    play music scene1Music
    pause 2
    show joseph Scene1 at left
    show diane Scene1 at right
    with dissolve
    diane "What do you think it was?"
    joseph "At the time I thought it was some kind of greater power, calling down to me."
    diane "And now?"
    menu:
        "I still believe it may have been God.":
            $isreligious = True;
            jump isReligious

        "It was something. But I don't believe in a higher power.":
            $isreligious = False;
            jump isntReligious

    label isReligious:
        joseph "I think it was some kind of higher power. Talking to me. Telling me I would be ok."
        diane "You've never told me about this."
        joseph "I used to avoid thinking about it."
        diane "I like it, Dad."
        jump continueconversation1

    label isntReligious:
        diane "You saw something, though. I can tell."
        joseph "More and more I think about it, the more I think I just saw what I needed to see, and that's all there was to it."
        joseph "Something that would get me as far as possible from..."
        pause(2)
        joseph "It was lonely out there. Just had my sister."
        diane "Aunt Cheryl talks enough for four people."
        show joseph Scene1Happy at left
        joseph "Heh! Isn't that the truth..."
        jump continueconversation1

    label continueconversation1:
    pause(3)
    show joseph Scene1Sad at left
    joseph "I'm probably not leaving this hospital, Diane."
    show diane Scene1Sad at right
    diane "Dad..."
    hide joseph Scene1Sad
    hide diane Scene1Sad
    with dissolve
    show holdingHands at center with dissolve
    pause(2)
    hide holdingHands with dissolve
    show joseph Scene1 at left
    show diane Scene1Sad at right
    with dissolve
    joseph "Do you remember when you were in high school, and I was in a car wreck?"
    show diane Scene1 at right
    diane "Yes."
    joseph "I was going... had to be hundred fifty, hundred sixty. Just outside of Montreal."
    joseph "Your Mom had left me and I didn't know what to do."
    diane "I remember."
    joseph "And I remember dangling upside down, and struggling to get my seatbelt unhooked..."
    joseph "And then I stopped, and just hung there. I gave up."
    if isreligious == True:
        joseph "I thought, please, God, come to me, speak to me like you spoke to me that day on the farm."
    else:
        joseph "I didn't know what to do. I was too scared to survive, and not religious enough to pray."
    pause(2)
    show joseph Scene1Happy at left
    joseph "I'm glad I lived."
    diane "I know."
    show joseph Scene1 at left
    joseph "I'm glad you're here. Right now, I mean."
    pause(1)
    diane "I know."
    pause(1)
    joseph "How are things at home?"
    menu:
        "What's Paul up to lately?":
            jump askAboutPaul

        "Are Liz and Emma doing ok?":
            jump askAboutLizEmma

        "How have you been?":
            jump askAboutDiane

        "How's that computer program of yours coming along?":
            jump askAboutIAC

    label askAboutPaul:
        diane "He's taking retirement hard."
        show joseph Scene1Happy at left
        joseph "I did too, at first."
        diane "He's been seeing his friends more, though."
        show joseph Scene1 at left
        joseph "From work?"
        diane "Mostly. Sometimes his best friend he grew up with visits."
        joseph "That's good."
        jump continueconversation2

    label askAboutLizEmma:
        diane "Liz is doing fine. She's been looking up and down for colleges."
        joseph "Oh, yeah. What's she majoring in?"
        diane "She doesn't know yet. Just getting her general degree."
        diane "Emma, of course, getting straight A's in everything. You know her."
        show joseph Scene1Happy at left
        joseph "Well, I'd like to see both of them."
        diane "I know, Dad. They're just both so busy now..."
        show joseph Scene1 at left
        jump continueconversation2

    label askAboutDiane:
        diane "I'm fine."
        show joseph Scene1Sad at left
        joseph "You've been coming here too often, Diane."
        diane "I said I'm fine, Dad."
        show joseph Scene1 at left
        joseph "Because I can-"
        diane "Dad."
        joseph "You're fine."
        diane "I'm fine."
        jump continueconversation2

    label askAboutIAC:
        diane "IAC is... well, astonishing."
        show joseph Scene1Sad at left
        joseph "I know that I wasn't exactly... the best... about encouraging you. When you were growing up."
        joseph "With the computer stuff, I mean. Assuming you couldn't learn to- what an idiot I was."
        diane "Well, your weird... old person sexism only made me more determined to prove you wrong."
        show joseph Scene1Happy
        joseph "Ha! I guess so."
        joseph "You're so brilliant, Diane. The things you've done. You've changed the world."
        show joseph Scene1
        joseph "I'm sorry, though. I really am."
        diane "...Thank you."
        jump continueconversation2

    label continueconversation2:
        pause(1)
        joseph "Diane?"
        diane "What?"
        joseph "When I go, I want them there. Liz and Emma."
        show diane Scene1Sad at right
        joseph "For the funeral."
        diane "Of course they'll be there, Dad."
        show diane Scene1 at right

    menu:
        "I didn't go to my father's funeral.":
            $attendedfathersfuneral = False;
            jump didntgofuneral

        "I went to my father's funeral.":
            $attendedfathersfuneral = True;
            jump attendedfuneral

    label didntgofuneral:
        show joseph Scene1Sad at left
        joseph "I'll never forgive myself for what I did."
        joseph "I was angry, but missing my own father's funeral..."
        diane "It's alright. I'm sure he knew you cared about him."
        joseph "It was disgusting. I was a coward."
        if isreligious == True:
            joseph "And I'll pay for it, when the time comes."
            diane "That wasn't a sin, Dad."
            joseph "Of course it was."
        else:
            joseph "You can't let go of that."
        jump continueconversation3

    label attendedfuneral:
        joseph "Burying my father was..."
        show joseph Scene1Sad at left
        joseph "He and I never got closure. At all. I hadn't seen him since I left home."
        diane "I know. Mom told me."
        joseph "Well, I'll never feel good about our relationship."
        show joseph Scene1 at left
        joseph "But I know that Cheryl appreciated it. And that's why I went."
        joseph "Anyway I'm glad I went."
        if isreligious == True:
            joseph "God only knows if the old man would've wanted me there."
        else:
            joseph "I still don't know if the old man wouldn've wanted me there."
        joseph "Anyway, I want you there for mine."
        diane "I will be, Dad."
        jump continueconversation3

    label continueconversation3:
    diane "You've never talked about him before. Not like this."
    show joseph Scene1 at left
    joseph "I'm at the point where I won't get to later."
    joseph "Nobody deserves to be completely forgotten. Not even him."
    diane "What... what happened between you two?"
    joseph "I, umm..."
    joseph "After my mother died, I became the target of his grief."
    joseph "One day I had to stand up to him. And I did."
    joseph "The next day, I left home. And I never saw him again."
    if attendedfathersfuneral == True:
        joseph "Until the funeral."
    else:
        pause(1)
    diane "When you left... did you hate him?"
    menu:
        "Oh, I sure did.":
            $hatedfather = True;
            jump hatedHim

        "No, I didn't hate him":
            $hatedfather = False;
            jump didntHateHim

    label hatedHim:
        show joseph Scene1Happy
        joseph "Oh, I sure did."
        joseph "I hated him like no other."
        show joseph Scene1
        if attendedfathersfuneral == False:
            joseph "And even when I was forty, and heard he died, I still hated him."
            joseph "Part of me still hates him. And the other part of me is just sad."
            joseph "What's happened happened. Can't do anything about it."
            joseph "I wish I'd gone to his funeral..."
        else:
            joseph "But by the time he died, I was forty years old, and realized I would never understand him."
            joseph "Part of me still hates him. And the other part of me is just sad."
            joseph "What's happened happened. Can't do anything about it."
            joseph "I'm glad I went to his funeral."
            diane "Thank you for telling me about him."
            joseph "I should have a long time ago."
            joseph "I'm sorry."
            pause(1)
        jump continueconversation4

    label didntHateHim:
        joseph "No. I was angry, but... I knew he didn't understand."
        joseph "I would never understand him either. We were just too different."
        joseph "Growing up, he'd tell me how I was just like my mother."
        joseph "And he was right, I was."
        joseph "I couldn't live with him anymore. So I left."
        if attendedfathersfuneral == True:
            diane "It's good that you went to the funeral."
            joseph "Yes, it was."
        else:
            diane "Why didn't you go to the funeral?"
            joseph "I left him and never came back. How could I?"
            pause(1)
            joseph "How could I."
            diane "Thank you for telling me about him."
            joseph "I should have a long time ago."
            joseph "I'm sorry."
            pause(2)
        jump continueconversation4

    label continueconversation4:
    diane "Dad, you know how after I divorced Eric, I was just working on IAC for a year straight?"
    menu:
        "I remember. I didn't understand what you were doing.":
            $understoodIAC = False;
            jump didntUnderstandIAC

        "Of course I do. I was so proud of you.":
            $understoodIAC = True;
            jump understoodIAC

    label didntUnderstandIAC:
    show joseph Scene1Sad
    joseph "I remember. I didn't understand."
    diane "Well... I was furious with you."
    joseph "I know."
    if hatedfather == True:
        diane "And I felt like I could have walked out of your life too."
        joseph "I know."
        diane "For you to say..."
        joseph "It was stupid. And I still don't understand why I said what I said."
        joseph "I'm sorry."
        diane "Don't be. It was twenty years ago."
        diane "I guess I'm just saying... I understand. How you felt when you left your Dad."
        show joseph Scene1
    else:
        diane "I didn't hate you though."
        show joseph Scene1
        joseph "Well, you're like me. You always have been."
        diane "You couldn't hate your father, I can't hate mine."
        joseph "I don't understand how it works. How we work. But I don't mind."
    jump continueconversation5

    label understoodIAC:
    joseph "Of course I do."
    diane "When I got divorced... it felt like my life was being torn apart."
    diane "And all I had was IAC."
    if isreligious == True:
        joseph "Well, sure. You know, when I went through my divorce, we got a lot of comments from our church."
        joseph "It was '73. People gave us a hard time."
        joseph "I lost some friendships, and I felt completely alone."
        joseph "So all I'd do all day was work at the shop. It was the only thing that could keep me occupied."
        diane "And all I felt like I had was IAC."
        diane "And... you and Mom."
    else:
        joseph "Well, sure. My divorce was no party. I understood."
        diane "Your understanding was what got me through all of that."
    if hatedfather == True:
        diane "I have to wonder if you and your father could have had a relationship, if you had tried to be more understanding."
    else:
        diane "Do you think you and your father could have worked things out?"
        diane "You say there wasn't understanding, even though you didn't hate him."
        diane "Do you think you could have found understanding?"
    joseph "I don't know."
    jump continueconversation5

    label continueconversation5:
    #cell phone sound effect
    diane "That's mine, hold on."
    hide joseph Scene1
    hide diane Scene1
    with dissolve
    show dianeOnPhone at center with dissolve
    pause(1)
    diane "Hey, Em."
    pause(2)
    diane "What time?"
    pause(1)
    diane "Alright, I'll be there soon."
    pause(1)
    diane "Ok. See ya."
    hide dianeOnPhone with dissolve
    show joseph Scene1 at left
    show diane Scene1 at right
    with dissolve
    joseph "Gotta run?"
    diane "Yes. But I'll be back tomorrow."
    joseph "Diane..."
    diane "Dad?"
    show joseph Scene1Happy at left
    joseph "Thank you."
    hide joseph Scene1
    hide diane Scene1
    with dissolve
    stop music fadeout 1.0
    jump monologue1

    ############################################# MONOLOGUE 1 #############################################
    label monologue1:
    scene blackbackground with dissolve
    pause 1
    play music distortedMusic
    blank "As I walk up to the steps of the chapel, my daughter's face glows."
    blank "2004. Her second marriage."
    blank "I'm so happy she found someone good to spend her life with."
    blank "I look around, trying to spot Paul,"
    blank "Can't see him. Turn back to Diane."
    blank "She looks so happy."
    blank "Liz and Emma stand beside her, and..."
    blank "No... no, this is wrong. Who is this?"
    blank "What's happening to me?"
    blank "I was... I was on the farm, in the field, I don't..."
    blank "I don't have a daughter..."
    scene 1995background with dissolve
    stop music fadeout 1.0
    pause 3
    scene blackbackground with dissolve
    pause 1
    jump scene2
    ############################################# SCENE 2 #############################################

    label scene2:
    scene scenetwobackground with dissolve
    play music scene2happyMusic
    pause 2
    show joseph Scene2 at left
    show diane Scene2 at right
    with dissolve
    diane "Dad, I have a question about you and Mom."
    joseph "Uh oh."
    diane "What was your divorce like?"
    diane "I know you both pretended it went smoothly and you were both civil, but..."
    diane "How was it, really?"
    menu:
        "It was a mess.":
            $divorcemessy = True;
            jump divorceWasMessy

        "It actually was civil.":
            $divorcemessy = False;
            jump divorceWasCivil

    label divorceWasMessy:
    if isreligious == True:
        joseph "Well, and you know. The church community wasn't thrilled."
    else:
        joseph "Well, and you know. The community we lived in wasn't thrilled."
        joseph "That hyper religious community your mom was so into."
    diane "I remember. Got made fun of a lot by the other kids."
    joseph "So we put on a show. Pretended everything was handled smoothly."
    diane "You shouldn't have lied."
    joseph "Listen, Diane... I'm not getting into what actually happened. It was bad."
    diane "I've asked Mom about it. She never tells me what went on."
    joseph "Well, she wouldn't. I hurt her, and she hurt me. It wasn't easy for either of us."
    pause(1)
    jump continueconversation6

    label divorceWasCivil:
    joseph "We tried our best to keep from hurting each other."
    joseph "We had our spats, but we really did both want out."
    diane "I'm glad you guys didn't keep me in the dark, then."
    joseph "No, we wouldn't lie to you."
    diane "Thanks."
    jump continueconversation6

    label continueconversation6:
    diane "What... what happened? Between you two, I mean?"
    joseph "She didn't want to be married to a mechanic her whole life."
    diane "You don't think she knew what she was getting into when she married you?"
    joseph "I don't know. Ask her."
    diane "She won't talk about this stuff, Dad."
    joseph "I think she wanted me to keep doing what I was doing when she met me."
    diane "What was that?"

    menu:
        "I was going to college.":
            $attendedCollege = True;
            jump goingToCollege

        "I was starting my own business.":
            $attendedCollege = False;
            jump startingBusiness

    label goingToCollege:
    joseph "Wanted to be a teacher."
    joseph "That's when your Mother and I met."
    joseph "Then the money ran out, and I started working on cars."
    joseph "Pretty soon, it just made more sense to keep doing that."
    diane "Neither of you ever mentioned it."
    joseph "Well, I'm not very proud of it. And your mother wasn't happy about it either."
    jump continueconversation7

    label startingBusiness:
    joseph "When I left home, my best friend and I started a tiling company."
    joseph "That's when your Mother and I met."
    joseph "Then the business fell through, and I started working on cars."
    joseph "Pretty soon, it just made more sense to keep doing that."
    diane "Neither of you ever mentioned it."
    joseph "Well, I'm not very proud of it. And your mother wasn't happy about it either."
    jump continueconversation7

    label continueconversation7:
    diane "Dad, it's... ok to tell me what happened."
    diane "If it's more than that..."
    menu:
        "That's all there was to it.":
            jump hideSecretAbility

        "There was... something else.":
            jump revealSecretAbility

    label hideSecretAbility:
    ##Joseph sad portrait##
    joseph "There may have been... other small stuff that wasn't working, but that was... it."
    jump continueconversation8

    label revealSecretAbility:
    joseph "I, umm..."
    ##Joseph Sad portrait##
    joseph "I thought I knew... how things would go."
    joseph "I had... I don't know."
    show Joseph Scene2 at left
    joseph "I had convinced myself that things were somehow predetermined."
    joseph "That there wasn't anything to be suprised by in my life."
    joseph "And your mother, well... I don't think she realized until it was too late that I was serious."
    joseph "That I really had convinced myself that I somehow knew how everything around me would go."
    ##Joseph Sad portrait##
    joseph "And when she left I realized how wrong I was."

    label continueconversation8:
    show Joseph Scene2 at left
    joseph "Anyway, that's all in the past now."
    joseph "I'm sure she has her own version of everything."
    pause(1)
    joseph "What brought this on?"
    pause(2)
    hide joseph Scene2
    hide diane Scene2
    with dissolve
    show teaKettle at center with dissolve
    pause(2)
    joseph "Tea's ready."
    hide teaKettle with dissolve
    show diane Scene2 at right with dissolve
    #joseph leaves room
    #tea kettle sound effect
    diane "Dad?"
    joseph "What's that?"
    #tea kettle stops
    diane "Come back in, I have to tell you something."
    joseph "One second."
    #joseph walks back into room
    pause(1)
    show joseph Scene2 at left with dissolve
    joseph "What's up?"
    diane "I quit my job. I'm going to be working on IAC as a full time gig."
    joseph "The- wait- the program?"
    ##Diane Scene 2 happy##
    diane "IAC has become so much more than that, Dad."
    if understoodIAC == True:
        joseph "Can... can you afford to do that?"
        diane "Well, it's not going to be easy... but I think so. Yeah."
        pause(1)
        ##Joseph Happy Portrait##
        joseph "Alright. Then I think you should go for it."
        diane "Thanks, Dad."
        show diane Scene2 at right
        if attendedCollege == True:
            show Joseph Scene2 at left
            joseph "Dropping out of college is one of my biggest regrets."
            joseph "Now, seeing you here, doing things that will change the world..."
            ##Joseph Happy Portrait##
            joseph "Well. I'm proud of you."
        else:
            show Joseph Scene2 at left
            joseph "I never had a dream to chase after."
            joseph "Everything I did felt like it was just enough to keep myself fed, and with a place to live."
            joseph "Now, seeing you here, chasing your dreams..."
            ##Joseph Happy Portrait
            joseph "Well. I'm proud of you."
        diane "Thank you."
        diane "I should get going."
        joseph "You're sure? The tea-"
        diane "I just had an idea. For something to do with IAC."
        joseph "That thing is all you can think about, isn't it?"
        show Joseph Scene2 at left
        joseph "I hope it's worth it."
        diane "It will be."
        diane "I'll be back tomorrow to take you to your appointment."
        joseph "Drive safe."
        diane "Will do!"
        diane "And don't forget your insurance card."
        joseph "I- I know how to go to a new doctor, Diane."
        diane "Okay! Sorry! Just trying to help."
        diane "Since they're putting you under you won't be much help on the way back."
        diane "Ok. I really gotta go. See you."
        stop music fadeout 1.0
        jump monologue2
    else:
        joseph "Oh? So it's become... what? A source of income?"
        show diane Scene2 at right
        play music scene2angryMusic
        diane "Dad, please-"
        joseph "I'm- ok. I'm sorry. I'll listen."
        diane "IAC is advancing at a rate I can't even believe."
        ##Diane Scene 2 Happy##
        diane "Dad, I know I've been working on this for a long time."
        diane "But this is real! With enough time and patience, IAC could become something really valuable."
        diane "Not just to me, but... to the world."
        joseph "How much time?"
        show diane Scene2 at right
        diane "I don't-"
        joseph "You're 29, Diane."
        joseph "How much more time can you afford to pour into this thing?"
        diane "That's unfair."
        joseph "It's the truth."
        diane "Do you think, what, that this is all a waste?"
        joseph "I think that you're throwing away whole parts of your life,"
        joseph "whether it's with this computer program, or with Eric, or-"
        diane "You can't do that. Stop it."
        show joseph Scene2Angry at left
        joseph "Sooner or later, Diane, you need to accept that you threw a lot of time away with that marriage-"
        show joseph Scene2 at left
        show diane Scene2Angry at right
        diane "How dare you."
        diane "My life is- was not just one relationship."
        diane "I can't... I can't believe you just said that."
        joseph "Diane, I-"
        diane "No. Listen to me. I'm going to work on IAC."
        diane "I actually have a whole bunch of plans put together for how I'm going to get by."
        joseph "Ok, see, that's something I didn't-"
        diane "But you don't LISTEN to me. You just ASSUME I don't have anything figured out!"
        show joseph Scene2Angry at left
        joseph "Because I know that you don't!"
        joseph "Because I didn't have anything figured out at your age either!"
        joseph "And I have to sit here and watch you make the same mistakes I did, watch you fumble around!"
        joseph "Wasting your life away in front of that computer screen, wasting it with that piece of shit you married!"
        joseph "I won't let you grow old and feel like I do! And be like I am! And know-"
        ##Joseph sad portrait##
        show joseph Scene2 at left
        joseph "And know how this is all going to play out."
        show diane Scene2 at right
        joseph "I don't want this for you, Diane..."
        diane "Nobody knows how anything is going to play out, Dad."
        diane "I should go."
        joseph "Diane, please..."
        diane "You know what? I can't even begin to unpack whatever weird, repressed trauma you're dealing with."
        diane "That's not my job. I know what my job is. I can't..."
        diane "I can't think right now. Find another ride to your appointment tomorrow."
        diane "Just give me space."
        hide joseph Scene2
        hide diane Scene2
        with dissolve
        stop music fadeout 1.0
        jump monologue2

    ############################################# MONOLOGUE 2 #############################################
    label monologue2:
    scene blackbackground with dissolve
    pause 1
    play music distortedMusic
    blank "How long have I been here?"
    blank "As my memory rushes throught me I begin to make sense of it all."
    blank "I feel... torn in half, like one part of me is an adult and the other a child."
    blank "This is horrible."
    blank "I begin to let it take hold of me, to ignore what I desire and instead see that which I have already been."
    blank "My existence is more temporary than I realize; the time that I will be on this earth is short."
    blank "I look forward and see nothing."
    pause(1)
    blank "What's that noise?"
    pause(1)
    blank "It's coming. Don't let it take me."
    blank "Don't let it take me!"
    scene 1975background with dissolve
    stop music fadeout 1.0
    pause 3
    scene blackbackground with dissolve
    pause 1
    if attendedfathersfuneral == True:
        jump scene3AttendedFuneral
    else:
        jump scene3NoFuneral

    ############################################# SCENE 3 #############################################
    label scene3AttendedFuneral:
    scene scenethreebackground with dissolve
    play music scene3Music
    pause 2
    show josephWalking at center with dissolve
    pause 2
    hide josephWalking
    #Joseph walks into park, approaches cheryl, waiting on bench
    show joseph Scene3 at left
    show cheryl Scene3 at right
    with dissolve
    joseph "Hi."
    cheryl "Hi."
    joseph "Thanks again for driving with me halfway."
    cheryl "Well, like I said, it just lined up nicely with this conference I have to be at."
    cheryl "What are you planning on doing?"
    joseph "I'm crashing at a hotel a few blocks over tonight."
    joseph "I'll be doing the rest of the drive East tomorrow."
    pause 1
    joseph "You okay?"
    cheryl "Yeah. Last week just... took a lot out of me."
    pause 1
    hide joseph Scene3
    hide cheryl Scene3
    with dissolve
    show onBench with dissolve
    joseph "I know."
    joseph "It was weird, seeing him there."
    cheryl "Not for me."
    cheryl "I've been watching him go for months now."
    pause(1)
    if hatedfather == True:
        cheryl "I know you hated him for what he did to you. And it wasn't fair of him."
    else:
        cheryl "There was some level of understanding between you two. You both knew you had to leave."
        cheryl "I know you had your reasons for leaving. And I've never blamed you for that."
    cheryl "But it hasn't made this any easier."
    joseph "I'm sorry."
    cheryl "I'm glad you made it."
    joseph "So am I."
    pause(1)
    hide onBench with dissolve
    show joseph Scene3 at left
    show cheryl Scene3Happy at right
    with dissolve
    cheryl "How's Diane doing?"
    show joseph Scene3Happy at left
    joseph "Working hard. Getting good grades."
    cheryl "That's good."
    pause(1)
    show joseph Scene3 at left
    show cheryl Scene3 at right
    if attendedCollege == True:
        cheryl "I think part of him... just didn't want you to go."
        cheryl "When you left."
        joseph "I didn't get that when he was yelling at me the night before I left to get out."
        cheryl "Well, he never would've admitted it. You two were more similar than you'll ever realize."
        joseph "I don't want to talk about this."
    else:
        cheryl "He was proud of you, you know."
        cheryl "When you left."
        joseph "If he was, he didn't show it."
        cheryl "No. But he was."
        cheryl "Went on about how you starting your own business 'made you a man'."
        joseph "I didn't need his validation on that."
    cheryl "I know."
    pause(1)
    cheryl "God, this... this isn't right, is it? This isn't how a brother and sister are supposed to talk..."
    show joseph Scene3Happy at left
    joseph "I didn't know there was a way we should talk."
    cheryl "You know, if you hadn't shown up the day of the actual funeral, we would've had a chance to..."
    joseph "Hey, I made it, didn't I?"
    cheryl "Barely."
    joseph "Still made it."
    cheryl "See that kid with the guitar?"
    show joseph Scene3 at left
    joseph "Yeah?"
    cheryl "Have him play something."
    joseph "...What?"
    cheryl "I just... really need to hear some music right now."
    joseph "Uh, I mean, I have... a few nickles..."
    jump continueconversation9

    label scene3NoFuneral:
    scene scenethreebackground with dissolve
    play music scene3Music
    pause(2)
    show josephWalking at center with dissolve
    pause(2)
    hide josephWalking
    #Joseph walks into park, approaches cheryl, waiting on bench
    show joseph Scene3 at left
    show cheryl Scene3 at right
    with dissolve
    joseph "Hi."
    cheryl "Hi."
    joseph "Uh, listen, I-"
    cheryl "Just... stop. Let me say what I have to say."
    joseph "Okay."
    cheryl "You said you'd be there. For Dad. You told me you would come last month."
    joseph "I know."
    cheryl "No. Let me talk. I let you not show up. I let you, because I knew this was difficult for you."
    cheryl "I've accepted that you would never talk to him again. I don't understand it; I don't know what went on between you two."
    cheryl "But it was your thing, and not mine, and it was mutual. So whatever."
    cheryl "But then you weren't there last week. For the funeral."
    if hatedfather == True:
        cheryl "So you hated him. So what? What on earth gives you the right to not be there for the family?"
    else:
        cheryl "You've always said you respected him. What the hell happened to you?"
    pause(1)
    hide joseph Scene3
    hide cheryl Scene3
    with dissolve
    show onBench with dissolve
    joseph "I'm sorry."
    cheryl "I don't care."
    joseph "I know."
    pause(1)
    cheryl "You're not going to tell me why you left."
    joseph "No."
    if attendedCollege == True:
        cheryl "When you went to college... everything changed, you know."
    else:
        cheryl "When you and your friend went and started that business... everything changed, you know."
    cheryl "You weren't around for it, but nothing was the same again."
    cheryl "Dad wasn't the same."
    pause(1)
    cheryl "I can't hate you. But I'm so... mad..."
    pause(2)
    cheryl "And now it's on me, you know? To explain to everyone why you weren't there. Because you won't."
    joseph "I didn't want anyone to have to deal with that. But I can't."
    pause(1)
    hide onBench with dissolve
    show joseph Scene3 at left
    show cheryl Scene3 at right
    with dissolve
    cheryl "See that kid with the guitar?"
    joseph "Yeah?"
    cheryl "Have him play something."
    joseph "...What?"
    cheryl "I just... really need to hear some music right now."
    joseph "Uh, I mean, I have... a few nickles..."
    jump continueconversation9

    label continueconversation9:
    hide cheryl Scene3
    hide joseph Scene3
    with dissolve
    show josephWalking at center with dissolve
    pause(2)
    hide josephWalking
    show coinsIntoCase at center
    with dissolve
    #Joseph walks over to 20 year old holding guitar, tosses some coins into his hat. Acoustic guitar music starts playing
    joseph "Here. Mind playing something? Thanks."
    pause(1)
    hide coinsIntoCase
    show josephWalkingReversed at left
    show guitarPlaying at right
    with dissolve
    #Joseph walks back over to Cheryl
    pause(2)
    hide josephWalkingReversed
    show onBench at left
    with dissolve
    joseph "Hey, kid's not half bad."
    pause(2)
    cheryl "I'm sorry."
    joseph "What? Why?"
    cheryl "I came here ready to argue with you..."
    pause(1)
    cheryl "The truth is, I don't know what happened. I never will."
    hide onBench
    hide guitarPlaying
    with dissolve
    show joseph Scene3 at left
    show cheryl Scene3 at right
    with dissolve
    cheryl "I don't care what the family thought, and I don't care about what went on between you two."
    show cheryl Scene3Happy at right
    cheryl "I care that you're my brother, and that you're in my life still."
    pause(2)
    joseph "I haven't seen you enough. I haven't been around."
    cheryl "Well, we need to fix that. I'll start visiting more. Seeing Diane more."
    show joseph Scene3Happy at left
    joseph "She'd love that."
    pause(2)
    show joseph Scene3 at left
    show cheryl Scene3 at right
    cheryl "So you and Elizabeth aren't..."
    joseph "She, umm, moved out."
    if divorcemessy == False:
        joseph "We've been trying to do this as carefully as possible. We don't want to upset Diane."
    else:
        joseph "To tell you the truth, it's... it's been a mess."
        joseph "I'm doing everything I can to convince Diane that everything will be alright."
        joseph "But Elizabeth won't even talk to me."
    cheryl "I'm sorry."
    pause(2)
    cheryl "When you left the house..."
    joseph "Cheryl, I really don't want to talk about that."
    cheryl "Do you remember how he reacted to it?"
    cheryl "Please, just... tell me what Dad said when you left."
    menu:
        "He was furious.":
            $dadwasmad = True;
            joseph "He didn't yell. He just sat there. But I could tell he was more furious with me than he had ever been before."
            jump continueconversation10

        "He was sad.":
            $dadwasmad = False;
            joseph "He just sat in his chair. Wouldn't move. I've never seen him so depressed."
            jump continueconversation10

    label continueconversation10:
    joseph "And then I... went to Elizabeth, with my stuff in the car, and she and I drove out to Toronto."
    joseph "And that was that."
    pause(2)
    joseph "Do you remember the time we went down to the lake with the McKinleys?"
    cheryl "And you broke your leg?"
    show cheryl Scene3Happy at right
    joseph "Yeah. On that rope that swung out over the water."
    joseph "I had to be... what, nine? Ten?"
    cheryl "Dad was so angry."
    pause(1)
    joseph "I remember swinging forward, and feeling the wind rush past me, and then hearing the crack of the branch breaking."
    cheryl "I wasn't looking. By the time I'd turned around you were already in the water."
    show joseph Scene3Happy at left
    joseph "Hurt like nothing else. May as well have not hit water at all, the rocks were so shallow."
    cheryl "I ran in and Jerome and I carried you out of there."
    pause(2)
    show joseph Scene3 at left
    joseph "Cheryl, do you still go to church?"
    show cheryl Scene3 at right
    cheryl "No. Stopped years ago."
    if isreligious == True:
        joseph "I do."
        cheryl "Yeah? I guess I just reached the point where... I don't buy it anymore."
        joseph "I still do. Believe, that is."
        pause(1)
        cheryl "Well, I'm happy for you."
        joseph "You are?"
        cheryl "Well, sure. Who am I to say what's right or wrong to believe in?"
    else:
        joseph "I don't, either."
        cheryl "You hit that point where you stopped buying it too?"
        pause(2)
        joseph "I guess so. Just not for me, I guess."
        pause(1)
        cheryl "You ever consider going back?"
        joseph "I've considered. Still can't bring myself to actually believe, though."
        cheryl "Same. At the end of the day, that's kind of the point, isn't it?"
        joseph "I appreciate the stories. Just can't commit myself to the belief."
    pause(2)
    joseph "I knew."
    joseph "Cheryl, I knew."
    cheryl "Knew what?"
    joseph "I knew that would happen. The rope would break, I would fall, that you'd come and get me..."
    joseph "Everything that happened that day at the McKinley's. I knew all of it. Every detail."
    joseph "And I've known so much more. I knew we would talk here. I knew our father would die."
    cheryl "You didn't know that."
    joseph "Yes, I did, I did. I know you don't believe me."
    joseph "I knew all of that."
    ##Show Joseph sad##
    joseph "So why didn't I know she would leave me?"
    if isreligious == True:
        joseph "Why would God leave that part out?"
        joseph "Why would God pretend to tell me everything that would come to pass, but leave my own wife out?"
        joseph "Why?"
    else:
        joseph "Why wouldn't I know to expect that?"
    cheryl "Joseph, listen."
    cheryl "Nobody can know what's going to happen."
    cheryl "You've convinced yourself that the world is something that it isn't."
    cheryl "You're going through a lot right now."
    cheryl "But it sounds to me like you need someone to talk to."
    cheryl "Someone who isn't me, or Elizabeth, or..."
    cheryl "Joseph, honestly, I think you should see a doctor."
    cheryl "I think you need help figuring this out."
    hide joseph Scene3
    hide cheryl Scene3
    with dissolve
    stop music fadeout 1.0
    jump monologue3

    ############################################# MONOLOGUE 3 #############################################
    label monologue3:
    blank "I'm tying Diane's shoes."
    blank "She's going to be late for school."
    blank "It's my turn to drive her to the bus stop."
    blank "No."
    blank "I make sure she's buckled in,"
    blank "Stop."
    blank "And we arrive at her bus safely."
    blank "Please."
    blank "Goodbye, have fun learning."
    blank "This is hurting me."
    blank "What a happy happy happy happy"
    blank "happy happy happy day."
    jump scene4

    ############################################# SCENE 4 #############################################
    label scene4:
    scene scene4
    jump scene5

    ############################################# SCENE 5 #############################################
    label scene5:
    scene scene5
    #background of wheat field
    blank "I was born on a farm in Alberta, along the Rockies."
    blank "My mother passed when I was still too young to work, and my father cared for my sister and I."
    blank "When I was eight years old, I experienced somthing very odd."
    #shot of orb descending in front of Joseph
    blank "I was walking through the high grass near the river, when a bright orb appeared in the sky."
    #orb hovers in front of Joseph
    blank "It slowly descended, until it hovered in place just before me."
    blank "I experienced something that I do not understand."
    if attendedfathersfuneral == True:
        ##Grave cutaway##
        blank "I saw myself at my father's funeral."
    else:
        ##Park bench cutaway##
        blank "I saw myself apologizing for missing my father's funeral."
    if hatedfather == True:
        ##Puching wall cutaway##
        blank "I saw the hate I held onto when I left home."
    else:
        ##Holding head guiltily cutaway##
        blank "I saw the respect I had for my father, in spite of our differences."
    #orb makes sounds, rotates, whatever
    if attendedCollege == True:
        ##Exterior of college cutaway##
        blank "I saw myself attending, and then dropping out of college."
    else:
        ##Exterior of tiling company cutaway##
        blank "I saw myself starting a business with my closest friend."
    if divorcemessy == False:
        ##Elizabeth and Joseph pouring over documents across a table cutaway##
        blank "I saw Elizabeth and I sitting down to discuss our divorce."
    else:
        ##Elizabeth and Joseph yelling at each other cutaway##
        blank "I saw Elizabeth and I yelling at each other while our daughter wasn't home."
    if understoodIAC == True:
        ##Cutaway of IAC##
        blank "I saw my daughter explaining her work in artificial intelligence, and myself finally understanding what she had accomplished."
    else:
        ##Cutaway of Diane alone in garage, crying##
        blank "I saw my inability to understand my daughter's work in artificial intelligence, and how she needed my support."
    if dadwasmad == True:
        ##Cutaway of Joseph's father looking furious##
        blank "I saw my Father's look of utter hatred as I walked out of my childhood home."
    else:
        ##Cutaway of Joseph's father looking shameful##
        blank "I saw my father's shame as I walked out of my childhood home."
    if isreligious == True:
        ##Cutaway of Joseph in confessional
        blank "I saw myself speaking with members of my church, trying to come to terms with what I had experienced."
    else:
        ##Cutaway of Joseph in mirror##
        blank "I saw myself staring into a mirror, struggling to understand what I had experienced."
    ##Cutaway of Joseph hovering in air before orb##
    blank "I saw myself screaming in agony as I spent a lifetime within my own future."

    scene blackbackground
    ##Cutaway of Joseph on hands and knees##
    blank "And then, at once, it stopped. And my legs gave way and I felt the earth beneath me."
    #sound effect of hearbeat monitor stopping







    # This ends the game.

    return
