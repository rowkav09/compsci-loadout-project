import tkinter as tk
import urllib.request
import io
from PIL import ImageTk, Image

root = tk.Tk()
root.title("cs2 loadout generator")
root.geometry("500x500")
link = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_frHcVuPaoafU1JqiVWWSVkux15OQ8Giiylk0k5mvTnIqpd3PCaQIhWMYkE_lK7EcNeCKW-w"

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        image = Image.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image

img = WebImage(link).get()

imagelab = tk.Label(root, image=img)
imagelab.image = img  # keep reference
imagelab.pack()
count = 1
def change_func():
    global count
    if count == 0:
        link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_frHcVuPaoafU1JqiVWWSVkux15OQ8Giiylk0k5mvTnIqpd3PCaQIhWMYkE_lK7EcNeCKW-w"
    elif count == 1:
        link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu4vx603vRA_Olpfu-TVJ7uK9V6xsLvSEHGaA_uh3svNgTBa7mggpty6RlYDtKRTILFd-XccfGb5d6lSmwdS1Zrzr4Q3Ygo5Ayiur23lL5idr5eZQBapzqPDRignHY-U058QHLOHnE0oCUw1MCg"
    elif count == 2:
        link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Dx60noTyL6kJ_m-B1P7vG6YadsLM-QG1iA1PxmvORWRzy9gQ4qsjO6lob-KT-JbFQlC5YhFrQN4xe4m4ezNL7g4QyLiItFyS772C5I7ilq6rpWUaYh-rqX0V82KISxGQ"
    if count< 2:
        count += 1
    else:
        count = 0   
    i = WebImage(link1).get()

    imagelab.config(image=i)
    imagelab.image = i  # keep reference

button = tk.Button(root, text="Update image", command=change_func)
button.pack(anchor='w',side='bottom')
root.mainloop()

root.mainloop()
