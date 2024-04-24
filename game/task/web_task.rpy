


screen web_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            if taskweb == True:
                textbutton "Pertemuan 4" action ToggleScreen("web_prev")
            else:
                hbox:
                    xpos 330
                    text "Tidak ada tugas yang dapat dikerjakan pada mata kuliah ini" font "fonts/Montserrat-SemiBoldItalic.ttf"
    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/web.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("web_task")

screen web_prev:

    #content

    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"
        $ time = 60
        $ timer_range = 60
        $ timer_jump = 'web_task2'
        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"

            textbutton "Mulai" action [Hide("web_prev"), Show("web_task1"), Show('countdown2')]

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("web_prev")

screen web_task1:

    #content

    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        $ taskweb = False
        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt1.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task1'), Show("web_task2")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task1'), Show("web_task2")]

screen web_task2:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt2.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task2'), Show("web_task3")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task2'), Show("web_task3")]
        

screen web_task3:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt3.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task3'), Show("web_task4")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task3'), Show("web_task4")]
        

screen web_task4:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt4.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task4'), Show("web_task5")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task4'), Show("web_task5")]
        

screen web_task5:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt5.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task5'), Show("web_task6")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task5'), Show("web_task6")]

screen web_task6:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt6.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task6'), Show("web_task7")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task6'), Show("web_task7")]

screen web_task7:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt7.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task7'), Show("web_task8")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task7'), Show("web_task8")]

screen web_task8:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt8.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task8'), Show("web_task9")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task8'), Show("web_task9")]

screen web_task9:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt9.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task9'), Show("web_task10")]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task9'), Show("web_task10")]

screen web_task10:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/web/webt10.png"
        
        #A
        imagebutton:
            xpos 690
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_webT", a_webT+2), Hide('web_task10'), Show("web_done"), Hide('countdown2')]

        #B
        imagebutton:
            xpos 1040
            ypos 520
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('web_task10'), Show("web_done"), Hide('countdown2')]        

screen web_done:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"
        $ taskweb = False
        vbox:
            xpos 450
            ypos 280
            spacing 25

            text "Tugas selesai dikerjakan" font "fonts/Montserrat-SemiBoldItalic.ttf"

    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/web.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("web_done"), Hide("web_task")]    
