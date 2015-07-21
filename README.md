# raspgif

## Setup

Build an image:

    docker build -t raspgif .


## Run

Get info about **Thermal Updraft Velocity and B/S ratio** for today and tomorrow and save it as a gif:

    docker run raspgif python raspgif/main.py --parameter "Thermal Updraft Velocity and B/S ratio" --when today > today.gif
    docker run raspgif python raspgif/main.py --parameter "Thermal Updraft Velocity and B/S ratio" --when tomorrow > tomorrow.gif

Get info about **Cu Cloudbase where Cu Potential>0** for today and tomorrow and save it as a gif:

    docker run raspgif python raspgif/main.py --parameter "Cu Cloudbase where Cu Potential>0" --when today > today.gif
    docker run raspgif python raspgif/main.py --parameter "Cu Cloudbase where Cu Potential>0" --when tomorrow > tomorrow.gif
