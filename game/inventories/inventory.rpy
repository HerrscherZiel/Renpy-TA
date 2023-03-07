
init python:

    class Inventory():
        def __init__(self,items):
            self.items = items

        def add_item(self, item):
            pass
        
        def remove_item(self, item):
            pass 

        def list_item(self):
            pass

    class InventoryItem():
        def __init__(self, name, description):
            self.name = name
            self.description = description


# frame:
#     xsize 1920
#     ysize 1080
#     xpos 1200
#     ypos 100
    # background "items/get_frame.png"
    # background "items/box_get.png"

    # vbox:
#     imagebutton:
#         xpos 85
#         ypos 70
#         idle "items/box_get.png"
    
#     timer 3.0 action [Hide("get_box"), Show("trans_img")]

# screen trans_img:

#     frame:
#         xsize 1920
#         ysize 1080
#         xpos 750
#         ypos 350
#         # background "items/get_frame.png"
#         background "items/trans_img.png"
    
#     if renpy.get_screen("mapUI"):
#         timer 0.1 action Return()

#     else:
#         pass
