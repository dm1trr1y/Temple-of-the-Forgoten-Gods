# пример использования
# image test = Par("bg", "layer1", "layer2")
# или
# show expression Par("bg", "layer1", "layer2") as room

# картинки должны быть разного размера, например,
# 3130х1760, 2614х1470, 2099х1180

# либо одинакового размера, но тогда их нужно увеличивать программно:
# Par(("bg", 1.5), ("layer1", 1.3), ("layer2",1.15))

init -1111 python:
    # на случай, если не используется модуль для пузырей с диалогами
    speaker = None

    # положение говорящего, если он часть параллакса
    parallax_tag = None
    parallax_x, parallax_y, parallax_w, parallax_h = -1, -1, -1, -1

init python:
    import math

    # класс для параллакса
    class Par(renpy.Displayable):
        # инициализация класса
        def __init__(self, *args):
            super(Par, self).__init__()
            self.mouse_x, self.mouse_y = int(config.screen_width / 2), int(config.screen_height / 2)
            self.actual_x = None
            self.actual_y = 0
            self.last_st = 0

            # заполнение данных слоёв
            self.images = []
            for i in args:
                image, zoom = i, 1
                if isinstance(i, (tuple, list)):
                    image, zoom = i[0], i[1]
                self.images.append((str(image), Transform(image, zoom=zoom)))
            return

        # отрисовка displayable
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            # перебираем слои
            for sprite_name, image in self.images:
                # рендерим и узнаем размеры
                cr = renpy.render(image, 0, 0, 0, 0)
                w, h = cr.get_size()

                if self.actual_x is None:
                    self.actual_x = width / 2
                    self.actual_y = height / 2

                minimum_speed = .3
                maximum_speed = .7
                speed = .2 + minimum_speed
                dx = min(maximum_speed, max(minimum_speed, self.mouse_x - self.actual_x))
                dy = min(maximum_speed, max(minimum_speed, self.mouse_y - self.actual_y))
                st_change = st - self.last_st
                self.last_st = st
                self.actual_x = math.floor(self.actual_x + (self.mouse_x - self.actual_x) * speed * st_change)
                self.actual_y = math.floor(self.actual_y + (self.mouse_y - self.actual_y) * speed * st_change)

                x = self.actual_x - self.actual_x * w / width
                y = self.actual_y - self.actual_y * h / height

                # положение спрайта говорящего, если он часть параллакса
                # спрайт может быть ещё в пути, но он стремится к курсору мыши
                if store.speaker:
                    if str(store.speaker) in str(sprite_name):
                        store.parallax_tag = speaker
                        store.parallax_x = x
                        store.parallax_y = y
                        store.parallax_w = w
                        store.parallax_h = h

                # выводим слой на общую картинку
                r = renpy.render(image, int(w), int(h), st, at)
                render.blit(r, (int(x), int(y)))
            # перерисовываем экран
            renpy.redraw(self, 0)
            return render    
        
        # считывание позиции мышки
        def event(self, ev, x, y, st):
            import pygame
            hover = ev.type == pygame.MOUSEMOTION
            # click = ev.type == pygame.MOUSEBUTTONDOWN
            # mousefocus = pygame.mouse.get_focused()
            if hover:
                if (x != self.mouse_x) or (y != self.mouse_y):
                    self.mouse_x, self.mouse_y = x, y
            return