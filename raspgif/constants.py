import os

RASP_URL = "http://rasp.linta.de/GERMANY/"
suffix = "lst.d2.png"
today = "curr"
tomorrow = "curr+1"

parameters = {
    "Cu Cloudbase where Cu Potential>0": "zsfclclmask",
    "Thermal Updraft Velocity and B/S ratio": "wstar_bsratio",
}

here = os.path.abspath(os.path.dirname(__file__))
hours = ["07", "08", "09"] + list(map(str, range(10, 20)))
