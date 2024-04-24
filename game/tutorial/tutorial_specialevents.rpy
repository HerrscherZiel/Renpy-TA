  
  
screen tutorial_specialevents1:

    frame:
        xsize 1920
        ysize 1080

        background "tutorial/tutorial_specialevents1.png"

    #close
    if t_spec == True:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_specialevents1", transition=fade), SetVariable('t_spec', False)]
    else:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_specialevents1", transition=fade), Return()]


