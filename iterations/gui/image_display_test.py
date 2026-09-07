# importing modules
import urllib.request
from PIL import Image
url = 'https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XsnXwtmkJjSU91dh8bj35VTqVBP4io_fr3EVvKD6MKU_cKPKXWHFxLkls7FsSnDqwUl_sWTczoqheHifbwMmD5F1RvlK7Ec_KL6Q_A'
urllib.request.urlretrieve(
  url,
   "gfg.png")

img = Image.open("gfg.png")
img.show()