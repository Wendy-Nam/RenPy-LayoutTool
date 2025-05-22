########################### CUSTOMIZABLE VARIABLES ###########################

init:
    # modify this line as the path to the bin!
    define bin_img = './layout-visualizer/bin.png' 
    
    # opacity of the bg filter!
    define light_mode_opacity = 0.5 
    define dark_mode_opacity = 0.5

    # These outlines use other outline shader assets
    # so include the outline_shader.rpy file to see the same visual on preview video.
    
    # OURLINE SHADER USED HERE
    # https://feniksdev.itch.io/outline-shader-renpy

    # default item_active_trans = glow_outline(12, "#11d427", num_passes=6)
    # default item_hover_trans = glow_outline(12, "#f5b5c0", num_passes=3)
    
    # If outlines are not needed, change these to None
    define item_active_trans = None
    define item_hover_trans = None

# Layout Tool Guide
# -----------------
# The `layout_tool` in Ren'Py allows you to add and position images or UI elements
# on the screen by dragging them. This temporarily pauses interactions like dialog playback.
#
# Usage Instructions:
# 1. **Open Tools**: Press **L** to open the layout tool. To close the tool and return to normal 
#    game interactions, press **ESC**.
#    
# 2. **Add Images**: Use the search bar in the top-right corner of the tool to input the name of 
#    an image (either a Ren'Py image object or a direct image file with its full path and extension). 
#    Press **Enter** to load the image to the screen.
#    
# 3. **Position Images**: Once the image appears, you can drag it around the screen to position it. 
#    The image’s coordinates will be displayed in the preview box, allowing you to use these exact 
#    values for final positioning.
#
# 4. **Remove Images**: To remove an image from the tool’s screen, drag the image to the trash 
#    icon located next to the search bar (top-right corner).
#
# Important Notes:
# ----------------
# - If the image is inside a container (such as `frame`, `vbox`, `hbox`, `viewport`), 
#   or if it already has position-related properties, the final position displayed in the tool
#   might not reflect the real placement due to overlapping layout rules.
#   
# - To avoid this issue:
#    1. Remove any position attributes from the image.
#    2. Place the image in a `fixed` container, which ignores the influence of other containers 
#       and allows for absolute positioning.
#
# Example:
# --------
# The following is an example of using a `fixed` container to ensure the image is positioned 
# correctly without interference from other containers:
#
# screen example_fixed:
#     fixed:
#         add "example_image.png" xpos 400 ypos 300
#
# This guarantees the image will stay at the exact coordinates specified (400, 300) without being 
# affected by other layout elements.


############################## TOOL INTERFACE #################################

init python:
    config.underlay.append(
        renpy.Keymap( 
            K_l = lambda: renpy.run( Show("layout_tool_visualizer") ) ) )

############################## COLOR THEME #################################

init -1:
    default last_valid_image = None
    if not persistent.pos_tool_mode:
        default persistent.pos_tool_mode = "dark" 

init python:
    what = ""

    def get_colors():
        if persistent.mode == "dark":
            return {
                "background": "#000000",
                "foreground": "#ffffff",
                "frame_background": "#000000",
                "frame_opacity": renpy.store.dark_mode_opacity,
            }
        else:
            return {
                "background": "#ffffff",
                "foreground": "#000000",
                "frame_background": "#f0f0f0",
                "frame_opacity": renpy.store.light_mode_opacity
            }

    def switch_mode():
        if persistent.mode == "dark":
            persistent.mode = "light"
        else:
            persistent.mode = "dark"
        renpy.restart_interaction()

############################## INTERFACE #################################

init:
    screen poptag(message):
        zorder 160
        style_prefix "poptag"
        frame at poptag_appear:
            text "[message!tq]"
        timer 3.25 action Hide('poptag')

    default tool_group = LayoutToolManager()
    default trash_slot = DiscardArea(tool_group)   
    default image_name = './gui/frame.png'
    default postool.img_search = ""
    default postool.img_scale = 1.0
    default custom_input = CustomInputValue(object=store.postool, field="img_search")

screen overlay_movable_images:
    zorder 200
    draggroup:
        add trash_slot.widget
        for item in tool_group.items:
            add item.widget

screen layout_tool_visualizer():
    roll_forward False
    modal True
    zorder 150
    frame:
        background At(Solid(get_colors()["background"]), Transform(Null(), alpha=get_colors()["frame_opacity"]))
        fixed:
            pos (30, 40)
            vbox:
                fit_first True
                frame:
                    background At(Solid(get_colors()["frame_background"]), Transform(Null(), alpha=get_colors()["frame_opacity"]))
                    padding (30, 50)
                    if tool_group.items and last_valid_image and last_valid_image.widget:
                        vbox:
                            label _("Image #%d" % last_valid_image.image_path) text_color ("#FFFFFF" if persistent.mode == "dark" else "#000000") text_size 18
                            label _("Pos") text_color ("#FFFFFF" if persistent.mode == "dark" else "#000000") text_size 18
                            label _("{i}(#%d, #%d){/i}" % (last_valid_image.widget.last_x, last_valid_image.widget.last_y)) text_color ("#FFFFFF" if persistent.mode == "dark" else "#000000") text_size 18
                    else:
                        label _("No Image") text_color ("#FFFFFF" if persistent.mode == "dark" else "#000000") text_size 22
                button:
                    offset (5, 20)
                    xysize (150, 50)
                    action Function(switch_mode)
                    at toggle_appear
                    has vbox
                    if persistent.mode == "dark":
                        text "Switch to Light Mode" color "#FFFFFF" size 20
                    else:
                        text "Switch to Dark Mode" color "#000000" size 20
        fixed:
            pos (int(config.screen_width * 0.7), 45)
            hbox:
                button:
                    style 'button_inputbox'
                    background Solid("#ffffff")
                    xysize (350, 75)
                    padding (40, 20)
                    ycenter 0.5
                    focus_mask True
                    key_events True
                    action custom_input.Toggle()
                    viewport:
                        draggable True
                        fixed:
                            input value custom_input style 'button_inputbox'
                            key 'input_enter' action Function(handle_search_input, custom_input.get_text())
                button:
                    style 'tool_searchbox'
                    xysize (90, 75)
                    padding (10, 18)
                    xcenter 0.5 ycenter 0.5
                    action SetField(postool, "img_search", "")
                    add Text("Clear", style='button_inputclear') 
                at transform:
                    alpha 0.9
        # key_events 
        key 'game_menu' action Hide('layout_tool_visualizer', Dissolve(0.5))
        key 'skip' action NullAction()
    fixed:
        use overlay_movable_images

transform toggle_appear:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0

transform poptag_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style poptag_frame:
    ypos 68
    background Frame("gui/notify.png", 24, 8, 60, 8, tile=False)
    padding (24, 8, 60, 8)

style poptag_text:
    size 24

style tool_searchbox:
    background "#D1180B"
    insensitive_background "#D1180B"
    hover_background "#FF9A98"

style button_inputbox:
    color "#000000"
    size 23

style button_inputclear:
    color "#ffffff"
    size 25


############################## UTILITY #################################

init 100 python:

    class LayoutToolManager:
        def __init__(self):
            self.items = []  
            self.slot = None
        
        def add_item(self, item):
            item.index = len(self.items)
            self.items.append(item)
    
    class DiscardArea:
        def __init__(self, group, xpos=1800, ypos=50, bin_img=renpy.store.bin_img):
            self.xpos, self.ypos = 1800, 50
            self.group = group
            self.group.slot = self
            self.img = At(Image(bin_img), Transform(Null(), zoom=3.0))
            self.widget = self.create_widget()
        
        def create_widget(self):
            return Drag(d=self.img, drag_name="bin", \
                    droppable=True, draggable=False, pos=(self.xpos, self.ypos))

    class MovableImage:
        def __init__(self, group, img=None, image_path=None, xpos=400, ypos=300, zoom=1.0):
            self.index = None
            self.group = group
            self.group.add_item(self)
            self.zoom = zoom
            self.xpos = xpos
            self.ypos = ypos
            self.zoom = zoom
            self.is_dragging = False
            self.image_path = image_path
            # self.update_pos = Transform(function=self.update_position, delay=0.05)
            self.check_active = Transform(function=self.manage_active_item, delay=0.1)
            if image_path is not None and img is not None:
                self.img = At(img, self.check_active)
            else:
                self.img = At(Image(self.image_path), self.check_active)
            self.hover_trans = renpy.store.item_hover_trans or Transform(Null())
            self.hover_img = At(self.img, self.hover_trans)
            self.active_trans = renpy.store.item_active_trans or Transform(Null())
            self.active_img = At(self.img, self.active_trans)
            self.widget = self.create_widget()
            self.is_active_rendered = True  # Does this widget should be rendered active?
            renpy.store.last_valid_image = self
            renpy.restart_interaction() 
            
        def create_widget(self):
            widget = Drag(
                d=self.img,
                hover_child=self.hover_img,
                drag_name="movable_{}".format(self.index),
                pos=(self.xpos, self.ypos),
                draggable=True,
                droppable=False,
                dragged=self.on_drag_end,
                dragging=self.on_drag_start,
                clicked=mark_active_item
            )
            widget.last_x, widget.last_y = self.xpos, self.ypos
            return widget

        def on_drag_start(self, drags):
            """Sets the item as being dragged."""
            self.is_dragging = True
            dragged_idx = int(drags[0].drag_name.split("_")[1])
            dragged_item = self.group.items[dragged_idx]
            self.switch_active_item()
        
        def on_drag_end(self, drags, drop):
            self.is_dragging = False
            dragged_idx = int(drags[0].drag_name.split("_")[1])
            dragged_item = self.group.items[dragged_idx]
            self.switch_active_item()
            if drop:
                if drop.drag_name == "bin":
                    dropped_slot = self.group.slot.widget
                    dragged_item.widget = None
                    for item in reversed(self.group.items):
                        if item.widget is not None:
                            renpy.store.last_valid_image = item
                            item.is_active_rendered = True
                    renpy.show_screen('poptag', message="Image deleted")
                    renpy.redraw(self, 0)
                renpy.restart_interaction()

        def switch_active_item(self):
            self.xpos = self.widget.last_x
            self.ypos = self.widget.last_y
            prev_item = renpy.store.last_valid_image
            renpy.store.last_valid_image = self
            prev_item.manage_active_item()
            self.is_active_rendered = True  # Mark as active
            self.manage_active_item()

        def manage_active_item(self, trans=None, st=None, at=None):
            if self.widget is None:
                return
            if (renpy.store.last_valid_image is self) and self.is_active_rendered:
                self.widget.set_child(self.active_img)
                self.is_active_rendered = False
                renpy.redraw(self.widget, 0)  # Force redraw to reflect the active state
                renpy.restart_interaction()
            elif renpy.store.last_valid_image is not self:
                if (self.is_active_rendered) or (self.widget.child is self.active_img):
                    self.widget.set_child(self.img)
                    self.is_active_rendered = False
                    renpy.redraw(self.group, 0)  # Force redraw to reflect the active state 
                    renpy.restart_interaction()

    def mark_active_item(dragged):
        group = renpy.store.tool_group
        dragged_idx = int(dragged.drag_name.split("_")[1])
        dragged_item = group.items[dragged_idx]
        # If there's a previously active item, set it to idle
        renpy.store.last_valid_image = dragged_item
        for item in group.items:
            item.is_active_rendered = True
            item.manage_active_item()  # Reset other items to idle
        # Set the current item as active
        dragged_item.is_active_rendered = True
        dragged_item.manage_active_item()  # Activate the new item
        renpy.redraw(dragged_item, 0)  # Force update the widget

init python:

    def get_drag_tag_attrs(who, what, adjust=True, filter_swap=False):
        who = who.strip()
        who_split = who.split(' ')
        tag = who_split[0]
        adjust_fn = (config.adjust_attributes.get(tag, None)
            or config.adjust_attributes.get(None, None))
        if len(who_split) > 1:
            attrs = tuple(who_split[1:])
            if what:
                what = tuple(what.split(' '))
                attrs += what
        elif what:
            attrs = tuple(what.split(' '))
        else:
            attrs = tuple()
        # Remove the dev swap attribute, if applicable
        if filter_swap and swap_attr:
            attrs = tuple(filter(lambda x: x != swap_attr, attrs))
        if adjust_fn and attrs and adjust:
            attrs = adjust_fn((tag,) + attrs)
            # Strip off the tag
            attrs = attrs[1:]
        return tag, attrs

    def add_tool_image(image_name):
        if image_name is None or image_name == "":
            return None
        valid_extensions = ['.png', '.jpg', '.webp', '.avif']
        image_path = ""
        if any(image_name.lower().endswith(ext) for ext in valid_extensions):
            image_path = get_tool_image_file(image_name)
        elif image_name:  
            image_path = get_tool_image(image_name)  
        if image_path is not "image_not_found":   
            xpos = 400  
            ypos = 400
            new_item = MovableImage(tool_group, image_path, xpos, ypos)
            return "Image found : " + image_name
        return "Image not found : " + image_name

    def get_tool_image_file(image_name):
        if renpy.loader.loadable(image_name):
            return image_name
        return "image_not_found"

    def get_tool_image(who):
        last_valid_image = None
        if not who:
            return "image_not_found"
        tag, attrs = get_drag_tag_attrs(who, what)
        img = "{} {}".format(tag, ' '.join(attrs)).strip()
        result = renpy.can_show(img)
        if result is not None:
            last_valid_image = ' '.join(result)
            return ' '.join(result)
        return last_valid_image or "image_not_found"
    
    def handle_search_input(text):
        msg = add_tool_image(text)
        if msg is not None:
            renpy.show_screen('poptag', message=msg)

init 999 python:    
    class CustomInputValue(FieldInputValue):
        def __init__(self, object, field, default=False, set_callback=None,
            enter_callback=None, starting_value=None, disable_on_enter=False, strip_on_close=True):
            self.object = object
            self.field = field
            self.default = default
            self.set_callback = set_callback
            self.enter_callback = enter_callback
            if starting_value is not None:
                self.set_text(starting_value)
            self.disable_on_enter = disable_on_enter
            self.strip_on_close = strip_on_close

        def strip_text(self):
            s = self.get_text()
            if s != s.strip():
                self.set_text(s.strip())

        def Disable(self):
            return [Function(self.strip_text), super(CustomInputValue, self).Disable()]
            
        def enter(self):
            if self.disable_on_enter:
                renpy.run(self.Disable())
            elif self.strip_on_close:
                self.strip_text()
            if self.enter_callback:
                self.enter_callback()
            raise renpy.IgnoreEvent()


################################################################################

## Exclude this tool on build, to avoid any potential issues.

init python:
    build.classify("**layout_tool.rpy", None)
    build.classify("**layout_tool.rpyc", None)

################################################################################
