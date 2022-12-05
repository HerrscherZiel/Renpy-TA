screen stats_screen:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "menuUI/statsmenu.png"
        action ShowMenu("stats")

screen stats:

    add "menuUI/bg grey.png"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Health" size 40
                text "Hunger" size 30
                text "Energy" size 30
                text "Vit" size 30

            vbox:
                spacing 10
                text "[health]" size 40
                text "[hunger]" size 30
                text "[energy]" size 30
                text "[vit]" size 30
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 30
        idle "menuUI/back_arrow.png"
        action Return()

