

default tutorial_jadwalkalender1 = 1
  
screen tutorial_jadwalkalender1:

    frame:
        xsize 1920
        ysize 1080
        background "tutorial/tutorial_jadwalkalender.png"

    #slide left
    imagebutton:
        if (tutorial_jadwalkalender1 == 1):
            xpos 1090
            ypos 940
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1090
            ypos 940
            auto "tutorial/left_%s.png"
            action  [SetVariable("tutorial_jadwalkalender1", If(tutorial_jadwalkalender1>=2, tutorial_jadwalkalender1-1, )), Show("tutorial_jadwalkalender_image")]

    #slide right
    imagebutton:
        if (tutorial_jadwalkalender1 == 3):
            xpos 1260
            ypos 940
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1260
            ypos 940
            auto "tutorial/right_%s.png"
            action  [SetVariable("tutorial_jadwalkalender1", If(tutorial_jadwalkalender1<=3, tutorial_jadwalkalender1+1, )), Show("tutorial_jadwalkalender_image")]

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("tutorial_jadwalkalender1", transition=fade), Hide("tutorial_jadwalkalender_image", transition=fade), Return()]

screen tutorial_jadwalkalender_image:

    frame:
        xsize 1920
        ysize 1080

        if (tutorial_jadwalkalender1 == 1):
            xpos 708
            ypos 252
            background "tutorial/tutorial_jadwalkalender1.png"
        
        elif (tutorial_jadwalkalender1 == 2):
            xpos 708
            ypos 252
            background "tutorial/tutorial_jadwalkalender2.png"

        else:
            xpos 708
            ypos 252
            background "tutorial/tutorial_jadwalkalender3.png"
