# start with python environment

FROM python:3.10-slim


# choose the working dirctory inside the container
WORKDIR /app


#copy the packages list first

COPY requirements.txt .

#Install Python dependences.
RUN python -m pip install --no-cache-dir -r requirements.txt


#Copy the project file into the image.
COPY . .

#streamlit listen on this port 
EXPOSE 8051

#Start the streamlit application
CMD ["python", "-m", "streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8051" ]