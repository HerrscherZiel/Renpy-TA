
default tutorial_task1 = 1
  
screen tutorial_task1:

    frame:
        xsize 1920
        ysize 1080
        background "tutorial/tutorial_task.png"

    #slide left
    imagebutton:
        if (tutorial_task1 == 1):
            xpos 1090
            ypos 940
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1090
            ypos 940
            auto "tutorial/left_%s.png"
            action  [SetVariable("tutorial_task1", If(tutorial_task1>=2, tutorial_task1-1, )), Show("tutorial_task_image")]

    #slide right
    imagebutton:
        if (tutorial_task1 == 3):
            xpos 1260
            ypos 940
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1260
            ypos 940
            auto "tutorial/right_%s.png"
            action  [SetVariable("tutorial_task1", If(tutorial_task1<=3, tutorial_task1+1, )), Show("tutorial_task_image")]

    #close
    if t_task == True:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_task1", transition=fade), Hide('tutorial_task_image'), SetVariable('t_task', False)]
    else:
        imagebutton:
            xpos 70
            ypos 950
            idle "menuUI/stats/return_idle.png"
            hover "menuUI/stats/return_hover.png"
            action [Hide("tutorial_task1", transition=fade), Hide('tutorial_task_image'), Return()]

screen tutorial_task_image:

    frame:
        xsize 1920
        ysize 1080

        if (tutorial_task1 == 1):
            xpos 708
            ypos 252
            background "tutorial/tutorial_task_1.png"
        
        elif (tutorial_task1 == 2):
            xpos 708
            ypos 252
            background "tutorial/tutorial_task_2.png"

        else:
            xpos 708
            ypos 252
            background "tutorial/tutorial_task_3.png"
