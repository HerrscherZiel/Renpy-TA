
#choice counter
default lockota = 0
default lockotap = 0
default lockotas = 0
default lockotam = 0

default loclib = 0
default loclibs = 0


default loccamp = 0
default loccamps = 0

default lockamp = 0
default lockampp = 0
default lockamps = 0
default lockampm = 0

default lockos = 0
default lockosp = 0
default lockoss = 0
default lockosm = 0

default locmin = 0
default locmins = 0
default locminm = 0

screen mapUI:
    add "bg black.png"
    add "map/map new.png" 
    frame:
        background "menuUI/days.png"
        xalign 0.0
        yalign 0.0
        xsize 600
        ysize 200
        hbox:
            spacing 20
            vbox xpos 200 ypos 62:
                spacing 10
                text "[day]" size 30 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

    #dayphase conditional
    frame:
        xpos 5
        ypos 10
        xsize 1920
        ysize 1080
        if timephase == 1:
            background "menuUI/time/morning.png"
        elif timephase == 2:
            background "menuUI/time/noon.png"
        else:
            background "menuUI/time/night.png"

    if prologue == True:
        if prologueCount == 1 or prologueCount == 5 and day !=4 and KRS3 == False:
            imagebutton:
                xpos 370
                ypos 710
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")
        
        elif prologueCount == 2 or prologueCount == 6:
            imagebutton:
                xpos 1100
                ypos 10
                idle "map/kosan idle.png"
                hover "map/kosan hover.png"
                action Jump("go_to_kos")
        
        elif prologueCount == 3:
            imagebutton:
                xpos 1450
                ypos 150
                idle "map/kampung idle.png"
                hover "map/kampung hover.png"
                action Jump("go_to_kampung")

        elif prologueCount == 4:
            imagebutton:
                xpos -35
                ypos 480
                idle "map/kampus idle.png"
                hover "map/kampus hover.png"
                action Jump("go_to_campus")

        elif KRS3 == True and day !=4 :
            imagebutton:
                xpos 870
                ypos 350
                idle "map/perpustakaan idle.png"
                hover "map/perpustakaan hover.png"
                action Jump("go_to_library")

        elif day == 4 :
            imagebutton:
                xpos 370
                ypos 710
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")

            imagebutton:
                xpos 1450
                ypos 150
                idle "map/kampung idle.png"
                hover "map/kampung hover.png"
                action Jump("go_to_kampung")

            imagebutton:
                xpos 1100
                ypos 10
                idle "map/kosan idle.png"
                hover "map/kosan hover.png"
                action Jump("go_to_kos")

            imagebutton:
                xpos 1000
                ypos 210
                idle "map/kosan idle.png"
                hover "map/kosan hover.png"
                action Jump("go_do_sport")

        else:
            pass
    
    else: 
        if timephase == 3:
            #night
            #kos
            imagebutton:
                    xpos 1100
                    ypos 10
                    idle "map/kosan idle.png"
                    hover "map/kosan hover.png"
                    action Jump("go_to_kos")
            #kampung
            imagebutton:
                    xpos 1450
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")
            #kota
            imagebutton:
                    xpos 1300
                    ypos 680
                    idle "map/kota idle.png"
                    hover "map/kota hover.png"
                    action Jump("go_to_kota")

            #campuss
            imagebutton:
                xpos -35
                ypos 480
                idle "map/kampus idle.png"
                action NullAction()

            #mart
            imagebutton:
                xpos 370
                ypos 710
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")

            #library
            imagebutton:
                xpos 870
                ypos 350
                idle "map/perpustakaan idle.png"
                action NullAction()

        elif timephase == 1:
            #morn
            #kos            
            imagebutton:
                    xpos 1100
                    ypos 10
                    idle "map/kosan idle.png"
                    hover "map/kosan hover.png"
                    action Jump("go_to_kos")
            #kampung
            imagebutton:
                    xpos 1450
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")
            #kota
            imagebutton:
                    xpos 1300
                    ypos 680
                    idle "map/kota idle.png"
                    hover "map/kota hover.png"
                    action Jump("go_to_kota")

            #campuss
            imagebutton:
                xpos -35
                ypos 480
                idle "map/kampus idle.png"
                action NullAction()

            #mart
            imagebutton:
                xpos 370
                ypos 710
                idle "map/minimart idle.png"
                action NullAction()

            #library
            imagebutton:
                xpos 870
                ypos 350
                idle "map/perpustakaan idle.png"
                action NullAction()

        else:
            #noon
            #kos
            imagebutton:
                    xpos 1100
                    ypos 10
                    idle "map/kosan idle.png"
                    hover "map/kosan hover.png"
                    action Jump("go_to_kos")
            #kampung
            imagebutton:
                    xpos 1450
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")
            #kota
            imagebutton:
                    xpos 1300
                    ypos 680
                    idle "map/kota idle.png"
                    hover "map/kota hover.png"
                    action Jump("go_to_kota")
            #campuss
            imagebutton:
                xpos -35
                ypos 480
                idle "map/kampus idle.png"
                hover "map/kampus hover.png"
                action Jump("go_to_campus")

            #mart
            imagebutton:
                xpos 370
                ypos 710
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")

            #library
            imagebutton:
                xpos 870
                ypos 350
                idle "map/perpustakaan idle.png"
                hover "map/perpustakaan hover.png"
                action Jump("go_to_library")
    
label go_to_minimart:
    $ maps = True
    menu:
        "Pergi ke minimart":
            $ placeKeys = 2
            play music minimart loop volume 0.3

            if firstMart == True:
                $ maps = False
                call change_timephase from _call_change_timephase_28
                show screen trans_screen with dissolve             
                jump minimart_pertama

            elif KRS3 == False and day ==3:
                $ maps = False
                call change_timephase from _call_change_timephase_29
                show screen trans_screen with dissolve
                $ locmin += 1              
                jump mini3N

            elif day == 4:
                $ maps = False
                call change_timephase from _call_change_timephase_30
                show screen trans_screen with dissolve
                $ locmin += 1               
                jump mart_noonS1
            
            else:
                $ maps = False
                $ locmin += 1  
                show screen trans_screen with dissolve
                if timephase == 2:
                    $ locmins += 1  
                    jump choice_mart_noon
                elif timephase == 3:
                    $ locminm += 1  
                    jump choice_mart_night
                else:
                    pass

        "Tunggu dulu...":
            call screen mapUI()

label go_to_kos:

    $ maps = True
    
    menu:
        "Pergi ke Kos":
            $ placeKeys = 3
            stop music fadeout 2.0
            play music kos loop volume 0.3

            if firstKos == True:
                $ maps = False
                call change_timephase from _call_change_timephase_31
                show screen trans_screen with dissolve
                jump first_kos

            elif day == 4:
                $ maps = False
                call change_timephase from _call_change_timephase_32
                show screen trans_screen with dissolve
                $ lockos += 1
                jump kos_dayS1
            
            else:
                $ maps = False
                $ lockos += 1
                show screen trans_screen with dissolve
                if timephase == 2:
                    $ lockoss += 1
                    jump choice_kos_noon
                elif timephase == 3:
                    $ lockosm += 1
                    jump choice_kos_night
                else:
                    $ lockosp += 1
                    jump choice_kos_morn
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    $ maps = True
    menu:
        "Pergi ke kampung?":
            $ placeKeys = 4
            stop music fadeout 2.0
            play music kampung loop volume 0.3
            if firstKampung == True and day < 4:
                $ maps = False
                show screen trans_screen with dissolve
                jump first_kampung

            elif day == 4:
                $ maps = False
                $ lockamp += 1
                jump first_kota
            
            else:
                $ maps = False
                $ lockamp += 1
                show screen trans_screen with dissolve
                if timephase == 2:
                    $ lockamps += 1
                    jump choice_kampung_noon
                elif timephase == 3:
                    $ lockampm += 1
                    jump choice_kampung_night
                else:
                    $ lockampp += 1
                    jump choice_kampung_morn
                
        "Tunggu dulu...":
            call screen mapUI()

label go_do_sport:

    $ maps = True
    menu:
        "Pergi Berolahraga?":
            $ placeKeys = 4
            stop music fadeout 2.0
            play music kota loop

            if day == 4:
                $ maps = False
                call change_timephase from _call_change_timephase_33
                show screen trans_screen with dissolve
                jump sport_dayS1
            
            else:
                $ maps = False
                show screen trans_screen with dissolve
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_library:

    $ maps = True
    menu:
        "Pergi ke Perpustakaan":
            $ placeKeys = 6
            stop music fadeout 2.0   
            play music library loop volume 0.3

            if KRS3 == True and day == 3:
                $ maps = False
                $ loclib +=1
                call change_timephase from _call_change_timephase_34
                show screen trans_screen with dissolve
                $ loclibs +=1
                jump krs
            
            else:
                $ maps = False
                $ loclib +=1
                # call change_timephase
                show screen trans_screen with dissolve
                $ loclibs +=1
                jump choice_libary_noon
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kota:

    $ maps = True
    
    menu:
        "Pergi ke Kota":
            $ placeKeys = 7
            stop music fadeout 2.0
            play music kota loop volume 0.3
            
            $ maps = False
            $ lockota += 1
            show screen trans_screen with dissolve
            
            if timephase==1:
                $ lockotap += 1
                jump choice_kota_morn
            elif timephase==2:
                $ lockotas += 1
                jump choice_kota_noon
            else:
                $ lockotam += 1
                jump choice_kota_night
            
        "Tunggu dulu...":
            call screen mapUI()

label go_to_campus:

    $ maps = True
    menu:
        "Pergi ke Kampus":
            $ placeKeys = 8         
            stop music fadeout 2.0
            play music kampus loop volume 0.3

            if firstKampus == True and day <5:
                $ maps = False
                call change_timephase from _call_change_timephase_35
                show screen trans_screen with dissolve
                jump first_kampus

            elif day == 8:
                $ maps = False
                $ loccamp += 1
                show screen trans_screen with dissolve
                $ loccamps += 1
                jump join_hima

            elif day>7 and day%4 == 0:
                $ maps = False
                $ loccamp += 1
                show screen trans_screen with dissolve
                $ loccamps += 1
                $ olahragac += 1
                jump sport_noonS3

            else:
                $ maps = False
                $ loccamp += 1
                show screen trans_screen with dissolve
                $ loccamps += 1
                jump datang_kampus
                
        "Tunggu dulu...":
            call screen mapUI()
