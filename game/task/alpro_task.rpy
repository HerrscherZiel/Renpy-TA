
default taskpro = '1256341'

screen alpro_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            if taskalpro == True:
                textbutton "Pertemuan 2" action ToggleScreen("alpro_prev")
            else:
                hbox:
                    xpos 330
                    text "Tidak ada tugas yang dapat dikerjakan pada mata kuliah ini" font "fonts/Montserrat-SemiBoldItalic.ttf"
    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/alpro.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("alpro_task")

screen alpro_prev:

    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Urutkan gambar agar menjadi sebuah flowchart yang tepat!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"

            textbutton "Mulai Tugas!!" action [Hide("alpro_prev"), Show("alpro_task1")]

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("pti_prev")

screen alpro_task1:

    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"
        $ taskalpro = False
        vbox:
            xpos 350
            ypos 250
            spacing 30
            image "task/alpro/alprot1.png"

        vbox:
            # image "images/krs/krs_captcha.png"
            xpos 1400
            ypos 770
            spacing 10
            text "Masukan jawaban disini:" color "#f1f1f1" size 32
            button:
                id "name_input2"
                xysize (250, 40)
                action NullAction()
                add Input(size=32, color="#ffffff", default='123456', changed=name_func, length=10, button=renpy.get_widget("alpro_task1","name_input2")) yalign 1.0
                #confirm
        imagebutton:
            id "conf"
            xpos 1400
            ypos 870
            auto "krs/confirm_%s.png"
            action [Hide('alpro_task1'), Show('alpro_answer')]

screen alpro_answer:

    if taskpro == note:
        frame:
            background "trivia/menu/desc_layer.png"
            xpos 625
            ypos 450 
            vbox:
                text "Jawaban yang diisikan benar!!!"
            imagebutton:
                xpos 170
                ypos 110
                auto "krs/ok_%s.png"
                action [SetVariable("a_alproT", a_alproT + 10), SetVariable("application", application + 15), Hide('alpro_answer'), Show('alpro_done')]

    else:
        frame:
            background "trivia/menu/desc_layer.png"
            xpos 625
            ypos 450 
            vbox:
                text "Jawaban yang diisikan kurang tepat!!!"
            imagebutton:
                xpos 200
                ypos 110
                auto "krs/ok_%s.png"
                action [SetVariable("a_alproT", a_alproT + 4), Hide('alpro_answer'), Show('alpro_done')]


screen alpro_done:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"
        $ taskalpro = False
        vbox:
            xpos 450
            ypos 280
            spacing 25

            text "Tugas selesai dikerjakan" font "fonts/Montserrat-SemiBoldItalic.ttf"

    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/alpro.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("alpro_done"), Hide("alpro_task")]    
