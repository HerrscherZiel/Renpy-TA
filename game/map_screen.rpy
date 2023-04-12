
screen mapUI:

    add "bg black.png"
    add "map/map.png" 

    if prologue == True:
        if prologueCount == 1 or prologueCount == 5 and day !=4 and KRS3 == False:
            imagebutton:
                xpos 1250
                ypos 760
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")
        
        elif prologueCount == 2 or prologueCount == 6:
            imagebutton:
                xpos 1150
                ypos 10
                idle "map/house idle.png"
                hover "map/house hover.png"
                action Jump("go_to_kos")
        
        elif prologueCount == 3:
            imagebutton:
                xpos 1500
                ypos 150
                idle "map/kampung idle.png"
                hover "map/kampung hover.png"
                action Jump("go_to_kampung")

        elif prologueCount == 4:
            imagebutton:
                xpos 300
                ypos 760
                idle "map/kampus idle.png"
                hover "map/kampus hover.png"
                action Jump("go_to_campus")

        elif KRS3 == True and day !=4 :
            imagebutton:
                xpos 900
                ypos 450
                idle "map/perpustakaan idle.png"
                hover "map/perpustakaan hover.png"
                action Jump("go_to_library")

        elif day == 4 :
            imagebutton:
                xpos 1250
                ypos 760
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")

            imagebutton:
                xpos 1500
                ypos 150
                idle "map/kampung idle.png"
                hover "map/kampung hover.png"
                action Jump("go_to_kampung")

            imagebutton:
                xpos 1150
                ypos 10
                idle "map/house idle.png"
                hover "map/house hover.png"
                action Jump("go_to_kos")

            imagebutton:
                xpos 1000
                ypos 210
                idle "map/house idle.png"
                hover "map/house hover.png"
                action Jump("go_do_sport")

        else:
            pass

    else:

        if timephase == 3:
            #Night to Morning
            imagebutton:
                    xpos 1150
                    ypos 10
                    idle "map/house idle.png"
                    hover "map/house hover.png"
                    action Jump("go_to_kos")
            
            imagebutton:
                    xpos 1500
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")

            imagebutton:
                    xpos 300
                    ypos 760
                    idle "map/kampus idle.png"
                    hover "map/kampus hover.png"
                    action Jump("go_to_kota")

            # pass

        elif timephase == 1:
            #Morning to Noon

            imagebutton:
                    xpos 1150
                    ypos 10
                    idle "map/house idle.png"
                    hover "map/house hover.png"
                    action Jump("go_to_kos")
            
            imagebutton:
                    xpos 1500
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")

            imagebutton:
                    xpos 600
                    ypos 760
                    idle "map/kampus idle.png"
                    hover "map/kampus hover.png"
                    action Jump("go_to_kota")
            # imagebutton:
            #     xpos 1250
            #     ypos 760
            #     idle "map/minimart idle.png"
            #     hover "map/minimart hover.png"
            #     action Jump("go_to_minimart")
        
            # imagebutton:
            #         xpos 1150
            #         ypos 10
            #         idle "map/house idle.png"
            #         hover "map/house hover.png"
            #         action Jump("go_to_kos")
            
            # imagebutton:
            #         xpos 1500
            #         ypos 150
            #         idle "map/kampung idle.png"
            #         hover "map/kampung hover.png"
            #         action Jump("go_to_kampung")

            # imagebutton:
            #         xpos 300
            #         ypos 760
            #         idle "map/kampus idle.png"
            #         hover "map/kampus hover.png"
            #         action Jump("go_to_campus")

            # imagebutton:
            #         xpos 900
            #         ypos 450
            #         idle "map/perpustakaan idle.png"
            #         hover "map/perpustakaan hover.png"
            #         action Jump("go_to_library") 

        else:
            #Noon to Night
            imagebutton:
                xpos 1250
                ypos 760
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")
        
            imagebutton:
                    xpos 1150
                    ypos 10
                    idle "map/house idle.png"
                    hover "map/house hover.png"
                    action Jump("go_to_kos")
            
            imagebutton:
                    xpos 1500
                    ypos 150
                    idle "map/kampung idle.png"
                    hover "map/kampung hover.png"
                    action Jump("go_to_kampung")

    
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

            elif KRS3 == False:
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
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump nothing

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
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    $ maps = True

    menu:
        "Pergi Jalan-jalan?":
            $ placeKeys = 4

            if firstKampung == True and day != 4:
                $ maps = False
                show screen trans_screen with dissolve
                jump first_kampung

            elif day == 4:
                $ maps = False
                jump first_kota
            
            else:
                $ maps = False
                # call change_timephase
                show screen trans_screen with dissolve
                jump nothing
                
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
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_campus:

    $ maps = True
    # scene bg black with dissolve

    menu:
        "Pergi ke Kampus":
            $ placeKeys = 8         

            if firstKampus == True:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump first_kampus
            
            else:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_library:

    $ maps = True
    # scene bg black with dissolve

    menu:
        "Pergi ke Perpustakaan":
            $ placeKeys = 6       

            if KRS3 == True:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump krs
            
            else:
                $ maps = False
                call change_timephase
                show screen trans_screen with dissolve
                # window show
                jump nothing
                
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