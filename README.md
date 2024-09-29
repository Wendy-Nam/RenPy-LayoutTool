# Ren'Py Layout Tool

![Version: Beta](https://img.shields.io/badge/Version-Beta-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green)

> Instantly Preview and Place Images in Ren'Py
- Load new images directly into your current scene as overlays
   - making it easy to visualize and adjust their positions without leaving the game.
- This tool is for previewing purposes only.
   - It doesn't add images directly to the code but helps you assess the placement and suitability of multiple assets before finalizing your scene.

## Overview

The Ren'Py Layout Tool helps developers position images and UI elements on the screen by dragging them. This project is currently in **beta**, so there may be changes or updates based on user feedback.


### ✨ Features
- **Draggable, trackable coordinates**: Easily drag and drop images while tracking their coordinates in real-time.
- **Loads files and Ren'Py images**: Supports both direct image file paths and Ren'Py image objects.
- **Semi-transparent filter with light/dark toggle**: Toggle between light and dark semi-transparent filters to adjust the visibility.
- **Highlights selected images**: Highlights images when clicked or dragged for easy selection and manipulation.
- **Multiple asset placements**: Add multiple images or UI elements to the layout simultaneously.
- **Deletes images via drag to trash bin**: Drag images to the trash bin to remove them from the layout.

## Outline Shader Notice

We are currently using **outline shader effects** in this project. Make sure the outline shaders are properly set up in your project for consistent visuals. 

**Outline Shader Assets by FeniksDev**  
🔗 [https://feniksdev.itch.io/outline-shader-renpy](https://feniksdev.itch.io/outline-shader-renpy)

- If the shaders are not required, we **strongly recommend** changing their value to `None`:

```renpy
# If you don't want to use the outlines, change the value to "None"
default item_active_trans = glow_outline(12, "#11d427", num_passes=6)
default item_hover_trans = glow_outline(12, "#f5b5c0", num_passes=3)

# To disable the outlines:
# define item_active_trans = None
# define item_hover_trans = None
```

# 🖼️ Layout Tool Guide

The `layout_tool` in Ren'Py allows you to visually position images or UI elements on the screen by dragging them around. The tool temporarily pauses interactions like dialog playback, allowing you to fine-tune your layout.

## 🛠️ Installation Guide

1. **Add `bin.png` Image:**
   - Place the `bin.png` image file inside your game's `images` directory.
   - If you want to place the `bin.png` image file in a different location, you'll need to update the path in the `layout_tool.rpy` file.
   
   To modify the path, go to the top of the `layout_tool.rpy` file and update line 5 as follows:
   ```renpy
   define bin_img = './images/bin.png'
    ```
2. **Place `layout_tool.rpy` in Your Project:**
   - You can place the `layout_tool.rpy` file **anywhere** inside your Ren'Py project directory. It does not require a specific location.

3. **Check for Optional Outline Shader:**
   - The tool uses an outline shader by default. If you don't want to use the outlines, change the following values in `layout_tool.rpy` to `None`:
   ```renpy
   default item_active_trans = None
   default item_hover_trans = None

4. **Start the Game:**
    - Run your Ren'Py game and press `L` to open the layout tool, anywhere in your game.

## 🔧 Usage Instructions

### 1. Open the Tool:
Press `L` to open the layout tool. To exit and return to normal game interactions, press `ESC`.

### 2. Add Images:
Use the search bar in the top-right corner of the tool to input the name of an image. You can use either a Ren'Py image object or a direct image file (with the full path and extension). Press `Enter` to load the image onto the screen.

### 3. Position Images:
Once the image appears, you can drag it around the screen to position it. The image’s coordinates will be displayed in the preview box, allowing you to use these exact values for final positioning in your scripts.

### 4. Remove Images:
To remove an image, simply drag it to the trash icon located next to the search bar (top-right corner).

## ⚠️ Important Notes:
If the image is inside a container (e.g., `frame`, `vbox`, `hbox`, `viewport`) or already has position-related properties, the final position shown in the tool might not reflect its true placement due to overlapping layout rules.

### Solution:
To avoid positioning issues, follow these steps:

1. **Remove any position attributes** from the image.
2. Place the image in a **fixed** container, which allows for absolute positioning without interference from other layout elements.

### Example:
Here’s an example using a fixed container to ensure the image is correctly positioned without being affected by other layout elements:

```renpy
screen example_fixed:
    fixed:
        add "example_image.png" xpos 400 ypos 300
```

In this example, the image will be positioned at `xpos 400` and `ypos 300` and won't be affected by other layout rules.

## Notice

**Contributions & Pull Requests:** Welcome!  
**Issues:** Please let us know if you encounter any issues. This version is public due to requests, but future updates and fixes may be made.
