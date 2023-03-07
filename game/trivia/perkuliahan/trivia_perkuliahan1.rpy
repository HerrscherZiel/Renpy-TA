
default trivia_perkuliahan1 = 1

screen trivia_perkuliahan1:

    frame:
        xsize 1920
        ysize 1080

        background "trivia/perkuliahan/trivia_alurperkuliahan.png"

        #base image
        imagebutton:
            xpos 482
            ypos 275
            idle "trivia/perkuliahan/semester.png"

    #slide left
    imagebutton:
        if (trivia_perkuliahan1 == 1):
            xpos 1030
            ypos 850
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1030
            ypos 850
            auto "tutorial/left_%s.png"
            action  [SetVariable("trivia_perkuliahan1", If(trivia_perkuliahan1>=2, trivia_perkuliahan1-1, )), Show("trivia_perkuliahan_image")]

    #slide right
    imagebutton:
        if (trivia_perkuliahan1 == 5):
            xpos 1200
            ypos 850
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1200
            ypos 850
            auto "tutorial/right_%s.png"
            action  [SetVariable("trivia_perkuliahan1", If(trivia_perkuliahan1<=4, trivia_perkuliahan1+1, )), Show("trivia_perkuliahan_image")]

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_perkuliahan1", transition=fade), Hide("trivia_perkuliahan_image", transition=fade), Return()]

screen trivia_perkuliahan_image:

    frame:
        xsize 1920
        ysize 1080

        if (trivia_perkuliahan1 == 1):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/semester.png"
        
        elif (trivia_perkuliahan1 == 2):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/pertemuan.png"

        elif (trivia_perkuliahan1 == 3):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/krs.png"
        
        elif (trivia_perkuliahan1 == 4):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/krs 1.png"

        else:
            xpos 488
            ypos 281
            background "trivia/perkuliahan/krs 2.png"
