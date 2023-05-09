
screen jadwal_btn:
    if renpy.get_screen("mapUI"):
        pass

    elif maps == True:
        pass
    else:
        imagebutton:
            xpos 1775
            ypos 280
            auto "menuUI/button/jadwal_%s.png"
            action ShowMenu("jadwal_kuliah")

screen kalendar_btn:
    if renpy.get_screen("mapUI"):
        pass

    elif maps == True:
        pass
    else:
        imagebutton:
            xpos 1775
            ypos 350
            auto "menuUI/button/kalender_%s.png"
            action ShowMenu("kalender_kuliah")              

screen jadwal_kuliah:

    add "bg black.png"

    frame:
        xsize 1920
        ysize 1080
        xpos 220
        ypos 70
        background "menuUI/jadwal.png"

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()

screen kalender_kuliah:

    add "bg black.png"

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/kalender.png"

    frame:
        background "trivia/menu/desc_layer.png"
        hbox:
            spacing 87
            if k_days == 5:
                imagebutton:
                    xpos 1182
                    ypos 223
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 5:
                imagebutton:
                    xpos 1182
                    ypos 223
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 6:
                imagebutton:
                    xpos 1182
                    ypos 223
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 6:
                imagebutton:
                    xpos 1182
                    ypos 223
                    idle "menuUI/pass.png"
                    action NullAction()
        hbox:
            spacing 87
            if k_days == 7:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 7:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 8:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 8:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 9:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 9:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 10:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 10:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 11:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 11:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 12:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 12:
                imagebutton:
                    xpos 353
                    ypos 373
                    idle "menuUI/pass.png"
                    action NullAction()
        hbox:
            spacing 87
            if k_days == 13:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 13:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 14:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 14:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 15:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 15:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 16:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 16:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 17:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 17:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 18:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 18:
                imagebutton:
                    xpos 353
                    ypos 530
                    idle "menuUI/pass.png"
                    action NullAction()
        hbox:
            spacing 87
            if k_days == 19:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 19:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 20:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 20:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 21:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 21:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 22:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 22:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 23:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 23:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 24:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 24:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
        hbox:
            spacing 87
            if k_days == 25:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 25:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 26:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 26:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 27:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 27:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 28:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 28:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 29:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 29:
                imagebutton:
                    xpos 353
                    ypos 684
                    idle "menuUI/pass.png"
                    action NullAction()
            if k_days == 30:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/today.png"
                    action NullAction()
            elif k_days > 30:
                imagebutton:
                    xpos 353
                    ypos 837
                    idle "menuUI/pass.png"
                    action NullAction()

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()