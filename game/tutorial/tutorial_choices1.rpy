  
  
screen tutorial_choices1:

    frame:
        xsize 1920
        ysize 1080

        background "tutorial/tutorial_choice1.png"

    #slide left
    imagebutton:
        xpos 1150
        ypos 950
        idle "tutorial/left_idle.png"
        hover "tutorial/left_idle.png"
        action NullAction()

    #slide right
    imagebutton:
        xpos 1320
        ypos 950
        auto "tutorial/right_%s.png"
        action [Hide("tutorial_choices1"), Show("tutorial_choices2")]

    #close
    if t_choices == True:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_choices1", transition=fade), SetVariable('t_choices', False)]
    else:    
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_choices1", transition=fade), Return()]


screen tutorial_choices2:

    frame:
        xsize 1920
        ysize 1080
        background "tutorial/tutorial_choice2.png"

    #slide left
    imagebutton:
        xpos 1150
        ypos 950
        auto "tutorial/left_%s.png"
        action  [Hide("tutorial_choices2"), Show("tutorial_choices1")]

    #slide right
    imagebutton:
        xpos 1320
        ypos 950
        idle "tutorial/right_idle.png"
        hover "tutorial/right_idle.png"

    #close
    if t_choices == True:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_choices2", transition=fade), SetVariable('t_choices', False)]
    else:    
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_choices2", transition=fade), Return()]

