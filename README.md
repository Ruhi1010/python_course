# Python Course

### ❤️ Heart Shape Drawing with Turtle and Math in Python (filename: heart.py)

This Python script draws a heart using parametric equations and the Turtle graphics library. It creates a glowing red heart on a black background, with lines radiating from the center to each point on the curve.

---

## 💻 Full Code with Line-by-Line Comments

```python
import math                  # Import math module for trigonometric functions
from turtle import *         # Import all turtle graphics functions

# Define the x-coordinate of the heart using a parametric equation
def hearta(k):
    return 15 * math.sin(k) ** 3  # x = 15 * sin³(k)

# Define the y-coordinate of the heart using a parametric equation
def heartb(k):
    return (12 * math.cos(k)      # y = 12cos(k)
            - 5 * math.cos(2 * k) #     - 5cos(2k)
            - 2 * math.cos(3 * k) #     - 2cos(3k)
            - math.cos(4 * k))    #     - cos(4k)

speed(0)                  # Set the turtle drawing speed to maximum (fastest)
bgcolor('black')          # Set the background color of the canvas to black

# Loop through a large number of points to draw the heart
for i in range(6000):
    # Calculate (x, y) coordinates for the current value of k (i)
    x = hearta(i) * 20         # Scale x-coordinate to make it visible
    y = heartb(i) * 20         # Scale y-coordinate similarly

    goto(x, y)                 # Move turtle to the (x, y) point

    for j in range(1):         # Dummy loop (can be removed), runs once
        color('red')           # Set the pen color to red for the heart

    goto(0, 0)                 # Return to origin (0, 0) to draw a line back (radiating effect)

done()                         # Finish turtle drawing and keep the window open
```

---

## 🔍 How It Works

- **`hearta(k)` and `heartb(k)`** define the **x** and **y** positions for a heart-shaped curve using sine and cosine functions.
- The loop runs **6000 times**, plotting and connecting each point to the origin `(0, 0)` to create a burst pattern.
- The **`* 20`** multiplier scales the heart to fill more space on the screen.
- **Turtle settings**:
  - `speed(0)`: fastest drawing speed
  - `bgcolor('black')`: improves visibility with red
  - `color('red')`: standard heart color

---

## 🖼️ Output

The drawing will display a red heart with spiky lines radiating from the center, creating a stylized glowing effect.

---

## ▶️ How to Run

1. Save the code to a file named `heart.py`
2. Run with Python:

```bash
python heart.py
```

Make sure you have Python installed. The Turtle module is built-in and does not need separate installation.

---

## 🧠 Notes

- To **just draw the heart outline**, remove the line `goto(0, 0)`.
- You can **change the color**, scale, or speed to customize the heart's appearance.
- This is a creative example of **parametric equations + turtle graphics** for visual learning.

---

___

