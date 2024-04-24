
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

init:
    $ timer_range = 0
    $ timer_range2 = 0
    $ timer_jump = 0
    $ timer_jump2 = 0
    $ timer_jump3 = 0
    $ time = 0
    $ time2 = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve

screen countdown2:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown2'), Hide('pti_task1'), Show('ptit_done')])
    
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve

screen countdown3:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown3'), Hide('web_task1'), Show('web_done')])
    
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 600 at alpha_dissolve
