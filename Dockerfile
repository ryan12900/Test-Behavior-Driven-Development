# FROM alpine:3.13.6 
# # Install python and pip 
# RUN apk add --update py3-pip 
# # install Python modules needed by the Python app 
# COPY /sandbox/requirements.txt sandbox/
# RUN pip install --no-cache-dir -r sandbox/requirements.txt
#  # copy files required for the app to run 
# COPY /sandbox/app.py sandbox/
# COPY /sandbox/BankFunctions.py sandbox/
#  # tell the port number the container should expose 
# EXPOSE 5000
# CMD echo Hi
#  # run the application 
# CMD ["python3", "sandbox/app.py"] 

FROM python:3.8-alpine
WORKDIR /Test-Behavior-Driven-Development
#ADD ./Test-Behavior-Driven-Development
COPY /sandbox/requirements.txt sandbox/
ENV PORT 8080
ENV HOST 0.0.0.0
RUN pip install --no-cache-dir -r sandbox/requirements.txt
RUN python -m pip install --upgrade pip
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["sandbox/app.py"]