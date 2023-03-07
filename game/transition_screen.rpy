
screen trans_screen:

    # xsize 1920
    # ysize 1080

    add "bg black.png"

    frame:

        xsize 1920
        ysize 640
        xalign 0.5
        yalign 0.5
        background "trans/transition.png"


        if timephase == 1:

            vbox:
                xalign 0.5
                yalign 0.35
                xanchor 0.5
                text "PAGI" size 75 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

            vbox:
                xalign 0.5
                yalign 0.6
                xanchor 0.5
                if placeKeys == 1:
                    text "Jalan Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 2:
                    text "Minimarket" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 3:
                    text "Kos" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 4:
                    text "Kampung" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 5:
                    text "Warmindo" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 6:
                    text "Perpustakaan" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 7:
                    text "Parkiran" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 8:
                    text "Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 9:
                    text "Kelas" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                else:
                    pass

        elif timephase == 2:
            vbox:
                xalign 0.5
                yalign 0.35
                xanchor 0.5
                text "SIANG" size 75 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

            vbox:
                xalign 0.5
                yalign 0.6
                xanchor 0.5
                if placeKeys == 1:
                    text "Jalan Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 2:
                    text "Minimarket" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 3:
                    text "Kos" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 4:
                    text "Kampung" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 5:
                    text "Warmindo" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 6:
                    text "Perpustakaan" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 7:
                    text "Parkiran" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 8:
                    text "Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 9:
                    text "Kelas" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                else:
                    pass
        else:
            vbox:
                xalign 0.5
                yalign 0.35
                xanchor 0.5
                text "MALAM" size 75 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"

            vbox:
                xalign 0.5
                yalign 0.6
                xanchor 0.5
                if placeKeys == 1:
                    text "Jalan Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 2:
                    text "Minimarket" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 3:
                    text "Kos" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 4:
                    text "Kampung" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 5:
                    text "Warmindo" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 6:
                    text "Perpustakaan" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 7:
                    text "Parkiran" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 8:
                    text "Kampus" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                elif placeKeys == 9:
                    text "Kelas" size 55 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
                else:
                    pass

        # imagebutton:
        #     xalign 0.5
        #     yalign 0.5
        #     idle "trans/layer.png"
        #     action Return()

    timer 2.5 action Hide("trans_screen", dissolve)



