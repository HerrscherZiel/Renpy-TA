
screen mapUI:

    add "menuUI/bg grey.png"
    add "map/map.png" 

    if prologue == True:
        if prologueCount == 1 or prologueCount == 5:
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
    
    else:
        pass
    
label go_to_minimart:
    # init python:
    #     def label_callback(name, abnormal):
    #         store.last_label = name

    #     config.label_callback = label_callback
    # scene bg black with dissolve
    # $maps 
    $ maps = True

    menu:
        "Pergi ke minimart":
            $ placeKeys = 2

            if timephase != 3:
                $ timephase += 1


            else:
                $ timephase = 1

            if firstMart == True:
                $maps = False
                jump minimart_pertama
            
            else:
                $maps = False
                jump nothing

        "Tunggu dulu...":
            call screen mapUI()

label go_to_kos:

    scene bg black with dissolve
    
    $ maps = True
    menu:
        "Pergi ke Kos":
            $ placeKeys = 3
            
            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1

            if firstKos == True:
                $maps = False
                jump first_kos
            
            else:
                $maps = False
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    $ maps = True
    menu:
        "Pergi Jalan-jalan?":
            $ placeKeys = 4

            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1

            if firstKampung == True:
                $maps = False
                jump first_kampung
            
            else:
                $maps = False
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_campus:

    $ maps = True
    menu:
        "Pergi ke Kampus":
            $ placeKeys = 8

            if timephase != 3:
                $ timephase += 1
            else:
                $ timephase = 1            

            if firstKampus == True:
                $maps = False
                jump first_kampus
            
            else:
                $maps = False
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()