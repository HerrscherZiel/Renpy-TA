
default trivia_perkuliahan2 = 1

screen trivia_perkuliahan2:

    frame:
        xsize 1920
        ysize 1080

        background "trivia/perkuliahan/trivia_kuliah.png"

        #base image
        imagebutton:
            xpos 482
            ypos 275
            idle "trivia/perkuliahan/kuliah_nilai.png"

    #slide left
    imagebutton:
        if (trivia_perkuliahan2 == 1):
            xpos 1030
            ypos 850
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1030
            ypos 850
            auto "tutorial/left_%s.png"
            action  [SetVariable("trivia_perkuliahan2", If(trivia_perkuliahan2>=2, trivia_perkuliahan2-1, )), Show("trivia_perkuliahan2_image")]

    #slide right
    imagebutton:
        if (trivia_perkuliahan2 == 4):
            xpos 1200
            ypos 850
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1200
            ypos 850
            auto "tutorial/right_%s.png"
            action  [SetVariable("trivia_perkuliahan2", If(trivia_perkuliahan2<=4, trivia_perkuliahan2+1, )), Show("trivia_perkuliahan2_image")]

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_perkuliahan2", transition=fade), Hide("trivia_perkuliahan2_image", transition=fade), Return()]

screen trivia_perkuliahan2_image:

    frame:
        xsize 1920
        ysize 1080

        if (trivia_perkuliahan2 == 1):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/kuliah_nilai.png"
        
        elif (trivia_perkuliahan2 == 2):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/kuliah_ip.png"

        elif (trivia_perkuliahan2 == 3):
            xpos 488
            ypos 281
            background "trivia/perkuliahan/kuliah_jadwalkalendar.png"

        else:
            xpos 488
            ypos 281
            background "trivia/perkuliahan/kuliah_tugas.png"
