# The script of the game goes in this file.
# The game starts here.
label start:

    scene reception
    with fade

show byrne at right

byrne "Oh hey great to see ya!"

byrne "Welcome to the team kid!"

byrne "It's me your mentor, you already know that by now I guess."

byrne "We did just have a 4-stage six month long interview process before hiring you after all."

byrne "So for your internship, we'll have you sit in cubicle all day, you'll get a taste of what its like to work with us."

byrne "And hopefully you'll enjoy it."

byrne "Here's the sheet with the programmes for today."

byrne "Let me know if you need anything or we can catch up during the mentoring session."

byrne "Which will be after lunch so don't be late!"

byrne "Ah here, my card so you can contact me if you need anything."

byrne "Until then enjoy kiddo!"

hide byrne


##### work 1 - morning #####
label work_1:

    scene office
    with fade

"You spend the morning doing work."

"Which was going through emails & remote meetings with the team."

"It's time for a short break, you head over to The Watercooler Zone to meet the people you'll be spending 1/3 of your life with from now on."

"That's if you manage these three months first."

###### interview intro ######
label interview:
    scene interview
    with fade

"As you make your way to, I don't know, where ever, you come across-"

"A young man panicking infront of a very chill woman."

me "He's literally me for real, for real."

show lucas at left

vue "Man I'm so stressed about this interview."

me "Oh."

vue "Give me some moral support Seong."

show seong at right

tech "I'm surprised you made it this far."

vue "That's not what I meant."

vue "Ok I gotta be positive."

vue "I'm gonna pass!"

vue "R-right?"

tech "Maybe."

vue "So then help me out man."

vue "I was so busy stressing about the interview I forgot to practice for it!"

tech "This sounds like your problem."

vue "Man you're the only I can trust."

vue "You literally work here so give me some insider info on what's gonna pop up."

tech "Hmm."

tech "No."

vue "It be your own people..."

tech "It's your own damn fault for not preparing."

"The interviewee sees you not minding your own business."

vue "Hey you, you also doing the interview?"

label interview_intro:

        "So you here for the interview?"

menu:
        "I'm literally the interviewer, the Technical Lead.":
            jump interview_intro_a

        "Yes, best of luck to both of us.":
            jump interview_intro_b

        #"No, I'm an intern.":
            #jump interview_intro_c

        "Just walk away.":
            jump interview_intro_d

##### lie - technical lead #####
label interview_intro_a:

me "I'm literally the interviewer, the Technical Lead."

tech "..."

vue "..."

vue "Kinda sus man."

vue "Don't wanna be rude, you just don't look the type."

vue "You two just messing with me ugh!"

vue "I'm gonna go practice in the toilet, you guys can't distract me there atleast."

hide vue

"He walks off, pulling out a crumpled piece of paper with some scribbles on it."

tech "Atleast he's being serious about practicing now."

tech "Even if it's too late."

tech "Looks like you already made it past the interview process."

tech "Guess we'll be seeing each other around then."

hide seong

"She gives a small wave as she heads off."

me "Damn, I didn't even get her number."

jump work_2


##### lie - 2 interviewees #####
label interview_intro_b:

vue "Shit, I was hoping I wouldn't have to see any rivals before the interview but alas!"

vue "Best of luck to you too pal."

vue "Oh, I'm Lucas by the way."

vue "Let's do some interview prep questions so we can both benefit, us folks gotta look for each other and all."

vue "Even if we're fighting for the same spot."

jump interview_quiz

##### technical quiz #####
label interview_quiz:

tech "You two have fun with your last minute prepping."

hide seong

"She gives a small wave as she heads off."

me "Damn, I didn't even get her number."

vue "We must stay focused!"

me "My bad, the grind always comes first."

vue "For real, for real."

vue "Ok, so I have a feeling there's gonna be some questions on the Agile & Scrum stuff so I wanna do a refresher on that."

vue "I'm gonna ask you questions and hopefully you get it right cus I don't know it fully myself you see."

#1
label interview_q_1:
vue "First one, although Scrum was intended for management of software development projects, it can be used to run software maintenance teams, or as a general project/program management approach."

menu:

    "True":
        jump interview_q_2

    "False":
        jump interview_q_2

label interview_q_2:
#2
vue "Why does the Daily Scrum need to be held at the same location and time?"

menu:

    "The booking of a room needs to be done in advance for the duration of the Sprint.":
        jump interview_q_3

    "The constant time and place is best for continuity of the Scrum framework.":
        jump interview_q_3

    "The Project Manager needs to get the status updates at a given time every day.":
        jump interview_q_3

label interview_q_3:
#3
vue "A Scrum team failed to meet the Sprint objectives.
One of the key members of the team fell ill and was away for two days right at the beginning of the four week Sprint.
What is the most likely reason that the team did not meet the Sprint objectives?"

menu:

    "The Product Owner is unable to prioritise.":
        jump interview_q_4

    "The team is lacking skills.":
        jump interview_q_4

    "The team did not plan the Sprint effectively.":
        jump interview_q_4

    "The team is over-worked.":
        jump interview_q_4


label interview_q_4:
#4
vue "What is an information radiator?"

menu:

    "A physical display for the team that gives information about the current status.":
        jump interview_q_5


    "A tool that automatically sends relevant information to the Product Owner.":
        jump interview_q_5


    "A status report or dashboard that is maintained by the Scrum Master.":
        jump interview_q_5


label interview_q_5:
#5
vue "Finally, collaboration is the most important parameter for the success of an Agile team. What term best describes this type of interaction?"

menu:
    "Distributed team working.":
        jump interview_end

    "Information radiator sharing.":
        jump interview_end

    "Osmotic communication.":
        jump interview_end

label interview_end:

vue "Phew!"

vue "Thanks for the help, I feel more confident now."

"You see a woman appear out of the conference room."

"Is Mr Brent here?"

vue "Looks like it's time."

#vue "oh can you hold onto my stuff, i know i turned my phone off but what if it still goes off? i don't wanna risk it after coming all this way."

#vue "I trust you wont steal my money cus i have nothing in my bank."

"Lucas gives you a quick nod before following the interviewer into the small room."

hide lucas

me "Best of luck."

jump work_2

##### end of quiz #####
label interview_intro_d:

"Without a word you walk away."

hide lucas
hide tech

jump work_2

##### back to work 2 ######
label work_2:

show office
with fade

"You head back to your desk, thinking about the awesome fun work day ahead."

"NOOOooo!!!"

"You hear someone trying their best to scream in their whisper but it's just about loud enough for only the main character"

"-you-"

"to hear it."

"You, not staying in your own lane, go close to the source of drama."

scene conference2
with fade

show van at left

pr "Oh no a very important client is coming to meet us but the conference room is still a mess!"

"The fashionable woman seems to be in her late 20s, the stress is doing no good for her well maintained 7 step skincare routine."

"She looks around for her assistants only to see you."

pr "Hey, you're the new intern for our department right?"

pr "Come over here and help!"

hide van

"This isn't your department but you help anyway."

window hide

pause

#do a black out and it reveals the conference room in a mess.

label conference_cleaner:
#cleaning the conference room by clicking items

#show screen

#After  cleaning.

"After you clear up the room as well as the situation."

show van at left

pr "Sorry for mistaking you for one of our interns and dragging you in like this."

pr "But thank you so much for helping out at such a short notice."

pr "Can I have your name and department?"

pr "I'm Vanessa by the way, as you can tell from my ID card."

pr "How's your time working with us been so far?"

pr "Bad? Terrible? Down right horrendous?"

pr "What am I saying it's always great here, everyday is a new experience!"

"She continues talking about her life at the office."

"Her home."

"The bars."

"The club."

"This is no longer a conversation but she keeps going and you just nod along."

"You start to think about you're gonna have for lunch, you didn't pack anything since you left 10 minute before your work starts."

"But that's okay, you made it on time on your first day."

"You heard the canteen has good stuff so there's something to look forward to."

"A group of people call for Vanessa, she looks their way telling them to wait just a moment before she looks back at you."

"Looks like it's time for that important meeting."

pr "You're pretty cool, keep helping around the workplace and you'll get yourself a good reputation."

pr "Let's get to know each other more too."

hide van

"She struts off, and the crowd engulfs her."

"It's like watching a celeb get swarmed by the paparazzi."

#Get contact card.

##### IT Bug Fixer #####

scene office
with fade

"As you sit back down on your desk, you go to turn your monitor on but only to find out that it won't?"

show byrne at right

byrne "Hey kid, I know you didn't call me but my paternal instincts started to flare up!"

"You explain to him that your computer is not working."

byrne "Hmm."

byrne "I'm not so tech savvy, best to call Tech Support for this one."

hide byrne

"Byrnestone takes you to the IT Support Room, it's located fairly close to your work area.
It's at the centre of the building so every department can come crying for help,"

show  it_support
with fade

"begging that the IT hopefully has a minute old copy of the documents that they saved hours ago."

"You meet one of the IT Support, Sunny."

"Despite the name she has a rather gloom appearance."

show sunny at left

it "What is it this time, you didn't use the DVD Drive to hold your coffee again right?"

show byrne at right

byrne "Aw geez, not in front of the new kid!"

byrne "I was just joking. I know what that thing is for!"

it "Hopefully you do now. I guess you can teach an old dog new tricks."

byrne "You see, our new recruits got a  problem with their computer."

byrne "The thing won't turn on."

hide byrne
hide sunny

"You nod at each word as evidence that it in fact does not turn on."

show office
with fade

"The three of you make your way to the problem, Byrnestone & Sunny continue to chatter along the way."

"Once Sunny takes over your workstation, within seconds she finds the problem. As expected from Tech Support!"

it "Yep, it's bugs."

byrne "Let's watch our star tech support fix these bugs then."

it "Oh, it's not the fixing kind."

"She then opens the tower case next to the monitor."

"You see lots of bugs."

"It's so colourful and disgusting."

it "It's this kind."

### spray shooting gallery game
