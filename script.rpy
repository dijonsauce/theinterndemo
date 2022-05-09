# The script of the game goes in this file.

# The game starts here.
label start:

    scene reception
    with fade

byrne "Oh hey great to see ya. welcome to the team kid!"

byrne "It's me your mentor, you already know that by now I guess."

byrne "We did just have a 4-stage six month long interview process before hiring you after all."

byrne "So for your internship, we'll have you sit in cubicle all day, you'll get a taste of what its like to work with us."

byrne "And hopefully you'll enjoy it."

byrne "Here's the sheet with the programmes for today."

byrne "Let me know if you need anything or we can catch up after lunch during the mentoring session."

byrne "Until then enjoy kiddo!"



label work_1:

    scene office
    with fade

"You spend the morning doing work."

"Which was going through emails & remote meetings with the team."

"It's time for a short break, you head over to The Watercooler Zone to meet the people you'll be spending 1/3 of your life with from now on."

"That's if you manage these three months first."


label interview:
    scene interview
    with fade

"As you make your way to, I don't know, where ever, you come across-"

vue "Man I'm so stressed about this interview."

"A young man panicking next to a very chill woman."

vue "Give me some moral support bro."

tech "I'm surprised you made it this far."

vue "Thats not what I meant but-"

vue "I'm gonna go even further!"

vue "I'm gonna pass!"

vue "R-right?"

tech "Maybe."

vue "So then help me out man."

vue "I was so busy stressing about the interview I forgot to practice for it!"

tech "This sounds like your problem."

vue "Man you're the only I can trust."

vue "You literally work here so give me the insider info on what's gonna pop up."

tech "No."

vue "It be your own people..."

tech "It's your own damn fault for not preparing."

"The interviewee sees you not minding your own business."

vue "Hey you, you also doing the interview?"

label interview_intro:
        "So you here for the interview?"

menu:
        "I'm literally the interviewer, the Technical Lead."
            jump interview_intro_a

        "Yes, best of luck to both of us.":
            jump interview_intro_b

        "Let's do some interview prep questions so we can both benefit, us folks gotta look for each other and all."

		"No, I'm an intern."
            jump interview_intro_c

		"Just walk away."
            jump interview_intro_d

label interview_intro_a:

    me "I'm literally the interviewer, the Technical Lead."

    tech "..."

    vue "Kinda sus man."

    vue "Don't wanna be rude, you just don't look the type."

    vue "You two just messing with me ugh!"

    vue "I'm gonna go practice in the toilet, you guys can't distract me there atleast."

    "He walks off, pulling out a crumpled piece of paper with some scribbles on it."

    tech "Atleast he's being serious about practicing now."

    tech "Even if it's too late."

    tech "Looks like you already made it past the interview process."

    tech "Guess we'll be seeing each other around then."

"She gives a small wave as she heads off."

    me "Damn, I didn't even get her name."
        jump work_2


label interview_intro_b:

        vue "Shit, I was hoping I wouldn't have tto see any rivals before the interview but alas!"

        vue "Best of luck to you too pal."

        vue "Let's do some interview prep questions so we can both benefit, us folks gotta look for each other and all."

        vue "Even if we're fighting for the same spot."
            jump interview_quiz

##### technical quiz #####
label interview_quiz:

vue "Ok, so I have a feeling there's gonna be some questions on the Agile & Scrum stuff so I wanna do a refressher on that."

vue "I'm gonna ask you questions and hopefully you get it right cus I don't know it fully myself you see."

menu:

    jump work_2
##### end of quiz #####

label work_2:
