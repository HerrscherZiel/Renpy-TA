
screen get_box:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        # background "items/get_frame.png"
        background "items/box_get.png"
    
    timer 4.0 action Hide("get_box", dissolve)

screen get_box2:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        # background "items/get_frame.png"
        background "items/box2_get.png"
    
    timer 4.0 action Hide("get_box2", dissolve)

screen get_bread:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        background "items/breads_get.png"
    
    timer 4.0 action Hide("get_bread", dissolve)

    # #close
    # imagebutton:
    #     xpos 70
    #     ypos 950
    #     idle "menuUI/stats/return_idle.png"
    #     hover "menuUI/stats/return_hover.png"
    #     action [Hide("tutorial_specialevents1", transition=fade), Return()]