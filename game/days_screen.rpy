
screen days_screen:

    frame:
        # add "menuUI/bg grey.png"
        xpadding 10
        ypadding 5
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 20

        hbox:
            spacing 20

            vbox:
                spacing 10
                text "Day" size 45
                text "[day]" size 30
            
            vbox:
                spacing 10
                if timephase == 1:
                    text "Noon"
                elif timephase == 2:
                    text "Night"
                else:
                    text "Morning"

                text "[place_list[1]]"