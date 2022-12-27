# screen map_screen:
#     imagebutton:
#         xalign 1.0
#         yalign 0.5
#         xoffset -30
#         yoffset 30
#         idle "menuUI/statsmenu.png"
#         action ShowMenu("mapUI")

screen mapUI:

    add "menuUI/bg grey.png"
    add "map/map.png"

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
        action Jump("go_to_boarding_house")
    
    imagebutton:
        xpos 1250
        ypos 150
        idle "map/kampung idle.png"
        hover "map/kampung hover.png"
        action Jump("go_to_kampung")

    imagebutton:
        xpos 300
        ypos 760
        idle "map/kampus idle.png"
        hover "map/kampus hover.png"
        action Jump("go_to_campus")
    
label go_to_minimart:

    menu:
        "Pergi ke minimart":

            if firstMart == True:
                jump minimart_pertama
            
            else:
                jump nothing

        "Tunggu dulu...":
            call screen mapUI()

label go_to_boarding_house:

    menu:
        "Pergi ke Kos":

            if firstKos == True:
                jump first_boarding_house
            
            else:
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_kampung:

    menu:
        "Pergi Jalan-jalan?":

            if firstKampung == True:
                jump first_kampung
            
            else:
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()

label go_to_campus:

    menu:
        "Pergi ke Kos":

            if firstKampus == True:
                jump first_kampus
            
            else:
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()