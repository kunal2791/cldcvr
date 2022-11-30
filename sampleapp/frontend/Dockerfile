# set base image (host OS)
FROM python:3.8-slim
#test
#The working directory in Docker
WORKDIR /workdir

#Copy requirements from current directory to the code directory
COPY sampleapp/frontend/requirements.txt requirements.txt

#Install libraries
RUN pip install -r requirements.txt

#Environemnt variables to configure app
ENV FLASK_APP=app.run
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

#Open the port
EXPOSE 5100

#Copy the current directory . in the project to the workdir . in the image.
COPY . .
#Makes the app library available in the python console
RUN pip install -e sampleapp/frontend/.

CMD flask run -p 5100