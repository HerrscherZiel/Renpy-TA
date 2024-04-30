
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

init:
    $ timer_range = 0
    $ timer_range2 = 30
    $ timer_range3 = 30
    $ timer_jump = 0
    $ timer_jump2 = 0
    $ timer_jump3 = 0
    $ time = 0
    $ time2 = 30
    $ time3 = 30

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve

screen countdown2:
    timer 0.01 repeat True action If(time2 > 0, true=SetVariable('time2', time2 - 0.01), false=[Hide('countdown2'), Hide('pti_task1'), Show('ptit_done')])
    
    bar value time2 range timer_range2 xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve

screen countdown3:
    timer 0.01 repeat True action If(time3 > 0, true=SetVariable('time3', time3 - 0.01), false=[Hide('countdown3'), Hide('web_task1'), Show('web_done')])
    
    bar value time3 range timer_range3 xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve

# screen countdown2:
#     timer 1 repeat True action If(time2 > 0, true=SetVariable('time2', time2 - 1), false=[Hide('countdown2'), Hide('pti_task1'), Show('ptit_done')])
#     if time2 <= 2:
#         text str(time2) xpos .5 ypos .1 color "#FF0000" at alpha_dissolve
#     else:
#         text str(time2) xpos .1 ypos .2 at alpha_dissolve

