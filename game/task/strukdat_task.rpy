

screen strukdat_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            hbox:
                xpos 330
                text "Tidak ada tugas yang dapat dikerjakan pada mata kuliah ini" font "fonts/Montserrat-SemiBoldItalic.ttf"
    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/strukdat.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("strukdat_task")