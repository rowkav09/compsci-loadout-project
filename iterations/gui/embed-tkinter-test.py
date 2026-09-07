import tkinter as tk
import urllib.request
import io
from PIL import ImageTk, Image

root = tk.Tk()
root.title("cs2 loadout generator")
root.geometry("500x500")
link = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Tk5UvzWCL2kpn2-DFk_OKherB0H-CGHHecxNF6ueZhW2exk01w4j7cmYn4eHPCbAMhApdwTOIN5BPsx9yyYu605FTeid0Uy3j3kGoXueKyz5wo"

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
    match count:
        case 0:
            link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Tk5UvzWCL2kpn2-DFk_OKherB0H-CGHHecxNF6ueZhW2exk01w4j7cmYn4eHPCbAMhApdwTOIN5BPsx9yyYu605FTeid0Uy3j3kGoXueKyz5wo"
        case 1:
            link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Tk5UvzWCL2kpn2-DFk_OKherB0H_KfG2Kv0ed4u95lRi67gVNx4T-Bw434IHyVb1QlAsd1FOUDthG4xNznMu3m4QXXg90Wzn_33C1I8G81tLaDi_rK"
        case 2:
            link1 = "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Tk5UvzWCL2kpn2-DFk6P6hfqFSM-CcHHOvx-J3veR6cCahlBMgtgKJk4jxNWWXblAgDJUiTeJZtBHpktDuY7m2sQPf2YNAxXn5iysf6Cc_67oGA6Ah5OSJ2AmILwG6"

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
