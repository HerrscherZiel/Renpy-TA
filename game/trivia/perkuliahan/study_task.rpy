


screen studytask_screen:

    if renpy.get_screen('trivia_study_task'):
        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 360
                ypos 250
                spacing 10
                textbutton "PTI" action [Hide('stask'), ToggleScreen('stask', None, 1)] hovered tt.Action("Tugas dari mata kuliah Pengantar Teknologi Informasi.")
                textbutton "Alpro" action [Hide('stask'), ToggleScreen('stask', None, 2)] hovered tt.Action("Tugas dari mata kuliah Algoritma Pemrograman.")
                textbutton "DE" action [Hide('stask'), ToggleScreen('stask', None, 3)] hovered tt.Action("Tugas dari mata kuliah Desain Elementer.")
                textbutton "Strukdat" action [Hide('stask'), ToggleScreen('stask', None, 4)] hovered tt.Action("Tugas dari mata kuliah Struktur Data.")
                textbutton "Basdat" action [Hide('stask'), ToggleScreen('stask', None, 5)] hovered tt.Action("Tugas dari mata kuliah Basis Data.")
                textbutton "Web" action [Hide('stask'), ToggleScreen('stask', None, 6)] hovered tt.Action("Tugas dari mata kuliah Pemrograman Web.")
                textbutton "PBO" action [Hide('stask'), ToggleScreen('stask', None, 7)] hovered tt.Action("Tugas dari mata kuliah Pemrograman Berbasis Objek.")
                textbutton "Jarkom" action [Hide('stask'), ToggleScreen('stask', None, 8)] hovered tt.Action("Tugas dari mata kuliah Jaringan Komputer.")

    else:
        timer 0.1 action Hide("studytask_screen")

screen stask(x):

    if x == 1:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pengantar Teknologi Informasi" action NullAction() hovered tt.Action("Tugas dari mata kuliah Pengantar Teknologi Informasi.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Tugas PTI minggu pertama.")
                text "Time limit pertanyaan dasar dan pemahaman teknologi informasi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan PTI minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan PTI minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan PTI minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 2:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Algoritma Pemrograman" action NullAction() hovered tt.Action("Tugas dari mata kuliah Algoritma Pemrograman.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu kedua.")
                text "Memilih urutan gambar Flowchart" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 3:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Desain Elementer" action NullAction() hovered tt.Action("Tugas dari mata kuliah Desain Elementer.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan DE minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan DE minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan DE minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan DE minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 4:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Struktur Data" action NullAction() hovered tt.Action("Tugas dari mata kuliah Struktur Data.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 5:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Basis Data" action NullAction() hovered tt.Action("Tugas dari mata kuliah Basis Data.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu ketiga.")
                text "Fill the blank pertanyaan seputar basis data" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 6:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pemrograman Web" action NullAction() hovered tt.Action("Tugas dari mata kuliah Pemrograman Web.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Web minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Web minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Web minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Web minggu keempat.")
                text "Quick time limit pertanyaan seputar pemrograman web" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 7:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pemrograman Berorientasi Objek" action NullAction() hovered tt.Action("Tugas dari mata kuliah Pemrograman Berbasis Objek.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan PBO minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan PBO minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan PBO minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan PBO minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 8:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Jaringan Komputer" action NullAction() hovered tt.Action("Tugas dari mata kuliah Jaringan Komputer.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu pertama.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu kedua.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu ketiga.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu keempat.")
                text "Tidak ada tugas" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
