# Transitions
define slowdissolve = Dissolve(0.5)
define flash_white = Fade(0.1, 0.0, 0.1, color="#FFFFFF")

transform slight_left:
    xalign 0.25
    yalign 1.00

transform slight_right:
    xalign 0.75
    yalign 1.00

transform left:
    xalign 0.1
    yalign 1.00

transform pos_right:
    xalign 0.9
    yalign 1.00

transform shake_animation:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    repeat

