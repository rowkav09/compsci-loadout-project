# Source - https://stackoverflow.com/a/65638774
# Posted by acw1668
# Retrieved 2026-06-15, License - CC BY-SA 4.0

import tkinter as tk
import urllib.request
#import base64
import io
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Weather")

link = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_frHcVuPaoafU1JqiVWWSVkux15OQ8Giiylk0k5mvTnIqpd3PCaQIhWMYkE_lK7EcNeCKW-w"

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        #self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image

img = WebImage(link).get()
imagelab = tk.Label(root, image=img)
imagelab.grid(row=0, column=0)

root.mainloop()
