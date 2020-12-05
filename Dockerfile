FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY test ./test
#CMD [ "python", "test/demo.py" ]
CMD [ "python", "pytest test" ]