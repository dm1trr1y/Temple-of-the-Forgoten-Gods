
init python:
    _game_menu_screen = "game_menu" #what the screen will be a game menu

    renpy.music.register_channel("ambience", "ambience") #register the ambience mixer channel

    import renpy.store as store
    #func for save with chapter_name
    def new_chapter(chapter_name=""):
        global save_name
        
        save_name = chapter_name 


# Define the all of characters
define stp = Character(_('Степан'), color="#c8ffc8")
define stp_d = Character(_('Степан'), color="#af0000", who_italic=True, what_italic=True)
define voice = Character(_('???'), color="#fff")





# Define the number of try. It will be used to unlock a secret endings or something else.
default persistent.number_of_try = 0


# Stepan`s madness. It is need to change the horrorability of game))))
default stp_madness = 70

# SPLASHSCREEN START
style splashscreen_text:
    color "#c30000"
    font gui.main_menu_font
    size 70
    xalign 0.5
    yalign 0.5

style splashscreen_text_second:
    color "#fff"
    font gui.main_menu_font
    size 100
    xalign 0.5
    yalign 0.5
    
# label splashscreen:
#     scene black
#     show text _("{=splashscreen_text}18+ \n{=welcome_text}В игре присутствуют страшные сцены и ругань. \nНе рекомендуется для людей младше 16 лет. \nА там как хочешь")
#     with fade
#     $ pause(t=4, hard=True)
#     show text _("{=welcome_text}Для лучшего погружения в игру \nиспользуйте наушники")
#     with fade
#     pause(3)
#     hide text with fade    
#     show text _("{=welcome_text}Tenki And His Tales presents...")
#     with fade
#     pause(3)
#     hide text with fade 
#     show fire_side
#     with fade
#     show text _("{=splashscreen_text}Храм забытых богов:\n{=splashscreen_text_second}Приключения Степана")
#     with dissolve
#     $ pause(t=3, hard=True)
#     hide text with dissolve
#     hide fire_side with fade
#     return
# SPLASHSCREEN ENDS