init python:
    def name_func(newstring):
        store.note = newstring
    def con_func(newstring):
        store.capt = newstring

default krsroll1 = 1
default capt = ""

#var matkul
default alpro1 = False
default strukdat1 = False
default basdat1 = False
default pbo1 = False
default pti1 = False
default web1 = False
default jarkom1 = False
default de1 = False

#var count matkkul
default matkulcount = 0
default alpro2 = False



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

    add "bg black.png"

    frame:
        
        # xsize 1920
        # ysize 2249
        
        side ("c r"):
            # area (1,0,1920,2278)
            viewport id "my_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                # scrollbars vertical
                child_size 1920, 2778
                image "images/krs/krs2.png"
                text "[name]" size 20 color "#000000" xpos 980 ypos 318

                vbox:#1
                    xpos 200
                    ypos 957
                    spacing 6

                    imagebutton:
                        if(alpro1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 1)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(alpro1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 1)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#2
                    xpos 200
                    ypos 1222
                    spacing 6
                    imagebutton:
                        if(strukdat1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 2)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(strukdat1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 2)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#3
                    xpos 200
                    ypos 1468
                    spacing 6
                    imagebutton:
                        if(basdat1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 3)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(basdat1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 3)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#4
                    xpos 200
                    ypos 1713
                    spacing 6
                    imagebutton:
                        if(pbo1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 4)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(pbo1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 4)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#5
                    xpos 200
                    ypos 1956
                    spacing 6
                    imagebutton:
                        if(pti1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 5)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(pti1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 5)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#6
                    xpos 200
                    ypos 2077
                    spacing 6
                    imagebutton:
                        if(web1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 6)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(web1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 6)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#7
                    xpos 200
                    ypos 2315
                    spacing 6
                    imagebutton:
                        if(jarkom1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 7)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(jarkom1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 7)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

                vbox:#8
                    xpos 200
                    ypos 2553
                    spacing 6
                    imagebutton:
                        if(de1==True):
                            idle "krs/button_selected.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()
                        else:
                            id "n1"
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 8)
                            # action Show("captcha")
                    imagebutton:
                        auto "krs/button_%s.png"
                        action Show("wrong_class")
                    imagebutton:
                        if(de1==True):
                            auto "krs/button_%s.png"
                            action Show("captcha", None, 8)
                        else:
                            idle "krs/button_idle.png"
                            hover "krs/button_hover.png"
                            # auto "krs/button_%s.png"
                            action NullAction()

            vbar value YScrollValue("my_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
       
        imagebutton:
            xpos 1793
            ypos 170
            # xoffset -30
            # yoffset 30
            auto "krs/kode_%s.png"
            action ShowMenu("kode_matkul")

        if matkulcount > 7:

            if day < 4:
                imagebutton:
                    xalign 0.0
                    yalign 1.0 
                    idle "trans/layer.png"
                    action Jump('fin_krs')
            
            else:
                imagebutton:
                    xalign 0.0
                    yalign 1.0 
                    idle "trans/layer.png"
                    action Return()
        else:
            pass

        # imagebutton:
        #     xpos 1480
        #     ypos 65
        #     auto "krs/close_%s.png"
        #     action Return()

screen captcha(x):

    tag captcha
    key "K_a" action NullAction()

    $ krsroll = renpy.random.randint(1111, 9999)
    # $ capt = "%d" % krsroll
    $ inStr = "%d" % krsroll

    frame:

        background "images/krs/krs_captcha.png"
        xpos 575
        ypos 450

        vbox:
            xpos 135
            ypos 125
            text "[krsroll]" size 22 color "#000000"


        vbox:
            xpos 370
            ypos 87
            spacing 10
            text "Masukan di sini" color "#000000" size 22
            button:
                id "name_input1"
                xysize (250, 40)
                action NullAction()
                add Input(size=22, color="#ff0066", default=note, changed=name_func, length=10, button=renpy.get_widget("captcha","name_input1")) yalign 1.0

        #confirm
        imagebutton:
            id "conf"
            xpos 160
            ypos 210
            # Show("test2", pic2=pic1)
            # , If(capt==note, alpro2==True)
            auto "krs/confirm_%s.png"
            action [SetVariable("capt", inStr), Hide('captcha'), Show('check', None, x)]

            # action Hide('captcha')

        #batal
        imagebutton:
            xpos 530
            ypos 210
            # xoffset -30
            # yoffset 30
            auto "krs/batal_%s.png"
            # action [renpy.hide_screen("captcha"), renpy.restart_interaction]
            action [renpy.hide_screen("captcha"), renpy.restart_interaction]

screen check(x):

    if x==1:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("alpro1", If(alpro1==False, True, False)), SetVariable('matkulcount', If(alpro1==False, matkulcount+1, matkulcount-1)),Hide('check')]
                    # Show("test2", pic2=pic1)
                    # , If(capt==note, alpro2==True)
        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

    elif x==2:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("strukdat1", If(strukdat1==False, True, False)), SetVariable('matkulcount', If(strukdat1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')
    
    elif x==3:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("basdat1", If(basdat1==False, True, False)), SetVariable('matkulcount',If(basdat1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

    elif x==4:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("pbo1", If(pbo1==False, True, False)), SetVariable('matkulcount', If(pbo1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

    elif x==5:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("pti1", If(pti1==False, True, False)), SetVariable('matkulcount', If(pti1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

    elif x==6:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("web1", If(web1==False, True, False)), SetVariable('matkulcount', If(web1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

    elif x==7:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("jarkom1", If(jarkom1==False, True, False)), SetVariable('matkulcount', If(jarkom1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')
    
    else:
        if capt == note:
            frame:
                background "krs/konf_captcha_correct.png"
                xpos 625
                ypos 450 

                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action [SetVariable("de1", If(de1==False, True, False)), SetVariable('matkulcount', If(de1==False, matkulcount+1, matkulcount-1)),Hide('check')]

        else:
            frame:
                background "krs/konf_captcha_false.png"
                xpos 625
                ypos 450 
                
                imagebutton:
                    xpos 250
                    ypos 110
                    auto "krs/ok_%s.png"
                    action Hide('check')

screen wrong_class:

    imagebutton:
        xalign 0.0
        yalign 1.0 
        # auto "krs/ok_%s.png"
        idle "krs/wrong_class.png"
        action [Hide('wrong_class'), Show('wrong_class_2', dissolve)]

screen wrong_class_2:

    imagebutton:
        xalign 0.0
        yalign 1.0 
        # auto "krs/ok_%s.png"
        idle "krs/wrong_class_2.png"
        action Hide("wrong_class_2")

    
