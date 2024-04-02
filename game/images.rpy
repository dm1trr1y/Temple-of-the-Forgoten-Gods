# This is allows to Renpy init this file faster than else
init offset = -5

# SET OF IMAGES TO MAIN MENU PARALLAX BG
# Button animation
image hovered_menu:
    "gui/main_menu_idle.png" 
    linear 0.5 brightness(.02)
    linear 0.5 brightness(.0)
    repeat

image main_menu_par = Par(("images/main menu prlx/main_menu_A.png",1.08),("images/main menu prlx/main_menu_B.png",1.05))
image main_menu_kusty = Par(("images/main menu prlx/main_menu_D.png",1.15))

# just a glitched overlay
image glitched_overlay= Fixed("gui/overlay/game_menu.png",Glitch(Solid("#ffffff1f"), glitch_strength=1.0, _fps=10, min_crop_width=.01, max_crop_width=.3, min_crop_height=.01, max_crop_height=.02, color_range1=(255,255,255,10), color_range2=(255,255,255,20)))


# FIRE STARTS
image fire_1:
    "fire1"
    linear 3 rotate 360 zoom 1.5 alpha 0.0
    repeat
image fire_2:
    rotate 0
    "fire2"
    linear 3 rotate 360 zoom 1.5 alpha 0.0
    repeat

image fire_side = SnowBlossom("fire_1", 60, border=50, xspeed=(600, 1300), yspeed=(-150, -140), start=25, horizontal=True)
image fire_main = SnowBlossom("fire_2", 140, xspeed=(10,70), yspeed=(-400, -500), start=10)
# FIRE ENDS


# SNOW STARTS
image snow_1:
    "snow"
    rotate 0
    zoom 1.1
    alpha 1.0
    linear 8 rotate 360 alpha 0.0

image snow_2:
    "snow"
    rotate 0
    zoom 0.5
    alpha 1.0
    linear 5 rotate 360 alpha 0.0
    
image snow_far = SnowBlossom("snow_2", 80, xspeed=(10, 50), yspeed=(200, 500), start=3)
image snow_close = SnowBlossom("snow_1", 100, xspeed=(10, 100), yspeed=(220, 490), start=2)
image snow_side = Fixed(SnowBlossom("snow_1", 280, xspeed=(100, 300), yspeed=(220, 600), start=1, horizontal=True), xysize=(2560,1440))
# SNOW ENDS

# CLOUDS STARTS
image clouds_1:
    "clouds-1"
    choice:
        ypos 0.1
    choice:
        ypos 0.2
    choice:
        ypos 0.3
    choice:
        ypos 0.4
    choice:
        ypos 0.5
    choice:
        ypos 0.6
    xpos -0.3
    ease rnd(i_from=20, i_to=30) xpos 1.1
    repeat

image clouds_2:
    "clouds-2"
    choice:
        ypos 0.1
    choice:
        ypos 0.2
    choice:
        ypos 0.3
    choice:
        ypos 0.4
    xpos -0.3
    ease rnd(i_from=25, i_to=35) xpos 1.1
    repeat
# CLOUDS ENDS

# SMOKE STARTS
image smoke_1:
    "smoke-1"
    ypos 0.8
    xpos rnd(i_from=-1, i_to=0)
    ease rnd(i_from=25, i_to=29) xpos 1.5
image smoke_2:
    "smoke-2"
    ypos 0.85
    xpos rnd(i_from=-1, i_to=0)
    ease rnd(i_from=30, i_to=35) xpos 1.5
image smoke_3:
    "smoke-3"
    ypos 0.9
    xpos rnd(i_from=-1, i_to=0)
    ease rnd(i_from=25, i_to=35) xpos 1.5


layeredimage stepan:
    zoom 0.5
    group pose:
        attribute idle default
        attribute cross

    group face auto:
        pos (0, 0)
        attribute serio default
        attribute angry
        attribute happy
        attribute smile
        attribute think 

    group clothes:
        attribute home 