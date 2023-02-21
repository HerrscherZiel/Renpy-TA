screen test():
    default xadj = ui.adjustment()
    default yadj = ui.adjustment()
    frame:
        background Transform(Solid("FFF", xysize=(420, 420)), alpha=0.5)
        has viewport:
            align (0.5, 0.5)
            child_size (10000, 10000)
            xysize (400, 400)
            id "test"
            xadjustment xadj
            yadjustment yadj
            
            has vbox spacing 10
            for i in xrange(100):
                hbox:
                    spacing 10
                    for i in xrange(10):
                        add Solid("F00", xysize=(50, 100))
                
    vbox:
        align (1.0, 0.5)
        spacing 3
        textbutton "up":
            xalign 0.5
            action Function(yadj.change, yadj.value - 10), renpy.restart_interaction
        hbox:
            textbutton "left":
                action Function(xadj.change, xadj.value - 10), renpy.restart_interaction
            textbutton "down":
                action Function(yadj.change, yadj.value + 10), renpy.restart_interaction
            textbutton "right":
                action Function(xadj.change, xadj.value + 10), renpy.restart_interaction

label starting:
    call screen test