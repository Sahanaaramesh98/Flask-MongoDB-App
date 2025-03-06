# Use an official Python runtime as a parent image
FROM python:3.7-alpine

ADD . /app

# Set the working directory in the container
WORKDIR /app

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Make port 5000 available to the world outside this container
EXPOSE 5000
# Copy the current directory contents into the container at /app
COPY . .
# Run the Flask app
CMD [ "python", "app.py" ]