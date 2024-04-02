# --- СЛОЁННЫЙ ФОН ---
# С помощью этого экрана я создаю анимированный фон для своей игры. Сделан он довольно просто и совсем не замудренно
# imgs - это список слоёв начиная с 0 и заканчивая самым верхним слоем 
# glitch - переменная которая добавляет глитч ефект сверху фона как бы это воспоминания
# horror - если True то добавляет h_img как хоррор каринку которая меняется с основным фоном тем самым создаёт некий страшный эффект
# --- КАК ИСПОЛЬЗОВАТЬ ---
# Показываем экран в файле сценария с указанием нужных изображений и параметров. ВАЖНО: экран не поддерживает свойство at
# для анимации перехода добавляте with после изображения
# -show screen my_bg(("out-cave-1", "out-cave-2", "clouds_1", "out-cave-3", "clouds_2", "out-cave-4", "snow_far", "snow_close", "out-cave-5"))
# -with fade
screen my_bg(imgs, glitch=False, horror=False, h_img=""):
    layer "master"
    tag my_bg
    if isinstance(imgs, tuple):
        for img in imgs:
            add img
    else:
        add args
    if horror:
        add h_img at horror_transform
    if glitch:
        add Solid("#00000067")
        add Solid("#ffffff41") at Glitch(_fps=rnd(i_from=1, i_to=1000), glitch_strength=.01, min_crop_width=.01, max_crop_width=.3, min_crop_height=.01, max_crop_height=.01, color_range1=(255,255,255,10), color_range2=(255,255,255,20))
# Просто анимация для хоррор слоя
transform horror_transform:
    .1
    choice:
        alpha 0.3 
        1.0
    choice:
        alpha 0.1
        .5
    choice:
        alpha 1.0
        .1
    choice:
        alpha 0.5
        .75
    choice:
        alpha 0.75
        .25
    choice:
        alpha 0.25
        .5
    repeat
