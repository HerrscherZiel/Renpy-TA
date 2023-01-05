

screen days_screen:

    if renpy.get_screen("mapUI"):
        pass

    elif maps == True:
        pass

    else:
        frame:
            background "menuUI/days.png"
            # xpadding 10
            # ypadding 5
            xalign 0.0
            yalign 0.0
            xsize 600
            ysize 200
            # xoffset 30
            # yoffset 20

            hbox:
                spacing 20

                vbox xpos 200 ypos 62:
                    spacing 10
                    # ypadding 10
                    # text "Day" size 26
                    text "[day]" size 30 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    
                
                vbox xpos 120:
                    spacing 10
                    if placeKeys == 1:
                        text "Jalan Kampus" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 2:
                        text "Minimarket" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 3:
                        text "Kos" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 4:
                        text "Warmindo" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 5:
                        text "Kampung" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 6:
                        text "Perpustakaan" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 7:
                        text "Parkiran" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 8:
                        text "Kampus" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    elif placeKeys == 9:
                        text "Kelas" color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                    else:
                        pass

        frame:
            # xpadding 10
            # ypadding 5
            # xalign 0.5
            # yalign 0.0
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
            # xoffset 30
            # yoffset 20
