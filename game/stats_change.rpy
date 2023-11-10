

screen stats_changer(tstats, tpoint):

    if tstats=="fond":
            
        timer 0.1 action [Hide("stats_changer"), Show("fond_change", dissolve)]

    #health
    elif tstats == "eat":

        timer 0.1 action [Hide("stats_changer"), Show("eat_change", dissolve)]

    elif tstats == "small_eat":

        timer 0.1 action [Hide("stats_changer"), Show("seat_change", dissolve)]

    elif tstats == "nap":

        timer 0.1 action [Hide("stats_changer"), Show("nap_change", dissolve)]

    elif tstats == "drink":

        timer 0.1 action [Hide("stats_changer"), Show("drink_change", dissolve)]
    
    #time
    elif tstats == "change_timephase":

        timer 0.5 action [Hide("stats_changer"), Show("time_change", dissolve)]

    elif tstats == "change_day":

        timer 3.0 action [Hide("stats_changer"), Show("day_change", dissolve)]

    #sports
    elif tstats == "jog":

        timer 0.1 action [Hide("stats_changer"), Show("jog_change", dissolve)]

    elif tstats == "futsal":

        timer 0.1 action [Hide("stats_changer"), Show("futsal_change", dissolve)]

    #class
    elif tstats == "class":

        timer 0.1 action [Hide("stats_changer"), Show("class_change", dissolve)]

    #social
    elif tstats == "kerja_bakti":

        timer 0.1 action [Hide("stats_changer"), show("kerja_bakti_change", dissolve)]

    else:

        text "How"

#social
screen fond_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        background "menuUI/stats/fond_up.png"

    timer 4.0 action Hide("fond_change", dissolve)


#health
screen eat_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30

        background "menuUI/stats/hunger_up.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()        

    timer 4.0 action Hide("eat_change", dissolve)

screen seat_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30

        background "menuUI/stats/hunger_up.png"     

    timer 4.0 action Hide("seat_change", dissolve)

screen nap_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30

        background "menuUI/stats/hunger_down.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()        

    timer 4.0 action Hide("nap_change", dissolve)

screen drink_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1050
        ypos 30

        background "menuUI/stats/hunger_up.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_up.png"
                action NullAction()   

    timer 4.0 action Hide("drink_change", dissolve)


#time
screen time_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30

        background "menuUI/stats/hunger_down.png"
  

        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_down.png"
                action NullAction()        

    timer 4.0 action Hide("time_change", dissolve)

screen day_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30

        background "menuUI/stats/hunger_down.png"
  

        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_down.png"
                action NullAction()        

    timer 4.0 action Hide("day_change", dissolve)
    

#sport
screen jog_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30

        background "menuUI/stats/hunger_down.png"
  

        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/hunger_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/energy_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()        

    timer 4.0 action Hide("jog_change", dissolve)

screen futsal_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30
        background "menuUI/stats/energy_down.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/energy_down.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/public_up.png"
                action NullAction()        

    timer 4.0 action Hide("futsal_change", dissolve)


#class
screen class_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1050
        ypos 30

        background "menuUI/stats/knowl_up.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/knowl_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/pract_up.png"
                action NullAction()   

    timer 4.0 action Hide("class_change", dissolve)

screen kerja_bakti_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30
        background "menuUI/stats/public_up.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/public_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/community_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()        

    timer 4.0 action Hide("kerja_bakti_change", dissolve)