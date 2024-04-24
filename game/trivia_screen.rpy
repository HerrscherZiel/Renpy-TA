
default tt = Tooltip("")

screen trivia:

    tag menu

    frame:
        xsize 1920
        ysize 1080
        background "trivia/menu/trivia.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Game" action ToggleScreen("trivia_game") hovered tt.Action("Informasi mengenai {b}GAME{/b}, mulai dari Character, Tutorial, dan lain sebagainya")
            textbutton "Study" action ToggleScreen("trivia_study") hovered tt.Action("Informasi mengenai semua {b}MATA KULIAH{/b} dan setiap sesi pertemuan yang ada")

    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"

    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()

#game
screen trivia_game:

    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Game" action NullAction() hovered tt.Action("Informasi mengenai {b}GAME{/b}, mulai dari Character, Tutorial, dan lain sebagainya")
            textbutton "Study" action [Show("trivia_study"), Hide('trivia_game'), Hide('trivia')] hovered tt.Action("Informasi mengenai semua {b}MATA KULIAH{/b} dan setiap sesi pertemuan yang ada")

        vbox:
            xpos 360
            ypos 280
            spacing 20
            textbutton "Characters" action [Show("trivia_game_characters"), Hide('trivia_game'), Hide('trivia')] hovered tt.Action("Informasi mengenai {b}Characters{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Tutorial" action [Show("trivia_game_tutorials"), Hide('trivia_game'), Hide('trivia')] hovered tt.Action("Informasi mengenai {b}Tutorials{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")

    #Tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"
    
    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_game"), Show('trivia')]

##game_chars
screen trivia_game_characters:

    #content
    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia_detail.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Characters" action Show("trivia_game_characters") hovered tt.Action("Informasi mengenai {b}Characters{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Tutorial" action [Hide("trivia_game_characters"), Show("trivia_game_tutorials")] hovered tt.Action("Informasi mengenai {b}Tutorials{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")

    #Tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"

    timer 0.1 action Show("characters_screen")

    #header
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 150
            ypos 80
            text "Trivia Game Characters" size 60 color "#e6e6e6" font "fonts/Montserrat-SemiBoldItalic.ttf"

    #Return    
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_game_characters"), Show('trivia')]

##game_tutors
screen trivia_game_tutorials:

    #content
    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia_detail.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Characters" action [Hide("trivia_game_tutorials"), Show("trivia_game_characters")] hovered tt.Action("Informasi mengenai {b}Characters{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Tutorial" action Show("trivia_game_tutorials") hovered tt.Action("Informasi mengenai {b}Tutorials{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")

    timer 0.1 action Show("tutorials_screen")

    #header
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 150
            ypos 80
            text "Trivia Game Tutorials" size 60 color "#e6e6e6" font "fonts/Montserrat-SemiBoldItalic.ttf" 

    #tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"
    
    #return    
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_game_tutorials"), Show('trivia')]

#study change needed
screen trivia_study:

    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Game" action [Show("trivia_game"), Hide('trivia_study'), Hide('trivia')] hovered tt.Action("Informasi mengenai {b}GAME{/b}, mulai dari Character, Tutorial, dan lain sebagainya")
            textbutton "Study" action NullAction() hovered tt.Action("Informasi mengenai semua {b}MATA KULIAH{/b} dan setiap sesi pertemuan yang ada")

        vbox:
            xpos 360
            ypos 280
            spacing 20
            textbutton "Classes" action ToggleScreen("trivia_study_class") hovered tt.Action("Informasi mengenai {b}Kelas Pertemuan{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Task" action ToggleScreen("trivia_study_task") hovered tt.Action("Informasi mengenai {b}Tugas{/b} yang ada dalam game, tambahan tugas dapat ditambahkan setelah pemain membukanya dalam Game")

    #Tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value
    
    #Return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_study"), Show('trivia')]


screen trivia_study_class:

    #content
    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia_detail.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Classes" action Show("trivia_study_class") hovered tt.Action("Informasi mengenai {b}Kelas Perkuliahan{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Task" action [Hide("trivia_study_class"), Show("trivia_study_task")] hovered tt.Action("Informasi mengenai {b}Tugas{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")

    #Tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"

    timer 0.1 action Show("studyclasses_screen")

    #header
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 150
            ypos 80
            text "Trivia Study Classes" size 60 color "#e6e6e6" font "fonts/Montserrat-SemiBoldItalic.ttf"

    #Return    
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_study_class"), Show('trivia')]


screen trivia_study_task:

    #content
    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia_detail.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Classes" action [Hide("trivia_study_task"), Show("trivia_study_class")] hovered tt.Action("Informasi mengenai {b}Kelas Perkuliahan{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Task" action Show("trivia_study_task") hovered tt.Action("Informasi mengenai {b}Tugas{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")
            

    timer 0.1 action Show("studytask_screen")

    #header
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 150
            ypos 80
            text "Trivia Study Task" size 60 color "#e6e6e6" font "fonts/Montserrat-SemiBoldItalic.ttf" 

    #tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value font "fonts/Montserrat-Italic.ttf"
    
    #return    
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_study_task"), Show('trivia')]

#others change needed
screen trivia_others:

    frame:
        xsize 400
        ysize 1080
        background "trivia/menu/trivia.png"

        vbox:
            xpos 100
            ypos 250
            spacing 20
            textbutton "Game" action [Show("trivia_game"), Hide('trivia_others'), Hide('trivia')] hovered tt.Action("Informasi mengenai {b}GAME{/b}, mulai dari Character, Tutorial, dan lain sebagainya")
            textbutton "Study" action [Show("trivia_study"), Hide('trivia_others'), Hide('trivia')] hovered tt.Action("Informasi mengenai semua {b}MATA KULIAH{/b} dan setiap sesi pertemuan yang ada")
            textbutton "Others" action NullAction() hovered tt.Action("Informasi mengenai {b}HAL LAIN{/b} yang ada di dalam Game, termasuk Items, Trivia, dan lain sebagainya")

        vbox:
            xpos 360
            ypos 280
            spacing 20
            textbutton "Characters" action ToggleScreen("trivia_game_characters") hovered tt.Action("Informasi mengenai {b}Characters{/b} yang ada dalam game, tambahan informasi dapat ditambahkan selama memainkan Game")
            textbutton "Tutorial" action ToggleScreen("trivia_game_tutorials") hovered tt.Action("Informasi mengenai {b}Tutorials{/b} yang ada dalam game, tambahan tutorial dapat ditambahkan setelah pemain membukanya dalam Game")
            textbutton "Special Events" action ToggleScreen("trivia_game_special") hovered tt.Action("Informasi mengenai {b}Special Events{/b} yang ada dalam game, tambahan informasi dapat ditambahkan setelah pemain menemuinya dalam Game")

    #Tooltip
    frame:
        background "trivia/menu/desc_layer.png"
        vbox:
            xpos 780
            ypos 300
            xsize 1000
            text tt.value
    
    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("trivia_others"), Show('trivia')]
