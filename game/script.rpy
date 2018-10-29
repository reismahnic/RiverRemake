# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define joseph = Character("Joseph")
define diane = Character("Diane")
define cheryl = Character("Cheryl")
define father = Character("Father")
define blank = Character("")


#Setting up images:
image josephScene1 = "josephsceneoneportrait"
image josephScene3 = "josephscenethreeportrait"
image cheryl = "cherylscenethreeportrait"
image dianeScene2 = "dianescenetwoportrait"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene blackbackground

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    blank "I was born on a farm in Alberta, along the Rockies."
    blank "My mother passed when I was still too young to work, and my father cared for my sister and I."
    blank "When I was eight years old, I experienced somthing very odd."
    blank "I was walking through the high grass near the river, when a bright orb appeared in the sky."
    blank "It slowly descended, until it hovered in place just before me."
    blank "I experienced something that I do not understand."

    #Display Title

    scene sceneonebackground
    show josephScene1 at left
    show dianeScene2 at right
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
        joseph "Heh! Isn't that the truth..."
        jump continueconversation1

    label continueconversation1:
    pause(3)
    joseph "I'm probably not leaving this hospital, Diane."
    diane "Dad..."
    pause(1)
    joseph "Do you remember when you were in high school, and I was in a car wreck?"
    diane "Yes."
    joseph "I was going... had to be 150, 160. Just outside of Toronto."
    joseph "Your Mom had left me and I didn't know what to do."
    diane "I remember."
    joseph "And I remember dangling upside down, and struggling to get my seatbelt unhooked..."
    joseph "And then I stopped, and just hung there. I gave up."
    if isreligious == True:
        joseph "I thought, please, God, come to me, speak to me like you spoke to me that day on the farm."
    else:
        joseph "I didn't know what to do. I was too scared to survive, and not religious enough to pray."
    pause(2)
    joseph "I'm glad I lived."
    diane "I know."
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
        joseph "I did too, at first."
        diane "He's been seeing his friends more, though."
        joseph "From work?"
        diane "Mostly. Sometimes his best friend he grew up with visits."
        joseph "That's good."
        jump continueconversation2

    label askAboutLizEmma:
        diane "Liz is doing fine. She's been looking up and down for colleges."
        joseph "Oh, yeah. What's she majoring in?"
        diane "She doesn't know yet. Just getting her general degree."
        diane "Emma, of course, getting straight A's in everything. You know her."
        joseph "Well, I'd like to see both of them."
        diane "I know, Dad. They're just both so busy now..."
        jump continueconversation2

    label askAboutDiane:
        diane "I'm fine."
        joseph "You've been coming here too often, Diane."
        diane "I said I'm fine, Dad."
        joseph "Because I can-"
        diane "Dad."
        joseph "You're fine."
        diane "I'm fine."
        jump continueconversation2

    label askAboutIAC:
        diane "IAC is... well, astonishing."
        joseph "I know that I wasn't exactly... the best... about encouraging you."
        joseph "With the computer stuff, I mean. Assuming you couldn't learn to- what an idiot I was."
        diane "It was a different time, Dad."
        joseph "No- no. It was sexism. Plain and simple. It was."
        joseph "You're so brilliant, Diane. The things you've done. You've changed the world."
        jump continueconversation2

    label continueconversation2:
        pause(1)
        joseph "Diane?"
        diane "What?"
        joseph "When I go, I want them there. Liz and Emma."
        joseph "For the funeral."
        diane "Of course they'll be there, Dad."

    menu:
        "I didn't go to my father's funeral.":
            $attendedfathersfuneral = False;
            jump didntgofuneral

        "I went to my father's funeral.":
            $attendedfathersfuneral = True;
            jump attendedfuneral

    label didntgofuneral:
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
        joseph "He and I never got closure. At all. I hadn't seen him since I left home."
        diane "I know. Mom told me."
        joseph "Well, I'll never feel good about our relationship."
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
    joseph "I'm at the point where I won't get to later."
    joseph "Nobody deserves to be completely forgotten. Not even him."
    diane "What... what happened between you two?"
    joseph "He wasn't what you'd call a loving parent."
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
        joseph "Oh, I sure did."
        joseph "I hated him like no other."
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
        joseph "No. I was angry, but... I knew I didn't understand."
        joseph "I would never understand him. We were just too different."
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
    diane "Dad, you know when I divorced Eric?"
    menu:
        "I remember. I didn't understand.":
            $understooddivorce = False;
            jump didntUnderstandDivorce

        "Of course I do. I was happy for you.":
            $understooddivorce = True;
            jump understoodDivorce

    label didntUnderstandDivorce:
    joseph "I remember. I didn't understand."
    diane "Well... I was furious with you."
    joseph "I know."
    if hatedfather == True:
        diane "And I felt like I could have walked out of your life too."
        joseph "I know."
        diane "After you and Mom divorced, for you to say..."
        joseph "It was stupid. And I still don't understand why I said what I said."
        joseph "I'm sorry."
        diane "Don't be. It was twenty years ago."
        diane "I guess I'm just saying... I understand. How you felt when you left your Dad."
    else:
        diane "I didn't hate you though."
        joseph "Well, you're like me. You always have been."
        diane "You couldn't hate your father, I can't hate mine."
        joseph "I don't understand how it works. How we work. But I don't mind."
    jump continueconversation5

    label understoodDivorce:
    joseph "Of course I do."
    diane "I remember when you and Mom got divorced, and I felt like my life was being torn apart."
    if isreligious == True:
        joseph "Well, sure. You know, when I went through my divorce, we got a lot of comments from our church."
        joseph "It was '73. People gave us a hard time."
    else:
        joseph "Well, sure. My divorce was no party. I understood."
    diane "Your understanding was what got me through all of that."
    if hatedfather == True:
        diane "I have to wonder if you and my Grandfather could have had a relationship, if you had tried to be more understanding."
    else:
        diane "Do you think you and my Grandfather could have worked things out?"
        diane "You say there wasn't understanding, even though you didn't hate him."
        diane "Do you think you could have found understanding?"
    joseph "I don't know."
    jump continueconversation5

    label continueconversation5:
    #cell phone sound effect
    diane "That's mine, hold on."
    pause(1)
    diane "Hey, Emma."
    pause(2)
    diane "What time?"
    pause(1)
    diane "Alright, I'll be there soon."
    pause(1)
    diane "Ok. See ya."
    joseph "Gotta run?"
    diane "Yes. But I'll be back tomorrow."
    joseph "Diane..."
    diane "Dad?"
    joseph "Thank you."
    jump monologue1

    ############################################# MONOLOGUE 1 #############################################
    label monologue1:
    scene blackbackground
    blank "As I walk up to the steps of the chapel, my daughter's face glows."
    blank "2004. Her second marriage."
    blank "I'm so happy she found someone good to spend her life with."
    blank "I look around, trying to spot Paul,"
    blank "Can't see him. Turn back to Diane."
    blank "She looks so happy."
    blank "Liz and Emma stand beside her, and..."
    blank "No... no, this is wrong. Who is this?"
    blank "What's happening to me?"
    blank "I was... I was on the farm, in the field, I dont..."
    blank "I don't have a daughter..."
    jump scene2
    ############################################# SCENE 2 #############################################

    label scene2:
    scene scene2

    diane "Dad, I have a question about Mom and you."
    joseph "Uh oh."
    diane "How was your divorce?"
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
    diane "I remember. Got made fun of a lot by the other kids."
    joseph "So we put on a show. For you, for everyone. It was the 70's."
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
    diane "Didn't she know what she was getting into when she married you?"
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
    joseph "Anyway, that's all in the past now."
    pause(1)
    joseph "What brought this on?"
    pause(2)
    joseph "Tea should be ready."
    #joseph leaves room
    #tea kettle sound effect
    diane "Dad?"
    joseph "What's that?"
    #tea kettle stops
    diane "Come back in, I have to tell you something."
    joseph "One second."
    #joseph walks back into room
    joseph "What's up?"
    diane "I'm leaving Eric."
    joseph "What?"
    diane "There's nothing there anymore."
    diane "He's verbally abusive to me. Every day now. I'm done trying to understand why he's become this way."
    if understooddivorce == True:
        joseph "Well, alright."
        diane "That's it?"
        joseph "It's your business."
        joseph "You know when your Mom and I got divorced... it wasn't fair, what we put you through."
        joseph "I just hope you two are okay with this."
        diane "We are. It's not working."
        joseph "...Well, if it's not working, it's not working."
        diane "Dad... thanks for understanding. Thank you."
        jump monologue2
    else:
        joseph "This is a joke, right?"
        diane "What?"
        joseph "You heard me."
        diane "Dad?"
        joseph "Are you really going to tell me you're making the same mistakes I did?"
        joseph "Do you have any idea what my life has been since..."
        diane "Excuse me? Are you really going to make this about you?"
        joseph "Well it sounds to me like you were already set on that!"
        diane "Oh, wow."
        joseph "What?"
        diane "I... I have to leave."
        joseph "Diane, give me a-"
        diane "I don't have anything to say to you."
        jump monologue2

    ############################################# MONOLOGUE 2 #############################################
    label monologue2:
    scene blackbackground
    blank "How long have I been here?"
    blank "As my memory rushes throught me I begin to make sense of it all."
    blank "I feel... torn in half, like one part of me is an adult and the other a child."
    blank "This is horrible."
    blank "I begin to let it take hold of me, to ignore that which I desire and instead see that which I have already been."
    blank "My existence is more temporary than I realize; the time that I will be on this earth is short."
    blank "I look forward and see nothing."
    pause(1)
    blank "What's that noise?"
    pause(1)
    blank "It's coming. Don't let it take me."
    blank "Don't let it take me!"
    if attendedfathersfuneral == True:
        jump scene3AttendedFuneral
    else:
        jump scene3NoFuneral

    ############################################# SCENE 3 #############################################
    label scene3AttendedFuneral:
    scene scenethreebackground
    #Joseph walks into park, approaches cheryl, waiting on bench
    show josephScene3 at left
    show cheryl at right
    joseph "Hi."
    cheryl "Hi."
    joseph "Well don't get up and hug me or anything."
    cheryl "Sorry, I just..."
    joseph "You okay?"
    cheryl "Yeah. Last week just... took a lot out of me."
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
    cheryl "How's Diane doing?"
    joseph "Working hard. Getting good grades."
    joseph "That's good."
    pause(1)
    if attendedcollege == True:
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
    joseph "I didn't know there was a way we should talk."
    cheryl "See that kid with the guitar?"
    joseph "Yeah?"
    cheryl "Have him play something."
    joseph "...What?"
    cheryl "I just... really need to hear some music right now."
    joseph "Uh, I mean, I have... a few nickles..."
    jump continueconversation8

    label scene3NoFuneral:
    scene scenethreebackground
    show josephScene3 at left
    show cheryl at right
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
    cheryl "To miss your own father's funeral... there is no good reason you can give."
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
    cheryl "You weren't there, but nothing was the same again."
    pause(1)
    cheryl "I can't hate you. But I'm so... mad..."
    pause(2)
    cheryl "God, this... this isn't right, is it? This isn't how a brother and sister are supposed to talk..."
    joseph "I didn't want this for you."
    pause(1)
    cheryl "See that kid with the guitar?"
    joseph "Yeah?"
    cheryl "Have him play something."
    joseph "...What?"
    cheryl "I just... really need to hear some music right now."
    joseph "Uh, I mean, I have... a few nickles..."
    jump continueconversation8

    label continueconversation8:
    #Joseph walks over to 20 year old holding guitar, tosses some coins into his hat. Acoustic guitar music starts playing
    joseph "Here. Mind playing something? Thanks."
    #Joseph walks back over to Cheryl
    joseph "Hey, kid's not half bad."
    pause(2)
    cheryl "I'm sorry."
    joseph "What? Why?"
    cheryl "I came here ready to argue with you..."
    pause(1)
    cheryl "The truth is, I don't know what happened. I never will."
    cheryl "I don't care what the family thought, and I don't care about what went on between you two."
    cheryl "I care that you're my brother, and that you're in my life still."
    pause(2)
    joseph "I haven't seen you enough. I haven't been around."
    cheryl "Well, we need to fix that. I'll start visiting more. Seeing Diane more."
    joseph "She'd love that."
    pause(2)
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
    joseph "How are you and Josh doing?"
    cheryl "We're good."
    joseph "Good."
    pause(2)
    joseph "Do you remember the time we went down to the lake with the McKinleys?"
    cheryl "And you broke your leg?"
    joseph "Yeah. On that rope that swung out over the water."
    cheryl "Dad was so angry."
    pause(1)
    joseph "I remember swinging forward, and feeling the wind rush past me, and then hearing the crack of the branch breaking."
    cheryl "I wasn't looking. By the time I'd turned around you were already in the water."
    joseph "Hurt like nothing else. May as well have not hit water at all, the rocks were so shallow."
    cheryl "I ran in and Jerome and I carried you out of there."
    joseph "Well, I still owe you for that."
    pause(2)
    joseph "Cheryl, do you still go to church?"
    cheryl "No. Stopped years ago."
    if isreligious == True:
        joseph "I do."
        cheryl "Yeah? I guess I just reached the point where... I don't buy it anymore."
        joseph "I still do. Belive, that is."
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
    cheryl "I, uh... I want to know something."
    joseph "What is it?"
    pause(2)
    cheryl "You... you know, I wasn't... home, when you left."
    joseph "I know."
    cheryl "Do you remember how he reacted to it?"
    menu:
        "He was furious.":
            $dadwasmad = True;
            jump dadWasMad

        "He was sad.":
            $dadwasmad = False;
            jump dadWasMad

    label dadWasMad:
    joseph "He didn't yell. He just sat there. But I could tell he was more furious with me than he had ever been before."
    jump scene4

    label dadwassad:
    joseph "He just sat in his chair. Wouldn't move. I've never seen him so depressed."
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
    scene scene4
    label scene4:
    #Shots of bedroom, hallways, stairs, then living room. Takes a few seconds. Cinematic.
    #Shot of father on couch, framing Joseph
    joseph "I'm leaving, Father."
    pause(2)
    if attendedcollege == True:
        joseph "I'm going to college."
    else:
        joseph "I'm going with Jack to start my own business."
    pause(2)
    if dadwasmad == True:
        father "Get your stuff. And get the hell out of my house."
    else:
        father "Why did it turn out this way?..."
        father "I'm sorry, I'm sorry..."
        joseph "You can't take yesterday back."
        father "I know."
    #Shots of Joseph gathering his things
    if hatedfather == True:
        joseph "I hate you."
        father "Leave."
    else:
        joseph "I wish things were different."
        father "I do too."
        father "Now get out."
        joseph "Fine."
    #Shot of Joseph closing front door
    jump scene5

    ############################################# SCENE 5 #############################################
    scene scene5
    label scene5:
    #shots of wheat field
    blank "I was born on a farm in Alberta, along the Rockies."
    blank "My mother passed when I was still too young to work, and my father cared for my sister and I."
    blank "When I was eight years old, I experienced somthing very odd."
    #shot of orb descending in front of Joseph
    blank "I was walking through the high grass near the river, when a bright orb appeared in the sky."
    #orb hovers in front of Joseph
    blank "It slowly descended, until it hovered in place just before me."
    blank "I experienced something that I do not understand."
    if attendedfathersfuneral == True:
        blank "I saw myself at my father's funeral."
    else:
        blank "I saw myself apologizing for missing my father's funeral."
    if hatedfather == True:
        blank "I saw the hate I held onto when I left home."
    else:
        blank "I saw the respect I had for my father, in spite of our differences."
    #orb makes sounds, rotates, whatever
    if attendedcollege == True:
        blank "I saw myself attending, and then dropping out of college."
    else:
        blank "I saw myself starting a business with my closest friend."
    if divorcemessy == False:
        blank "I saw my wife and I sitting down to discuss our divorce."
    else:
        blank "I saw my wife and I yelling at each other while our daughter wasn't home."
    if understooddivorce == True:
        blank "I saw my daughter explaining her divorce to me, and my understanding of her."
    else:
        blank "I saw myself lecturing my daughter on her divorce."
    if dadwasmad == True:
        blank "I saw my Father's look of utter hatred as I walked out of my childhood home."
    else:
        blank "I saw my father's shame as I walked out of my childhood home."
    if isreligious == True:
        blank "I saw myself attending church to explain what I was experiencing just then."
    else:
        blank "I saw myself staring into a mirror, struggling to understand what I was experiencing just then."
    blank "I saw myself screaming in agony as I spent a lifetime within my own future."

    scene blackbackground
    blank "And then, at once, it stopped. And my legs gave way as I felt the earth beneath me."
    #sound effect of hearbeat monitor stopping







    # This ends the game.

    return
