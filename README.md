# TextbookScreenshotter
This script screenshots textbook pages and merges them into a pdf.

# How to use it
If you don't have it installed already, make sure to download the latest version of Python from https://www.python.org/downloads/

Next, you're going to want to download the external libraries this uses, Pillow and PyAutoGUI. See: https://packaging.python.org/tutorials/installing-packages/, https://pillow.readthedocs.io/en/latest/installation.html, and https://pyautogui.readthedocs.io/en/latest/install.html

Make a new folder somewhere. Save the script as a .py file there. See https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs

Take a screenshot of the first page of your ebook, name it "Cover.png" and place it into the folder you made.

Open the .py file and replace the 100 in "book_length = 100" with however long your ebook is.

Set the dimensions of your screenshots. You do this by using a program such as snipping tool on windows or CMD-Shift-4 on OSX. Replace the X1, Y1 values with the coordinates of the top left of the ebook and the X2, Y2 with the coordinates of the bottom right.

Ensure that pressing the down arrow key moves to the next page. If it doesn't, change " press("down") " to the correct key (for instance, if the right arrow key worked instead, it'd be press("right") ).

Run the program then switch back to the cover page of the ebook. After a few seconds, it should be flipping through a page every second or so.

Wait for the program to complete. If everything worked out, you should have a complete pdf named "Textbook.pdf" in the folder you made

Last but not least, upload your book to Libgen using username: **genesis**, password: **upload**

If you get a memory error you can try reducing the loop size and running it multiple times. (Instead of "for i in range(0, book_length)" change to "for i in range(0, book_length/2)")

**All credit goes to ** [u/elitesla](https://www.reddit.com/user/elitesla) **on reddit. I am just putting it on github for more people to find.**
