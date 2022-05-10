screen achievements():
    tag menu
    add "#aaaa"

    frame:
        xpadding 50
        ypadding 25
        xalign 0.5
        yalign 0.3
        text "ACHIEVEMENTS"

    frame:
        xpadding 50
        ypadding 25
        xalign 0.5
        yalign 0.5
        grid 2 4:

            if achievement.has("first_day"): #first phrase is the completed one.
                 text "First day." color "#2D6E65"
                 text "Not looking forward to tomorrow." color "#2D6E65"

            if achievement.has("Employee_of_the_Week"):
                 text "Employee of the Week." color "#2D6E65"
                 text "You understood the assignment." color "#2D6E65"

            else:
                 text "Employee of the Week." color "#873737"
                 text "Complete all your tasks." color "#873737"


    textbutton "Close" action Return()
