init python:
    all_tent = 0
    def drag_placed(drags, drop):
        if not drop:
            return
        global all_tent


       
        all_tent +=1
        drags[0].draggable = False
        
        store.tent_sides = drags[0].drag_name
        store.tent_spot = drop.drag_name
        
        if all_tent == 3:
            return True
        

screen tent_game():
    draggroup:
        drag:
            drag_name "Front"
            child "tent_2.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Top"
            child "tent_3.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Side"
            child "tent_1.png"
            xpos 700
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "Tent Spot"
            xpos 0.1
            ypos 0.6
            child "tent_spot.png"
            draggable False
            droppable True
