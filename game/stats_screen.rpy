
screen stats_screen:
    if renpy.get_screen("mapUI"):
        pass

    elif maps == True:
        pass

    else:
        frame:
            xsize 1920
            ysize 1080

            # xpadding 10
            # ypadding 5
            xpos 1555
            ypos -2
            # xsize 365
            background "menuUI/stats/stats.png"

            bar:
                value hunger
                range 100
                left_bar "menuUI/stats/left_bar.png"
                right_bar "menuUI/stats/right_bar.png"
                xysize(272,16)
                xpos 60
                ypos 14
            
            bar:
                value vit
                range 100
                left_bar "menuUI/stats/left_bar.png"
                right_bar "menuUI/stats/right_bar.png"
                xysize(272,16)
                xpos 60
                ypos 50

            bar:
                value energy
                range 100
                left_bar "menuUI/stats/left_bar.png"
                right_bar "menuUI/stats/right_bar.png"
                xysize(272,16)
                xpos 60
                ypos 90
            # bar:
            #     value hunger
            #     range 100
            #     left_bar "menuUI/stats/left_bar.png"
            #     right_bar "menuUI/stats/right_bar.png"
            #     xysize(272,16)
            #     xpos 60
            #     ypos 100

        imagebutton:
            xalign 1.0
            ypos 133
            # xoffset -30
            # yoffset 30
            auto "menuUI/button/menu_%s.png"
            action ShowMenu("stats")

        imagebutton:
            xpos 1740
            ypos 133
            # xoffset -30
            # yoffset 30
            auto "menuUI/button/stats_%s.png"
            action ShowMenu("stats")

        # imagebutton:
        #     xpos 1655
        #     ypos 133
        #     # xoffset -30
        #     # yoffset 30
        #     auto "menuUI/button/task_%s.png"
        #     action ShowMenu("stats")

screen stats:

    # add "menuUI/bg grey.png"

    frame:
        xsize 1920
        ysize 1080
        # xalign 0.5
        # yalign 0.5
        # xpadding 30
        # ypadding 30
        background "menuUI/stats/stats screen.png"

        hbox:
            xpos 360
            ypos 355
            spacing 450
            $ health = round((hunger+energy+vit) / 3)
            text "[health]" size 40 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[academic]" size 40 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        
        hbox:
            xpos 1350
            ypos 355
            spacing 460
            text "[social]" size 40 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        #health
        bar:
            value hunger
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 230
            ypos 505
        
        bar:
            value vit
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 230
            ypos 625

        bar:
            value energy
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 230
            ypos 765

        #akademic
        bar:
            value knowledge
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 710
            ypos 505
        
        bar:
            value practice
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 710
            ypos 625

        bar:
            value application
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 710
            ypos 765

        #social
        bar:
            value friend
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 1190
            ypos 505
        
        bar:
            value community
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 1190
            ypos 625

        bar:
            value public
            range 100
            left_bar "menuUI/stats/bigleft_bar.png"
            right_bar "menuUI/stats/bigright_bar.png"
            xysize(294,33)
            xpos 1190
            ypos 765
    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()

