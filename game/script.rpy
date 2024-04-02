# Вы можете расположить сценарий своей игры в этом файле.

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# Игра начинается здесь:

label start:
    $ persistent.number_of_try +=1
    $ new_chapter("Пролог")
    $ renpy.music.stop(channel="music", fadeout=1)
    scene black

    play ambience "horror ambience.wav"
    
    show screen my_bg(("cave bg", "snow_far", "snow_close", "cave main"))
    with fade
    show stepan smile at top 
    with dissolve 
    "Какой-то текст для теста"
    
    # show stepan angry at top 
    # with dissolve 

    # "А сейчас я зол!!!"

    

    window hide
    pause 4
    return