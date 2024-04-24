define t_choices = False
define t_maps = False
define t_times = False
define t_stats = False
define t_cstats = False
define t_spec = False
define t_task = False
define t_jadkal = False

screen tutorials_screen:

    if renpy.get_screen('trivia_game_tutorials'):
        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 360
                ypos 240
                spacing 10
                textbutton "Pilihan" action [Hide('tutorials'), ToggleScreen('tutorials', None, 1)] hovered tt.Action("Tutorial yang membahas mengenai pilihan atau choices dalam permainan.")
                textbutton "Peta" action [Hide('tutorials'), ToggleScreen('tutorials', None, 2)] hovered tt.Action("Tutorial yang mengajarkan kepada pemain bagaimana untuk memilih pilihan dalam menu peta.")
                textbutton "Hari dan Fase Waktu" action [Hide('tutorials'), ToggleScreen('tutorials', None, 3)] hovered tt.Action("Tutorial yang memperlihatkan pemain mengenai perubahan hari dan fase waktu dalam gim.")
                textbutton "Stats" action [Hide('tutorials'), ToggleScreen('tutorials', None, 4)] hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai fitur stats yang terdapat dalam gim.")
                textbutton "Perubahan Stats" action [Hide('tutorials'), ToggleScreen('tutorials', None, 5)] hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai perubahan stats yang terjadi dalam gim.")
                textbutton "Kejadian Special" action [Hide('tutorials'), ToggleScreen('tutorials', None, 6)] hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai kegiatan spesial yang terjadi dalam gim.")
                textbutton "Task" action [Hide('tutorials'), ToggleScreen('tutorials', None, 7)] hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai task atau tugas perkuliahan yang ada pada permainan.")
                textbutton "Jadwal dan Kalender" action [Hide('tutorials'), ToggleScreen('tutorials', None, 8)] hovered tt.Action("Tutorial yang berisi penjeleasan mengenai menu jadwal perkuliahan dan kalender dalam gim.")

    else:
        timer 0.1 action Hide("tutorials_screen")

screen tutorials(x):

    if x == 1:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Pilihan" action NullAction() hovered tt.Action("Tutorial yang membahas mengenai pilihan atau choices dalam permainan.")
                text "Tutorial yang membahas mengenai pilihan atau choices dalam permainan. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_choices1"), SetVariable('t_choices', True)] 

    if x == 2:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Peta" action NullAction() hovered tt.Action("Tutorial yang mengajarkan kepada pemain bagaimana untuk memilih pilihan dalam menu peta.")
                text "Tutorial yang membahas mengenai menu ini, dimana pemain akan diperlihatkan bagaimana cara untuk memilih pilihan pada menu ini. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_maps1"), SetVariable('t_maps', True)] 

    if x == 3:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Hari dan Fase Waktu" action NullAction() hovered tt.Action("Tutorial yang memperlihatkan pemain mengenai perubahan hari dan fase waktu dalam gim.")
                text "Tutorial ini memperlihatkan pemain ikon dan tampilan dari hari dan fase waktu yang terdapat dalam permainan. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_daytimes1"), SetVariable('t_times', True)] 

    if x == 4:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Stats" action NullAction() hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai fitur stats yang terdapat dalam gim.")
                text "Tutorial yang menjelaskan kepada pemain tentang stats dan pengaruhnya yang terdapat dalam permainan. Klik tombol dibwah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_stats1"), SetVariable('t_stats', True)] 

    if x == 5:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Perubahan Stats" action NullAction() hovered tt.Action("Tutorial yang membahas mengenai pilihan atau choices dalam permainan.")
                text "Tutorial yang membahas mengenai pilihan atau choices dalam permainan. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_statschange1"), SetVariable('t_cstats', True)] 

    if x == 6:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Special Events" action NullAction() hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai kegiatan spesial yang terjadi dalam gim.")
                text "Tutorial yang menjelaskan kepada pemain mengenai kegiatan spesial yang dapat terjadi pada permainan. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_specialevents1"), SetVariable('t_spec', True)] 

    if x == 7:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Task" action NullAction() hovered tt.Action("Tutorial yang menjelaskan kepada pemain mengenai task atau tugas perkuliahan yang ada pada permainan.")
                text "Tutorial yang menjelaskan kepada pemain task atau tugas yang didapat dari pertemuan perkuliahan dalam gim. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_task1"), SetVariable('t_task', True)] 

    if x == 8:

        frame:
            xsize 1000
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Jadwal dan Kalender" action NullAction() hovered tt.Action("Tutorial yang berisi penjeleasan mengenai menu jadwal perkuliahan dan kalender dalam gim.")
                text "Tutorial yang menjelaskan kepada pemain mengenai menu jadwal perkuliahan dan menu kalender yang terdapat pada permainan. Klik tombol dibawah untuk membuka tutorial ini." font "fonts/Montserrat-SemiBoldItalic.ttf"
                textbutton "lihat" action [Show("tutorial_jadwalkalender1"), SetVariable('t_spec', True)] 
