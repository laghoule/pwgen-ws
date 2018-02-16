FROM python:3

WORKDIR /pwgen

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8090

CMD [ "python", "./pwgen.py" ]