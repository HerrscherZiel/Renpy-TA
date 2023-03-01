  
  
screen tutorial_statschange1:

    frame:
        xsize 1920
        ysize 1080

        background "tutorial/tutorial_statschange1.png"

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("tutorial_statschange1", transition=fade), Return()]


