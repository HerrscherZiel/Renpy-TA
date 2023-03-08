

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
                textbutton "Main Characters" action Return()
                textbutton "Rissa" action NullAction()
                textbutton "Pak Andy" action NullAction()
    else:
        timer 0.1 action Hide("characters_screen")