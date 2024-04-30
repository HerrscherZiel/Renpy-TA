init:
    $ time2 = 30
    $ timer_range2 = 30
    $ timer_jump = 'ptit_done'

# default time2 = 30
# default timer_range2 = 30

screen pti_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            if taskpti == True:
                textbutton "Pertemuan 1" action ToggleScreen("pti_prev")
            else:
                hbox:
                    xpos 330
                    text "Tidak ada tugas yang dapat dikerjakan pada mata kuliah ini" font "fonts/Montserrat-SemiBoldItalic.ttf"
    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/pti.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("pti_task")



screen pti_prev:

    #content

    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"

            textbutton "Mulai" action [Hide("pti_prev"), Show("pti_task1"), Show("countdown2")]

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("pti_prev")

label jumpas:

    "loncat"


screen pti_task1:

    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        $ taskpti = False
        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"
            image "task/pti/ptit1.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task1'), Show("pti_task2")]

        #B
        imagebutton:
            xpos 430
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task1'), Show("pti_task2")]
        
        #C
        imagebutton:
            xpos 1150
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task1'), Show("pti_task2")]
        
        #D
        imagebutton:
            xpos 1150
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_ptiT", a_ptiT+2), SetVariable("application", application + 3), Hide('pti_task1'), Show("pti_task2")]

screen pti_task2:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"
            image "task/pti/ptit2.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task2'), Show("pti_task3")]

        #B
        imagebutton:
            xpos 430
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_ptiT", a_ptiT+2), SetVariable("application", application + 3), Hide('pti_task2'), Show("pti_task3")]
        
        #C
        imagebutton:
            xpos 1150
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task2'), Show("pti_task3")]
        
        #D
        imagebutton:
            xpos 1150
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task2'), Show("pti_task3")]

screen pti_task3:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"
            image "task/pti/ptit3.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task3'), Show("pti_task4")]

        #B
        imagebutton:
            xpos 430
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task3'), Show("pti_task4")]
        
        #C
        imagebutton:
            xpos 1150
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task3'), Show("pti_task4")]
        
        #D
        imagebutton:
            xpos 1150
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_ptiT", a_ptiT+2), SetVariable("application", application + 3), Hide('pti_task3'), Show("pti_task4")]

screen pti_task4:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"
            image "task/pti/ptit4.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task4'), Show("pti_task5")]

        #B
        imagebutton:
            xpos 430
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_ptiT", a_ptiT+2), SetVariable("application", application + 3), Hide('pti_task4'), Show("pti_task5")]
        
        #C
        imagebutton:
            xpos 1150
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task4'), Show("pti_task5")]
        
        #D
        imagebutton:
            xpos 1150
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task4'), Show("pti_task5")]

screen pti_task5:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Jawab semua pertanyaan dibawah ini sebelum timer habis!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"
            image "task/pti/ptit5.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_ptiT", a_ptiT+2),SetVariable("application", application + 3), Hide('pti_task5'), Show("ptit_done")]

        #B
        imagebutton:
            xpos 430
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task5'), Show("ptit_done")]
        
        #C
        imagebutton:
            xpos 1150
            ypos 570
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task5'), Show("ptit_done")]
        
        #D
        imagebutton:
            xpos 1150
            ypos 740
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('pti_task5'), Show("ptit_done")]
        

screen ptit_done:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"
        $ taskpti = False
        vbox:
            xpos 450
            ypos 280
            spacing 25

            text "Tugas selesai dikerjakan" font "fonts/Montserrat-SemiBoldItalic.ttf"

    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/pti.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("ptit_done"), Hide("pti_task"), Hide("pti_task1"), Hide("pti_task2"), Hide("pti_task3"), Hide("pti_task4"), Hide("pti_task5")]    
