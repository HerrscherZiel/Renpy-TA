
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
            textbutton "Alpro" action ToggleScreen("alpro_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Algoritma Pemrograman{/b}")
            textbutton "DE" action ToggleScreen("de_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Desain Elementer{/b}")
            textbutton "Strukdat" action ToggleScreen("strukdat_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Struktur Data{/b}")
            textbutton "Basdat" action ToggleScreen("basdat_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Basis Data{/b}")
            textbutton "Web 1" action ToggleScreen("web_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Pemrograman Web 1{/b}")
            textbutton "PBO" action ToggleScreen("pbo_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Pemrograman Berorientasi Objek{/b}")
            textbutton "Jarkom" action ToggleScreen("jarkom_task") hovered tt.Action("Pilih untuk melihat informasi mengenai tugas pada mata kuliah {b}Jaringan Komputer{/b}")


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



