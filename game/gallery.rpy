init python:

    max_x = 3
    max_y = 3 

    thumbnail_x = 400
    thumbnail_y = int(thumbnail_x * 0.5625)

    max_page = max_x * max_y
    gallery_resolution_scaling = config.screen_width / 1920.0
    gallery_navigation_width = int(400 * gallery_resolution_scaling)
    # gallery_page = 0
    # gallery_items = []
    # g = Gallery()
    # g.transition = dissolve
    # g.locked_button = im.Scale("lock.png",thumbnail_x,thumbnail_y)


    gallery = Gallery()

    # gallery.button("edkutu")
    # gallery.image("cg_alvea")
    # gallery.unlock_image("cg_alvea")

    #cuma nama
    gallery.button("kutu")
    #gambar asli ketika unlocked
    gallery.image("cg_kutubuku")
    #var persistent nya
    gallery.condition("persistent.edkutucg")

    gallery.button("nolife")
    gallery.image("cg_nolife")
    gallery.condition("persistent.ednolifecg")

    gallery.button("anti_kupu")
    gallery.image("cg_antikupu")
    gallery.condition("persistent.edantikupucg")

    gallery.button("bagai_kuda")
    gallery.image("cg_bagaikuda")
    gallery.condition("persistent.edbagaikudacg")

    gallery.button("sehatno")
    gallery.image("cg_sehatno")
    gallery.condition("persistent.edsehatnocg")

    gallery.button("badend")
    gallery.image("cg_badend")
    gallery.condition("persistent.edbadendcg")

    gallery.button("normies")
    gallery.image("cg_normies")
    gallery.condition("persistent.ednormiescg")

    gallery.button("idaman")
    gallery.image("cg_idaman")
    gallery.condition("persistent.edidamancg")

    # $ persistent.kaga_unlocked = True

screen gallery():
    tag menu
    
    frame:
        xsize 1920
        ysize 1080
        background "gui/overlay/main_menu_overlay.png"
        use navigation

        hbox:
            vbox:
                xpos 63
                ypos 943
                spacing 20
                imagebutton:
                    idle "menuUI/stats/return_idle.png"
                    hover "menuUI/stats/return_hover.png"
                    action Return()

            grid 4 2:

                # xfill True
                # yfill True
                xpos 700
                ypos 100
                # hbox:
                xalign 0.35
                yalign 1
                spacing 15


                # add gallery.make_button(name="alvea", unlocked="cg_alvea2.png", locked="lock.png")
                add gallery.make_button(name="kutu", unlocked="cg_kaga2.png", locked="lock.png")
                add gallery.make_button(name="nolife", unlocked="cg_kaga2.png", locked="lock.png")

                # add gallery.make_button(name="alvea", unlocked="cg_alvea2.png", locked="lock.png")
                add gallery.make_button(name="anti_kupu", unlocked="cg_kaga2.png", locked="lock.png")
                add gallery.make_button(name="bagai_kuda", unlocked="cg_beatrice.png", locked="lock.png")

                # add gallery.make_button(name="alvea", unlocked="cg_alvea2.png", locked="lock.png")
                add gallery.make_button(name="sehatno", unlocked="cg_beatrice.png", locked="lock.png")
                add gallery.make_button(name="badend", unlocked="cg_beatrice.png", locked="lock.png")

                add gallery.make_button(name="normies", unlocked="cg_beatrice.png", locked="lock.png")
                add gallery.make_button(name="idaman", unlocked="cg_beatrice.png", locked="lock.png")


            


# KENEEE

# init python:

#     ### CONFIG ###
#     # file extension of the CGs, used in creating automatic thumbnails
#     cg_format = ".jpg" 
#     # path to CGs
#     cg_path = "images/cg/" 
#     # number of columns of thumbnails in the gallery grid
#     max_x = 3 
#     # number of rows of thumbnails in the gallery grid
#     max_y = 3 
#     # this will be the width of the thumbnails, height will be calculated automatically for 16:9 aspect ratio thumbnails
#     # recommended sizes:
#     # 290 for 1280x720 resolution
#     # 400 for 1920x1080 resolution
#     thumbnail_x = 400
#     ### END OF CONFIG ###

#     max_page = max_x * max_y
#     thumbnail_y = int(thumbnail_x * 0.75) # to change the aspect ratio from 16:9 to 4:3, change the value in formula to 0.75
#     gallery_resolution_scaling = config.screen_width / 1920.0
#     gallery_navigation_width = int(400 * gallery_resolution_scaling)
#     gallery_page = 0
#     gallery_items = []
#     g = Gallery()
#     g.transition = dissolve
#     g.locked_button = im.Scale("lock.png",thumbnail_x,thumbnail_y)

#     # A class for gallery items (no need to change anything here)
#     # when creating a GalleryItem object, provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
#     # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
#     # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
#     class GalleryItem:
#         def __init__(self, name, images, thumb=None):
#             self.name = name
#             self.images = images 
#             if thumb is None:
#                 self.thumb = im.Scale(cg_path+images[0]+cg_format,thumbnail_x,thumbnail_y) 
#             else:
#                 self.thumb = im.Scale(thumb,thumbnail_x,thumbnail_y)

#         def num_images(self):
#             return len(self.images)

# image gallery_idle_overlay = im.Scale("lock.png",thumbnail_x,thumbnail_y)
# image gallery_background_overlay: 
#     "images/gallery_overlay/gallery_background_overlay.png"
#     zoom gallery_resolution_scaling

# screen gallery():

#     python:
#         if len(gallery_items) == 0:

#             ### CGs ###
#             # Provide button name, a list of images to display, and alternatively a path to a custom thumbnail
#             gallery_items.append(GalleryItem("alvea", ["cg alvea"]))
#             gallery_items.append(GalleryItem("kaga", ["cg kaga"]))

#             for item in gallery_items:
#                 g.button(item.name)
#                 for img in item.images:
#                     g.unlock_image(img)

#         start = gallery_page * max_page
#         end = min(start + max_page - 1, len(gallery_items) - 1)


#     ### Layout ###
#     tag menu
#     style_prefix "game_menu"
#     # add im.Blur(gui.main_menu_background, 1.5)
#     add "gui/overlay/bg.png"
#     # add "gallery_background_overlay"

#     hbox:
#         vbox:
#             style_prefix "navigation"
#             yalign 0.9
#             xsize gallery_navigation_width
#             xpos gui.navigation_xpos
#             spacing gui.navigation_spacing

#             textbutton "Previous":
#                 if gallery_page > 0:
#                     action SetVariable("gallery_page", gallery_page - 1)
#             textbutton "Next":
#                 if (gallery_page + 1) * max_page < len(gallery_items):
#                     action SetVariable("gallery_page", gallery_page + 1)
#             textbutton "Return" action Return()

#         grid max_x max_y:
#             xfill True
#             yfill True
#             for i in range(start, end + 1):
#                 $ item = gallery_items[i]
#                 add g.make_button(item.name, item.thumb, idle_border="gallery_idle_overlay", xalign=0.5, yalign=0.5)
#             for i in range(end - start + 1, max_page):
#                 null


#images copyright
#canteen Photo by <a href="https://unsplash.com/@anhvygor?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Anh Vy</a> on <a href="https://unsplash.com/photos/assorted-foods-on-tray-display-I0aBAeof-nk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
#rumah makan Photo by <a href="https://unsplash.com/@innasafa?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Inna Safa</a> on <a href="https://unsplash.com/photos/a-restaurant-with-tables-and-chairs-and-a-tree-in-the-middle-of-the-room-rAGCUafRVM4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
#bioskop dalam Image by <a href="https://pixabay.com/users/derks24-5892478/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2502213">Alfred Derks</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2502213">Pixabay</a>
