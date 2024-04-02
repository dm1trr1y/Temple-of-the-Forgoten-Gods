﻿################################################################################
## Инициализация
################################################################################

## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2

## Вызываю gui.init, чтобы сбросить стили, чувствительные к стандартным
## значениям, и задать высоту и ширину окна игры.
init python:
    gui.init(2560, 1440)



################################################################################
## Конфигурируемые Переменные GUI
################################################################################


## Цвета #######################################################################
##
## Цвета текста в интерфейсе.

## Акцентный цвет используется в заголовках и подчёркнутых текстах.
define gui.accent_color = '#d50000'

## Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define gui.idle_color = '#ce0000'

## Small_color используется в маленьком тексте, который должен быть ярче/темнее,
## для того, чтобы выделяться.
define gui.idle_small_color = '#ffa0a0'

## Цвет, используемых в кнопках и панелях, когда они наведены.
define gui.hover_color = '#e23131'

## Цвет, используемый текстовой кнопкой, когда она выбрана, но не наведена.
## Кнопка может быть выбрана, если это текущий экран или текущее значение
## настройки.
define gui.selected_color = '#ff5900'

## Цвет, используемый текстовой кнопкой, когда она не может быть выбрана.
define gui.insensitive_color = '#5d4545f9'

## Цвета, используемые для частей панелей, которые не заполняются. Они
## используются не напрямую, а только при воссоздании файлов изображений.
define gui.muted_color = '#c30303'
define gui.hover_muted_color = '#ff0000'

## Цвета, используемые в тексте диалогов и выборов.
define gui.text_color = '#d5d5d5'
define gui.interface_text_color = '#d5d5d5'
define gui.text_outlines = [(2,"#000", 2,3)]

## Шрифты и их размеры #########################################################

## Шрифт, используемый внутриигровым текстом.
define gui.text_font = "fonts/Zhizn.otf"
define gui.hyperlink_text_font = "fonts/beer money.ttf"

define gui.dialogue_text_font = "fonts/LEngineer-Regular.otf"

## Шрифт, используемый именами персонажей.
define gui.name_text_font = "fonts/Zhizn.otf"

## Шрифт, используемый меткой в главном меню
define gui.main_menu_font = "fonts/beer money.ttf"

## Шрифт, используемый текстом вне игры.
define gui.interface_text_font = "fonts/beer money.ttf"

## Размер нормального текста диалога.
define gui.text_size = 40

## Размер имён персонажей.
define gui.name_text_size = 40

## Размер текста в пользовательском интерфейсе.
define gui.interface_text_size = 45

## Размер заголовков в пользовательском интерфейсе.
define gui.label_text_size = 60

## Размер текста на экране уведомлений.
define gui.notify_text_size = 40

## Размер заголовка игры.
define gui.title_text_size = 100


## Главное и игровое меню. #####################################################

## Изображения, используемые в главном и игровом меню.
# define gui.main_menu_background = "gui/main_menu.png"
# define gui.game_menu_background = "gui/game_menu.png"
define gui.preferences_menu_background = "gui/preferences.png"
define gui.loadSave_menu_background = "gui/loadSave.png"
define gui.about_menu_background = "gui/about.png"



## Диалог ######################################################################
##
## Эти переменные контролируют, как диалог появляется на отдельной строчке.

## Высота текстового окна, содержащего диалог.
define gui.textbox_height = 300

## Местоположение текстового окна по вертикали экрана. 0.0 — верх, 0.5 — центр и
## 1.0 — низ.
define gui.textbox_yalign = 1.0


## Местоположение имени говорящего персонажа по отношению к текстовому окну.
## Это могут быть целые значения в пикселях слева и сверху от начала окна или
## процентное отношение, например, 0.5 для центрирования.
define gui.name_xpos = 0.5
define gui.name_ypos = 10


define gui.name_outlines = [(4,"#000", 2,3)]
# define gui.text_kerning = -1


## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.name_xalign = 0.5

## Ширина, высота и границы окна, содержащего имя персонажа или None, для
## автоматической размерки.
define gui.namebox_width = None
define gui.namebox_height = None

## Границы окна, содержащего имя персонажа слева, сверху, справа и снизу по
## порядку.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Если True, фон текстового окна будет моститься (расширяться по эффекту
## плитки). Если False, фон текстового окна будет фиксированным.
define gui.namebox_tile = True


## Размещение диалога по отношению к текстовому окну. Это могут быть целые
## значения в пикселях слева и сверху от текстового окна или процентное
## отношение, например, 0.5 для центрирования.
define gui.dialogue_xpos = 0.5
define gui.dialogue_ypos = 0.3

## Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = 1440

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.dialogue_text_xalign = 0.5


## Кнопки ######################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = None

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(8, 8, 8, 8)

## Если True, фон изображения будет моститься. Если False, фон изображения будет
## линейно масштабирован.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_outlines = [(3, "#000", 2, 3)]
## Горизонтальное выравнивание текста в кнопке. (0.0 — лево, 0.5 — по центру,
## 1.0 — право).
define gui.button_text_xalign = 0.5


## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(60, 0, 0, 10, 0,0,60,0)
define gui.radio_button_yalign = 0.5
define gui.radio_button_text_color = "#bfbfbf"
define gui.radio_button_text_hover_color = "#929292"
define gui.radio_button_text_selected_color = "#c86060"

define gui.check_button_text_color = "#bfbfbf"
define gui.check_button_text_hover_color = "#929292"
define gui.check_button_text_selected_color = "#c86060" 

define gui.check_button_borders = Borders(60, 0, 0, 10, 0,0,60,0)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(20, 8, 20, 8)

define gui.quick_button_borders = Borders(20, 8, 20, 0)

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250




#labels properties
define gui.label_text_size = gui.interface_text_size
define gui.label_text_outlines = [(3, "#000000cc", 2,3)]



## Кнопки Выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 1580
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(200, 10, 200, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Кнопки Слотов ###############################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = 550
define gui.slot_button_height = 390
define gui.slot_button_borders = Borders(20, 20, 20, 20)
define gui.slot_button_text_size = 28
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 510
define config.thumbnail_height = 290


## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 4
define gui.file_slot_rows = 2


## Позиционирование и Интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define gui.navigation_xpos = 0.5

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 20

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 20

## Интервал между выборами в меню.
define gui.choice_spacing = 44

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 8

## Контролирует интервал между настройками.
define gui.pref_spacing = 50

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 10

## Интервал между кнопками страниц.
define gui.page_spacing = -10

## Интервал между слотами.
define gui.slot_spacing = 20

## Позиция текста главного меню.
define gui.main_menu_text_xalign = 0


## Рамки #######################################################################
##
## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Генерируем рамки.
define gui.frame_borders = Borders(8, 8, 8, 8)

## Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(32, 10, 100, 10)

## Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(32, 10, 80, 10)

## Должны ли фоны рамок моститься?
define gui.frame_tile = True


## Панели, Полосы прокрутки и Ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 20
define gui.scrollbar_size = 14
define gui.slider_size = 32


define gui.slider_xsize = 500
define gui.slider_hbox_xsize = 600

## True, если изображения панелей должны моститься. False, если они должны быть
## линейно масштабированы.
define gui.bar_tile = True
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(8, 8, 8, 8)
define gui.scrollbar_borders = Borders(10, 6, 10, 6)
define gui.slider_borders = Borders(6,10,6,10)

## Вертикальные границы.
define gui.vbar_borders = Borders(8, 8, 8, 8)
define gui.vscrollbar_borders = Borders(6, 10, 6, 10)
define gui.vslider_borders = Borders(6,6,6,6)

## Что делать с непрокручиваемыми полосами прокрутки в интерфейсе. "hide" прячет
## их, а None их показывает.
define gui.unscrollable = "hide"


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## Количество диалоговых блоков истории, которые Ren'Py будет хранить.
define config.history_length = 250

## Высота доступных записей на экране истории, или None, чтобы задать высоту в
## зависимости от производительности.
define gui.history_height = 140

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.history_name_xpos = 150
define gui.history_name_ypos = 0
define gui.history_name_width = 150
define gui.history_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = 170
define gui.history_text_ypos =5
define gui.history_text_width = 1700
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 20, 0, 40)

## Максимальное число показываемых строк в режиме NVL. Когда количество строчек
## начинает превышать это значение, старые строчки очищаются.
define gui.nvl_list_length = 6

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = 230

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = 20

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = 860
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 300
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 900
define gui.nvl_text_ypos = 16
define gui.nvl_text_width = 1180
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = 480
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1560
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 900
define gui.nvl_button_xalign = 0.0

## Локализация #################################################################

## Эта настройка контролирует доступ к разрыву линий. Стандартная настройка
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    ## Этот параметр увеличивает размер быстрых кнопок, чтобы сделать их
    ## доступнее для нажатия на планшетах и телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(80, 28, 80, 0)

    ## Это изменяет размеры и интервалы различных элементов GUI, чтобы
    ## убедиться, что они будут лучше видны на телефонах.
    @gui.variant
    def small():

        ## Размеры шрифтов.
        gui.text_size = 40
        gui.name_text_size = 50
        gui.notify_text_size = 30
        gui.interface_text_size = 45
        gui.button_text_size = 40
        gui.label_text_size = 50

        ## Регулирует местоположение текстового окна.
        gui.textbox_height = 370
        gui.name_xpos = 160
        gui.dialogue_xpos = 560
        gui.dialogue_width = 1700

        ## Изменяет размеры и интервалы различных объектов.
        gui.slider_size = 35
        gui.slider_xsize = 600

        gui.scrollbar_size = 20

        gui.choice_button_width = 2480
        gui.choice_button_text_size = 60

        gui.navigation_spacing = 40
        gui.pref_button_spacing = 20

        gui.history_height = 380
        gui.history_text_width = 1380

        gui.quick_button_text_size = 30

        ## Местоположение кнопок слотов.
        gui.file_slot_cols = 3
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = 340

        gui.nvl_name_width = 610
        gui.nvl_name_xpos = 650

        gui.nvl_text_width = 1830
        gui.nvl_text_xpos = 690
        gui.nvl_text_ypos = 10

        gui.nvl_thought_width = 2480
        gui.nvl_thought_xpos = 40

        gui.nvl_button_width = 2480
        gui.nvl_button_xpos = 40
