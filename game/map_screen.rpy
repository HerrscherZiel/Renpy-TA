
screen mapUI:

    add "bg black.png"
    add "map/map.png" 

    if prologue == True:
        if prologueCount == 1 or prologueCount == 6:
            imagebutton:
                xpos 1250
                ypos 760
                idle "map/minimart idle.png"
                hover "map/minimart hover.png"
                action Jump("go_to_minimart")
        
        elif prologueCount == 2:
            imagebutton:
                xpos 1150
                ypos 10
                idle "map/house idle.png"
                hover "map/house hover.png"
                action Jump("go_to_kos")
        
        elif prologueCount == 3:
            imagebutton:
                xpos 1250
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

        elif KRS3 == True:
            imagebutton:
                xpos 900
                ypos 450
                idle "map/perpustakaan idle.png"
                hover "map/perpustakaan hover.png"
                action Jump("go_to_library") 
    
    else:
        pass
    
label go_to_minimart:

    $ maps = True

    menu:
        "Pergi ke minimart":
            $ placeKeys = 2

            if timephase != 3:
                $ timephase += 1

            else:
                $ timephase = 1

            if firstMart == True:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase                
                window show
                jump minimart_pertama
            
            else:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                # window show
                jump nothing

        "Tunggu dulu...":
            call screen mapUI()

label go_to_kos:

    $ maps = True

    # scene bg black with dissolve
    
    menu:
        "Pergi ke Kos":
            $ placeKeys = 3
            
            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1

            if firstKos == True:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                window show
                jump first_kos
            
            else:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                # window show
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    $ maps = True
    # scene bg black with dissolve

    menu:
        "Pergi Jalan-jalan?":
            $ placeKeys = 4

            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1

            if firstKampung == True:
                $ maps = False
                $ timephase -= 1
                call screen trans_screen with dissolve
                call change_timephase
                window show
                jump first_kampung
            
            else:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
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

            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1            

            if firstKampus == True:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                window show
                jump first_kampus
            
            else:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
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

            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1            

            if KRS3 == True:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                window show
                jump krs
            
            else:
                $ maps = False
                call screen trans_screen with dissolve
                call change_timephase
                # window show
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()