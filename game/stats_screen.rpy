
screen stats_screen:
    if renpy.get_screen("mapUI"):
        pass

    elif maps == True:
        pass

    else:
        frame:
            xsize 1920
            ysize 1080
            xpos 1555
            ypos -2
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

        imagebutton:
            xalign 1.0
            ypos 133
            auto "menuUI/button/menu_%s.png"
            action ShowMenu("stats")

        imagebutton:
            xpos 1740
            ypos 133
            auto "menuUI/button/stats_%s.png"
            action ShowMenu("stats")

        imagebutton:
            xpos 1655
            ypos 133
            auto "menuUI/button/task_%s.png"
            action ShowMenu("task")

        imagebutton:
            xpos 1569
            ypos 133
            auto "menuUI/button/trivia_%s.png"
            action ShowMenu("trivia")

screen stats:

    frame:
        xsize 1920
        ysize 1080

        background "menuUI/stats/stats screen.png"

        hbox:
            xpos 370
            ypos 355
            spacing 450
            $ health = round((hunger+energy+vit) / 3)
            $ academic = round((knowledge+practice+application) / 3)
            text "[health]" size 40 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
            text "[academic]" size 40 color '#ffffff' font "fonts/Montserrat-SemiBoldItalic.ttf"
        
        hbox:
            xpos 1350
            ypos 355
            spacing 460
            $ social = round((friend+community+public) / 3)
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

        #status
        vbox:
            xpos 1550
            ypos 240
            spacing 20
            if fulls == True:
                #kenyang
                imagebutton:
                    idle "status/kenyang.png"
                    action NullAction()
            if thin == True:
                #kurus
                imagebutton:
                    idle "status/kurus.png"
                    action NullAction()
            if healthy == True:
                #sehat
                imagebutton:
                    idle "status/sehat.png"
                    action NullAction()
            if sick == True:    
                #sakit
                imagebutton:
                    idle "status/sakit.png"
                    action NullAction()
            if fitt == True:
                #bugar
                imagebutton:
                    idle "status/bugar.png"
                    action NullAction()
            if weak == True:    
                #loyo
                imagebutton:
                    idle "status/loyo.png"
                    action NullAction()
    #return
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action Return()

