screen kod_matkul_btn:

    imagebutton:
        xpos 1793
        ypos 230
        # xoffset -30
        # yoffset 30
        auto "krs/kode_%s.png"
        action ShowMenu("kode_matkul")
        

screen kode_matkul:

    add "bg black.png"

    frame:
        xsize 1920
        ysize 1080
        # xalign 0.5
        xpos 220
        ypos 30
        # yalign 0.5
        # xpadding 30
        # ypadding 30
        background "krs/kode matkul.png"

    #close
    imagebutton:
        xpos 1480
        ypos 65
        auto "krs/close_%s.png"
        action Return()

screen isi_krs:

    # add "bg black.png"

    frame:
        xsize 720
        ysize 560
        background "bg black.png"

        hbox:
            text "UNDER CONSTRUCTION" size 55


    imagebutton:
        xpos 1480
        ypos 65
        auto "krs/close_%s.png"
        action Return()

