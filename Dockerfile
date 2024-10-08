FROM python:3.11-alpine3.20
WORKDIR /app
COPY . .
RUN mkdir /app/result
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python"]
CMD ["start.py"]