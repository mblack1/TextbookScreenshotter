from PIL import Image, ImageGrab
from pyautogui import press
import time

book_length = 100  # How many pages is your book
cover_location = "Cover.png"  # Specify the name of the cover picture (make sure it is a .png)

# IMPORTANT: Manually specify the dimensions for your screenshot
X1 = 488
Y1 = 87
X2 = 950
Y2 = 800


# You have 5 seconds to switch to the textbook. Make sure you start on the cover page
time.sleep(5)

box = (X1, Y1, X2, Y2)
im_list = []
cover = Image.open(cover_location).convert("RGB")

for i in range(0, book_length):
    press("down")  # Assuming the down arrow key switches between pages
    # Change to press("right") if right arrow key works instead, and so on.

    time.sleep(1)  # arbitrary delay between screenshots
    im = ImageGrab.grab(bbox=box).convert('RGB')
    im_list.append(im)

cover.save("Textbook.pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list)