

screen studyclasses_screen:

    if renpy.get_screen('trivia_study_class'):
        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 360
                ypos 250
                spacing 10
                textbutton "PTI" action [Hide('classes'), ToggleScreen('classes', None, 1)] hovered tt.Action("Pengantar Teknologi Informasi, mata kuliah yang mempelajari mengenai perkembangan teknologi informasi.")
                textbutton "Alpro" action [Hide('classes'), ToggleScreen('classes', None, 2)] hovered tt.Action("Algoritma Pemrograman, mata kuliah yang membahas konsep-konsep dasar algoritma dan pemrograman prosedural.")
                textbutton "DE" action [Hide('classes'), ToggleScreen('classes', None, 3)] hovered tt.Action("Desain Elementer, mata kuliah yang membahas konsep dan dasar-dasar yang perlu dipelajari ketika membuat sebuah desain atau seni.")
                textbutton "Strukdat" action [Hide('classes'), ToggleScreen('classes', None, 4)] hovered tt.Action("Struktur Data, mata kuliah yang membahas konsep, teknik dan manipulasi pengorganisasian sebuah data yang diimplementasikan kedalam sebuah bahasa pemrograman.")
                textbutton "Basdat" action [Hide('classes'), ToggleScreen('classes', None, 5)] hovered tt.Action("Basis Data, mata kuliah yang membahas konsep dasar basis data kepada mahasiswa.")
                textbutton "Web" action [Hide('classes'), ToggleScreen('classes', None, 6)] hovered tt.Action("Pemrograman Web, mata kuliah yang mempelajari konsep dasar mengenai hal-hal yang dilakukan dalam pengembangan sebuah web.")
                textbutton "PBO" action [Hide('classes'), ToggleScreen('classes', None, 7)] hovered tt.Action("Pemrograman Berbasis Objek, mata kuliah yang mempelajari konsep dasar mengenai pemrograman yang berorientasikan kepada objek.")
                textbutton "Jarkom" action [Hide('classes'), ToggleScreen('classes', None, 8)] hovered tt.Action("Jaringan Komputer, mata kuliah yang membahas mengenai perangkat  yang saling terhubung dan bertukar data serta berbagi sumber daya dan konsep yang ada didalamnya.")
                
    else:
        timer 0.1 action Hide("studyclasses_screen")

screen classes(x):

    if x == 1:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pengantar Teknologi Informasi" action NullAction() hovered tt.Action("Pengantar Teknologi Informasi, mata kuliah yang mempelajari mengenai perkembangan teknologi informasi.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan PTI minggu pertama.")
                text "Mempelajari mengenai pengertian, perkembangan, dan penggunaan teknologi informasi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan PTI minggu kedua.")
                text "Mempelajari mengenai data, informasi, dan pengertahuan juga mengenai sistem operasi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan PTI minggu ketiga.")
                text "Mempelajari mengenai keamanan sistem informasi termasuk cybercrime dan malware" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan PTI minggu keempat.")
                text "Mempelajari mengenai komponen sistem informasi seperti Hardware, Software, Jaringan, Basis Data, dan SDM" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 2:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Algoritma Pemrograman" action NullAction() hovered tt.Action("Algoritma Pemrograman, mata kuliah yang membahas konsep-konsep dasar algoritma dan pemrograman prosedural.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu pertama.")
                text "Mempelajari mengenai pengertian program dan algotitma, serta 3 level bahasa pemrograman" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu kedua.")
                text "Mempelajari mengenai macam konstruksi algoritma, serta Flowchart dan Pseudocode" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu ketiga.")
                text "Mempelajari mengenai pengertian, perbedaan, contoh, dan manfaat dari prosedur dan fungsi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Alpro minggu keempat.")
                text "Mempelajari mengenai pengertian dan contoh dari algoritma pencarian dan pengurutan." font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 3:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Desain Elementer" action NullAction() hovered tt.Action("Desain Elementer, mata kuliah yang membahas konsep dan dasar-dasar yang perlu dipelajari ketika membuat sebuah desain atau seni.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan DE minggu pertama.")
                text "Mempelajari mengenai pengertian desain elementer dan unsur seni." font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan DE minggu kedua.")
                text "Mempelajari mengenai prinsip seni, teori warna, dan roda warna." font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan DE minggu ketiga.")
                text "Mempelajari mengenai pengertian warna, kelompok warna, dan skema warna." font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan DE minggu keempat.")
                text "Quiz mata kuliah dengan materi yang telah dipelajari" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 4:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Struktur Data" action NullAction() hovered tt.Action("Struktur Data, mata kuliah yang mempelajari mengenai perkembangan teknologi informasi.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu pertama.")
                text "Mempelajari mengenai pengertian struktur data dan contohnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu kedua.")
                text "Mempelajari mengenai struktur data linked list, tree, graph, dan manfaatnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu ketiga.")
                text "Mempelajari mengenai pengertian jenis data, contoh, dan penjelasannya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Strukdat minggu keempat.")
                text "Quiz mata kuliah dengan materi yang telah dipelajari" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 5:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Basis Data" action NullAction() hovered tt.Action("Basis Data, mata kuliah yang membahas konsep dasar basis data kepada mahasiswa.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu pertama.")
                text "Mempelajari mengenai pengertian basis data dan manfaatnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu kedua.")
                text "Mempelajari mengenai sistem manajemen basis data dan DDL juga DML" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu ketiga.")
                text "Mempelajari mengenai perintah DDL Create, Alter, dan Drop" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Basdat minggu keempat.")
                text "Mempelajari mengenai perintah DML Insert, Select, Delete, dan Update" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 6:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pemrograman Web" action NullAction() hovered tt.Action("Pemrograman Web, mata kuliah yang mempelajari konsep dasar mengenai hal-hal yang dilakukan dalam pengembangan sebuah web.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Web minggu pertama.")
                text "Mempelajari mengenai pengertian Web dan dasar-dasar pemrograman Web" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Web minggu kedua.")
                text "Mempelajari mengenai teknologi pada pemrograman web dan jenis pemrograman web" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Web minggu ketiga.")
                text "Mempelajari mengenai pembuatan dokumen dasar HTML" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Web minggu keempat.")
                text "Mempelajari mengenai pengembangan dokumen HTML membuat tabel dan form" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 7:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Pemrograman Berorientasi Objek" action NullAction() hovered tt.Action("Pemrograman Berbasis Objek, mata kuliah yang mempelajari konsep dasar mengenai pemrograman yang berorientasikan kepada objek.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan PBO minggu pertama.")
                text "Mempelajari mengenai pengertian dan konsep-konsep PBO" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan PBO minggu kedua.")
                text "Mempelajari mengenai prinsip-prinsip dalam PBO dan manfaatnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan PBO minggu ketiga.")
                text "Mempelajari mengenai penjelasan prinsip Enkapsulasi dan Abstraksi beserta contohnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan PBO minggu keempat.")
                text "Mempelajari mengenai penjelasan prinsip Inheritance dan Polymorphism beserta contohnya" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20

    if x == 8:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 400    
                spacing 6
                textbutton "Jaringan Komputer" action NullAction() hovered tt.Action("Jaringan Komputer, mata kuliah yang membahas mengenai perangkat  yang saling terhubung dan bertukar data serta berbagi sumber daya dan konsep yang ada didalamnya.")
                textbutton "Pertemuan 1" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu pertama.")
                text "Mempelajari mengenai pengertian dan jenis jaringan menutur geografis" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 2" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu kedua.")
                text "Mempelajari mengenai jenis jaringan menurut fungsi, distribusi data, dan media transmisi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 3" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu ketiga.")
                text "Mempelajari mengenai pengertian dan penjelasan 7 OSI Layer" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
                textbutton "Pertemuan 4" action NullAction() hovered tt.Action("Perkuliahan Jarkom minggu keempat.")
                text "Mempelajari mengenai contoh dan penjelasan masing-masing topologi" font "fonts/Montserrat-SemiBoldItalic.ttf" size 20
