### -------- ###
# -- MULTI --- #
# -- STAGE --- #
# -- BUILD --- #
### -------- ###
# Author: Christopher Ek
# Version: 1.12.1


### -------------------------------  STAGE 1  -------------------------------------- ###
FROM python:3.10-slim as builder 

ARG MAINTAINER="Christopher Ek"
ARG Version="23.2"
ARG PORT="5000"
# Make is permanent sort of.
ENV PORT=$PORT

LABEL Description=""
LABEL MAINTAINER="${MAINTAINER}"
LABEL Version="${Version}"

WORKDIR /app
# Copy and download dependency using go mod.
COPY requirements.txt .
# Layer 01 ^
RUN pip install -r requirements.txt
# Layer 02 ^ also remove req

# When that is cached, we copy the rest.
COPY . .

# Create the exe file
RUN pip install pyinstaller
RUN pyinstaller --onefile main.py
### -------------------------------  STAGE 2  ------------------------------- ###
# mini image, to only run the exe file
FROM scratch

# Copy from builder or stage 1
COPY --from=builder ["/app/dist/main.exe", "."] # Copy the executable to the root of the image.

# get some updates.
RUN apt-get update

# no nano here, 
# I would remove this line, 
# because we dont need any editor. 
# on the container that just runs the exe file.
RUN apt-get install nvim 

# run the application
ENTRYPOINT [ "./main" ] # Run the executable.