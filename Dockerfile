FROM python:3-alpine

WORKDIR /pwgen

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 5001

CMD [ "python", "./pwgen.py" ]