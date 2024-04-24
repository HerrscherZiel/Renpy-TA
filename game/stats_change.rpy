

default fulls = False
default fullscount = 6
default fitt = False
default fittcount = 6
default healthy = False
default healthycount = 6
default thin = False
default thincount = 6
default weak = False
default weakcount = 6
default sick = False
default sickcount = 6
default publicc = 0
default communityc = 0



label stat_change:

#status
    if fulls == True:
        $ fullscount -= 2
        $ hunger += 10
        if fullscount == 0:
            $ fulls = False

    if fitt == True:
        $ fittcount -= 2
        $ vit +=5
        if fittcount == 0:
            $ fitt = False

    if healthy == True:
        $ healthycount -= 2
        $ energy += 10
        if healthycount == 0:
            $ healthy = False

    if thin == True:
        $ thincount -= 2
        $ hunger -= 10
        if thincount == 0:
            $ thin = False

    if weak == True:
        $ weakcount -= 2
        $ vit -= 5
        if weakcount == 0:
            $ weak = False

    if sick == True:
        $sickcount -= 2
        $hunger -= 10
        if sickcount == 0:
            $sick = False

#stats
    if hunger >= 100:
        $ hunger = 100
        $ obesseCount +=1
        if obesseCount  %  5 == 0:
            $ fulls = True
            $ fullscount = 6
            
    if hunger <= 0:
        $ hunger = 0
        $ thinCount +=1
        if thinCount  %  5 == 0:
            $ thin = True
            $ thins += 1
            $ thincount = 6
        
    if energy >= 100:
        $ energy = 100
        $ healthyCount +=1
        if healthyCount  %  5 == 0:
            $ healthy = True
            $ healthycount = 6

    if energy <= 0:
        $ energy = 0
        $ sickCount +=1
        if sickCount  %  5 == 0:
            $ sick = True
            $ sicks += 1
            $ sickcount = 6

    if vit >= 70:
        $ vit = 100
        $ fitCount +=1
        if fitCount  %  5 == 0:
            $ fitt = True
            $ fittcount = 6

    if vit <= 0:
        $ vit = 0
        $ weakCount +=1
        if weakCount  %  5 == 0:
            $ weak = True
            $ weaks += 1
            $ weakcount = 6

#friend
    if rissa_fond >= 30 and rissa_fond < 60:
        $ kenalan +=1
    elif rissa_fond >= 60:
        $ friendc +=1
        $ kenalan -=1

    if trije_fond >= 30 and trije_fond < 60:
        $ kenalan +=1
    elif trije_fond >= 60:
        $ friendc +=1
        $ kenalan -=1
        
    if kevin_fond >= 30 and kevin_fond < 60:
        $ kenalan +=1
    elif kevin_fond >= 60:
        $ friendc +=1
        $ kenalan -=1

    return

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
        
    elif tstats == "jalan_sehatS":

        timer 0.1 action [Hide("stats_changer"), Show("jalan_sehat_change", dissolve)]

    elif tstats == "futsal":

        timer 0.1 action [Hide("stats_changer"), Show("futsal_change", dissolve)]

    #class
    elif tstats == "class":

        timer 0.1 action [Hide("stats_changer"), Show("class_change", dissolve)]

    #social
    elif tstats == "kerja_bakti":

        timer 0.1 action [Hide("stats_changer"), Show("kerja_bakti_change", dissolve)]

    elif tstats == "hangout":

        timer 0.1 action [Hide("stats_changer"), Show("hangout_change", dissolve)]

    elif tstats == "hima_act":

        timer 0.1 action [Hide("stats_changer"), Show("hima_change", dissolve)]
    
    #task
    elif tstats == "n_task":

        timer 0.1 action [Hide("stats_changer"), Show("tasknew_change", dissolve)]
    
    elif tstats == "c_task":

        timer 0.1 action [Hide("stats_changer"), Show("taskcom_change", dissolve)]

    else:

        text "How"

#task
screen tasknew_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        background "menuUI/stats/new task.png"

    timer 4.0 action Hide("tasknew_change", dissolve)

screen taskcom_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1300
        ypos 30
        background "menuUI/stats/task completed.png"

    timer 4.0 action Hide("taskcom_change", dissolve)

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

screen jalan_sehat_change:

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

    timer 4.0 action Hide("jalan_sehat_change", dissolve)

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

#social
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
                idle "menuUI/stats/commu_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/fit_up.png"
                action NullAction()        

    timer 4.0 action Hide("kerja_bakti_change", dissolve)

screen hima_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 800
        ypos 30
        background "menuUI/stats/commu_up.png"
  
        hbox:
            spacing 15

            imagebutton:
                xpos -6
                ypos -6
                idle "menuUI/stats/commu_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/public_up.png"
                action NullAction()

            imagebutton:
                idle "menuUI/stats/friend_up.png"
                action NullAction()    

    timer 4.0 action Hide("hima_change", dissolve)         

screen hangout_change:

    frame:
        xsize 1920
        ysize 1080
        xpos 1050
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
                idle "menuUI/stats/friend_up.png"
                action NullAction()   

    timer 4.0 action Hide("hangout_change", dissolve)    