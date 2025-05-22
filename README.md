# Ren'Py Layout Tool
> Instantly Preview and Place Images in Ren'Py

> Currently, this version is only available on GitHub (not yet on Itch.io).

![Version: Beta](https://img.shields.io/badge/Version-Beta-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Image](https://github.com/user-attachments/assets/50270935-7d56-4e37-beda-07d35281df5e)

### Preview 
- Video1 : https://youtu.be/f3nDPWE2CIc
- Video2 : https://youtu.be/MNqknAaeDuE


- Load new images directly into your **`current scene`** as **overlays**
   - making it easy to visualize and adjust their positions without leaving the game.
- This tool is for **previewing purposes** only.
   - It doesn't add images directly to the code.
   - but helps you assess the placement and suitability of multiple assets before finalizing your scene.

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



# 🖼️ Layout Tool Guide

The `layout_tool` in Ren'Py allows you to visually position images or UI elements on the screen by dragging them around. The tool temporarily pauses interactions like dialog playback, allowing you to fine-tune your layout.

## 🛠️ Installation Guide

1.  Place the folder named `layout-visualizer` directly into your game's root directory.
    * Ensure the `bin.png` image file and the `layout_tool.rpy` file are located inside this `layout-visualizer` folder.

2.  **Start the Game:**
    * Run your Ren'Py game. You can access the layout tool from anywhere in your game by pressing the `L` key.

### **Optional: Enable Fen's Outline Shader (for video-like effect):**
   🔗 [https://feniksdev.itch.io/outline-shader-renpy](https://feniksdev.itch.io/outline-shader-renpy)

   * This tool optionally supports Fen's outline shader. For a video-like effect, download FeniksDev's Outline Shader asset. To enable it, find these lines in `layout_tool.rpy` and remove the `#` at the beginning of each line:
      
        ```renpy
        # default item_active_trans = glow_outline(12, "#11d427", num_passes=6)
        # default item_hover_trans = glow_outline(12, "#f5b5c0", num_passes=3)
        ```
   * If you prefer not to use the outline shader, make sure these lines are either commented out (with a `#` at the start) or set to `None`:
        ```renpy
        default item_active_trans = None
        default item_hover_trans = None
        ```

### ⚠️ File Relocation Notice

* If you later move the `layout_tool.rpy` file or the `bin.png` image, you'll need to update the image path within `layout_tool.rpy`. Open the file and check the `define bin_img` line at the top to ensure the path to `bin.png` is correct.

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
