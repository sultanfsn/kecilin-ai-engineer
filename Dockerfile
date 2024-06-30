# Base python that this application will be using
FROM python:3.9.0

# Every file will be installed and ran on this directory (equivalent to cd app)
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --default-timeout=1000 -r requirements.txt

# copy everything that needed to run the app from local to container
COPY main.py main.py
COPY input/ input/
RUN mkdir /output
COPY models/ models/

# run the script to launch the app
ENTRYPOINT ["python", "main.py"]