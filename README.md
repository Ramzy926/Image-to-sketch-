
# Image to Sketch 🖼️✏️

Convert images into sketch-style art using Python, Pillow, and NumPy — even on Android using Termux!

📱 Install Python in Termux
1. Install Termux from [F-Droid](https://f-droid.org) (recommended).
2. Open Termux and run:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   pip install pillow numpy
   ```

🚀 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Ramzy926/Image-to-sketch-.git
   cd Image-to-sketch-
   ```
2. Place your image in the folder (you can move it with `mv` or Termux's shared storage).
3. Run the script:
   ```bash
   python sketch.py
   ```

🧠 How It Works
- Loads the image using Pillow.
- Converts it to grayscale.
- Applies a sketch effect using NumPy operations.

📁 Example
Input: `photo.jpg`  
Output: `sketch_photo.jpg`

---

👤 *Author:* *Ramsfield*  
Use, fork, or improve it as you like!


