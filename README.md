![Version: Beta](https://img.shields.io/badge/Version-Beta-blue) 
![License: MIT](https://img.shields.io/badge/License-MIT-green)

# 📌 Available on Itch.io

### [seo-a-nam.itch.io/layouttools](https://seo-a-nam.itch.io/layouttools)  
> Most users download it here. Troubleshooting and updates are also handled on Itch.io.

# 💡 Overview 

## Ren'Py Layout Tool

> **A visual preview editor to help you accurately place images and UI elements on screen in Ren'Py.**


<img src="https://github.com/user-attachments/assets/50270935-7d56-4e37-beda-07d35281df5e" width="400"/>

This tool allows you to load new images as overlays onto your current scene, making it easy to visualize and adjust their positions without exiting the game. 

It's for **previewing purposes only**; 

it doesn't directly alter your code but helps you evaluate asset placement before finalizing your scene.

> ⚠️ This project is currently in **beta** and may receive updates based on user feedback.



## 📺 Demo Videos (Preview)

- Video1 : https://youtu.be/f3nDPWE2CIc
- Video2 : https://youtu.be/MNqknAaeDuE

## ✨ Features

- ⌨️ **Keyboard Shortcuts** – Press `L` to open, `ESC` to close. No reloads needed.
- 🛠️ **Runs In-Game** – Fully integrated into Ren'Py. No external tools required.
- 🖱️ **Drag & Track** – See real-time coordinates while moving elements.
- 📂 **Flexible Loading** – Supports both file paths and Ren'Py image objects.
- 🌗 **Light/Dark Overlay** – Toggle semi-transparent preview background.
- ✨ **Image Highlighting** – Outlines selected items (with outline shader).
- 🖼️ **Multi-Element Support** – Add multiple images or UI elements at once.
- 🗑️ **Drag to Delete** – Remove items by dropping them into the trash bin.

---

## 🖼️ Layout Tool Guide

The `layout_tool` in Ren'Py lets you visually position images or UI elements by dragging them. It temporarily pauses interactions like dialog playback for precise layout adjustments.

### 🔧 Installation

1. Download or extract the archive.
2. Place the `layout-visualizer/` folder into your `game/` directory.
3. Ensure `bin.png` and `layout_tool.rpy` are inside this folder.

### ▶️ Usage

1. **Open the Tool:**
   - Press `L` during gameplay to activate, `ESC` to close.
   - Adjust UI placement on the semi-transparent preview background.

2. **Add Images:**
   - Enter an image name or path in the top-right `search bar` and press `Enter`.
   - Dragging an image displays `real-time coordinates`, which can be directly applied to your code.
   - You can load `images with Ren'Py transform (including animations)` applied, ensuring accurate in-game positioning.

3. **Remove Images:**
   - Drag the image to the `trash icon`.

---

## ⚠️ Important Notes

If an image is within a container (e.g., `frame`, `vbox`, `hbox`, `viewport`) or has existing position properties, its final position in the tool might differ due to overlapping layout rules.

### ✅ Solution

To avoid conflicts:

- **Remove all position attributes** from the image.
- **Place the image in a fixed container**, which allows absolute positioning without interference.

**Example:**

```renpy
screen example_fixed:
    fixed:
        add "example_image.png" xpos 400 ypos 300
```

In this example, the image will be positioned at xpos 400 and ypos 300 and will not be affected by other layout rules.

## 🖍️ Optional: Enabling Fen's Outline Shader

🔗 [Fen's Outline Shader - itch.io](https://feniksdev.itch.io/outline-shader-renpy)

This tool optionally supports **Fen's outline shader**. For effects like those in the demo video:

1. Download **FeniksDev's Outline Shader** asset.
2. In `layout_tool.rpy`, find and uncomment these lines:

```renpy
# default item_active_trans = glow_outline(12, "#11d427", num_passes=6)
# default item_hover_trans = glow_outline(12, "#f5b5c0", num_passes=3)
```

3. If you prefer **not** to use the outline shader, set them to None:

```renpy
default item_active_trans = None
default item_hover_trans = None
```

## 📁 File Relocation

If you later move the `layout_tool.rpy` file or the `bin.png` image, update the image path within `layout_tool.rpy`.  
Open the file and check the `define bin_img` line at the top for the correct path.

---

## 📣 Notice

- **Contributions & Pull Requests:** Welcome!
- **Issues:** Please report any issues. This public version may receive future updates and fixes.
