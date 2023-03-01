  
  
screen tutorial_statsdrops1:

    frame:
        xsize 1920
        ysize 1080

        background "tutorial/tutorial_statsdrops1.png"

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("tutorial_statsdrops1", transition=fade), Return()]


