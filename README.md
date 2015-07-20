# raspgif

## Setup

Build an image:

    docker build -t raspgif .


## Run

Get info about **Cu Potential** for today:

    docker run raspgif python raspgif/main.py --parameter "Cu Potential" --when today

