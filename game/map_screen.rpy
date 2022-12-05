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
                jump kos_pertama
            
            else:
                jump nothing
                
        "Tunggu dulu...":
            call screen mapUI()