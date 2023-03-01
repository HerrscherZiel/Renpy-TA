  
default simaster_dpa = 1  

screen simaster_dpa:

    frame:
        xsize 1920
        ysize 1080

        background "simaster/simaster_dpa.png"

        if (simaster_dpa == 1):
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Beranda{/i}" color "#FFFFFF" size 40
        
        elif (simaster_dpa == 2):
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Menu Akademik Kemahasiswaan{/i}" color "#FFFFFF" size 40

        elif (simaster_dpa == 3):
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Menu Akademik{/i}" color "#FFFFFF" size 40

        else:
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Halaman Diskusi DPA{/i}" color "#FFFFFF" size 40

        imagebutton:
            xpos 740
            ypos 265

            idle "simaster/home simaster.png"

    #slide left
    imagebutton:
        if (simaster_dpa == 1):
            xpos 1150
            ypos 850
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1150
            ypos 850
            auto "tutorial/left_%s.png"
            action  [SetVariable("simaster_dpa", If(simaster_dpa>=2, simaster_dpa-1, )), Show("simaster_image")]

    #slide right
    imagebutton:
        if (simaster_dpa == 4):
            xpos 1320
            ypos 850
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1320
            ypos 850
            auto "tutorial/right_%s.png"
            action  [SetVariable("simaster_dpa", If(simaster_dpa<=3, simaster_dpa+1, )), Show("simaster_image")]

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("simaster_dpa", transition=fade), Hide("simaster_image", transition=fade), Return()]

screen simaster_image:

    frame:
        xsize 1920
        ysize 1080

        if (simaster_dpa == 1):
            xpos 746
            ypos 271
            background "simaster/home simaster.png"
        
        elif (simaster_dpa == 2):
            xpos 746
            ypos 271
            background "simaster/home akademik.png"

        elif (simaster_dpa == 3):
            xpos 746
            ypos 271
            background "simaster/home akademik dpa.png"

        else:
            xpos 746
            ypos 271
            background "simaster/diskusi dpa.png"






