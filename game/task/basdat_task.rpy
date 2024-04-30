

screen basdat_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            if taskbasdat == True:
                textbutton "Pertemuan 3" action ToggleScreen("basdat_prev")
            else:
                hbox:
                    xpos 330
                    text "Tidak ada tugas yang dapat dikerjakan pada mata kuliah ini" font "fonts/Montserrat-SemiBoldItalic.ttf"
    imagebutton:
        xpos 145
        ypos 97
        idle "menuUI/basdat.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("basdat_task")

screen basdat_prev:

    #content

    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            text "Lengkapi kode dibawah ini agar menjadi kode yang tepat!" size 36 font "fonts/Montserrat-SemiBoldItalic.ttf"

            textbutton "Mulai" action [Hide("basdat_prev"), Show("basdat_task1")]

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("basdat_prev")

screen basdat_task1:

    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"
        # $ time = 5
        # $ timer_range = 5
        # $ timer_jump = 'basdat_done'
        $ taskpti = False
        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/basdat/badatt1.png"
        
        #A
        imagebutton:
            xpos 440
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_basdatT", a_basdatT+3), SetVariable("application", application + 3), Hide('basdat_task1'), Show("basdat_task2")]

        #B
        imagebutton:
            xpos 730
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task1'), Show("basdat_task2")]
        
        #C
        imagebutton:
            xpos 1030
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task1'), Show("basdat_task2")]
        
        #D
        imagebutton:
            xpos 1330
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task1'), Show("basdat_task2")]

screen basdat_task2:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/basdat/badatt2.png"
        
        #A
        imagebutton:
            xpos 440
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task2'), Show("basdat_task3")]

        #B
        imagebutton:
            xpos 730
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task2'), Show("basdat_task3")]
        
        #C
        imagebutton:
            xpos 1030
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_basdatT", a_basdatT+2), SetVariable("application", application + 3), Hide('basdat_task2'), Show("basdat_task3")]
        
        #D
        imagebutton:
            xpos 1330
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task2'), Show("basdat_task3")]

screen basdat_task3:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/basdat/badatt3.png"
        
        #A
        imagebutton:
            xpos 440
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task3'), Show("basdat_task4")]

        #B
        imagebutton:
            xpos 710
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_basdatT", a_basdatT+3), SetVariable("application", application + 3), Hide('basdat_task3'), Show("basdat_task4")]
        
        #C
        imagebutton:
            xpos 1070
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task3'), Show("basdat_task4")]
        
        #D
        imagebutton:
            xpos 1310
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task3'), Show("basdat_task4")]

screen basdat_task4:
    
    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 100
            image "task/basdat/badatt4.png"
        
        #A
        imagebutton:
            xpos 430
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task4'), Show("basdat_done")]

        #B
        imagebutton:
            xpos 710
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task4'), Show("basdat_done")]
        
        #C
        imagebutton:
            xpos 1060
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [Hide('basdat_task4'), Show("basdat_done")]
        
        #D
        imagebutton:
            xpos 1310
            ypos 670
            idle "task/radio_idle.png"
            hover "task/radio_hover.png"
            action [SetVariable("a_basdatT", a_basdatT+2), SetVariable("application", application + 6), Hide('basdat_task4'), Show("basdat_done")]
        

screen basdat_done:

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
        idle "menuUI/basdat.png"
        action NullAction()

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("basdat_done"), Hide("basdat_task")]    
