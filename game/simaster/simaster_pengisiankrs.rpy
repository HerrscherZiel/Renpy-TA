  
default simaster_pengisiankrs = 1  

screen simaster_pengisiankrs:

    frame:
        xsize 1920
        ysize 1080

        background "simaster/simaster_pengisiankrs.png"

        if (simaster_pengisiankrs == 1):
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Beranda{/i}" color "#FFFFFF" size 40
        
        elif (simaster_pengisiankrs == 2):
            vbox:
                xpos 1265
                ypos 180
                xanchor 0.5
                text "{i}Menu Akademik Kemahasiswaan{/i}" color "#FFFFFF" size 40

        elif (simaster_pengisiankrs == 3):
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
                text "{i}Halaman Pengisian KRS{/i}" color "#FFFFFF" size 40

        imagebutton:
            xpos 738
            ypos 283

            idle "simaster/home simaster.png"

    #slide left
    imagebutton:
        if (simaster_pengisiankrs == 1):
            xpos 1150
            ypos 850
            idle "tutorial/left_idle.png"
            hover "tutorial/left_idle.png"
            action  NullAction()

        else:
            xpos 1150
            ypos 850
            auto "tutorial/left_%s.png"
            action  [SetVariable("simaster_pengisiankrs", If(simaster_pengisiankrs>=2, simaster_pengisiankrs-1, )), Show("simaster_pengisiankrs_image")]

    #slide right
    imagebutton:
        if (simaster_pengisiankrs == 4):
            xpos 1320
            ypos 850
            idle "tutorial/right_idle.png"
            hover "tutorial/right_idle.png"

        else:
            xpos 1320
            ypos 850
            auto "tutorial/right_%s.png"
            action  [SetVariable("simaster_pengisiankrs", If(simaster_pengisiankrs<=3, simaster_pengisiankrs+1, )), Show("simaster_pengisiankrs_image")]

    #close
    imagebutton:
        xpos 70
        ypos 950
        idle "menuUI/stats/return_idle.png"
        hover "menuUI/stats/return_hover.png"
        action [Hide("simaster_pengisiankrs", transition=fade), Hide("simaster_pengisiankrs_image", transition=fade), Return()]


screen simaster_pengisiankrs_image:

    frame:
        xsize 1920
        ysize 1080

        if (simaster_pengisiankrs == 1):
            xpos 744
            ypos 289
            background "simaster/home simaster.png"
        
        elif (simaster_pengisiankrs == 2):
            xpos 744
            ypos 289
            background "simaster/home akademik.png"

        elif (simaster_pengisiankrs == 3):
            xpos 744
            ypos 289
            background "simaster/home akademik dpa.png"

        else:
            xpos 744
            ypos 289
            background "simaster/pengisian krs.png"






