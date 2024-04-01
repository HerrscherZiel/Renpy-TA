
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
                
            
            # vbox xpos 120:
            #     spacing 10
            #     if placeKeys == 1:
            #         text "Jalan Kampus" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 2:
            #         text "Minimarket" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 3:
            #         text "Kos" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 4:
            #         text "Kampung" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 5:
            #         text "Warmindo" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 6:
            #         text "Perpustakaan" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 7:
            #         text "Kota" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 8:
            #         text "Kampus" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     elif placeKeys == 9:
            #         text "Kelas" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            #     else:
            #         pass

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
    # imagebutton:
    #     xpos 320
    #     ypos 60
    #     auto "map/tasks_%s.png"
    #     action ShowMenu("task_list")

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

            if firstMart == True:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve             
                jump minimart_pertama

            elif KRS3 == False and day ==3:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve              
                jump mini3N

            elif day == 4:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve              
                jump mart_noonS1
            
            else:
                $ maps = False
                show screen trans_screen with dissolve
                if timephase == 2:
                    jump choice_mart_noon
                elif timephase == 3:
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
            
            if firstKos == True:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                jump first_kos

            elif day == 4:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                jump kos_dayS1
            
            else:
                $ maps = False
                show screen trans_screen with dissolve
                if timephase == 2:
                    jump choice_kos_noon
                elif timephase == 3:
                    jump choice_kos_night
                else:
                    jump choice_kos_morn
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    $ maps = True
    menu:
        "Pergi keluar?":
            $ placeKeys = 4

            if firstKampung == True and day < 4:
                $ maps = False
                show screen trans_screen with dissolve
                jump first_kampung

            elif day == 4:
                $ maps = False
                jump first_kota
            
            else:
                $ maps = False
                show screen trans_screen with dissolve
                if timephase == 2:
                    jump choice_kampung_noon
                elif timephase == 3:
                    jump choice_kampung_night
                else:
                    jump choice_kampung_morn
                
        "Tunggu dulu...":
            call screen mapUI()

label go_do_sport:

    $ maps = True
    menu:
        "Pergi Berolahraga?":
            $ placeKeys = 4

            if day == 4:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                jump sport_dayS1
            
            else:
                $ maps = False
                show screen trans_screen with dissolve
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_campus:

    $ maps = True
    menu:
        "Pergi ke Kampus":
            $ placeKeys = 8         

            if firstKampus == True and day <5:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                jump first_kampus

            elif day == 8:
                $ maps = False
                show screen trans_screen with dissolve
                jump join_hima

            elif day>7 and day%4 == 0:
                $ maps = False
                show screen trans_screen with dissolve
                jump sport_noonS3

            else:
                $ maps = False
                show screen trans_screen with dissolve
                jump datang_kampus
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_library:

    $ maps = True
    menu:
        "Pergi ke Perpustakaan":
            $ placeKeys = 6       

            if KRS3 == True:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                jump krs
            
            else:
                $ maps = False
                # call change_timephase
                show screen trans_screen with dissolve
                jump choice_libary_noon
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kota:

    $ maps = True
    
    menu:
        "Pergi ke Kota":
            $ placeKeys = 7
            
            $ maps = False
            show screen trans_screen with dissolve
            
            if timephase==1:
                jump choice_kota_morn
            elif timephase==2:
                jump choice_kota_noon
            else:
                jump choice_kota_night
            
        "Tunggu dulu...":
            call screen mapUI()