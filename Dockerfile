# FROM alpine:3.13.6 
# # Install python and pip 
# RUN apk add --update py3-pip 
# # install Python modules needed by the Python app 
# COPY /sandbox/requirements.txt /sandbox/
# RUN pip install --no-cache-dir -r /sandbox/requirements.txt
#  # copy files required for the app to run 
# #COPY /sandbox/app.py /sandbox/
# #COPY /sandbox/BankFunctions.py /sandbox/
# COPY ./sandbox /sandbox
#  # tell the port number the container should expose 
# EXPOSE 5000
#  # run the application 
# CMD ["python3", "/sandbox/app.py"] 


FROM python:3.8-alpine
ADD . /sandbox
WORKDIR /sandbox

COPY /sandbox/requirements.txt sandbox/
COPY /sandbox/app.py sandbox/
COPY /sandbox/BankFunctions.py sandbox/
ENV PORT 5000
ENV HOST 0.0.0.0
RUN apk update
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN apk add libressl-dev
RUN apk add libffi-dev
RUN pip install --no-cache-dir -r sandbox/requirements.txt
RUN python -m pip install --upgrade pip
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["sandbox/app.py"]
