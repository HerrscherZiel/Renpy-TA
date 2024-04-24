

screen characters_screen:

    if renpy.get_screen('trivia_game_characters'):
        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 360
                ypos 280
                spacing 10
                textbutton "Main Characters" action [Hide('characters'), ToggleScreen('characters', None, 1)] hovered tt.Action("Tokoh utama dalam gim, seorang pelajar dari luar kota yang baru pertama kali merantau.")
                textbutton "Rissa" action [Hide('characters'), ToggleScreen('characters', None, 2)] hovered tt.Action("Teman tokoh utama, seorang sosok pemimpin dalam kelas dan seorang teman yang baik.")
                textbutton "Pak Andy" action [Hide('characters'), ToggleScreen('characters', None, 3)] hovered tt.Action("Seorang dosen pengajar pada kampus dimana tokoh utama berkuliah, sering dan mudah bercanda dengan mahasiswa.")
                textbutton "Bu Nira" action [Hide('characters'), ToggleScreen('characters', None, 4)] hovered tt.Action("Seorang dosen pengajar pada kampus dimana tokoh utama berkuliah, dosen yang baik hati dan dihormati oleh banyak mahasiswa.")
                textbutton "Kevin" action [Hide('characters'), ToggleScreen('characters', None, 5)] hovered tt.Action("Teman tokoh utama, tinggal pada kosan yang sama dengan tokoh utama, merupakan mahasiswa semester akhir pada kampus yang berbeda.")
                textbutton "TriJe" action [Hide('characters'), ToggleScreen('characters', None, 6)] hovered tt.Action("Teman tokoh utama, merupakan salah satu teman yang berada pada program studi yang sama, orang kikuk yang suka berorganisasi.")
    else:
        timer 0.1 action Hide("characters_screen")

screen characters(x):

    if x == 1:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "MC" action NullAction()
                image "menuUI/pass.png"

    if x == 2:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Rissa" action NullAction()
                image "menuUI/today.png"

    if x == 3:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Pak Andy" action NullAction()
                image "menuUI/today.png"

    if x == 4:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Bu Nira" action NullAction()
                image "menuUI/today.png"

    if x == 5:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Kevin" action NullAction()
                image "menuUI/today.png"

    if x == 6:

        frame:
            xsize 1920
            ysize 1080
            background "trivia/menu/desc_layer.png"

            vbox:
                xpos 780
                ypos 430
                spacing 10
                textbutton "Trije" action NullAction()
                image "menuUI/today.png"
