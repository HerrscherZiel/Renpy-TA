
screen task:

    tag menu

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task.png"

        vbox:
            xpos 100
            ypos 230
            spacing 7
            xanchor 1
            textbutton "PTI" action Show("pti_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Pengantar Tekonologi Informasi{/b}")
            textbutton "Alpro" action ToggleScreen("trivia_study") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Algoritma Pemrograman{/b}")
            textbutton "DE" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Desain Elementer{/b}")
            textbutton "Strukdat" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Struktur Data{/b}")
            textbutton "Basdat" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Basis Data{/b}")
            textbutton "Web 1" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Pemrograman Web 1{/b}")
            textbutton "PBO" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Pemrograman Berorientasi Objek{/b}")
            textbutton "Jarkom" action ToggleScreen("trivia_others") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Jaringan Komputer{/b}")


    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 400
            ypos 300
            xsize 1300
            text tt.value font "fonts/Montserrat-Italic.ttf"
    
    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()


screen pti_task:

    frame:
        xsize 1920
        ysize 1080
        background "menuUI/task_detail.png"

        vbox:
            xpos 50
            ypos 280
            spacing 25
            textbutton "Pertemuan 1" action ToggleScreen("pti_task_1")
            textbutton "Pertemuan 2" action NullAction()
            textbutton "Pertemuan 3" action NullAction()
            textbutton "Pertemuan 4" action NullAction()

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
        action Hide("pti_task")

screen pti_task_1:

    #content
    frame:
        xsize 1200
        ysize 1080
        background "trivia/menu/desc_layer.png"

        vbox:
            xpos 350
            ypos 250
            spacing 20
            for task in my_task.task_list:
                if not(task.completed):
                    text "[task.name]: [task.description] | [task.completed]" size 25

    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Hide("pti_task_1")

