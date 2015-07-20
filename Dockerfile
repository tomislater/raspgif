FROM python
ADD . /raspgif
WORKDIR /raspgif
RUN pip install -r requirements.txt